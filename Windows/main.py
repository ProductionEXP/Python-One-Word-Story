import os
import time

dirname1 = os.path.dirname(__file__)
Story = os.path.join(dirname1, 'Story.txt')
dirname = os.path.dirname(__file__)
Names = os.path.join(dirname, 'Names.txt')

os.system('cls')
while True:
    L = ''
    os.system('cls')
    with open(Story) as file:
        contents = file.read()
        search_word = 'EndStory'
        if search_word in contents:
            exit()

    print('What is your name?')
    N1 = input()    
    N = N1.lower()
    
    os.system('cls')

    with open(Names) as file3:
        contents = file3.read()
        search_word = N
        if search_word in contents:
            print('You have already added your word')
            print('If you wish to see the story put your name in as SeeStory')
            time.sleep(2.5)
            os.system('cls')
            continue
    C = ''      
    if N == 'admin':
        print('Reqested Admin Access')
        print('To proceed enter password')
        AP = input()
        if AP == 'AdminAccessPassword4132':
            os.system('cls')
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
                    os.system('cls')

                if C == 'edit story':
                    print('Here is the story currently')
                    file1 = open(Story,'r')
                    file1.seek(0)
                    print(file1.read())
                    print()
                    file1.close()
                    print('What would you like to add?')
                    print('Hit enter twice when you are ready to submit your edits')
                    ASI = input()
                    input()
                    file1 = open(Story,'a')
                    file1.seek(0)
                    file1.writelines(ASI)
                    file1.close()
                    print('Done')
                    time.sleep(1)
                    os.system('cls')

                if C == 'clear names':
                    open(Names, 'w').close()
                    print('Cleared Names')
                    time.sleep(2.5)
                    os.system('cls')

                if C == 'clear story':
                    open(Story, 'w').close()
                    print('Cleared Story')
                    time.sleep(2.5)
                    os.system('cls')

                if C == 'clear all':
                    open(Story, 'w').close()
                    open(Names, 'w').close()
                    print('Cleared all data')
                    time.sleep(2.5)
                    os.system('cls')

                if C == 'see story':
                    file1 = open(Story,'r')
                    file1.seek(0)
                    print(file1.read())
                    print()
                    time.sleep(1)
                    input('Press enter to continue')
                    file1.close()
                    os.system('cls')

                if C == 'exit':
                    os.system('cls')
                    break

                if C == 'end':
                    os.system('cls')
                    exit()

                if C == 'clear':
                    os.system('cls')
                
                if C == 'exit main operation':
                    break
                continue

        else:
            continue

    if C == 'exit main operation':
        os.system('cls')
        break 

    if N == 'seestory':
        os.system('cls')
        file1 = open(Story,'r')
        file1.seek(0)

        print('Current Story is ')
        print(file1.read())
        print()

        file1.close()
        time.sleep(5)
        os.system('cls')
        continue

    if search_word not in contents and C != 'exit':
        file1 = open(Story,'r')
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
            os.system('cls')
            continue
        
        if len(L.split()) == 1:
            file1 = open(Story,'a')
            file1.writelines(' ')
            file1.writelines(L)

        else:
            print('You attempted to add more than one word, try again.')
            time.sleep(2)
            os.system('cls')
            continue

    if len(L.split()) == 1:
        file2 = open(Names,'a')
        file2.writelines(N)
        file2.writelines('\n')
        file2.close()

    os.system('cls')

print('Exited main operation')
input('Press enter to continue')
os.system('cls')

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

input('Press enter to exit script')
time.sleep(5)