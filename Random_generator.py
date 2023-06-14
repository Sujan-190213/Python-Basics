import random       # importing build in random module/ object
# for i in range(3):
#     print(random.random())             # rondom number between 0 to 1

# for i in range(3):
#     print(random.randint(10,20))         # rondom number between 10 to 20  (int)


# for i in range(3):
#     print(random.uniform(10.3,20.5))         # rondom number between 10.3 to 20.5  (float)

# name = "Sujan"
# print(random.choice(name))                    # rondom character "Sujan"  (string)

# print(random.randint(1,6))                    # Ludo

names = ["Sujan","Anamika","Tanmoy","Koushik","Marry"]
leader = random.choice(names)                   # rondom Lists 
print(f"Leader is : {leader}")
