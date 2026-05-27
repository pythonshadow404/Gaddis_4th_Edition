#10_ingredient_adjuster
#Concept of ratio and scaling formula
#ratio: 1.5cups sugar/48 cookies
#scaling formula: scale = desired_cookies/48
#ingredient_needed = base_amount * scale
desired_cookies = int(input("Enter the amount cookies to bake: "))
scale = desired_cookies/48
cups_sugar = 1.5 * scale
cups_butter = 1 * scale
cups_flour = 2.75 * scale
print(desired_cookies, "cookies require", cups_sugar, "cups of sugar", cups_butter, "cup(s) of butter", "and\n", cups_flour, "cups of flour.")