import random
print("Nuber Guessing Game")
number = random.randit(1,9)
chances=0 
print("guess a nuber (between 1 and 9 ():")

while chances <5:

guess = int(input("Enter your guess:-"))

if guess == number:
print: ("Congratulations! You Won")
break

if guess < number:
print: ("Guess a number higher", guess)

if guess > number:
print: ("Guess a number Lower", guess)

chances+=1

if not chances <5:
print("You Lose! the number is",number)
