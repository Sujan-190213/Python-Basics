# Numbers       >>> 10
# Strings       >>> "Sujan"
# Booleans      >>> True/False
# ------------
# Lists          >>> name = [value1,value2,value3...]
# Dictionaries   >>> name = {"name1" : "value1",
#                            "name2" : "value2",
#                            "name3" : "value3"}
# ------------------------------------------------------
# Classes



                       # defining  a function

# def fun():
#     print("It's a function")
#
# print("Start Function call")
# fun()
# print("Stop Function call")


                         # defining  a class

class Student:
    def activity(self):     # (self) refer to the current object     # class method with no parameter are always (self)
        print("Work with web!")

    def hobby(self):        # class method with no parameter are always (self)
        print("Listen Music!")


student1 = Student()      # Creating an object
print(student1.activity())  # This line print extra 'None' because print(print_something) returns 'None'
student1.hobby()
student2 = Student()      # Creating an object
