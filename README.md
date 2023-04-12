## Python one word story

  Each person inputs their name and then they are told the story so far, after reading they are allowed to add ONE word. Then that word is added and if that person inputs their name again they will be told they can not add another word, but can read they story. The naming file system is the same for all OS. 

    Names of the past users : Names.txt
    The story               : Story.txt
    The code to run         : main.py OR mainAM.py
#    
## Admin mode
  In either of the OS main.py has a admin mode for adjustments in the script run. The default password and username are:
  
Username (Name): Admin

Password: AdminAccessPassword4132

### Admin mode commands

  Help                - Displays this part of the README
  Clear names         - Clears the names file so that everyone can enter in another word
  Clear story         - CLears the story file, the names will stay but there will be no story
  Clear all           - Clears both story and names at the same time
  See Story           - Displays the story, after 1 sec you will be givin the option to press any key to remove the story and go back to the admin menu
  Edit story          - Allows editing (only additions) to the story
  Clear               - Clears the terminal
  Exit                - Exits admin mode
  End                 - Ends the script
  EXIT MAIN OPERATION - Exits, nothing else can be added, displays the story and contributors

### How to change either the username or password for admin mode

  Windows

  In windows in the mainAM.py file the username is located at line 34, if you wish to change it just remove admin and put in the new username. DO NOT USE CAPITALS, because for names the script forces everything to lower case, so if you make it capital it will be impossible to open the admin menu. Leave the ' at the begening and end of the username.

  For the password on windows, it is located on line 38 (mainAM.py), to change just remove AdminAccessPassword4132 and enter in your new password. Make sure to leave the ' at the begening and end of the password.

#

  MacOS

  In MacOS in the mainAM.py file the username is located at line 28, if you wish to change it just remove admin and put in the new username. DO NOT USE CAPITALS, because for names the script forces everything to lower case, so if you make it capital it will be impossible to open the admin menu. Leave the ' at the begening and end of the username.

  For the password on MacOS, it is located on line 32, to change just remove AdminAccessPassword4132 and enter in your new password. Make sure to leave the ' at the begening and end of the password.
#
## Other notes
  The MacOS version should work with linux, but this has not been tested.

  Once you have used any of the admin mode commands to clear data that data is gone unless you made a backup
