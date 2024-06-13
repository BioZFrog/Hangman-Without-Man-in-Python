import random 
from words import Words # Importing the list of words from words.py file

print("<------------Hangman------------>")
print("           BY BIOZFROG")

# Initializing Variables and Lists

guess_word = random.choice(Words) # Generating a random word from the list (Words) in words.py file
len_guess_word = len(guess_word)
blank_word = []
amount_guess_word = 7

# Using Blanks to represent the length of the random generated word 

for blank in range(len_guess_word):
    blank_word.append("_")

# Removing commas, and Square Brackets from the blanks

blank_word = str(blank_word)
blank_word = blank_word.replace("[","")
blank_word = blank_word.replace("]","")
blank_word = blank_word.replace(",", "")
blank_word = str(blank_word)
blank_word = blank_word.replace("'", "")

letter  = "" # Initializing the letter variable before use


print(f"\nYour Word is {blank_word}\n")

# Main loop

while letter != guess_word:
    letter = input("\nEnter a letter: ")
    
    # Amount of Guesses Conditions

    if str(letter) not in guess_word:
        amount_guess_word -= 1
        print(f"\n{amount_guess_word} Guesses")
    
    if amount_guess_word == 0:
        print(f"\n\nGame Over! The word was {guess_word}\n")
        break

    # Printing the input that matches the random generated word 

    for alph in guess_word:
        if alph in letter:
                if letter in guess_word:
                    print(alph, end = "")


    if letter == guess_word:
        print(f"\n\nCongratulations! You have guessed the word {guess_word}!\n")
