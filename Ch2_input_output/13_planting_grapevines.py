#13_planting_grapevines
row_length = int(input("Enter length of row:"))
end_post_length = int(input("Enter length of end-post assembly: "))
space_between_vines = int(input("Enter lenth of space between vines: "))
vine_numbers = (row_length-2*end_post_length)/ space_between_vines
print(vine_numbers)