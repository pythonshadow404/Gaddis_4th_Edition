#2. Areas of Rectangles
len1 = int(input("Enter length one: "))
width1 = int(input("Enter width one: "))
len2 = int(input("Enter length two: "))
width2 = int(input("Enter width two: "))

rect1 = len1*width1
rect2 = len2*width2

if rect1 > rect2:
    print("Rectangle 1 is greater than rectangle 2")
elif rect2 > rect1:
    print("Rectangle 2 is greater than rectangle 1")
else: 
    print("Rectangles have the same size")