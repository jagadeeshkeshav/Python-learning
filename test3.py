import random

#rock = 1
#paper = 2
#scissors = 3
user_point=0
computer_point=0
x = range(3)
for n in x:
    computer = random.randint(1, 3)
    user = int(input("Do you want Rock(1), Paper(2) or Scissors(3). Enter 1 or 2 or 3 :\n"))
    if user == computer :
        print("You have a TIE. Computer chose " +str(computer))
    elif computer == 1 and user == 3:
        print("WIN, the computer had " + str(computer))
        user_point+1
    elif user == 2 and user == 1:
        print("WIN, computer had " + str(computer))
        user_point+1
    elif user == 3 and user == 2:
        print("WIN, computer had " + str(computer))
        user_point+1
    else:
        print("Sorry. You lose. Computer had " + str(computer))
        computer_point+1
print(computer_point)
print(user_point)
if computer_point > user_point:
    print("Sorry, Computer wins")
    print("Computer final score"+str(computer_point))
    exit()
else:
    print("Hurray ! You won")
    print("Your final score" + str(user_point))
    exit()