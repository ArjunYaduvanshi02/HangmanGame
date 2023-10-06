import tkinter as tk
from PIL import Image,ImageTk

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "- "
    return displayed_word.strip()

def guess_letter():
    guess = letter_entry.get().lower()
    letter_entry.delete(0, tk.END)

    if guess == "quit":
        result_label.config(text="Thanks for playing!")
        letter_entry.config(state=tk.DISABLED)
        return

    if guess in guessed_letters:
        result_label.config(text="You already guessed that letter. Try again!")
        return

    guessed_letters.append(guess)

    if guess not in word:
        strikes[0] += 1
        result_label.config(text="Strike {} out of 5!".format(strikes[0]))
    else:
        if "-" not in display_word(word, guessed_letters):
            result_label.config(text="Congratulations! You guessed the word correctly!")
            letter_entry.config(state=tk.DISABLED)
            return

    word_label.config(text=display_word(word, guessed_letters))
    guessed_label.config(text="Guessed letters: {}".format(", ".join(guessed_letters)))

    if strikes[0] >= 5:
        result_label.config(text="Sorry, you lost! The word was: {}".format(word))
        letter_entry.config(state=tk.DISABLED)

def play_game():
    global word, guessed_letters, strikes

    word = word_entry.get().lower()
    word_entry.delete(0, tk.END)
    guessed_letters = []
    strikes = [0]

    word_label.config(text=display_word(word, guessed_letters))
    guessed_label.config(text="Guessed letters: ")
    result_label.config(text="")

    letter_entry.config(state=tk.NORMAL)
    letter_entry.focus()

root = tk.Tk()
root.title("Hangman Game")
root.geometry("800x200")
bg_image = Image.open("./bg.png")
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to hold the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, height=200,width=300)

word_frame = tk.Frame(root)
word_frame.pack(pady=10)

word_label = tk.Label(word_frame, text="Word: ")
word_label.pack(side=tk.LEFT)

guessed_label = tk.Label(word_frame, text="Guessed letters: ",font=("Arial", 16, "bold italic"))
guessed_label.pack(side=tk.LEFT, padx=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

word_entry_label = tk.Label(input_frame, text="Enter the word to guess: ",font=("Arial", 8, "bold italic"))
word_entry_label.grid(row=0, column=0)

word_entry = tk.Entry(input_frame)
word_entry.grid(row=0, column=1)

letter_label = tk.Label(input_frame, text="Guess a letter: ",font=("Arial",8,"bold italic"))
letter_label.grid(row=1, column=0)

letter_entry = tk.Entry(input_frame)
letter_entry.grid(row=1, column=1)
letter_entry.config(state=tk.DISABLED)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

guess_button = tk.Button(button_frame, text="Guess", command=guess_letter)
guess_button.grid(row=0, column=0)

play_button = tk.Button(button_frame, text="Start", command=play_game)
play_button.grid(row=0, column=1)

quit_button = tk.Button(button_frame, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=4)


result_label = tk.Label(root, text="")
result_label.pack(pady=10)

play_game()

root.mainloop()
