# Step 1
import random
import hangman_art
# import hangman_words
from hangman_words import word_list
# word_list = ["mouse","baboon","camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word

chosen_word = random.choice(word_list)

#  Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6
print(f"{hangman_art.logo}")
# Testing Code
# print(f"The solution is {chosen_word}")

#  TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase

# Create an empty list call display.
# For each letter in the chosen_word, add a "_" to 'display'.
# SO if the chosen_word was "apple", display should be ["__","__","__","__","__"] with 5 "_" representing each leetter to guess.

display = []
for letter in chosen_word:
    display += "_"
print (display)

# use while loop to let the user guess again. This loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks "_". Then you can tell user they've won.
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

#  TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word
# Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed 'p' and the chosen word was 'apple', then display should be ["_","p","p","_","_"].

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # print(f"Current postion: {position}")
        if letter == guess:
            display[position] = letter
        

# If guess is not a letter in the chosen_word, then reduce 'lives' by 1
# If lives goes down to 0 then the game should stop and it should print "You Lose".
    if guess not in chosen_word:
        #  if the letter is not in the chosen_word, print out the letter and let them know it's not in the word
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
              end_of_game = True
              print ("You lose")
              print(f"The actual word is {chosen_word}")

# Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}" )

# Print 'display' and you should see the guessed letter in the ccorrect position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 4.
    # print(display)

    if "_" not in display:
       end_of_game = True
       print("You win")

# print ASCII representation form "stages" that correspond to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])