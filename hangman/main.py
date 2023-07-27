import requests
import string


def get_random_word():
    url = 'https://random-word-api.vercel.app/api?words=1'
    response = requests.get(url)
    data = response.json()
    word = data[0].upper()
    return word


def hangman():
    word = get_random_word()
    letters_tried = []
    incorrect_guess = 6
    # wanted to make a simple gui of stickman here
    return word, letters_tried, incorrect_guess


def update_hidden(word, letters_tried, hidden_word):
    for i in range(len(word)):
        if word[i] in letters_tried:
            hidden_word[i] = word[i]
    return hidden_word


def stop_game(hidden_word):
    for i in hidden_word:
        if i == "_":
            return False
    return True


def game():
    word, letters_tried, incorrect_guess = hangman()
    hidden_word = ["_"] * len(word)
    alphabet = set(string.ascii_uppercase)
    i = 6

    while i != 0:
        print("--------------------------------------------")
        print("\nGuesses remaining:", i)
        
        print("Tried letters: ")
        for tried_letter in letters_tried:
            print (tried_letter, end = " ")

        print("\n")
        
        for letter in hidden_word:
            print (letter, end=' ')
        
        print("\n\n--------------------------------------------")
            
        guess = input("\nGuess a letter: ").upper()

        if guess not in alphabet:
            print("Invalid letter, please try again")
            continue

        if guess in letters_tried:
            print("You already guessed that letter!")
            continue

        letters_tried.append(guess)

        if guess in word:
            hidden_word = update_hidden(word, letters_tried, hidden_word)
            print(guess, " is in the word!")
            if stop_game(hidden_word):
                print("\n--------------------------------------------")
                print("Word: ", word)
                print("Congratulations, You Won!")
                print("Press any button to exit")
                print("--------------------------------------------")
                input()
                return
        else:
            i -= 1
            print("Incorrect guess!")
    print("Incorrect guesses:", i)
    print("\n--------------------------------------------")
    print("Game OVER!, the word was", word)
    print("Press any button to exit")
    print("--------------------------------------------")
    input()
    return
game()
