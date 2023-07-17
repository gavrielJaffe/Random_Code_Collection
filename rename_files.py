import os
import shutil

def rename_and_move_files(folder_path, new_folder_path):
    files = os.listdir(folder_path)
    files.sort()

    count = 1
    for file in files:
        if file.lower().endswith(".txt"):
            file_extension = os.path.splitext(file)[1]
            new_file_name = f"{count}{file_extension}"
            old_file_path = os.path.join(folder_path, file)
            new_file_path = os.path.join(new_folder_path, new_file_name)
            shutil.move(old_file_path, new_file_path)
            count += 1

    print("Files have been renamed and moved successfully!")

# Specify the folder path where the files are currently located ,Take the files from 
folder_path = "/home/simulation/PycharmProjects/yolo_alex/data/labels/train"

# Specify the new folder path where the renamed files should be moved ,Path to output
new_folder_path = "/home/simulation/PycharmProjects/yolo_alex/data/images/our_txt_shit"

# Create the new folder if it doesn't exist
os.makedirs(new_folder_path, exist_ok=True)

# Call the rename_and_move_files function
rename_and_move_files(folder_path, new_folder_path)