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
game_over = False
prev_guessed_letter = []

while not game_over:

    user_input = input("Guess a letter: ").lower()
    # print(user_input)


    display = ""


    for letter in random_name :
        if letter == user_input:
            display += letter
            prev_guessed_letter.append(user_input)
        elif letter in prev_guessed_letter:
            display += letter
        else:
            display+= "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You Win!!")


# correct_letter = ["a","b","d"]
# word = "abcd"
# display = ""
#
# for letter in word:
#     if letter in correct_letter:
#         display += letter
#
# print(display)