
import os
import shutil

path = r"C:/Users/Rakshita D/Downloads/new" #this is my folder directory

folder_names = {
    ".txt": "txt files",
    ".png": "png files",
    ".pdf": "pdf files",
    ".docx": "word files"
}

for folder in folder_names.values():
    folder_path = os.path.join(path, folder)
    os.makedirs(folder_path, exist_ok=True)

for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if not os.path.isfile(file_path):
        continue

    extension = os.path.splitext(file)[1].lower()

    if extension in folder_names:
        destination_folder = os.path.join(
            path, folder_names[extension]
        )
        destination_path = os.path.join(
            destination_folder, file
        )

        if not os.path.exists(destination_path):
            shutil.move(file_path, destination_path)
            print(f"Moved: {file}")
        else:
            print(f"Skipped (already exists): {file}")

print("File sorting completed!")
