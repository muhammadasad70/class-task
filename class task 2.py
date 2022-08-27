# take the age of the user in days and tell how old are his in year month and days
age=int(input("enter your date of birth in days\n"))
year=age//365
month1=age%365
month=month1//30
days=month1%30
print("your agr is",year,"year",month,"months","and",days,"days")