# Calculate with History Project

#### Concept

1. user give input with expression (2+3)
2. save result with txt file
3. show result
4. user select-> history, clear, exit
5. history -> show all history to calculate
6. clear -> clear all data => show message()
7. exit -> exit the program => show message()

### Pseudo

1. Start the program
2. Define the name of the history file ("history.txt")

3. Start Loop forever (While True)
   a. Ask the user to calculation (8+5) or command - history,clear,exit
   b. If user enters "exit"
   (b.1) print a Goodby message
   (b.2) Exit the program
   c. If user enter "history"
   (c.1) TRY to open the history file for reading
   (c.2) If file exists and not empty, print each line (calculation)
   (c.3) If file doesn't exits or is empty, print "No history found"
   (c.4) Continue to the next loop
   d. If user enters "clear"
   (d.1) Open the history file and overwrite it with nothing (empty it)
   (d.2) print "History cleared"
   (d.3) continue to the next loop
