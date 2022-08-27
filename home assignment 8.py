# print("enter 0 to convert DOLLAR to RMB and enter 1 to convert RMB to DOLLAR")
# num=int(input("enter a number\n"))
# if num==0:
#     amount=eval(input("enter the dollar you want to convert\n"))
#     dollar=amount*6.66
#     print('$',amount,"is",dollar,"yaun")
# if num==1:
#     amount=eval(input("enter the yaun you want to conver\n"))
#     yaun=amount/6.66
#     print(amount,"yaun is",yaun,"$")
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("\n",end="")
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print("\n",end="")
