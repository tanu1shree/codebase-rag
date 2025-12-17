import os

CODE_EXTENSIONS = {".py", ".js", ".ts", ".java", ".go", ".rs", ".md"}

EXCLUDE_FILES = {"main.py"}

def load_codebase(repo_path):
    files = []

    for root, dirs, filenames in os.walk(repo_path):
        dirs[:] = [
            d for d in dirs
            if d not in {".git", "venv", "__pycache__", "node_modules"}
        ]

        for filename in filenames:
            if filename in EXCLUDE_FILES:
                continue

            ext = os.path.splitext(filename)[1]
            if ext in CODE_EXTENSIONS:
                path = os.path.join(root, filename)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        files.append({
                            "path": path,
                            "content": content
                        })
                except Exception as e:
                    print(f"Skipped {path}: {e}")

    return files

if __name__ == "__main__":
    repo_path = "."
    code_files = load_codebase(repo_path)
    print(f"Loaded {len(code_files)} code files.")