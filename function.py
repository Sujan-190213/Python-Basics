# Function in Python

# Method overloading is not supported in Python but Method overriding is supported
# Keyword argument is useable for code readablity
# Order for keyword argument >> first positional argument then keyword argument
# Expect 2 blank line before and after function defination

# Function without parameter


# def message_1():
#     print("Hi,Sujan is here")
#     print("Welcome")


# Function with parameter



# def message_2(name):
#     print(f"Hi, {name} is here")
#
#
# print("Start!")
# message_1()
# message_2("Anamika")
# print("Finished!")

# def full_name(first_name,last_name):
#     print(f"Hi,{first_name} {last_name}")
#
#
# print("Start!")
# full_name('Sujan','Dhali')
# print("End!")

# Keyword argument


def full_name(first_name, last_name):
    print(f"Hi,{first_name} {last_name}")


print("Start!")
# full_name( first_name='Sujan','Dhali')  # Error ositional argument follows keyword argument
# full_name('Sujan',first_name='Dhali')    # 'Sujan' is treated as first_name so an error is occured ( full_name() got multiple values for argument 'first_name' )
full_name(last_name='Sujan',first_name='Dhali')     # So all the keyword argument is keyworded properly an fully
print("End!")

