
import random
from hangman_art import logo,stages
from hangman_words import word_list

print(logo)
game_is_finished = False
lives = len(stages)-1

chosen_word = random.choice(word_list)
word_lenth = len(chosen_word)

display =[]
for _ in range(word_lenth):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already {display} this word")

    for position in range(word_lenth):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess} and it is not in the list")
        lives -= 1
        if lives == 0:
            print("You lose")
            game_is_finished = True

    if not "_" in display:
        game_is_finished = True
        print("You won the game")

    print(stages[lives])











