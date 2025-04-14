import os
import shutil

# Define file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

# Folder path to organize (example: Desktop)
folder_path = os.path.expanduser("~/Desktop")  # change path if needed

def create_folder_if_not_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def organize_files():
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False
            for folder_name, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    target_folder = os.path.join(folder_path, folder_name)
                    create_folder_if_not_exists(target_folder)
                    shutil.move(file_path, os.path.join(target_folder, file))
                    print(f"Moved: {file} --> {folder_name}/")
                    moved = True
                    break
            if not moved:
                others_folder = os.path.join(folder_path, "Others")
                create_folder_if_not_exists(others_folder)
                shutil.move(file_path, os.path.join(others_folder, file))
                print(f"Moved: {file} --> Others/")

if __name__ == "__main__":
    print("📂 Organizing files...")
    organize_files()
    print("✅ Done!")
