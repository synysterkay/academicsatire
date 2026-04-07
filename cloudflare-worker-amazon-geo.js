/**
 * Cloudflare Worker: Amazon Link Geolocation Rewriter
 * 
 * Deploys on academicsatire.com via Cloudflare Workers.
 * Rewrites amazon.com links to the user's local Amazon store
 * based on their country (detected by Cloudflare's cf.country).
 *
 * SETUP:
 * 1. Go to Cloudflare Dashboard → Workers & Pages → Create Worker
 * 2. Paste this code
 * 3. Go to Worker → Triggers → Add Route: academicsatire.com/*
 * 4. Deploy
 */

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
  AE: 'www.amazon.ae',
  SA: 'www.amazon.sa',
  SE: 'www.amazon.se',
  PL: 'www.amazon.pl',
  BE: 'www.amazon.com.be',
  EG: 'www.amazon.eg',
  TR: 'www.amazon.com.tr',
};

// Countries that should map to a nearby Amazon store
const COUNTRY_FALLBACKS = {
  // Europe → amazon.co.uk or regional
  IE: 'www.amazon.co.uk',
  AT: 'www.amazon.de',
  CH: 'www.amazon.de',
  PT: 'www.amazon.es',
  // Middle East → amazon.ae
  QA: 'www.amazon.ae',
  KW: 'www.amazon.ae',
  BH: 'www.amazon.ae',
  OM: 'www.amazon.ae',
  // Asia-Pacific → amazon.com.au or .sg
  NZ: 'www.amazon.com.au',
  MY: 'www.amazon.sg',
  PH: 'www.amazon.sg',
  TH: 'www.amazon.sg',
};

function getAmazonDomain(countryCode) {
  return AMAZON_DOMAINS[countryCode] || COUNTRY_FALLBACKS[countryCode] || 'www.amazon.com';
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
      .on('a[href*="www.amazon.com"]', {
        element(el) {
          const href = el.getAttribute('href');
          if (href) {
            el.setAttribute('href', href.replace('www.amazon.com', targetDomain));
          }
        }
      })
      .transform(response);
  }
};
