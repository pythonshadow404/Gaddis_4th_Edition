#7. Color Mixer
primary_color1 = input("Please enter primary color: blue, red, or green: ")
primary_color2 = input("Please enter another primary color: blue, red, or green: ")

if primary_color1 == "red" and primary_color2 == "blue":
    print("Red and blue give you purple")
elif primary_color1 == "red" and primary_color2 == "yellow":
    print("Red and blue give you orange")
elif primary_color1 == "blue" and primary_color2 == "yellow":
    print("Yellow and blue give you get green")
else: 
    print("Please enter a primary color: blue, red, or yellow")
