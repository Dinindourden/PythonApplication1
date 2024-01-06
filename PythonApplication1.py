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
print (shapes[user_input])

computer_input = random.randint(0,2)
print(f"A számítógép választása:  \n {shapes[computer_input]}")

