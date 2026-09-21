import pathlib as p

def get_category(file_path):
    # Return the category based on the extension.
    ext = p.Path(file_path).suffix.lower()
    if ext in [".jpg", ".jpeg", ".png", ".gif"]:
        return "images"
    elif ext in [".mp4", ".avi", ".mov", ".mkv"]:
        return "videos"
    elif ext in [".mp3", ".wav", ".flac"]:
        return "audio"
    elif ext in [".pdf", ".doc", ".docx", ".txt"]:
        return "documents"
    elif ext in [".zip", ".rar", ".tar", ".gz"]:
        return "archives"
    else:
        return "others"

def organise(folder, apply=False):
    # Inspect files, choose destinations, then preview or move.
    pass

def main():
    # Read command-line arguments and call organise().
    pass

if __name__ == "__main__":
    main()