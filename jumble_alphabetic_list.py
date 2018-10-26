# Import the necessary libraries
import os
import random

#Function to rename .JPG files to include random numbers at the start, end,
#   and somewhere else before the "." in order to jumble and alhabetized file list
def rename_files():
    #(1) Define the current working directory
    original_path = os.getcwd()
    #(2) Define the path to the .JPG files to rename
    images_file_path = "" #"[FULL PATH TO FOLDER CONTAINING .JPG FILES]"
    #(3) get the files names from th folder
    file_list = os.listdir(images_file_path)
    #print(file_list)
    #(4) Change the current working directory to the images_file_path
    os.chdir(images_file_path)
    #(5) Loop (for) to rename each file
    for file_name in file_list:
        #(6) Generate 3 sets of random numbers
        rand = random.randint(0, 99)
        rand2 = random.randint(0, 99)
        rand3 = random.randint(0, 99)
        #(7) Define/Pick a random character index between the start of the file
        #   name and the "."
        index = random.randint(0, file_name.find("."))
        #(8) Define the character index of the "."
        index2 = file_name.find(".")
        #(9) Create the new file name using the original and the random numbers
        #   defined above
        new_file_name = str(rand) + file_name[:index] + str(rand2) + file_name[index:index2] + str(rand3) + ".jpg"
        #(10) Rename the original file name with the new file name
        os.rename(file_name, new_file_name)
        #(11) Print the old and new file name
        printout = "Old file name: {}  ---  New file name: {}"
        print(printout.format(file_name, new_file_name))
    #(12) Change the current working directory back to the original_path
    os.chdir(original_path)

rename_files()
