/**
 * Prof Y Not - Premium Author Website
 * Clean, Modern JavaScript - 2026 Edition
 */

(function() {
  'use strict';

  // ============================================
  // DOM Ready
  // ============================================
  const ready = (fn) => {
    if (document.readyState !== 'loading') {
      fn();
    } else {
      document.addEventListener('DOMContentLoaded', fn);
    }
  };

  ready(() => {
    initThemeToggle();
    initHeader();
    initMobileNav();
    initSmoothScroll();
    initRevealAnimations();
    initScrollHint();
  });

  // ============================================
  // Theme Toggle (Dark/Light Mode)
  // ============================================
  function initThemeToggle() {
    const toggle = document.querySelector('.theme-toggle');
    const html = document.documentElement;
    
    const getPreferredTheme = () => {
      const saved = localStorage.getItem('theme');
      if (saved) return saved;
      return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    };
    
    const setTheme = (theme) => {
      html.setAttribute('data-theme', theme);
      localStorage.setItem('theme', theme);
    };
    
    // Initialize
    setTheme(getPreferredTheme());
    
    if (toggle) {
      toggle.addEventListener('click', () => {
        const current = html.getAttribute('data-theme');
        setTheme(current === 'dark' ? 'light' : 'dark');
      });
    }
    
    // Listen for system changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      if (!localStorage.getItem('theme')) {
        setTheme(e.matches ? 'dark' : 'light');
      }
    });
  }

  // ============================================
  // Header Scroll Effects
  // ============================================
  function initHeader() {
    const header = document.querySelector('.header');
    if (!header) return;
    
    let lastScroll = 0;
    let ticking = false;
    
    const updateHeader = () => {
      const currentScroll = window.pageYOffset;
      
      // Add scrolled class after 50px
      if (currentScroll > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
      
      // Hide/show header on scroll direction (optional - only for non-hero pages)
      if (!header.classList.contains('on-hero') && currentScroll > 300) {
        if (currentScroll > lastScroll) {
          header.style.transform = 'translateY(-100%)';
        } else {
          header.style.transform = 'translateY(0)';
        }
      } else {
        header.style.transform = 'translateY(0)';
      }
      
      lastScroll = currentScroll;
      ticking = false;
    };
    
    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(updateHeader);
        ticking = true;
      }
    }, { passive: true });
  }

  // ============================================
  // Mobile Navigation
  // ============================================
  function initMobileNav() {
    const toggle = document.querySelector('.mobile-toggle');
    const mobileNav = document.querySelector('.mobile-nav');
    const header = document.querySelector('.header');
    
    if (!toggle || !mobileNav) return;
    
    toggle.addEventListener('click', () => {
      const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
      
      toggle.setAttribute('aria-expanded', !isExpanded);
      toggle.classList.toggle('active');
      mobileNav.classList.toggle('open');
      header.classList.toggle('nav-open');
      
      // Prevent body scroll when nav is open
      document.body.style.overflow = isExpanded ? '' : 'hidden';
    });
    
    // Close on link click
    mobileNav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        toggle.setAttribute('aria-expanded', 'false');
        toggle.classList.remove('active');
        mobileNav.classList.remove('open');
        header.classList.remove('nav-open');
        document.body.style.overflow = '';
      });
    });
    
    // Close on escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileNav.classList.contains('open')) {
        toggle.setAttribute('aria-expanded', 'false');
        toggle.classList.remove('active');
        mobileNav.classList.remove('open');
        header.classList.remove('nav-open');
        document.body.style.overflow = '';
      }
    });
  }

  // ============================================
  // Smooth Scroll
  // ============================================
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return;
        
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          
          const headerHeight = document.querySelector('.header')?.offsetHeight || 80;
          const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;
          
          window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
          });
        }
      });
    });
  }

  // ============================================
  // Reveal Animations on Scroll
  // ============================================
  function initRevealAnimations() {
    const reveals = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
    
    if (reveals.length === 0) return;
    
    // Use Intersection Observer for performance
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
          // Stagger animations slightly
          setTimeout(() => {
            entry.target.classList.add('visible');
          }, index * 50);
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -80px 0px'
    });
    
    reveals.forEach(el => observer.observe(el));
  }

  // ============================================
  // Scroll Hint
  // ============================================
  function initScrollHint() {
    const scrollHint = document.querySelector('.scroll-hint');
    if (!scrollHint) return;
    
    // Hide scroll hint after scrolling
    let hidden = false;
    window.addEventListener('scroll', () => {
      if (!hidden && window.pageYOffset > 100) {
        scrollHint.style.opacity = '0';
        scrollHint.style.visibility = 'hidden';
        hidden = true;
      }
    }, { passive: true });
    
    // Click to scroll to featured section
    scrollHint.addEventListener('click', () => {
      const featured = document.querySelector('#featured');
      if (featured) {
        const headerHeight = document.querySelector('.header')?.offsetHeight || 80;
        window.scrollTo({
          top: featured.offsetTop - headerHeight,
          behavior: 'smooth'
        });
      }
    });
  }

  // ============================================
  // Newsletter Form (Optional Enhancement)
  // ============================================
  const newsletterForm = document.querySelector('.newsletter-form');
  if (newsletterForm) {
    newsletterForm.addEventListener('submit', function(e) {
      const btn = this.querySelector('button[type="submit"]');
      if (btn) {
        btn.innerHTML = '<span class="loading"></span> Subscribing...';
        btn.disabled = true;
      }
    });
  }

})();
