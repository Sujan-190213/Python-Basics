# # Exception
#
# EOFError            # Raised when the input() function hits the end-of-file condition
# FloatingPointError  # Raised when floating point operation fails
# ImportError         # Raised when import module is not found
# IndexError          # Raised when the index of a sequence is out of range
# KeyError            # Raised when a key is not found in a dictionary
# NameError           # Raised when a variable is not found in the local or global scope
# NotImplementedError # Raised by abstract method
# OverflowError       # Raised when the result of an arithmetic operation is too large to be represented
# StopIteration       # Raised by the next() function to indicate that there is no further item to be returned by iterator
# SyntaxError         # Raised when a syntax error occured
# IndexError          # Raised when there is an incorrect indentation
# TypeError           # Raised when a function or operation is applied to an object of an incorrect type
# ValueError          # Raised when a function gets an argument of correct type but improper value   # int("dog")
# ZeroDivisionError   # Raised when the second operand of a division or module operation is zero



# Example 1

# try:
#     something = int(input("Enter something: "))    # input always returns a string
#     print(something  * 10)
#
# except ValueError:
#     print("You typed string which is not converted into integer")
# finally:
#     print("Thank you")      # This line always be exicuted



# Example 2


# try:
#     something = int(input("Enter something: "))    # input always returns a string
#     print(something  / 0)
#
# except ValueError:
#     print("You typed string which is not converted into integer")
# except ZeroDivisionError:
#     print("Division by Zero")
# finally:
#     print("Thank you")   # This line always be exicuted
