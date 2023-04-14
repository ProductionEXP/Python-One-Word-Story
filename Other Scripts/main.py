BW = open('bannedword.txt', 'a')
with open('words_alpha.txt') as f1, open('words_alpha1.txt') as f2:
    for l1, l2 in zip(f1, f2):
        if l1 != l2:
            BW.writelines(l1)
            #BW.writelines()

BW.close()     
