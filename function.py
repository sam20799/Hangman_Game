import random
from hangman_words import word_list
from hangman_art import stages,logo


# reversed items cuz we'll print items from backwards
stages.reverse()
print("MADE BY SAM")
print(logo)

random_name = (random.choice(word_list))
print(random_name)

size = len(random_name)

placeholder = ""
for i in range(size):
    placeholder += "_"

print(placeholder)
game_over = False
prev_guessed_letter = []
live = 8

while not game_over:

    user_input = input("Guess a letter: ").lower()
    if user_input in prev_guessed_letter:
        print(f"You have already guessed this letter '{user_input}'")




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

    if user_input not in random_name:
        live -= 1
        print(f"******** You have {live} lives left ********")
        print(f"You have guessed the wrong letter '{user_input}'")

        if live == 0:
            game_over = True
            print("******** You Loose! ********")
            print(f"Correct word was '{random_name}'")


    if "_" not in display:
        game_over = True
        print("******** You Win!! ********")

    print(stages[live])

# correct_letter = ["a","b","d"]
# word = "abcd"
# display = ""
#
# for letter in word:
#     if letter in correct_letter:
#         display += letter
#
# print(display)