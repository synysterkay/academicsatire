/**
 * Cloudflare Worker: Amazon Link Geolocation Rewriter
 * 
 * Deploys on academicsatire.com via Cloudflare Workers.
 * Rewrites amazon.com links to the user's local Amazon store
 * based on their country (detected by Cloudflare's cf.country).
 * 
 * - Normalizes links to /dp/ASIN format for cross-store compatibility
 * - Only rewrites to major Amazon stores with full Kindle catalogs
 * - Countries with small/new stores fallback to a major regional store
 *
 * SETUP:
 * 1. Go to Cloudflare Dashboard → Workers & Pages → Create Worker
 * 2. Paste this code
 * 3. Go to Worker → Triggers → Add Route: academicsatire.com/*
 * 4. Deploy
 */

// Only major Amazon stores with full Kindle book catalogs
const AMAZON_DOMAINS = {
  US: 'www.amazon.com',
  CA: 'www.amazon.ca',
  GB: 'www.amazon.co.uk',
  DE: 'www.amazon.de',
  FR: 'www.amazon.fr',
  ES: 'www.amazon.es',
  IT: 'www.amazon.it',
  NL: 'www.amazon.nl',
  AU: 'www.amazon.com.au',
  IN: 'www.amazon.in',
  JP: 'www.amazon.co.jp',
  BR: 'www.amazon.com.br',
  MX: 'www.amazon.com.mx',
  SG: 'www.amazon.sg',
};

// Map countries to the nearest major Amazon store with Kindle support
const COUNTRY_FALLBACKS = {
  // Europe → regional major store
  IE: 'www.amazon.co.uk',
  AT: 'www.amazon.de',
  CH: 'www.amazon.de',
  PT: 'www.amazon.es',
  BE: 'www.amazon.fr',
  PL: 'www.amazon.de',
  SE: 'www.amazon.co.uk',
  NO: 'www.amazon.co.uk',
  DK: 'www.amazon.de',
  FI: 'www.amazon.co.uk',
  CZ: 'www.amazon.de',
  HU: 'www.amazon.de',
  RO: 'www.amazon.de',
  GR: 'www.amazon.de',
  // Middle East → amazon.com (best catalog)
  AE: 'www.amazon.com',
  SA: 'www.amazon.com',
  QA: 'www.amazon.com',
  KW: 'www.amazon.com',
  BH: 'www.amazon.com',
  OM: 'www.amazon.com',
  EG: 'www.amazon.com',
  TR: 'www.amazon.com',
  // Asia-Pacific
  NZ: 'www.amazon.com.au',
  MY: 'www.amazon.sg',
  PH: 'www.amazon.sg',
  TH: 'www.amazon.sg',
  // Africa → amazon.com
  ZA: 'www.amazon.com',
  NG: 'www.amazon.com',
  KE: 'www.amazon.com',
};

function getAmazonDomain(countryCode) {
  return AMAZON_DOMAINS[countryCode] || COUNTRY_FALLBACKS[countryCode] || 'www.amazon.com';
}

// Extract ASIN from any Amazon URL and normalize to /dp/ASIN
function normalizeAmazonPath(href) {
  // Match /dp/ASIN or /gp/product/ASIN patterns
  const asinMatch = href.match(/\/(?:dp|gp\/product)\/([A-Z0-9]{10})/);
  if (asinMatch) {
    return '/dp/' + asinMatch[1];
  }
  // If no ASIN found, return the original path
  try {
    return new URL(href).pathname;
  } catch {
    return null;
  }
}

export default {
  async fetch(request) {
    const url = new URL(request.url);

    // Only process HTML pages (skip static assets)
    const ext = url.pathname.split('.').pop();
    const staticExts = ['css', 'js', 'png', 'jpg', 'jpeg', 'gif', 'svg', 'webp', 'woff', 'woff2', 'ico', 'xml', 'json', 'txt', 'webmanifest'];
    if (staticExts.includes(ext)) {
      return fetch(request);
    }

    const country = request.cf?.country || 'US';
    const targetDomain = getAmazonDomain(country);

    // If the user is in the US, no rewriting needed
    if (targetDomain === 'www.amazon.com') {
      return fetch(request);
    }

    const response = await fetch(request);
    const contentType = response.headers.get('content-type') || '';

    // Only rewrite HTML responses
    if (!contentType.includes('text/html')) {
      return response;
    }

    // Use HTMLRewriter to swap Amazon links at the edge
    return new HTMLRewriter()
      .on('a[href*="amazon.com"]', {
        element(el) {
          const href = el.getAttribute('href');
          if (href && href.includes('amazon.com')) {
            const normalizedPath = normalizeAmazonPath(href);
            if (normalizedPath) {
              el.setAttribute('href', 'https://' + targetDomain + normalizedPath);
            }
          }
        }
      })
      .transform(response);
  }
};
