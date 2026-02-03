import os
import re

books_data = [
    {"slug": "how-to-be-late-even-when-you-start-early", "cover": "https://m.media-amazon.com/images/I/91HiLxrp-XL._SL1500_.jpg"},
    {"slug": "how-to-be-exhausted-by-decisions-that-dont-matter", "cover": "https://m.media-amazon.com/images/I/9179uhuLOFL._SL1500_.jpg"},
    {"slug": "how-to-achieve-burnout-without-achieving-anything", "cover": "https://m.media-amazon.com/images/I/91WigqKWRqL._SL1500_.jpg"},
    {"slug": "why-everyone-is-wrong-except-me", "cover": "https://m.media-amazon.com/images/I/91FHiKJgScL._SL1500_.jpg"},
    {"slug": "why-success-feels-illegal-to-me", "cover": "https://m.media-amazon.com/images/I/91IW1g2bjQL._SL1500_.jpg"},
    {"slug": "why-do-i-hate-everyone-before-coffee", "cover": "https://m.media-amazon.com/images/I/91V1eWVBVwL._SL1500_.jpg"},
    {"slug": "i-promise-ill-start-tomorrow", "cover": "https://m.media-amazon.com/images/I/71jaxaBc0HL._SL1499_.jpg"},
    {"slug": "why-am-i-tired-after-doing-nothing-all-day", "cover": "https://m.media-amazon.com/images/I/91tHS6muSQL._SL1500_.jpg"},
    {"slug": "im-not-lazy-im-on-energy-saving-mode", "cover": "https://m.media-amazon.com/images/I/91XlR1IxWAL._SL1500_.jpg"},
    {"slug": "i-have-no-idea-what-i-am-doing-but-its-working", "cover": "https://m.media-amazon.com/images/I/91mdheGdhSL._SL1500_.jpg"},
    {"slug": "how-to-ruin-your-life-with-one-bad-decision", "cover": "https://m.media-amazon.com/images/I/910TsYMGVYL._SL1500_.jpg"},
    {"slug": "how-to-be-productive-without-producing-anything", "cover": "https://m.media-amazon.com/images/I/91o3z8RJ5TL._SL1500_.jpg"},
    {"slug": "how-to-be-broke-with-confidence", "cover": "https://m.media-amazon.com/images/I/91q6nJuywkL._SL1500_.jpg"},
    {"slug": "how-to-politely-tell-someone-that-you-dont-like-them", "cover": "https://m.media-amazon.com/images/I/71-tFh9st8L._SL1500_.jpg"},
    {"slug": "how-can-you-face-your-problem-when-the-problem-is-your-face", "cover": "https://m.media-amazon.com/images/I/71NDLPEIUCL._SL1500_.jpg"},
    {"slug": "how-can-i-double-my-body-fat-and-give-it-to-the-next-person", "cover": "https://m.media-amazon.com/images/I/711nFogc2pL._SL1500_.jpg"},
    {"slug": "how-to-hold-in-your-fart-when-talking-to-your-crush", "cover": "https://m.media-amazon.com/images/I/81z4n4qYxQL._SL1500_.jpg"},
    {"slug": "how-to-fart-and-blame-it-on-someone", "cover": "https://m.media-amazon.com/images/I/81SeN2VjMIL._SL1500_.jpg"},
    {"slug": "how-to-dodge-the-barber-s-sausage", "cover": "https://m.media-amazon.com/images/I/81aaZf3oKWL._SL1500_.jpg"},
    {"slug": "how-to-dodge-the-barbers-sausage", "cover": "https://m.media-amazon.com/images/I/81aaZf3oKWL._SL1500_.jpg"}
]

BLOG_DIR = "/Volumes/Flow/ProfYnot website/content/blog/"

def update_blog(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Try to find a matching book cover based on the blog slug
    filename = os.path.basename(file_path)
    blog_slug = filename.replace("-blog.md", "").replace(".md", "")
    
    # Check if slug matches any book slug
    book_data = next((b for b in books_data if b['slug'] == blog_slug), None)
    
    if book_data:
        content = re.sub(r'ogImage: ".*"', f'ogImage: "{book_data["cover"]}"', content)
        # Also replace image inside body
        content = re.sub(r'!\[.*\]\(https://images\.unsplash\.com/.*\)', f'![{book_data["slug"]} Cover]({book_data["cover"]})', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Updated blog: {filename}")
    else:
        # Fallback cover for non-book blogs
        fallback = "https://m.media-amazon.com/images/I/91FHiKJgScL._SL1500_.jpg"
        content = re.sub(r'ogImage: ".*"', f'ogImage: "{fallback}"', content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Updated blog (fallback): {filename}")

for filename in os.listdir(BLOG_DIR):
    if filename.endswith(".md") and filename != "_index.md":
        update_blog(os.path.join(BLOG_DIR, filename))

print("Applied real Amazon covers to all blog posts.")
