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

user_input = int(input("V�lassz k?(0), pap�r(1), vagy oll�(2) "))
while user_input > 2 or user_input < 0:
    user_input = int(input("K�rlek csak 0 �s 2 k�z�tti sz�mokat �rj be: V�lassz k?(0), pap�r(1), vagy oll�(2) "))
    
