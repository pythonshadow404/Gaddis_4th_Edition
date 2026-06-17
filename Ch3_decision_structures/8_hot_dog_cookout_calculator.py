# 8.Hot Dog Cookout Calculator
HOT_DOG_PACKAGE = 10
BUN_PACKAGE = 8
guests = int(input("Enter the number guest attending event: "))
dogs_per_person = int(input("Enter the number hot dogs for each guest:  "))
total_needed = (guests * dogs_per_person)
packages = (total_needed + HOT_DOG_PACKAGE -1) // HOT_DOG_PACKAGE
leftover = packages * HOT_DOG_PACKAGE - total_needed

print("Number of packages: ", total_needed)
print("Packages to buy:", packages)
print("Leftover hot dogs:", leftover)
