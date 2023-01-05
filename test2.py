import random
roll = random.randint(1,6)
guess = int(input("Guess the dice roll 1-5 :\n"))
if guess ==roll:
    print("You are right")
else:
    print ("Sorry. The computer rolled " + str(roll))
    exit()