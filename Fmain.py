import os
import shutil


directory = os.path.join(os.path.expanduser("~"), "Downloads")


file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar.gz"]
}

# Process each file in the directory

for file in os.listdir(directory):
    file_path = os.path.join(directory, file)

    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file_path)[1].lower()

        moved = False
        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                destination_path = os.path.join(folder_path, file)
                shutil.move(file_path, destination_path)
                print(f"Moved {file} to {folder_name} folder.")
                moved = True
                break

        if not moved:
            print(f"Skipped {file}. Unknown file extension.")

    else:
        print(f"Skipped {file}. It is a directory.")

print("File organization complete.")
print("All files have been organized into their respective folders.")
