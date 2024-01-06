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

user_input = int(input("V�lassz k�(0), pap�r(1), vagy oll�(2) "))
print(f"A te v�laszt�sod: {shapes[user_input]} ")

computer_input = random.randint(0,2)
print(f"A sz�m�t�g�p v�laszt�sa:  \n {shapes[computer_input]}")

if user_input == 2 and computer_input == 0:
    print("Nyert�l")

#Draw
if user_input == computer_input:
    print("D�ntetlen")
#User wins
elif user_input == 1 and computer_input == 3:
    print("Nyert�l :D ")
    
elif user_input == 2 and computer_input == 1:
    print("Nyert�l :D ")
    
elif user_input == 3 and computer_input == 2:
    print("Nyert�l :D ")
#Computer wins    
elif user_input == 1 and computer_input == 2:
    print("Vesztett�l =(")
    
elif user_input == 2 and computer_input == 3:
    print("Vesztett�l =(")
    
elif user_input == 3 and computer_input == 1:
    print("Vesztett�l =(")