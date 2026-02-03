import os

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Variations to catch
        new_content = content.replace("profynot.com", "academicsatire.com")
        new_content = new_content.replace("Prof Y Not", "Academic Satire")
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
    return False

content_dir = "/Volumes/Flow/ProfYnot website/content"
count = 0
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            if replace_in_file(os.path.join(root, file)):
                count += 1

print(f"Updated {count} files.")
