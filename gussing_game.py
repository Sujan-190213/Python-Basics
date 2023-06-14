secret_number = 3
guess_count = 0
guess_limit = 3
while guess_count < 3 :
    guess = int(input("Guess :"))

    if guess == secret_number :
        print("You're Win!")
        break
    else:
        print("You're Failed!")
    guess_count += 1
