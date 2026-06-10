# 5. Mass and Weight
GRAVITY_ACCELERATION = 9.8
mass = int(input("Enter the mass: "))
weight = mass * GRAVITY_ACCELERATION
if weight > 500:
    print("Too heavy")
elif weight < 100: 
    print("Too light")
else:
    print(weight, " Newton", " is within tolerance.", sep='')