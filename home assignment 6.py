print("Three digit lottery number is ")
import random
n=random.randrange(100,1000,)
print(n)
a=n%10
b=n%100
c=b//10
d=n//100
num=int(input("enter your  three didit lottery number :"))
a1=num%10
b1=num%100
c1=b1//10
d1=num//100
var1=d1,c1,a1
if n==num:
    print("you have won the lottery and your Reward is $10,000 is ")

elif (a1==a or a1==c or a1==d) and (c1==a or c1==c or c1==d) and (d1==a or d1==c or d1==d):
    print("you have won the lottery and your Reward is $3,000 is ")
elif (a1==a or a1==c or a1==d) or (c1==a or c1==c or c1==d) or (d1==a or d1==c or d1==d):
    print("you have won the lottery and your Reward is $1,000 is ")