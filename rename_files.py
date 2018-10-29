# Import the necessary libraries
import os

#Funtion to rename all of the files in a specified folder to strip all numbers
#   from the file name
def rename_files(folder_name):
    #(1) Define the current working directory
    original_path = os.getcwd()
    #(2) Define the path to the .JPG files to rename
    images_file_path = folder_name #"[FULL PATH TO FOLDER CONTAINING .JPG FILES]"
    #(3) get the files names from a folder
    file_list = os.listdir(images_file_path)
    #print(file_list)
    #(4) Change the current working directory to the images_file_path
    os.chdir(images_file_path)
    #(5) Loop (for) to rename each file
    for file_name in file_list:
        #(6) Define the new file name by stripping out numbers from the original name
        new_file_name = ''.join([num for num in file_name if not num.isdigit()])
        #(7) Rename the file
        os.rename(file_name, new_file_name)
        #(8) Print the old and new file name
        printout = "Old file name: {}  ---  New file name: {}"
        print(printout.format(file_name, new_file_name))
    #(9) Change the current working directory back to the original_path
    os.chdir(original_path)

folder = input("What is the name of the folder to decode?")
rename_files(folder)
