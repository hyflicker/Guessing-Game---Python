import random


def number_game():
    random_number = random.randint(1, 10)  # Numbers between 1 - 10
    guessed_number = int(input("Guess a number between 1 and 10:\n"))
    while random_number != guessed_number:
        if random_number > guessed_number:
            print("Too low, try again!")
        else:
            print("Too high, try again!")
        guessed_number = int(input("Guess a number between 1 and 10:\n"))
    print("Congratulation you guessed it! You won!")
    quit_game()


def quit_game(invalid=False):
    if invalid:
        print("That is not a valid answer!")
    ask_to_quit = input("Do you want to play again?\n")
    if ask_to_quit.lower() == "y":
        number_game()
    elif ask_to_quit.lower() == "n":
        print("Thanks for playing! Bye!")
    else:
        quit_game(True)


number_game()
