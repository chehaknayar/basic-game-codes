#this project involves writing a program that
# simulates rolling dice. When the program runs,
# it will randomly choose a number between 1 and 6.
# The program will print what that number is. It should then ask
#  you if youd like to roll again. For this project,
#  youll need to set the min and max number that your dice can produce. For the average die, that means a
# minimum of 1 and a maximum of 6. Youll also want a function that randomly grabs a
#  number within that range and prints it.
from random import randint

while(1):
    ans= raw_input("do you wish to roll the dice?y/n")
    if ans == 'y' or ans == 'Y':
        print "dice showed",
        print randint(1,6)
    else:
        exit()