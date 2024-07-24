import os
import shutil
import sys

def copy_and_sort_files(src_dir, dest_dir):
    try:
        os.makedirs(dest_dir, exist_ok=True)
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)
            if os.path.isdir(item_path):
                copy_and_sort_files(item_path, os.path.join(dest_dir, item))
            elif os.path.isfile(item_path):
                ext = os.path.splitext(item)[1][1:].lower()
                dest_subdir = os.path.join(dest_dir, ext)
                os.makedirs(dest_subdir, exist_ok=True)
                shutil.copy2(item_path, dest_subdir)
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python script.py <source_directory> [destination_directory]")
        sys.exit(1)
    
    source_directory = sys.argv[1]
    destination_directory = sys.argv[2] if len(sys.argv) > 2 else "dist"
    
    if not os.path.exists(source_directory):
        print(f"Директорія {source_directory} не існує.")
        sys.exit(1)
    
    copy_and_sort_files(source_directory, destination_directory)
    print(f"Файли успішно скопійовані та відсортовані в {destination_directory}.")
