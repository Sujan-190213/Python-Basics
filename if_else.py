# if , else if and else statement
# Example 1

# is_hot = True
# is_cold = False
# if is_hot :
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold :
#     print("It's a cold day")
#     print("Wear warm clothes")
# else :
#     print("It's a lovely day")
# print("Enjoy your day")

# Example 2

# price = 1000000
# has_good_credit = True
#
# if has_good_credit :
#     payment = price * 0.1
# else :
#     payment = price * 0.2
# print(f"The payment is : ${payment}")

# Example 3

# age = int(input("Enter your age : "))
# if age <=10 :
#     print("You're too young to see this video.[Age Restricted!]")
# elif age< 18 :
#     print("You are less than 18 and you are not eligible for this video.")
# else :
#     print("Enjoy this video")
# print("Thank you.")


# Example 3

# temperature = float(input("Enter the temperature : "))
# if temperature > 30 :
#     print("It's a hot day")
# elif temperature < 10 :
#     print("It's a cold day")
# else :
#     print("It's neither nor nor cold")


# Example 4
name = len(input("Enter the name : "))
if name <= 3 :
    print("Name must be at least 3 characters")
elif name <= 50 and name > 3 :
    print("Name can be a maximum of 50 characters ")
else :
    print("Name looks good!")
