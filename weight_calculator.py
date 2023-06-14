weight = float(input('Enter the weight : '))
input = input("Enter L for Pounds and K for Kilogram : ")
if input.upper() == 'L' :
    weight = weight * 0.454
    print(f"You're {weight} kilograms")

elif input.upper() == 'K' :
    weight = weight * 2.205
    print(f"You're {weight} pounds")

