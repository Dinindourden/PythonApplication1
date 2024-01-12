import random

difficulties = {"easy": 10, "hard": 5}

def guessing_the_number():
    hidden_number = random.randint(1,101)
    print(hidden_number)
    difficulty = input(f"Choose a difficulty level: easy or hard: ")
    number_of_tries = difficulties[difficulty]
    print (number_of_tries)
    used_guesses = 0
    while used_guesses < number_of_tries:
        print(f"You have {number_of_tries - used_guesses} attempts remaining.")
        user_guess = int(input("Guess a number: "))
        if user_guess > hidden_number:
            print("Too high.")
        elif user_guess < hidden_number:
            print("Too low")
        used_guesses += 1
        if user_guess == hidden_number:
            print("You guessed the number! You won!")
            break
            
        if used_guesses == number_of_tries:
            print(f"You lost the game. The number was {hidden_number}")


restart_game = True

while restart_game:
    guessing_the_number()
    play_again = input("Would you like to play again? (yes / no): ")
    if play_again == "no":
        restart_game = False


