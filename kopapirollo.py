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

user_input = int(input("Válassz k?(0), papír(1), vagy olló(2) "))
while user_input > 2 or user_input < 0:
    user_input = int(input("Kérlek csak 0 és 2 közötti számokat írj be: Válassz k?(0), papír(1), vagy olló(2) "))
    
