#!/usr/bin/env python3

import random

number = random.randint(1,10)
tries = 1

uname = input("Hello, what is your name? ")
print("Hello", uname + ".", )

question = input("Would you like to play a game? [y/n] ")
if question == "n":
    print("oh...okay")

if question == "y":
    print("I'm thinking of a number between 1 & 10")
    guess = int(input("Take a guess: "))
    if guess > number:
        print("Too high!")

    if guess < number:
        print("Too low!")
    while guess != number:
        tries += 1
        guess = int(input("Try again: "))
        if guess == number:
            print("You're right! The number was", number, "and it only took", tries, "tries" )
