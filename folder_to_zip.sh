#!/bin/bash

# Check if a folder name or path is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <folder>"
  echo "Please provide a folder name or path as an argument."
  exit 1
fi

# Specify the folder name or path
folder_path=$(realpath "$1")

# Check if the specified folder exists
if [ ! -d "$folder_path" ]; then
  echo "The specified folder does not exist."
  exit 1
fi

# Extract the folder name from the provided path
folder_name=$(basename "$folder_path")

# Specify the output directory
output_dir="/home/jj/Desktop/"

# Create a timestamp in the format YYYY-MM-DD-HH-MM-SS
timestamp=$(date +"%Y-%m-%d-%H-%M-%S")

# Specify the zip file name with the desired output directory, folder name, and timestamp
zip_filename="${output_dir}/${folder_name}_${timestamp}.zip"
# zip_filename="${output_dir}/${folder_name}.zip" # With no time file stamp


# Change the current working directory to the parent directory of the specified folder
cd "$(dirname "$folder_path")" || exit

# Create the zip file
zip -r "$zip_filename" "$folder_name"

# Check if the zip file was created successfully
if [ $? -eq 0 ]; then
  echo "Zip file created successfully: $zip_filename"
else
  echo "Failed to create the zip file."
fi
