s1,s2,s3=eval(input("enter the three edges: "))
sum=s1+s2
sum1=s1+s3
sum2=s2+s3
perimeter=s1+s2+s3
if (sum>s3 and sum1>s2) and (sum2>s1):
    print("The input is valid and\n The perimeter is ",perimeter)
else:
    print("The input is invalid")