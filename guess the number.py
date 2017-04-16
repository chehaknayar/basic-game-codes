
from random import randint
print "a number from 0-9 has been chosen"
ans=str(randint(0,9))

guess=raw_input("Guess the number")

print 'number chosen was:',
print ans

print 'your guess is:',
print guess

if guess == ans:
    print "correct guess"
else:
    print "incorrect guess"




