# Hints :
# (self) refer to the current object
# class method with no parameter are always (self)

            # Defyning a Class

# class Point:
#     def move(self):
#         print("Move the point")
#     def draw(self):
#         print('Draw the point')
#
#
# point1 = Point()         # Creating an object
# point1.draw()
# point1.x = 10            # assign a value in the variable 'x' but not manually(using constructor)
# print(point1.x)
# point1.move()
#
# point2 = Point()        # Creating another object
# point2.draw()
# point1.x = 10            # assign a value in the variable 'x' but not manually(using constructor)
# # print(point2.x)       # AttributeError: 'Point' object has no attribute 'x'
# point1.move()


                # Using Constructor
class Point:
    def __init__(self,x,y):       # constructor
        self.X = x               # self.x = x   # Good practice
        self.Y = y               # self.y = y   # Good practice 
    def move(self):
        print("Move the point")
    def draw(self):
        print('Draw the point')


point1 = Point(10,20)        # TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'
point1.draw()
print(point1.draw())
print(point1.Y)
point1.move()