# Removing duplicate in a list

numbers = [1,2,3,4,5,3,2,4]
uniques = []
for number in numbers :
    if number not in uniques :
        uniques.append(number)
print(uniques)



