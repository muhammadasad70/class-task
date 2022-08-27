num=int(input("enter the integer: "))
print(num,"is divisible by both 5 and 6 ",True) if num%5==0 and num%6==0 else print(num,"is divisible by 5 and 6 ",False)
print(num,"is divisible by 5 or 6",True) if num%5==0 or num%6==0 else print(num,"is divisible by 5 or 6 ",False)
if num%5==0 or num%6!=0:
    print(num,"is divisible by 5 but not both",True)
else:
    if num%6==0 or num%5!=0:
        print(num,"is divisible by 6 but not both",True)


