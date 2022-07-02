import json
import random
import string


def get_random_word():
    with open("/Users/antontenytskyi/Projects/small_projects/resources/words.json", 'r') as f:
        words = json.load(f)
        list_of_words = words.keys()
        return random.choice(list(list_of_words))


def play(word):
    tries = 10
    used_letters = set()
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)

    while tries > 0 and len(word_letters) > 0:
        print(f"You have {tries} lives left and you already tried letters: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(" ".join(word_list))
        user_letter = input('Please guess a new letter: ')

        # block with guessing the whole word
        if user_letter == "G":
            full_word = input("Please enter the whole word ")
            if full_word == word:
                print(f"Congrats, you win, the word is {word}")
                break
            else:
                tries -= 1
                print("No this is not the letter")
                print(f"You have {tries} tries left")
                continue

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                tries -= 1
                print("No, there is no such letter in the word")
        elif user_letter in used_letters:
            print("Already used")
        else:
            print("Not a valid character")

    if tries == 0:
        print("Sorry, you lost(")
    if len(word_letters) == 0:
        print("Congrats you win")


x = get_random_word()
print(x)
play(x)
