a =  float(input('Enter a number : '))
b =  float(input('Enter a number : '))
print("Enter your choice")
c = int(input('1=Addition, 2=Subtraction, 3=Multiplication, 4=Division : '))
if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a*b)
elif c == 4:
    print(a/b)
else:
    print("Enter valid choice: ")
    exit()




