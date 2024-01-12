from random import randint

def setting_difficulty():
    difficulties = {"easy": 10, "hard": 5}
    difficulty = input(f"Choose a difficulty level: easy or hard: ")
    return difficulties[difficulty]

def guessing_the_number(hidden_number, guess, turns):
    """Checks answer against guess. Returns the number of tries remaining."""
    if hidden_number > guess:
        print("Too low.")
        return turns - 1
    elif hidden_number < guess:
        print("Too high")
        return turns - 1
    else:
        print("You hit the guessed number! Congrats!")

def game():
    number_of_tries = setting_difficulty()

    hidden_number = randint(1,100)
    print(hidden_number)
    guess = 0
    while guess != hidden_number:
        print(f"You have {number_of_tries} attempts to guess the number. Good luck!")
        guess = int(input("Guess a number: "))
        number_of_tries = guessing_the_number(hidden_number, guess, number_of_tries)
        if number_of_tries == 0:
            print("You've run out of guesses, you loose :( )")
            return
        elif guess  != hidden_number:
            print("Guess again!")

replay = True
while replay:
    game()
    play_again = input("Would you like to play again? (yes / no): ")
    if play_again == "no":
        replay = False
        print("Thank you for playing, I hope you enjoyed it!")



