import math
h1=eval(input("Enter height of first rectangle:\n"))
w1=eval(input("Enter width of first rectangle:\n"))
x1,y1=eval(input("Enter the center of first rectangle i.e x and y coordinate:\n"))
h2=eval(input("Enter height of second rectangle:\n"))
w2=eval(input("Enter width of second rectangle:\n"))
x2,y2=eval(input("Enter the center of second rectangle i.e x and y coordinate:\n"))
distance=math.sqrt((x2-x1)*2+(y2-y1)*2)
if distance<w1 and distance <h1:
    print(f"The second rectangle is inside the first rectangle.")
elif distance<w2 and distance <h2:
    print(f"The first rectangle is inside the second rectangle.")
elif distance<w1 and distance>w2:
    print(f"The rectangles are overlapping.")