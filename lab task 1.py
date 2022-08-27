# take a three digit number from the user and print the sum of the digits
num=int(input("enter a number between 0 to 1000\n"))
a=num%10
b=num%100
c=b//10
d=num//100
sum=a+c+d
# print("the sum of the digit",a,",",c,"and",d,"=",sum)
print("the sum of the digit =",sum)