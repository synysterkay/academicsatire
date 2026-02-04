/**
 * Prof Y Not - Additional JavaScript Functionality
 * Search, Reading Progress, Form Validation, and More
 */

// =================================================================
// Search Functionality
// =================================================================
class SiteSearch {
  constructor() {
    this.searchIndex = null;
    this.searchInput = document.getElementById('search-input');
    this.searchResults = document.getElementById('search-results');
    
    if (this.searchInput) {
      this.init();
    }
  }
  
  async init() {
    // Load search index
    try {
      const response = await fetch('/index.json');
      const data = await response.json();
      this.searchIndex = data.pages;
    } catch (error) {
      console.error('Failed to load search index:', error);
    }
    
    // Set up event listeners
    this.searchInput.addEventListener('input', this.debounce(() => this.search(), 300));
  }
  
  search() {
    const query = this.searchInput.value.toLowerCase().trim();
    
    if (query.length < 2) {
      this.clearResults();
      return;
    }
    
    const results = this.searchIndex.filter(page => {
      return (
        page.title.toLowerCase().includes(query) ||
        page.content.toLowerCase().includes(query) ||
        (page.tags && page.tags.some(tag => tag.toLowerCase().includes(query))) ||
        (page.categories && page.categories.some(cat => cat.toLowerCase().includes(query)))
      );
    });
    
    this.displayResults(results, query);
  }
  
  displayResults(results, query) {
    if (!this.searchResults) return;
    
    if (results.length === 0) {
      this.searchResults.innerHTML = `
        <p class="search-no-results">No results found for "${query}". Try a different search term.</p>
      `;
      return;
    }
    
    const html = `
      <p class="search-results-count">${results.length} result${results.length === 1 ? '' : 's'} found</p>
      ${results.map(result => this.renderResult(result, query)).join('')}
    `;
    
    this.searchResults.innerHTML = html;
  }
  
  renderResult(result, query) {
    // Highlight matching text
    const highlightedContent = this.highlightText(result.content, query);
    
    return `
      <div class="search-result-item">
        <h3><a href="${result.url}">${this.highlightText(result.title, query)}</a></h3>
        <p>${highlightedContent}</p>
        <div class="search-result-meta">
          <span>${result.section}</span>
          ${result.date ? `<span>${result.date}</span>` : ''}
        </div>
      </div>
    `;
  }
  
  highlightText(text, query) {
    const regex = new RegExp(`(${this.escapeRegex(query)})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
  }
  
  escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }
  
  clearResults() {
    if (this.searchResults) {
      this.searchResults.innerHTML = '';
    }
  }
  
  debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  }
}

// =================================================================
// Reading Progress Indicator
// =================================================================
class ReadingProgress {
  constructor() {
    this.progressBar = document.querySelector('.reading-progress-bar');
    this.article = document.querySelector('article') || document.querySelector('.prose');
    
    if (this.progressBar && this.article) {
      this.init();
    }
  }
  
  init() {
    window.addEventListener('scroll', () => this.updateProgress());
    window.addEventListener('resize', () => this.updateProgress());
    this.updateProgress();
  }
  
  updateProgress() {
    const articleTop = this.article.offsetTop;
    const articleHeight = this.article.offsetHeight;
    const windowHeight = window.innerHeight;
    const scrollTop = window.scrollY;
    
    // Calculate progress
    const start = articleTop - windowHeight;
    const end = articleTop + articleHeight;
    const current = scrollTop - start;
    const total = end - start;
    
    let progress = (current / total) * 100;
    progress = Math.max(0, Math.min(100, progress));
    
    this.progressBar.style.width = `${progress}%`;
  }
}

// =================================================================
// Form Validation
// =================================================================
class FormValidator {
  constructor(form) {
    this.form = form;
    this.init();
  }
  
  init() {
    this.form.addEventListener('submit', (e) => this.handleSubmit(e));
    
    // Real-time validation
    const inputs = this.form.querySelectorAll('input, textarea, select');
    inputs.forEach(input => {
      input.addEventListener('blur', () => this.validateField(input));
      input.addEventListener('input', () => this.clearError(input));
    });
  }
  
  handleSubmit(e) {
    const inputs = this.form.querySelectorAll('input, textarea, select');
    let isValid = true;
    
    inputs.forEach(input => {
      if (!this.validateField(input)) {
        isValid = false;
      }
    });
    
    if (!isValid) {
      e.preventDefault();
      // Focus first invalid field
      const firstError = this.form.querySelector('.error input, .error textarea, .error select');
      if (firstError) {
        firstError.focus();
      }
    }
  }
  
  validateField(input) {
    const formGroup = input.closest('.form-group') || input.parentElement;
    let isValid = true;
    let message = '';
    
    // Required validation
    if (input.required && !input.value.trim()) {
      isValid = false;
      message = 'This field is required';
    }
    
    // Email validation
    if (input.type === 'email' && input.value) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(input.value)) {
        isValid = false;
        message = 'Please enter a valid email address';
      }
    }
    
    // Min length validation
    if (input.minLength > 0 && input.value.length < input.minLength) {
      isValid = false;
      message = `Must be at least ${input.minLength} characters`;
    }
    
    // Update UI
    if (!isValid) {
      this.showError(formGroup, message);
    } else {
      this.clearError(input);
    }
    
    return isValid;
  }
  
  showError(formGroup, message) {
    formGroup.classList.add('error');
    
    // Remove existing error message
    const existingError = formGroup.querySelector('.form-error-message');
    if (existingError) {
      existingError.remove();
    }
    
    // Add error message
    const errorElement = document.createElement('span');
    errorElement.className = 'form-error-message';
    errorElement.textContent = message;
    formGroup.appendChild(errorElement);
  }
  
  clearError(input) {
    const formGroup = input.closest('.form-group') || input.parentElement;
    formGroup.classList.remove('error');
    const errorElement = formGroup.querySelector('.form-error-message');
    if (errorElement) {
      errorElement.remove();
    }
  }
}

// =================================================================
// Estimated Reading Time
// =================================================================
function calculateReadingTime(text) {
  const wordsPerMinute = 200;
  const words = text.trim().split(/\s+/).length;
  const minutes = Math.ceil(words / wordsPerMinute);
  return minutes;
}

function displayReadingTime() {
  const article = document.querySelector('article .prose') || document.querySelector('.post-content');
  const readingTimeElement = document.querySelector('.reading-time');
  
  if (article && readingTimeElement) {
    const minutes = calculateReadingTime(article.textContent);
    readingTimeElement.textContent = `${minutes} min read`;
  }
}

// =================================================================
// Copy to Clipboard
// =================================================================
function initCopyButtons() {
  // Code blocks
  document.querySelectorAll('pre code').forEach(block => {
    const button = document.createElement('button');
    button.className = 'copy-button';
    button.innerHTML = '📋 Copy';
    button.addEventListener('click', () => copyToClipboard(block.textContent, button));
    
    const wrapper = block.closest('pre');
    wrapper.style.position = 'relative';
    wrapper.appendChild(button);
  });
  
  // Share links
  document.querySelectorAll('[data-copy]').forEach(element => {
    element.addEventListener('click', (e) => {
      e.preventDefault();
      const textToCopy = element.dataset.copy || window.location.href;
      copyToClipboard(textToCopy, element);
    });
  });
}

function copyToClipboard(text, button) {
  navigator.clipboard.writeText(text).then(() => {
    const originalText = button.innerHTML;
    button.innerHTML = '✓ Copied!';
    button.classList.add('copied');
    
    setTimeout(() => {
      button.innerHTML = originalText;
      button.classList.remove('copied');
    }, 2000);
  }).catch(err => {
    console.error('Failed to copy:', err);
  });
}

// =================================================================
// Lazy Loading Images
// =================================================================
function initLazyLoading() {
  if ('IntersectionObserver' in window) {
    const lazyImages = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
          observer.unobserve(img);
        }
      });
    }, {
      rootMargin: '50px 0px'
    });
    
    lazyImages.forEach(img => imageObserver.observe(img));
  }
}

// =================================================================
// Smooth Anchor Links
// =================================================================
function initSmoothAnchors() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        
        const headerOffset = 80;
        const elementPosition = targetElement.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
        
        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
        
        // Update URL
        history.pushState(null, null, targetId);
      }
    });
  });
}

// =================================================================
// Print Article
// =================================================================
function initPrintButton() {
  const printButton = document.querySelector('.print-article');
  if (printButton) {
    printButton.addEventListener('click', () => {
      window.print();
    });
  }
}

// =================================================================
// Keyboard Navigation
// =================================================================
function initKeyboardNav() {
  document.addEventListener('keydown', (e) => {
    // ESC to close modals
    if (e.key === 'Escape') {
      const modal = document.querySelector('.modal.active');
      if (modal) {
        modal.classList.remove('active');
      }
      
      const mobileMenu = document.querySelector('.nav-menu.active');
      if (mobileMenu) {
        mobileMenu.classList.remove('active');
      }
    }
    
    // / to focus search
    if (e.key === '/' && !e.target.matches('input, textarea')) {
      e.preventDefault();
      const searchInput = document.getElementById('search-input');
      if (searchInput) {
        searchInput.focus();
      }
    }
  });
}

// =================================================================
// External Links
// =================================================================
function markExternalLinks() {
  document.querySelectorAll('a[href^="http"]').forEach(link => {
    if (!link.href.includes(window.location.hostname)) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');
      
      // Add external link indicator if not already present
      if (!link.querySelector('.external-icon')) {
        const icon = document.createElement('span');
        icon.className = 'external-icon';
        icon.innerHTML = ' ↗';
        icon.style.fontSize = '0.8em';
        link.appendChild(icon);
      }
    }
  });
}

// =================================================================
// Initialize All Features
// =================================================================
document.addEventListener('DOMContentLoaded', () => {
  // Initialize components
  new SiteSearch();
  new ReadingProgress();
  
  // Initialize forms
  document.querySelectorAll('form:not([data-no-validate])').forEach(form => {
    new FormValidator(form);
  });
  
  // Initialize utilities
  displayReadingTime();
  initCopyButtons();
  initLazyLoading();
  initSmoothAnchors();
  initPrintButton();
  initKeyboardNav();
  markExternalLinks();
});

// Export for use in other scripts
window.ProfYNot = {
  SiteSearch,
  ReadingProgress,
  FormValidator,
  copyToClipboard
};
