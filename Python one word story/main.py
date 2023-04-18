# Imports

import os
import time

# Assigning of the name and password for admin mode
# See the Readme (README.MD) for more information

AdminName = 'admin'
AdminPassword = 'AdminAccessPassword4132'

# Automatic re-assigning of the terminal clear commands
if os.name == 'posix':
    CleanScreen = 'clear'

if os.name == 'nt':
    CleanScreen = 'cls'

# Makes relative paths for each of the files, we need this on Windows but not MacOS
# It will as assign these to a variabile for easy use
# In MacOS we just need to file names so we have those listed below

if os.name == 'nt':
    dirname1 = os.path.dirname(__file__)
    Story = os.path.join(dirname1, 'Story.txt')
    dirname2 = os.path.dirname(__file__)
    Names = os.path.join(dirname2, 'Names.txt')
    dirname3 = os.path.dirname(__file__)
    BannedWordsT = os.path.join(dirname3, 'Bannedwords.txt')
    dirname = os.path.dirname(__file__)
    wordbank = os.path.join(dirname, 'words_alpha.txt')

elif os.name == 'posix':
    Story = 'Story.txt'
    Names = 'Names.txt'
    BannedWordsT = 'Bannedwords.txt'
    wordbank = 'words_alpha.txt'

# Clear screen to start the main loop

os.system(CleanScreen)

# Main Loop

while True:
    # Reseting of variables, this makes sure each varabile always has a value assigned to it and
    # That in the begening it is zero, so the next user doesn't get run-off from the pevious user
    L = ''
    N = ''
    C = '' 
    N1 = ''
    WP = 0
    Bw = 0
    search_word = ''
    contents = ''

    os.system(CleanScreen)
  
    # First minnor loop, asks the user's name, and makes sure that is both their first and last
    # This is where the user can also enter admin mode
    while len(N1.split()) != 2:
        print('What is your name? (First and last)')
        N1 = input()
        if N1.lower() == AdminName:
            os.system(CleanScreen)
            break
        if len(N1.split()) == 2:
            # We lower the name of the user so that users can not just enter the same name and change a capital
            # and get in again
            N = N1.lower()
        else:
            # If the name was not two words it will restart and let the user try again
            print('Please enter both your first and last name')
            time.sleep(2)
            os.system(CleanScreen)
    
    os.system(CleanScreen)

    # If the users name is not the admin name and they have already enter a word, they can not enter another
    # They are told that they can still see it but they can not add another word.
    if N != AdminName:
        with open(Names) as file3:
            contents = file3.read()
            search_word = N
            if search_word in contents:
                print('You have already added your word')
                print('If you wish to see the story put your name in as See Story')
                time.sleep(2.5)
                os.system(CleanScreen)
                continue
    # Admin mode
    # If the name inputed is the same of the admin mode name, then they have requested admin mode access
    if N == AdminName:
        # If the password that is entered is wrong, it will just go back to the original screen and ask for
        # their name again
        print('Requested Admin Access')
        print('To proceed enter password')
        AP = input()
        if AP == AdminPassword:
            os.system(CleanScreen)
            print('Access granted\n')
            while True:
                # After every successful command the terminal is cleared and the command options are 
                # displayed again
                print('Admin Console\n')
                print('Command option are:\nHelp\nClear names\nClear story\nClear all\nSee Story\nEdit story\nClear\nExit\nEnd\nEXIT MAIN OPERATION\n')
                C1 = input()
                C = C1.lower()

                if C == 'help':
                    # Even though all of the commands are listed in the README
                    # we still have this for easy access
                    print('\nClear names          - Clears the names file so that everyone can enter in another word\nClear story          - Clears the story file, the names will stay but there will be no story\nClear all            - Clears both story and names at the same time\nSee Story            - Displays the story, after 1 sec you will be given the option to press any key to remove the story and go back to the admin menu\nEdit story           - Allows editing (only additions) to the story\nClear                - Clears the terminal\nExit                 - Exits admin mode\nEnd                  - Ends the script\nEXIT MAIN OPERATION  - Exits, nothing else can be added, displays the story and contributors\n')
                    input('Press enter to continue')
                    os.system(CleanScreen)

                if C == 'edit story':
                    # Edit story lets the admin add any ammount of words to the story, this is used for
                    # when a person enters a banned word, but in that context it is not bad
                    print('Here is the story currently')
                    file1 = open(Story,'r')
                    file1.seek(0)
                    print(file1.read() + '\n')
                    file1.close()
                    print('What would you like to add?\nHit enter when you are ready to submit your edits')
                    ASI = input()
                    file1 = open(Story,'a')
                    file1.seek(0)
                    file1.writelines(ASI)
                    file1.close()
                    print('Done')
                    time.sleep(1)
                    os.system(CleanScreen)

                if C == 'clear names':
                    # Clears the Names.txt file 
                    open(Names, 'w').close()
                    print('Cleared Names')
                    input('Press enter to continue')
                    os.system(CleanScreen)

                if C == 'clear story':
                    # Clears the Story.txt file
                    open(Story, 'w').close()
                    print('Cleared Story')
                    input('Press enter to continue')
                    os.system(CleanScreen)

                if C == 'clear all':
                    # Clears both the Names.txt and Story.txt files
                    open(Story, 'w').close()
                    time.sleep(0.1)
                    open(Names, 'w').close()
                    print('Cleared all data')
                    input('Press enter to continue')
                    os.system(CleanScreen)

                if C == 'see story':
                    # Displays the story for the admin
                    file1 = open(Story,'r')
                    file1.seek(0)
                    print(file1.read())
                    print()
                    time.sleep(1)
                    input('Press enter to continue')
                    file1.close()
                    os.system(CleanScreen)

                if C == 'exit':
                    # Exits admin mode
                    os.system(CleanScreen)
                    break

                if C == 'end':
                    # Ends the script
                    os.system(CleanScreen)
                    exit()

                if C == 'clear':
                    # Clears the terminal
                    os.system(CleanScreen)
                
                if C == 'exit main operation':
                    # Exit's the operation of the script and displays the names and story
                    # This break is to exit admin mode
                    break
                continue
        else:
            continue

    # Second break to exit the main loop
    if C == 'exit main operation':
        os.system(CleanScreen)
        break 
            
    if N == 'see story':
        # If the user inputs the name of 'See Story' it will display the story for them to read
        os.system(CleanScreen)
        file1 = open(Story,'r')
        file1.seek(0)
        print('Current Story is \n')
        print(file1.read())
        file1.close()
        input('Press enter to continue')
        os.system(CleanScreen)
        continue

    if search_word not in contents and C != 'exit':
        # If the inputed name has not benn used before and the admin has not juset exited the terminal 
        # We start the one word part
        file1 = open(Story,'r')
        file1.seek(0)

        print('Current Story is ')
        print(file1.read() + '\n')
        file1.close()

        print('What is the next word in the story?')
        L = input()

        if '-' in L:
            # First multi word protection
            print('You attempted to add more than one word, try again.')
            input('Press enter to continue')
            os.system(CleanScreen)
            continue

        # Defines banned words and opens it for checking 
        BannedWordsR = open(BannedWordsT, 'r')
        BannedWords = BannedWordsR.read()
        Llower = L.lower()
        UserInput = '.' + Llower

        if UserInput in BannedWords:
            # If a user has entered a banned word, their name is added to the names list so they can not add 
            # another word in the names files they have '- BANNEDWORD' next to their name so the operator can 
            # document who attempted to write the banned word
            print('You have entered a banned word, you can no longer add words.\nAs this list is crude, please as the station mannager if you can add it, we can let that happen in some contexts.')
            file2 = open(Names,'a')
            file2.writelines(N)
            file2.writelines(' - BANNEDWORD')
            file2.writelines('\n')
            file2.close()
            Bw = 1
            input('Press enter to continue')
        
        # Opens the dictionary to make sure that the word that the user imputed is a real word
        Dictionary1 = open(wordbank, 'r')
        Dictionary = Dictionary1.read()
        if  UserInput not in Dictionary and Llower not in BannedWords:
            # If it is not their name is not added and they can try again
            print('This word is not in our dictionary. \nIf you think it is a word call the mannager of the station over to have us add it')
            input('Press enter to continue')
            WP = 1
            Dictionary1.close()
            os.system(CleanScreen)

        # If the user has not entered more than one word, and the word is in our dictionary, and is not a banned word
        if len(L.split()) == 1 and WP == 0 and Bw == 0:
            file1 = open(Story,'a')
            file1.writelines(' ')
            file1.writelines(L)
        elif len(L.split()) == 0:
            # If they did not enter a word they are sent back to the beginning and they can try again
            print('You did not enter a word, try again.')
            input('Press enter to continue')
            os.system(CleanScreen)
            continue
        elif WP == 0 and Bw == 0:
            # If they entered more than one word they are sent back to the beginning and they can try again
            print('You attempted to add more than one word, try again.')
            input('Press enter to continue')
            os.system(CleanScreen)
            continue
        
    if len(L.split()) == 1 and WP == 0:
        # If all previous actions are valid and succeed then the user's name is writin to the names file (Names.txt)
        file2 = open(Names,'a')
        file2.writelines(N)
        file2.writelines('\n')
        file2.close()

    os.system(CleanScreen)

# If an admin exits main operation this is to display the story and contributors
print('Exited main operation')
input('Press enter to continue')
os.system(CleanScreen)

print('Final story')
file1 = open(Story,'r')
file1.seek(0)
print(file1.read())
print()
print()
print()
file1.close()

print('Contributors')
file2 = open(Names,'r')
file2.seek(0)
print(file2.read())
print()
print()
print()
file2.close()

# Once enter is press there is no more code nor loops so the script end itself
input('Press enter to exit script')