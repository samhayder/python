# try:
# except:
# else:
# finally:

try:
    file = open('data.txt')
    dicts = {"key":"value"}
    print(dicts['asas'])
except FileNotFoundError as error:
    file = open('data.txt','w')
    file.write("Here is the some data.")
    print(f"{error}")
except KeyError as error:
    print(f"{error} does not exit")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")
    
fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
  try:
    fruit = fruits[index]
  except IndexError:
    print("Fruit pie")
  else:
    print(fruit + " pie")
 
make_pie(4)




    