import random
import string
from words import words

word = random.choice(words)

def hangman():
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    guessCount = 5
    while len(word_letters) > 0 and guessCount > 0:
        print("You have ", guessCount,"lives left and you have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))
        user_input = input("Input a letter:").lower()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                guessCount -= 1
                print("You have not guessed the letter!")

        elif user_input in used_letters:
            print("You have already used that letter")
        else:
            print("You have not typed in a valid character")
    if guessCount == 0:
        print("You died! The word was: ", word)
    else:
        print("You guessed the word:", word,"!!!")
hangman()

