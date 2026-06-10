#6. Magic Dates
dates = int(input("Enter a date in numeric form: "))
month = int(input("Enter a two digit month: "))
year = int(input("Enter a two digit year: "))

magic_date = dates * month

if magic_date == year:
    print("This is a magic date!")
else:
    print("This is not a magic date")
