
# 📂 Automatic File Sorter

A simple Python automation project that organizes files into separate folders based on their file extensions.

## 📌 About the Project

The Automatic File Sorter is a beginner-friendly Python script designed to reduce the effort of manually organizing files. It scans a specified directory and moves supported files into their corresponding folders.

## ✨ Features

- Automatically creates folders if they don't exist.
- Organizes files by extension.
- Supports `.txt`, `.png`, `.pdf`, and `.docx` files.
- Uses Python's built-in modules for file management.
- Helps keep directories clean and organized.

## 🛠️ Technologies Used

- **Python**
- `os` — for listing files and managing directories.
- `shutil` — for moving files between folders.

## 📁 Folder Structure

After running the script, the directory will look like this:

```text
new/
├── txt files/
├── png files/
├── pdf files/
├── word files/
├── notes.txt
├── photo.png
├── report.pdf
└── document.docx
```

The supported files will be moved into their respective folders.

## ⚙️ How It Works

1. Reads the files in the specified directory.
2. Creates folders for supported file types if needed.
3. Identifies each file's extension.
4. Moves supported files into their corresponding folders.

## 🚀 Getting Started

### Prerequisites

- Python 3 installed on your computer.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Rakshita-Dhavaleshwar/automatic-file-sorter.git
   ```

2. Open the project folder.

3. Open `file_sorter.py` and update the directory path to a folder on your computer.

4. Run the script:

   ```bash
   python file_sorter.py
   ```

## ⚠️ Important Notes

- Test the script using sample files in a test directory first.
- The script moves files rather than copying them.
- Only the file types supported by the script are organized.
- Review the directory path before running the program.

## 📚 What I Learned

- Working with files and directories in Python.
- Using `os` and `shutil` for file management.
- Automating repetitive tasks.
- Applying conditional statements and loops to a practical problem.

## 👩‍💻 Author

Rakshita Dhavaleshwar

---

⭐ If you find this project useful, feel free to star the repository!


