def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "- "
    return displayed_word.strip()

def play_game():
    word = input("Enter the word to guess: ").lower()
    guessed_letters = []
    strikes = 0

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", ", ".join(guessed_letters))

        if "-" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word correctly!")
            break

        if strikes >= 5:
            print("Sorry, you lost! The word was:", word)
            break

        guess = input("Guess a letter (or type 'quit' to exit): ").lower()

        if guess == "quit":
            print("Thanks for playing!")
            break

        if guess in guessed_letters:
            print("You already guessed that letter. Try again!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            strikes += 1
            print("Strike", strikes, "out of 5!")
            
play_game()
