## Python one word story

  Each person inputs their name and then they are told the story so far, after reading they are allowed to add ONE word. Then that word is added and if that person inputs their name again they will be told they can not add another word, but can read they story. The naming file system is the same for all OS. 

    Names of the past users : Names.txt
    The story               : Story.txt
    The code to run         : main.py
#    
## Admin mode
  In either of the OS main.py has a admin mode for adjustments in the script run. The default password and username are:
  
Username (Name): Admin

Password: AdminAccessPassword4132

### Admin mode commands
| Command             | Action                                                                                                                          |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Help                | Displays this part of the README                                                                                                |
| Clear names         | Clears the names file so that everyone can enter in another word                                                                |
| Clear story         | Clears the story file, the names will stay but there will be no story                                                           |
| Clear all           | Clears both story and names at the same time                                                                                    |
| See story           | Displays the story, after 1 sec you will be given the option to press any key to remove the story and go back to the admin menu |
| Edit story          | Allows editing (only additions) to the story                                                                                    |
| Clear               | Clears the terminal                                                                                                             |
| Exit                | Exits admin mode                                                                                                                |
| End                 | Ends the script                                                                                                                 |
| EXIT MAIN OPERATION | Exits, nothing else can be added, displays the story and contributors                                                           |

### How to change either the username or password for admin mode

  In the main.py file, in what ever os you use, line 4&5 are the username and password respectively. Edit the name and password within the '. The name CAN NOT have any capitals, or the menu will be unassessable. The password can have any combination of letters, capitals and numbers.

#
## Other notes
  The MacOS version should work with linux, but this has not been tested.

  Once you have used any of the admin mode commands to clear data that data is gone unless you made a backup
