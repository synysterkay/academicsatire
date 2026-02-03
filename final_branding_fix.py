import os

def replace_in_files(directory, old_text, new_text):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if old_text in content:
                    new_content = content.replace(old_text, new_text)
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {path}")

if __name__ == "__main__":
    base_path = os.path.join(os.getcwd(), "content")
    print(f"Starting replacement in {base_path}")
    replace_in_files(base_path, "Prof Y Not", "Academic Satire")
    print("Replacement complete.")
