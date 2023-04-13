## Python one word story

  Each person inputs their name and then they are told the story so far, after reading they are allowed to add ONE word. Then that word is added and if that person inputs their name again they will be told they can not add another word, but can read they story.

    Names of the past users : Names.txt
    The story               : Story.txt
    English words           : words_dictionary.json
    Banned words            : banned_words.txt
    The code to run         : main.py

#
## Setup
  If you are not familiar with github, hit the green code button and download as zip. From this zip take the folder and move it to where you want it, then you can run the main.py file.

#    
## Admin mode
  Admin mode lets you do shit. You need to enter a username as your name and then enter a password. The default password and username are:
  
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

  In the main.py file, in what ever os you use, line 4&5 are the username and password respectively. Edit the name and password within the '. The name CAN NOT have any capitals, or the menu will be inaccessible. The password can have any combination of letters, capitals and numbers.

#
## Other notes
  Once you have used any of the admin mode commands to clear data that data is gone unless you made a backup