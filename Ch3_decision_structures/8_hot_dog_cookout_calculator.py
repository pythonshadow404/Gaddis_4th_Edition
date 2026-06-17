# 8.Hot Dog Cookout Calculator
HOT_DOG_PACKAGE = 10
BUN_PACKAGE = 8
guests = int(input("Enter the number guest attending event: "))
dogs_per_person = int(input("Enter the number hot dogs for each guest:  "))
packages_needed = (guests * dogs_per_person) / HOT_DOG_PACKAGE
print("Number of packages: ", packages_needed)
