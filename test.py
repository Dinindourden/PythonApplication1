from turtle import Turtle, Screen
import prettytable

table = prettytable.PrettyTable()

table.add_column("Pokemon name", ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"])
table.add_column("Type", ["Plant", "Fire", "Water", "Electric"])

print(table)