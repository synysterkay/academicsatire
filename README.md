# Prof Y Not - Author Portfolio & Satire Book Marketing Site

A modern, responsive static website for Prof Y Not, featuring satirical comedy books, an automated blog, and full SEO optimization. Built with Hugo and deployed on GitHub Pages.

## 🚀 Features

- **Modern 2026 Design**: Clean typography, bold colors, dark mode support
- **Fully Responsive**: Desktop, tablet, and mobile optimized
- **SEO Optimized**: Structured data, meta tags, sitemap, robots.txt
- **Automated Blog**: Daily AI-generated content via DeepSeek API
- **GDPR Compliant**: Cookie consent, privacy policy, opt-in forms
- **Performance Focused**: Minimal JS, optimized images, fast loading

## 📁 Project Structure

```
profynot-website/
├── .github/
│   └── workflows/
│       ├── daily-blog-deploy.yml    # Daily content generation & deploy
│       ├── hugo-deploy.yml          # Manual deployment
│       └── sitemap-update.yml       # Weekly sitemap ping
├── content/
│   ├── blog/                        # Blog posts (markdown)
│   ├── books/                       # Book pages
│   ├── about.md
│   ├── contact.md
│   ├── privacy.md
│   ├── terms.md
│   └── cookies.md
├── static/
│   ├── css/
│   │   └── main.css                 # Main stylesheet
│   ├── js/
│   │   └── main.js                  # Interactive features
│   ├── images/                      # Site images
│   ├── robots.txt
│   └── site.webmanifest
├── themes/
│   └── profynot-theme/
│       └── layouts/                 # Hugo templates
├── config.toml                      # Hugo configuration
└── README.md
```

## 🛠️ Setup Instructions

### Prerequisites

- [Hugo Extended](https://gohugo.io/installation/) (v0.124.0+)
- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/) (for blog generation)
- GitHub account

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/profynot-website.git
   cd profynot-website
   ```

2. **Start Hugo development server**
   ```bash
   hugo server -D
   ```

3. **View the site**
   Open http://localhost:1313 in your browser

### Configuration

1. **Update `config.toml`**
   - Replace `baseURL` with your GitHub Pages URL
   - Update `googleAnalyticsID` with your GA4 measurement ID
   - Add your verification codes for Google/Bing

2. **Images**
   - Images are pre-configured with Unsplash URLs
   - To use custom images, upload to `/static/images/` and update paths

3. **Update Amazon links**
   - Replace `YOUR_ASIN`, `YOUR_KINDLE_ASIN`, etc. with actual ASINs
   - Update affiliate tag if using Amazon Associates

## 🚀 Deployment to GitHub Pages

### Initial Setup

1. **Create GitHub repository**
   - Go to GitHub and create a new repository
   - Name it `profynot.github.io` (or your preferred name)

2. **Push code to GitHub**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git branch -M main
   git push -u origin main
   ```

3. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Source: "GitHub Actions"

4. **Add secrets for automated blog generation**
   - Go to Settings → Secrets and variables → Actions
   - Add `DEEPSEEK_API_KEY` with your DeepSeek API key

### Manual Deployment

The site auto-deploys on push to `main`. For manual deployment:

1. Go to Actions tab
2. Select "Build and Deploy Hugo Site"
3. Click "Run workflow"

## 📝 Adding Content

### New Blog Post

Create a new file in `content/blog/`:

```markdown
---
title: "Your Post Title"
description: "Meta description for SEO"
date: 2026-02-03
categories:
  - Academic Humor
tags:
  - satire
  - writing
ogImage: "/images/your-image.jpg"
---

Your content here...
```

### New Book

Create a new file in `content/books/`:

```markdown
---
title: "Book Title"
description: "Book description"
coverImage: "/images/book-cover.jpg"
kindlePrice: "9.99"
paperbackPrice: "14.99"
amazonKindle: "https://amazon.com/dp/ASIN"
amazonPaperback: "https://amazon.com/dp/ASIN"
rating: 4.5
ratingCount: 100
---

Full book description...
```

## 🤖 Automated Blog Generation

The site uses GitHub Actions + DeepSeek API to generate daily blog posts:

- **Schedule**: Daily at 6 AM UTC
- **Topics**: Rotates through satire, academic humor, KDP tips, etc.
- **Manual trigger**: Run anytime from Actions tab

### Customizing Topics

Edit `.github/workflows/daily-blog-deploy.yml` and modify the `topics` array in the Node.js script.

## 🔍 SEO Configuration

### Google Search Console

1. Go to [Google Search Console](https://search.google.com/search-console)
2. Add property with your URL
3. Copy verification code
4. Add to `config.toml` → `googleSiteVerification`
5. Submit sitemap: `https://yoursite.com/sitemap.xml`

### Bing Webmaster Tools

1. Go to [Bing Webmaster Tools](https://www.bing.com/webmasters)
2. Add your site
3. Copy verification code
4. Add to `config.toml` → `bingSiteVerification`

### Google Analytics 4

1. Create GA4 property at [Google Analytics](https://analytics.google.com)
2. Get Measurement ID (G-XXXXXXXXXX)
3. Add to `config.toml` → `googleAnalyticsID`

## 🎨 Customization

### Colors

Edit CSS variables in `static/css/main.css`:

```css
:root {
  --color-primary: #6366f1;
  --color-secondary: #f59e0b;
  /* ... */
}
```

### Fonts

Update Google Fonts link in `themes/profynot-theme/layouts/_default/baseof.html`

### Dark Mode

Dark mode colors are defined in `[data-theme="dark"]` section of CSS.

## 📊 Analytics & Tracking

- **Google Analytics 4**: Configured in `config.toml`
- **Event tracking**: Automatic for Amazon links, newsletter signups
- **UTM parameters**: Auto-appended to Amazon links

## 🔒 Privacy & Compliance

- **Cookie consent**: GDPR-compliant banner
- **Privacy policy**: Template included
- **Analytics opt-out**: Respects DNT, provides opt-out

## 📱 Progressive Web App

Site includes a web manifest for PWA features. Add icons to `static/images/`:
- `icon-192.png` (192x192)
- `icon-512.png` (512x512)
- `icon-maskable-512.png` (512x512, maskable)

## 🐛 Troubleshooting

### Build Errors

```bash
# Clear Hugo cache
hugo --gc --cleanDestinationDir

# Check for syntax errors
hugo --verbose
```

### Deployment Issues

1. Check GitHub Actions logs
2. Verify repository settings
3. Ensure Pages is set to "GitHub Actions" source

## 📄 License

Content © Prof Y Not. Code is MIT licensed.

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit pull request

---

Built with ❤️ and Hugo | Deployed on GitHub Pages
