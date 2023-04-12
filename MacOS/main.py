import os
import time
os.system('clear')
while True:
    L = ''
    os.system('clear')
    with open('Story.txt') as file:
        contents = file.read()
        search_word = 'EndStory'
        if search_word in contents:
            exit()

    print('What is your name?')
    N1 = input()    
    N = N1.lower()
    
    os.system('clear')

    with open('Names.txt') as file3:
        contents = file3.read()
        search_word = N
        if search_word in contents:
            print('You have already added your word')
            print('If you wish to see the story put your name in as SeeStory')
            time.sleep(2.5)
            os.system('clear')
            continue
    C = ''      
    if N == 'admin':
        print('Reqested Admin Access')
        print('To proceed enter password')
        AP = input()
        if AP == 'AdminAccessPassword4132':
            os.system('clear')
            print('Access granted')
            print()
            while True:
                print('Admin Console')
                print()
                print('Command option are:')
                print('Help')
                print('Clear names')
                print('Clear story')
                print('Clear all')
                print('See Story')
                print('Edit story')
                print('Clear')
                print('Exit')
                print('End')
                print('EXIT MAIN OPERATION')
                print()
                C1 = input()
                C = C1.lower()

                if C == 'help':
                    print()
                    print('Clear names          - Clears the names file so that everyone can enter in another word')
                    print('Clear story          - Clears the story file, the names will stay but there will be no story')
                    print('Clear all            - Clears both story and names at the same time')
                    print('See Story            - Displays the story, after 1 sec you will be givin the option to press any key to remove the story and go back to the admin menu')
                    print('Edit story           - Allows editing (only additions) to the story')
                    print('Clear                - Clears the terminal')
                    print('Exit                 - Exits admin mode')
                    print('End                  - Ends the script')
                    print('EXIT MAIN OPERATION  - Exits, nothing else can be added, displays the story and contributors')
                    print()
                    input('Press enter to continue')
                    os.system('clear')

                if C == 'edit story':
                    print('Here is the story currently')
                    file1 = open('Story.txt','r')
                    file1.seek(0)
                    print(file1.read())
                    print()
                    file1.close()
                    print('What would you like to add?')
                    print('Hit enter twice when you are ready to submit your edits')
                    ASI = input()
                    input()
                    file1 = open('Story.txt','a')
                    file1.seek(0)
                    file1.writelines(ASI)
                    file1.close()
                    print('Done')
                    time.sleep(1)
                    os.system('clear')

                if C == 'clear names':
                    open('Names.txt', 'w').close()
                    print('Cleared Names')
                    time.sleep(2.5)
                    os.system('clear')

                if C == 'clear story':
                    open('Story.txt', 'w').close()
                    print('Cleared Story')
                    time.sleep(2.5)
                    os.system('clear')

                if C == 'clear all':
                    open('Story.txt', 'w').close()
                    open('Names.txt', 'w').close()
                    print('Cleared all data')
                    time.sleep(2.5)
                    os.system('clear')

                if C == 'see story':
                    file1 = open('Story.txt','r')
                    file1.seek(0)
                    print(file1.read())
                    print()
                    time.sleep(1)
                    input('Press enter to continue')
                    file1.close()
                    os.system('clear')

                if C == 'exit':
                    os.system('clear')
                    break

                if C == 'end':
                    os.system('clear')
                    exit()

                if C == 'clear':
                    os.system('clear')
                
                if C == 'exit main operation':
                    break
                continue

        else:
            continue

    if C == 'exit main operation':
        os.system('clear')
        break 
            
    if N == 'seestory':
        os.system('clear')
        file1 = open('Story.txt','r')
        file1.seek(0)

        print('Current Story is ')
        print(file1.read())
        print()

        file1.close()
        time.sleep(5)
        os.system('clear')
        continue

    if search_word not in contents and C != 'exit':
        file1 = open('Story.txt','r')
        file1.seek(0)

        print('Current Story is ')
        print(file1.read())
        print()

        file1.close()

        print('What is the next word in the story?')
        L = input()

        if '-' in L:
            print('You attempted to add more than one word, try again.')
            time.sleep(2)
            os.system('clear')
            continue
        
        if len(L.split()) == 1:
            file1 = open('Story.txt','a')
            file1.writelines(' ')
            file1.writelines(L)

        else:
            print('You attempted to add more than one word, try again.')
            time.sleep(2)
            os.system('clear')
            continue

    if len(L.split()) == 1:
        file2 = open('Names.txt','a')
        file2.writelines(N)
        file2.writelines('\n')
        file2.close()

    os.system('clear')

print('Exited main operation')
input('Press enter to continue')
os.system('clear')

print('Final story')
file1 = open('Story.txt','r')
file1.seek(0)
print(file1.read())
print()
print()
print()
file1.close()

print('Contributors')
file2 = open('Names.txt','r')
file2.seek(0)
print(file2.read())
print()
print()
print()
file2.close()

input('Press enter to exit script')