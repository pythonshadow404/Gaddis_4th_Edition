#1_day_of_the_week
number_weekday = int(input("Enter number 1-7 for day of the week: "))
if number_weekday > 7:
    print("Enter a number between 1 and 7")
elif number_weekday == 1:
    print("Monday")
elif number_weekday == 2:
    print("Tuesday")
elif number_weekday == 3:
    print("Wednesday")
elif number_weekday == 4:
    print("Thurday")
elif number_weekday == 5:
    print("Friday")
elif number_weekday == 6:
    print("Saturday")
else: print("Sunday")

