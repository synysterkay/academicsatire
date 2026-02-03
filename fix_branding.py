import os

# Use relative path from the current directory
content_dir = "content"

print(f"Searching in: {os.path.abspath(content_dir)}")

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace("Prof Y Not", "Academic Satire")
    new_content = new_content.replace("profynot.com", "academicsatire.com")
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"FIXED: {path}")

for root, dirs, files in os.walk(content_dir):
    for name in files:
        if name.endswith(".md"):
            fix_file(os.path.join(root, name))
