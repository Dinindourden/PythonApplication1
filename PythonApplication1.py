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
print (shapes[user_input])

computer_input = random.randint(0,2)
print(f"A sz�m�t�g�p v�laszt�sa:  \n {shapes[computer_input]}")

