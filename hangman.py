import random
import hangman_art
import os


print(hangman_art.logo)
stages = hangman_art.stages
end_of_game = False
word_list = ["orosz", "cinege", "villamos", "csigabiga", "tortaszelet"]
chosen_word = random.choice(word_list)
lives = 6
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')
display = []
guessed_letters = []
for letter in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')

    if guess in display:
        print("You already guessed this letter correctly")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    if guess in guessed_letters:
        print(f"You have already guessed {guessed_letters} incorrectly.")

    if guess not in chosen_word and guess not in guessed_letters:
        print(f"The letter \"{guess}\" is not in the word. You loose a life.")
        lives -= 1
        guessed_letters.append(guess)
 
        if lives == 0:
            end_of_game = True
            print("YOU LOSE :(")
    
    print(f"{' '.join(display)}")
    
    print(stages[lives])
   
    if "_" not in display:
        end_of_game = True
        print("YOU WIN!")