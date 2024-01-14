
first = 100
second = 200

user_input = input("which is higher, A or B?: ")

if user_input == "A":
    choice = first
    shit = second
else:
    choice = second
    shit = first

if choice - shit > 0:
    print("You won")
else:
    print("You lost")    
