def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        word = ""
        for l in secret_word:
            if l in guesses:
                word += l
            else:
                word += "_"
        print(word)
        return word == secret_word
    return hangman_closure

secret_word = input("Enter the secret word: ")

hangman = make_hangman(secret_word)

while True:
    guess = input("Guess a letter: ")
    if hangman(guess):
        print("Congratulations! You guessed the word!")
        break




    