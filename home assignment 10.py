dict1={"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"sep":9
       ,"oct":10,"nov":11,"dec":12,"jan":13,"feb":14}
letter=input("Enter the \"month\":(e.g march,april,etc): ")
month=int(dict1.get(letter))
day=int(input("Enter the \"day\" of the month: "))
a=int(input("Enter the \"year\": "))
year=a%100
century=a//100
if month==13 or month==14:
    year1=year-1
    b=day+(13*(month+1)//5)+year1+(year1//4)+5-century
    R=b%7
    if R == 0:
        print("Day of the week is Sunday")
    elif R == 1:
        print("Day of the week is Monday")
    elif R == 2:
        print("Day of the week is Tuesday")
    elif R == 3:
        print("Day of the week is Wednesday")
    elif R == 4:
        print("Day of the week is Thursday")
    elif R == 5:
        print("Day of the week is Friday")
    elif R == 6:
        print("Day of the week is Saturday")
    elif R < 0:
        T = 7 + R
        if T == 0:
            print("Day of the week is Sunday")
        elif T == 1:
            print("Day of the week is Monday")
        elif T == 2:
            print("Day of the week is Tuesday")
        elif T == 3:
            print("Day of the week is Wednesday")
        elif T == 4:
            print("Day of the week is Thursday")
        elif T == 5:
            print("Day of the week is Friday")
        elif T == 6:
            print("Day of the week is Saturday")
else:
    b=day+(13*(month+1)//5)+year+(year//4)+5-century
    R=b%7
    if R==0:
        print("Day of the week is Sunday")
    elif R==1:
        print("Day of the week is Monday")
    elif R==2:
        print("Day of the week is Tuesday")
    elif R==3:
        print("Day of the week is Wednesday")
    elif R==4:
        print("Day of the week is Thursday")
    elif R==5:
        print("Day of the week is Friday")
    elif R==6:
        print("Day of the week is Saturday")
    elif R<0:
        T=7+R
        if T==0:
            print("Day of the week is Sunday")
        elif T==1:
            print("Day of the week is Monday")
        elif T==2:
            print("Day of the week is Tuesday")
        elif T==3:
            print("Day of the week is Wednesday")
        elif T==4:
            print("Day of the week is Thursday")
        elif T==5:
            print("Day of the week is Friday")
        elif T==6:
            print("Day of the week is Saturday")