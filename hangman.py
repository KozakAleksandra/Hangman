import sys

num_of_tries = 5 
word_to_guess = input("Choose the word: ")
used_letters = []

user_word = []

def find_indexes(word_to_guess, letter):
    indexes = []

    for index, letter_in_word in enumerate(word_to_guess):
        if letter == letter_in_word:
            indexes.append(index)
   
    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Number of tries:", num_of_tries)
    print("Used letters:", used_letters)
    print()


for letter in word_to_guess: 
    user_word.append("_")

while True:
    letter = input("Choose letter: ")
    used_letters.append(letter)

    found_indexes = (find_indexes(word_to_guess, letter))

    if len(found_indexes) == 0:
        print("The letter is not existing in this word.")
        num_of_tries -= 1 
        if num_of_tries == 0:
            print("You're out of lives. Sorry game over.")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word_to_guess:
            print("SUCCESS!! You win game, congratulation :)")
            sys.exit(0)

    show_state_of_game()



