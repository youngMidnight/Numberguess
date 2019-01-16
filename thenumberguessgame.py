#!/usr/python

import random
Number = random.randint(1,10)
guessanumber=0

print("hello whats your name")

Myname = input()

print(' hello ' +Myname )
print ( ' I am thinking of a number 1-10')


while(guessanumber !=3):
   print("guess a number")
   guess=input()
   guess=int(guess)


   if guess < Number:
      print('guess was to low')

   if guess >Number:
      print(' guess was to high')

   if guess == Number:
      print('thats my number you win')
      break
      
   guessanumber= guessanumber + 1


   while(guessanumber == 3):
      print(' you loose my number was ',Number,)
      break



