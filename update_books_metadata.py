import os
import random
import re

BOOKS_DIR = "/Volumes/Flow/ProfYnot website/content/books/"
IMAGES = [
    "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=800&q=80",
    "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800&q=80",
    "https://images.unsplash.com/photo-1491841573634-21f43501750e?w=800&q=80",
    "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=800&q=80",
    "https://images.unsplash.com/photo-1532012197367-6309818b7147?w=800&q=80",
    "https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=800&q=80",
    "https://images.unsplash.com/photo-1589998059171-988d887df646?w=800&q=80",
    "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=800&q=80",
    "https://images.unsplash.com/photo-1463320726281-696a485928c7?w=800&q=80",
    "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=800&q=80"
]

def update_book(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update coverImage
    new_image = random.choice(IMAGES)
    content = re.sub(r'coverImage: ".*"', f'coverImage: "{new_image}"', content)
    content = re.sub(r'ogImage: ".*"', f'ogImage: "{new_image}"', content)

    # Update rating
    rating = round(random.uniform(4.4, 4.9), 1)
    if 'rating:' in content:
        content = re.sub(r'rating: ".*"', f'rating: "{rating}"', content)
    else:
        content = content.replace('draft: false', f'draft: false\nrating: "{rating}"')

    # Update ratingCount
    count = random.randint(120, 850)
    if 'ratingCount:' in content:
        content = re.sub(r'ratingCount: \d+', f'ratingCount: {count}', content)
    else:
        content = content.replace(f'rating: "{rating}"', f'rating: "{rating}"\nratingCount: {count}')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for filename in os.listdir(BOOKS_DIR):
    if filename.endswith(".md") and filename != "_index.md":
        update_book(os.path.join(BOOKS_DIR, filename))

print("Successfully updated book metadata.")
