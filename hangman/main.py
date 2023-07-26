import requests


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
    i = 0

    print (word)

    while i < incorrect_guess:
        print("Max Guess: 6")
        print("Incorrect guesses:", i)
        
        print("Tried letters: ")
        for tried_letter in letters_tried:
            print (tried_letter, end = " ")

        print("\n")
        
        for letter in hidden_word:
            print (letter, end=' ')
            
        guess = input("\nGuess a letter: ").upper()

        if guess in letters_tried:
            print("You already guessed that letter!")
            continue

        letters_tried.append(guess)

        if guess in word:
            hidden_word = update_hidden(word, letters_tried, hidden_word)
            if stop_game(hidden_word):
                print("Word: ", word)
                print("Congratulations, You Won!")
                return
        else:
            i += 1
            print("Incorrect guess!")
    print("Incorrect guesses:", i)
    print("Game OVER, YOU SUCK!, the word was", word)



game()
