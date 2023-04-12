import os
import time
os.system('clear')
while True:
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
                print('See Story')
                print('Exit')
                print('End')
                print()
                C1 = input()
                C = C1.lower()
                if C == 'help':
                    print('Clear names - Clears the names file so that everyone can enter in another word')
                    print('Clear story - CLears the story file, the names will stay but there will be no story')
                    print('See Story   - Displays the story, after 1 sec you will be givin the option to press any key to remove the story and go back to the admin menu')
                    print('Exit        - Exits admin mode')
                    print('End         - Ends the script')
                    print()
                    input('Press any key to continue')
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
                if C == 'see story':
                    file1 = open('Story.txt','r')
                    file1.seek(0)
                    print(file1.read())
                    print()
                    time.sleep(1)
                    input('Press any key to continue')
                    file1.close()
                    os.system('clear')
                if C == 'exit':
                    os.system('clear')
                    break
                if C == 'end':
                    os.system('clear')
                    exit()
                continue
        else:
            continue
            
    if N == 'SeeStory':
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