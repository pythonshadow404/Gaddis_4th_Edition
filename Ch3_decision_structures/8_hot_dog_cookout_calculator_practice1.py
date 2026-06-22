# 8.Hot Dog Cookout Calculator
# HOT_DOG_PACKAGE = 10
# BUN_PACKAGE = 8
# guests = int(input("Enter the number guest attending event: "))
# dogs_per_person = int(input("Enter the number hot dogs for each guest:  "))
# total_needed = (guests * dogs_per_person)
# packages = (total_needed + HOT_DOG_PACKAGE -1) // HOT_DOG_PACKAGE
# leftover = packages * HOT_DOG_PACKAGE - total_needed
# total_buns = guests * BUN_PACKAGE
# print("Number of packages: ", total_needed)
# print("Packages to buy:", packages)
# print("Leftover hot dogs:", leftover)

people = 35
hot_dogs_per_person = 2

hot_dogs_per_package = 10
buns_per_package = 8

# total items needed
total_hot_dogs_needed = people * hot_dogs_per_person
#In the logic of the program, every hot dog requires exactly one bun:
total_buns_needed = total_hot_dogs_needed  # one bun per hot dog

# calculate packages of hot dogs
if total_hot_dogs_needed % hot_dogs_per_package == 0:
    hot_dog_packages = total_hot_dogs_needed // hot_dogs_per_package
else:
    

# calculate packages of buns
if 
else:
    bun_packages = total_buns_needed // buns_per_package + 1

# leftovers
hot_dog_leftover = hot_dog_packages * hot_dogs_per_package - total_hot_dogs_needed
bun_leftover = bun_packages * buns_per_package - total_buns_needed

print("Hot dog packages needed:", hot_dog_packages)
print("Bun packages needed:", bun_packages)
print("Leftover hot dogs:", hot_dog_leftover)
print("Leftover buns:", bun_leftover)
