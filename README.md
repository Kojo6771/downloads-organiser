# Downloads Organiser 🐍

A small Python script that organises files into folders based on their file extensions. Built to practise Python while solving an everyday problem: a cluttered Downloads folder.

## Features

- Preview planned moves before making changes.
- Sort files into categories automatically.
- Skip files when the destination filename already exists.
- Leave existing directories untouched.
- Use Python’s standard library—no additional packages required.

## File Categories

| Folder | Extensions |
|---|---|
| images | `.jpg`, `.jpeg`, `.png`, `.gif` |
| videos | `.mp4`, `.avi`, `.mov`, `.mkv` |
| audio | `.mp3`, `.wav`, `.flac` |
| documents | `.pdf`, `.doc`, `.docx`, `.txt` |
| archives | `.zip`, `.rar`, `.tar`, `.gz` |
| others | Unrecognised extensions or files without an extension |

Extensions are handled without regard to capitalisation, so `.JPG` and `.jpg` belong to the same category.

## Project Structure

```text
downloads-organiser/
├── organiser.py
├── README.md
└── sample_downloads/
    ├── photo.jpg
    ├── notes.txt
    └── mystery.xyz
```

The sample files are for testing and can be empty.

## Getting Started

You need Python 3 installed. `pathlib` is included with Python, so there is nothing extra to install.

Open a terminal in the project folder.

### Preview Changes

Inside `organiser.py`, set `main()` to:

```python
def main():
    organise("sample_downloads")
```

Run:

```bash
python organiser.py
```

The script prints the planned destinations without moving files or creating folders.

### Move Files

Enable moving by setting `apply=True`:

```python
def main():
    organise("sample_downloads", apply=True)
```

Save the script and run it again:

```bash
python organiser.py
```

The sample folder will look like this:

```text
sample_downloads/
├── images/
│   └── photo.jpg
├── documents/
│   └── notes.txt
└── others/
    └── mystery.xyz
```

### Organise Another Folder

Replace `"sample_downloads"` with the path to your chosen folder. For example, on Windows:

```python
def main():
    organise(r"C:\Users\YourName\Downloads")
```

Run the preview first. When you are happy with the destinations, add `apply=True` to move the files.

## How It Works

1. Read the files directly inside the selected folder.
2. Identify each file’s extension and category.
3. Build the destination path.
4. Skip the file if that destination already exists.
5. Preview the move, or create the category folder and move the file when `apply=True`.

## Current Limitations

- Files inside subfolders are not processed.
- Sorting uses file extensions, not file contents.
- Duplicate filenames are skipped rather than renamed.
- The folder and move setting are configured by editing `main()`.
- There is no undo feature yet.

## What I Practised

- Working with paths using `pathlib`
- Writing and calling functions
- Using loops and conditional logic
- Creating directories and moving files
- Checking for existing files before a move

## Future Improvements

- Command-line arguments for choosing a folder and enabling moves
- A summary of moved and skipped files
- Clearer handling of missing folders and permission errors
- A move history and undo option
