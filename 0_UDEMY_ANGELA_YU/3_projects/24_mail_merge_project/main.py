#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: 
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

ROOT = "0_UDEMY_ANGELA_YU/3_projects/24_mail_merge_project"

old_name = "[name]"

with open(f"{ROOT}/Input/Names/invited_names.txt") as file:
    name_lists = file.readlines()
    
with open (f"{ROOT}/Input/Letters/starting_letter.txt",'r') as file:
    letter = file.read()
    
for name_item in name_lists:
    new_name = name_item.strip()
    replace_name_with_letter = letter.replace(old_name,new_name)
    
    with open(f"{ROOT}/\Output\ReadyToSend\letter_of_{new_name}.txt", mode='w') as file:
        create_letter = file.write(replace_name_with_letter)
        
            