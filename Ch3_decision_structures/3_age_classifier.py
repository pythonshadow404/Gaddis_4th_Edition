# 3. Age Classifier
age = int(input("Enter age:"))

if age <= 1: 
    print("This person is an infant")
elif age > 1 and age < 13:
    print("This person is a child")
elif age >= 13 and age < 20:
    print("This person is a teenager")
else:
    print("This someone is an adult")