from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def caesar(start_text, shift_amount, chosen_direction):
    end_text = ""
    if chosen_direction == "decode":
        shift_amount *= -1
    for char in start_text:

        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Here's the {chosen_direction}d result: {end_text}")




print(logo)
restart = "yes"

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    over_shift = shift
    if over_shift > 26:
        shift %= 2
        if shift == 0:
            shift = over_shift
            shift %= 3
    caesar(start_text=text, shift_amount=shift, chosen_direction=direction)
    restart = input("Do you like restart the program? 'Yes' or 'No'\n").lower()
    if restart == "no":
        print("Goodbye")