import os
import shutil

folder = input("Enter Folder Path to organize: ")

if not os.path.exists(folder):
    print("Error: The folder does not exist.")
else:
    files = os.listdir(folder)

    images_count = 0
    documents_count = 0 
    videos_count = 0
    others_count = 0

    images_folder = 0
os

