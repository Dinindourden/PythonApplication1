#!/usr/bin/env python
# -*- coding: latin-1 -*-
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

shapes = [rock, paper, scissors]
import random

user_input = int(input("Válassz kõ(0), papír(1), vagy olló(2) "))
print(f"A te választásod: {shapes[user_input]} ")

computer_input = random.randint(0,2)
print(f"A számítógép választása:  \n {shapes[computer_input]}")

if user_input == 2 and computer_input == 0:
    print("Nyertél")

#Draw
if user_input == computer_input:
    print("Döntetlen")
#User wins
elif user_input == 1 and computer_input == 3:
    print("Nyertél :D ")
    
elif user_input == 2 and computer_input == 1:
    print("Nyertél :D ")
    
elif user_input == 3 and computer_input == 2:
    print("Nyertél :D ")
#Computer wins    
elif user_input == 1 and computer_input == 2:
    print("Vesztettél =(")
    
elif user_input == 2 and computer_input == 3:
    print("Vesztettél =(")
    
elif user_input == 3 and computer_input == 1:
    print("Vesztettél =(")