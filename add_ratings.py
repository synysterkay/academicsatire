#!/usr/bin/env python3
"""Add varied ratings (4.2-4.9) to book markdown files."""

import os
import random

BOOKS_DIR = "content/books"

# Predefined ratings for each book (looks more natural than pure random)
BOOK_RATINGS = {
    "how-can-i-double-my-body-fat-and-give-it-to-the-next-person.md": 4.6,
    "how-can-you-face-your-problem-when-the-problem-is-your-face.md": 4.4,
    "how-to-achieve-burnout-without-achieving-anything.md": 4.7,
    "how-to-be-broke-with-confidence.md": 4.5,
    "how-to-be-exhausted-by-decisions-that-dont-matter.md": 4.3,
    "how-to-be-late-even-when-you-start-early.md": 4.8,
    "how-to-be-productive-without-producing-anything.md": 4.6,
    "how-to-dodge-the-barbers-sausage.md": 4.2,
    "how-to-fart-and-blame-it-on-someone.md": 4.9,
    "how-to-hold-in-your-fart-when-talking-to-your-crush.md": 4.5,
    "how-to-politely-tell-someone-that-you-dont-like-them.md": 4.7,
    "how-to-ruin-your-life-with-one-bad-decision.md": 4.4,
    "i-have-no-idea-what-i-am-doing-but-its-working.md": 4.8,
    "i-promise-ill-start-tomorrow.md": 4.3,
    "im-not-lazy-im-on-energy-saving-mode.md": 4.6,
    "prof-or-not-here-i-come.md": 4.8,  # Keep existing
    "why-am-i-tired-after-doing-nothing-all-day.md": 4.5,
    "why-do-i-hate-everyone-before-coffee.md": 4.7,
    "why-everyone-is-wrong-except-me.md": 4.4,
    "why-success-feels-illegal-to-me.md": 4.6,
}

def add_rating_to_file(filepath, rating):
    """Add rating field after pages field in front matter."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Skip if already has rating in front matter
    if '\nrating:' in content.split('---')[1]:
        print(f"  Skipping {os.path.basename(filepath)} - already has rating")
        return
    
    # Find the pages line and add rating after it
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        new_lines.append(line)
        if line.startswith('pages:'):
            new_lines.append(f'rating: {rating}')
    
    with open(filepath, 'w') as f:
        f.write('\n'.join(new_lines))
    
    print(f"  Added rating {rating} to {os.path.basename(filepath)}")

def main():
    print("Adding ratings to books...\n")
    
    for filename, rating in BOOK_RATINGS.items():
        filepath = os.path.join(BOOKS_DIR, filename)
        if os.path.exists(filepath):
            add_rating_to_file(filepath, rating)
        else:
            print(f"  Warning: {filename} not found")
    
    print("\n✅ Done! All books now have varied ratings.")

if __name__ == "__main__":
    main()
