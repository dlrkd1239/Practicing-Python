# # # Step 1

# import random
# word_list = ["aardvark", "baboon", "camel"]

# # # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# chosen_word = random.choice(word_list)

# # # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# # guess = input("Make your guess : ").lower()
# # # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# # for letter in chosen_word:
# #     if (letter == guess):
# #         print("Right")
# #     else:
# #         print("Wrong")

# # Step 2
# count = 0

# # Testing code
# print(f'Pssst, the solution is {chosen_word}.')
# display = ["_"] * len(chosen_word)
# # TODO-1: - Create an empty List called display.
# # For each letter in the chosen_word, add a "_" to 'display'.
# # So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# while (count < len(chosen_word)):
#     guess = input("Guess a letter: ").lower()

#     # TODO-2: - Loop through each position in the chosen_word;
#     # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#     # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#     for n in range(len(chosen_word)):
#         if chosen_word[n] == guess:
#             display[n] = guess
#     print(display)
#     if ("_" not in display):
#         print("You win")
#         break
#     # TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#     # Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# Step 4

import random
import Hangman_Art
import Hangman_Word_List

print(Hangman_Art.logo)

end_of_game = False
chosen_word = random.choice(Hangman_Word_List.word_list)
word_length = len(chosen_word)
lives = 6

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    if (guess not in display):
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter
    else:
        print(f"You already guessed '{guess}'. Please try another one.")

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if (guess not in chosen_word):
        lives -= 1
        print(
            f"You guessed letter '{guess}' But '{guess}' is not in chosen word. You lose a life.")
        if (lives == 0):
            print("You lose.")
            end_of_game = True
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(Hangman_Art.stages[lives])
