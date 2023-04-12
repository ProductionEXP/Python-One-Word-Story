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
                if C == 'see story':
                    file1 = open(Story,'r')
                    file1.seek(0)
                    print(file1.read())
                    print()
                    time.sleep(1)
                    input('Press any key to continue')
                    file1.close()
                    os.system('cls')
                if C == 'exit':
                    os.system('cls')
                    break
                if C == 'end':
                    os.system('cls')
                    exit()
                continue
        else:
            continue

    if N == 'SeeStory':
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