import os
import re
import random
import shutil
import zipfile
import jumble_alphabetic_list

#Program structure
#   Take form input
#   Generate new file names (alphabetical) for each charindex in message input
#   Copy the appropriate images (alphabet) from ALPHABET folder to new folder and and rename images
#   Jumble the new file names by adding numbers to file names in different places

#Set variables
folder_alphabet = "alphabet" #Path to folder containing all images of the alphabet
file_extension = ".jpg" #file extension of the images
original_path = os.getcwd() #current directory
message_name = input('What do you want to call this message? ') #will be the name of the folder created
person = input('Enter your name: ')
message_text = input('Message: ')
printed_message = "The folder name will be '{}' and your message and signature will be {} Secretly, {}'"
print(printed_message.format(message_name, message_text, person))

full_printed_message = message_text + " Secretly, {}".format(person)
# Function to create a new folder with the message name provided in the current working directory
def create_folder(folder_name):
    # If the message name does not exist as a folder name, create it
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    #if a folder already exists with that name ask for a new one
    else:
        folder_name = input('Pick a different name for this message? ')
        create_folder(folder_name)

# Function to copy the appropriate letter image from the alphabet folder to the new message folder.
def copy_file(src, dest):
    print(src + " :: " + dest)
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print("Error: %s" % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print("Error: %s" % e.strerror)
# Rename message_name to remove non-alphanumeric characters
message_name = re.sub("[^0-9a-zA-Z]+", "_", message_name)
# Create a zipfile with the new message_name
#zip_file = zipfile.ZipFile(message_name + ".zip", mode="w")
# Call function to create the new folder for the message images
create_folder(message_name)

text_alphabet = "abcdefghijklmnopqrstuvwxyz"
message_length = len(full_printed_message)
letter_index = 0

# Function to look for specific characters in the message for punctuation
def letter_file(lett):
    lett_file = str()
    if lett == ",":
        lett_file = "_comma"
    elif lett == ".":
        lett_file = "_period"
    elif lett == " ":
        lett_file = "_space"
    elif lett == "?":
        lett_file = "_question"
    elif lett == "!":
        lett_file = "_exclamation"
    else:
        lett_file = lett
    return lett_file



word_list = []
for letter in full_printed_message:
    generated_word = ""
    letter_count = 0
    while letter_count < 10:
        selected_letter = text_alphabet[random.randint(0, 25)]
        generated_word += selected_letter
        letter_count += 1
    word_list.append(generated_word)
word_list.sort()
#print(word_list)

for index, item in enumerate(full_printed_message):
    letter_file_name = letter_file(item)
    letter_file_name = letter_file_name + file_extension
    new_name = word_list[index]
    new_letter_file_name = new_name + file_extension
    #print(letter_file_name + " :: " + new_letter_file_name)
    copy_file(folder_alphabet + "/" + letter_file_name, message_name + "/" + new_letter_file_name)
    letter_index += letter_index

jumble_alphabetic_list.rename_files(message_name)

shutil.make_archive(message_name, 'zip', message_name)
