import os
import time
os.system('clear')
while True:
    os.system('clear')
    with open('Python-One-Word-Story\\MacOS\\Story.txt') as file:
        contents = file.read()
        search_word = 'EndStory'
        if search_word in contents
            quit()

    print('What is your name?')
    N = input()    

    with open('Python-One-Word-Story\\MacOS\\Names.txt') as file3:
        contents = file3.read()
        search_word = N
        if search_word in contents:
            print('You have already added your word')
            print('If you wish to see the story put your name in as SeeStory')
            time.sleep(2.5)
            os.system('clear')
            continue

    if N == 'SeeStory':
        os.system('clear')
        file1 = open('Python-One-Word-Story\\MacOS\\Story.txt','r'
        file1.seek(0)

        print('Current Story is ')
        print(file1.read())
        print()

        file1.close()
        time.sleep(5)
        os.system('clear')
        continue

    if search_word not in contents:
        file1 = open('Python-One-Word-Story\\MacOS\\Story.txt','r')
        file1.seek(0)

        print('Current Story is ')
        print(file1.read())
        print()

        file1.close()

        print('What is the one word that you would like to add to the story?')
        print('Choose carefully, you can only add one.')
        L = input()
        file1 = open('Python-One-Word-Story\\MacOS\\Story.txt','a')

    if len(L.split()) == 1:
        file2 = open('Python-One-Word-Story\\MacOS\\Names.txt','a')
        file2.writelines(N)
        file2.writelines('\n')
        file2.close()

    if len(L.split()) != 1:
        print('You attempted to add more than one word, try again.')
        time.sleep(2)
        os.system('clear')
        continue

    os.system('clear')

    # Started at 5:45pm 10/4/2023
    # Finished at 8:57pm 10/4/2023
    # I know this code is probably shit