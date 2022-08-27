import random
num1=random.randint(0,50)
num2=random.randint(0,50)
print(num1)
print(num2)
sum=int(input("enter the sum of the result: "))
substraction=int(input("enter the substraction of the result: "))
multiplication=int(input("enter the multiplication of the result: "))
division=float(input("enter the division of the result: "))
sum1=num1+num2
substraction1=num1-num2
multiplication1=num1*num2
division1=num1/num2
print("Here  the result is")
if sum==sum1:
    print("sum of the result is :",True)
else:
    print("sum of the result is :",False)
if substraction==substraction1:
    print("substraction of the result is :",True)
else:
    print("substraction of the result is :",False)
if multiplication==multiplication1:
    print("multiplication of the result is :",True)
else :
    print("multiplication of the result is :",False)
if division==division1:
    print("division of the result is :",True)
else:
    print("division of the result is :",False)