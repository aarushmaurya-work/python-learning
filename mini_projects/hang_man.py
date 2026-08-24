import random

# hangman gaem

fruits = [
    "apple",
    "banana",
    "grapes",
    "kiwi",
    "orange",
    "dragonfruit",
    "mango",
    "watermelon",
    "strawberry",
    "blueberry",
    "pineapple",
    "peach",
    "pear",
    "plum",
    "cherry",
    "lemon",
    "lime",
    "pomegranate",
    "papaya",
    "raspberry",
    "blackberry",
    "fig",
    "guava",
]
#You can add more fruits
def get_random_fruit():
    random_fruit = random.choice(fruits)
    return random_fruit


def draw_hangman(stage):
    if stage == 1:
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")

    elif stage == 2:
        print("|------")
        print("|")
        print("|")
        print("|")
        print("|")

    elif stage == 3:
        print("|------|")
        print("|     (_)")
        print("|      |")
        print("|")
        print("|")

    elif stage == 4:
        print("|------|")
        print("|     (_)")
        print("|      |")
        print("|     /")
        print("|")
    elif stage == 5:
        print("|------|")
        print("|     (_)")
        print("|      |")
        print("|     / \\")
        print("|")
    else:
        print("(^_^)")
        print(" \\|/")
        print("  |")
        print(" / \\")


def pretty_print(word, char_used):
    result = ""
    for ch in word:
        if ch in char_used:
            result += ch
        else:
            result += "_"
        result += " "
    return result[:-1]


def main():
    fruit = get_random_fruit()
    char_used = []
    lives = 5
    while True:
        while True:
            guess = input("Enter a character: ")
            if len(guess) != 1:
                print("Enter single character only.")
            elif guess in char_used:
                print("Character already used.")
            else:
                break
        char_used.append(guess)
        if guess not in fruit:
            lives -= 1
        print()
        draw_hangman(5 - lives)
        print()
        print(pretty_print(fruit, char_used))
        print(f"LIFE : {lives}")
        if lives <= 0:
            print("You lost")
            print(f"The fruit was {fruit}")
            break
        if pretty_print(fruit, char_used).replace(" ", "") == fruit:
            print("You won")
            break

main()