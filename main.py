import random
import stages
import os

COLORS = {
    'reset': "\033[0m",
    'red': "\033[31m",
    'green': "\033[32m",
}

def choose_word():
    words = ["банан", "апельсин", "виноград", "ананас", "арбуз", "клубника"] #Вы можете добавить любые слова
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Давайте играть в Виселицу!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        stages.draw_hangman(attempts)
        guess = input("Введите букву: ").lower()

        if guess in guessed_letters:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Вы уже вводили эту букву. Попробуйте другую.")
            print(displayed_word)
            continue
        elif len(guess) != 1 or not guess.isalpha():
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Пожалуйста, введите только одну букву.")
            print(displayed_word)
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{COLORS['red']}Неправильно! {COLORS['reset']}У вас осталось {attempts} попыток.")
            if attempts == 0:
                stages.draw_hangman(0)
                print("Вы проиграли! Было загадано слово:", word_to_guess)
                break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{COLORS['green']}Правильно!{COLORS['reset']}")

        
        displayed_word = display_word(word_to_guess, guessed_letters)
        print(displayed_word)

        if "_" not in displayed_word:
            stages.draw_win()
            print("Поздравляем, вы выиграли!")
            break

if __name__ == '__main__':
    hangman()
