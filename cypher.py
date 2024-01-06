import cypher_art

print(cypher_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift):
  new_text = ""
  if direction == "decode":
    shift *= -1
  for char in text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift
        if new_position > len(alphabet)-1:
         new_position = new_position - len(alphabet)
        if new_position < 0:
          new_position = len(alphabet) + new_position
        new_text += alphabet[new_position]
    else:
       new_text += char
  print(f"The {direction}d text is: {new_text}")
  
restart_program = True

while restart_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift)
    choice = input("Would you like to execute the program again? (y/n) ")
    if choice == "n":
      restart_program = False