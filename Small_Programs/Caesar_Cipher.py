import numbers

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def caesar(start_text, shift_ammount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_ammount *= -1
    # If user enter a really big number, reduce it
    if shift_ammount > 26:
        shift_ammount = shift_ammount % 26
    for char in start_text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = alphabet.index(char) + shift_ammount
            end_text += alphabet[new_position]
    print(f"\nThe {cipher_direction} text is : {end_text}")


while direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type th shift number:\n"))

    caesar(start_text=text, shift_ammount=shift, cipher_direction=direction)

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
