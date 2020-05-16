#This is a text based game that uses a story file to make the game
#There is more to be added
#Developers: Zeptochicken and The Magnanimous Engineer
#The program loops through a text file and looks for key terms that shape the game
#A basic program mostly for learning. An interface version will eventually come.

import os
maindir = os.getcwd() + '/story.txt'
f = open(maindir, 'r')
lines = f.readlines()


l = ['a', 'b', 'c', 'd', 'e', 'f']
a, z, c = False, False, False
y, cc, aa = 0, 0, 0
x = lines[y]
while x != lines[-1]:
    x = lines[y]
###############################
    if "txt-" in x:
        z = True
        y += 1
        continue

    elif "-txt" in x:
        z = False
        print('\n')

    if z == True:
        print(x.rstrip('\n'))
##############################
    if "choice-" in x:
        c = True
        y += 1
        print("")
        continue
    elif "-choice" in x:
        c = False
        i = input()
        l = l[0:cc]
        while i.lower() not in l:
            i = input()

    if c == True:
        print(x)
        cc += 1
##############################
    if "c_action-" in x:
        a = True
        y += 1
        continue
    elif "-c_action" in x:
        a = False

    if a == True:
        prev = x
        if aa == l.index(i):
            y += 1
            x = lines[y]
            while x != prev:
                x = lines[y]
                y += 1
        aa += 1
##############################
    if "-end" in x:
        x = lines[-1]
        print('end')
##############################
    y += 1
