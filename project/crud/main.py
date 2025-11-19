from pathlib import Path

# create function to show file & folder current directory
def showFileAndFolder(folderName):
  try:
    path = Path(folderName)
    if not path.exists:
      print(f"Folder '{folderName}' not found.")
      return
    
    items = list(path.glob('*'))

    if not items:
      print(f"No items found inside '{folderName}'")

    else:
      for i, item in enumerate(items, start=1):
        print(f"{i}: {items}")
    
  except Exception as err:
    print(f"An error occurred by {err}")

# create function to create file name with write data
def createFile():
  try:
    showFileAndFolder('/project/crud/')

    name = input("Write your file name with extension. ")
    path = Path(name)
    data = input("Write your text to created this file. ")

    with open(path, 'w') as fs:
      fs.write(data)
    
    print("CREATED FILE SUCCESSFULLY.")

  except Exception as err:
    print(f"An error occurred by {err}")


# create function to read data to selected file
def readFile():
  try:
    showFileAndFolder('/project/crud/')

    name = input("Write your file name. ")
    path = Path(name)

    if path.exists and path.is_file:
      with open(path,'r') as fs:
       fs.read()
    
      print("FILE READ SUCCESSFULLY.")
    else:
      print("File is not exist. To crate the file.")
    
  except Exception as err:
    print(f"An error occurred by {err}")







print("Press 1 for create a file. ")
print("Press 2 for read the file. ")
print("Press 3 for update the file. ")
print("Press 4 for delete the file. ")

press = int(input("Write 1-4 to choose your action. "))

if press == 1:
  createFile() 

if press == 2:
  readFile() 