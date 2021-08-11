import math
import random
import time

print ("Welcome to Guess the Number!")
time.sleep(1)
print ("The way this works is you think of a number and the computer will try to guess the number")
time.sleep(2)

Max = 100
Min = 1
Guess = math.trunc((Max + Min) / 2)

inquiry = ""

while inquiry != "equal":
    inquiry = input("Is your number higher or lower than "+ str(Guess)+ "? Type higher or lower or equal here: ")
    if inquiry == "higher" or inquiry == "Higher":
        Min = Guess + 1
        Guess = math.trunc((Max + Min) / 2)
    if inquiry == "lower" or inquiry == "Lower":
        Max = Guess - 1
        Guess = math.trunc((Max + Min) / 2)
    if inquiry == "equal" or inquiry == "Equal":
        print ("Let's goooooo")
        print ("Thanks for playing!")
        break        