#9. Roulette Wheel Colors

pocket_number = int(input("Enter pocket number: "))

if pocket_number == 0:
    pocket_0 = "green"
    print("Pocket 0 is", pocket_0)

if pocket_number >= 1 and pocket_number <= 10:
    if pocket_number == 1:
        pocket_1 = "red"
        print("Pocket 1 is", pocket_1)
    elif pocket_number == 2:
        pocket_2 = "black" 
        print("Pocket 2 is", pocket_2)
    elif pocket_number == 3:
        pocket_3 = "red" 
        print("Pocket 3 is", pocket_3)
    elif pocket_number == 4:
        pocket_4 = "black" 
        print("Pocket 4 is", pocket_4)
    elif pocket_number == 5:
        pocket_5 = "red"
        print("Pocket 5 is", pocket_5) 
    elif pocket_number == 6:
        pocket_6 = "black" 
        print("Pocket 6 is", pocket_6)
    elif pocket_number == 7:
        pocket_7 = "red" 
        print("Pocket 7 is", pocket_7)
    elif pocket_number == 8:
        pocket_8 = "black"
        print("Pocket 8 is", pocket_8) 
    elif pocket_number == 9:
        pocket_9 = "red"
        print("Pocket 9 is", pocket_9) 
    else:
        pocket_10 = "black"
        print("Pocket 10 is", pocket_10)
    

