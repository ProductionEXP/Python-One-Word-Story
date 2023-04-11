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
    N = input()    

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

    if search_word not in contents:
        file1 = open('Story.txt','r')
        file1.seek(0)

        print('Current Story is ')
        print(file1.read())
        print()

        file1.close()

        print('What is the next word in the story?')
        L = input()
        
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
