import os

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Order matters: replace domain first, then name
    new_content = content.replace("profynot.com", "academicsatire.com")
    new_content = new_content.replace("Prof Y Not", "Academic Satire")
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")

content_dir = "/Volumes/Flow/ProfYnot website/content/"
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            replace_in_file(os.path.join(root, file))

print("Cleanup complete.")
