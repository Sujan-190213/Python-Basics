# car game
show = input("Enter something for hint : ")
print('''start - to start the car
stop - to stop the car
quit - to exit
''')
started = False
stopped = False
while True :
    command = input(">")
    if command.lower() == "start" :
        if started :
            print("Car is already started!")
        else :
            print("Car started...Ready to go!")
            started = True
    elif command.lower() == "stop" :
        if stopped :
            print("Car is already stopped!")
        else :
            print("Car stopped!")
            stopped = True
    elif command.lower() == "quit" :
        break
    else :
        print("Sorry,I don't understand that...")
