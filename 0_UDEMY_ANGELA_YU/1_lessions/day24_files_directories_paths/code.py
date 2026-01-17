# Read file
with open(r"0_UDEMY_ANGELA_YU\\1_lessions\\day24_files_directories_paths\\readme.txt") as file:
    content = file.read()
    print(content)
    
# Write file
with open(r"0_UDEMY_ANGELA_YU\\1_lessions\\day24_files_directories_paths\\readme.txt", mode='a') as file:
    file.write("\nI'm professional web coder.")
    