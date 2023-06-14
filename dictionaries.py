# Dictionaries in Python

# Dictionaries key should be unique
# Like object in C++
# student ={
#     "name" : "Sujan Dhali",
#     "discipline" : "CSE",
#     "e-mail" : "sujandhali1999@gmail.com",
#     "student_id" : 190213,
#     "is_verified" : True
# }
# print(type(student))            # <class 'dict'>
# print(student["discipline"])
# print(student["student_id"])
# print(student.get("birth_date","24-11-1999"))
# print(student)   # printing the dictionaries
# student["name"] = "Anamika Mondal"  # Modifying
# print(student)   # printing the dictionaries after modifying
# student["is_good"] = "Yes"  # add an element in the dictionaries
# print(student)   # printing the dictionaries after add an element


# Example 1
# Emoji convater
message = input(">")
words = message.split()
                             # print(message.split())
                             # print(message.split(' '))
emojis = {
    ":)" :"😊",
    ":(" : "😭"
}
output = ""
for word in words :
    output += emojis.get(word,word) + " "
print(output)




