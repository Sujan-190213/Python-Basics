# Lists

# names = ["Saagata","Rupali","Anamika","Puja"]
#         #    0         1        2        3
# print(names[1])
# print(names[1:])
# print(names[:3]) # Except 3 th index
# print(names) # This list will not affected by previous operation
#
# # To change the list item
# names[0] = "Swagata"
# print(names)


# Example 1
# Find the largest value in the list

# lists = [3,6,2,8,4,10,333]
#      #   0 1 2 3 4 5
# length = len(lists)   #  Calculate Length
# large = lists[0]
# for x in range(length) :
#     if lists[x] > large :
#         large = lists[x]
#     else :
#         large = lists[0]
# print(f"Largest number of the lists is : {large}")


# Example 2
# Matrix or 2D array

matrix = [
    [1,2,3],    # 0
  #  0 1 2
    [4,5,6],    # 1
  #  0 1 2
    [7,8,9]     # 2
  #  0 1 2
]
length = len(matrix)   # length of the matrix
for row in range(length) :
    for coloumn in range(length) :
        # print(matrix[row][coloumn])  # Easy way
        print(f"index is : [{row},{coloumn}] and value is : {matrix[row][coloumn]}") # Better way