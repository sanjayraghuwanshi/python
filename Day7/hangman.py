import random
import hangman_words
import hangman_art

# print(stages[6]) - start
# print(stages[0]) - game over

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in chosen_word:
        display += "_"
#print(display)

end_of_game = False
lives = 6
list_of_guesses = []

# Loop through chosen word for each guess
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in list_of_guesses:
        print(f"You've already guessed {guess}")
    list_of_guesses.append(guess)
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}\n")
 
# Reduce lives if guess is wrong.   
    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
        if lives == 0:
            end_of_game = True
            print("Game Over")
    print(hangman_art.stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You Win")    