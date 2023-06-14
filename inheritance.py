                    # Inheritance

# class Class_name(Inherited Class_name)

# Example 1


# class Mammal:
#     def walk(self):
#         print("Mammal is Walking")
#
#
# class Dog(Mammal):      # inherited
#     pass                # Because this class has no variable or method
#
# class Cat(Mammal):
#     def walk(self):
#         print("Cat is Walking")
#
#
# dog1 = Dog()
# dog1.walk()
# cat1 = Cat()
# cat1.walk()


# Example 2

class Student:
    def __init__(self,name,university_name):
        self.name = name
        self.university_name = university_name
    def activity(self):
        print("Study")


student1 = Student("Sujan","Khulna University")
print(student1.name)
student1.activity()


