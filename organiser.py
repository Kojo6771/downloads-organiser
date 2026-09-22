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

# Organise files in the specified folder into categories based on their extensions.
def organise(folder, apply=False):
    # Inspect files, choose destinations, then preview or move.
    folder = p.Path(folder)
    # Iterate over each file in the folder and determine its category.
    for file in folder.iterdir():
        if file.is_file():
            category = get_category(file)
            destination = folder / category
            target = destination / file.name

            # Check if the target file already exists to avoid overwriting.
            if target.exists():
                print(f"Target {target} already exists. Skipping {file}.")
                continue

            print(f"File: {file} -> Destination: {destination}")

            # Preview the planned move before actually performing it.
            if apply:
                destination.mkdir(exist_ok=True)
                file.rename(target)
                print(f"Moved {file} to {target}")
                print(f"Successfully moved {file.name} to {destination}")
                print(f"Finished processing {file.name}")
                print()  # Add a blank line for readability between file operations
                print(f"Destination folder: {destination}")
            else:
                print(f"Preview only: {file} would be moved to {destination}")
        else:
            print(f"Skipping {file} as it is not a file.")

    

def main():
    # Read command-line arguments and call organise().
    organise("sample_downloads", apply=True)




if __name__ == "__main__":
    main()