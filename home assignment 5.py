import random
num=random.randint(0,1)
print(num)
guess=input("enter your guess: ")
if guess=="head":
    guess=0
elif guess=="tail":
    guess=1
if guess==num:
    print("your guess is correct")
else:
    print("your guess is wrong")
