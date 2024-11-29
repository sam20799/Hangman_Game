import random

# print("Hello")
# total_char = len("Hello")
# print(total_char)
#
# def function():
#     print("SAM")
#     print(len("sam"))
#
#
# for i in range(6):
#     print(i)


names = ["sam","dam","obam","sahzam"]

random_name = (random.choice(names))
print(random_name)

size = len(random_name)

placeholder = ""
for i in range(size):
    placeholder += "_"

print(placeholder)

user_input = input("Guess a letter: ").lower()
# print(user_input)


display = ""


for letter in random_name :
    if letter == user_input:
        display += letter

    else:
        display+= "_"

print(display)


