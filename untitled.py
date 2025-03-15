orin_lower = "abcdefghijklmnopqrstuvwxyz"
x_lower = "nopqrstuvwxyzabcdefghijklm"

orin_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x_upper = "NOPQRSTUVWXYZABCDEFGHIJKLM"

orin_numbers = "0123456789"
x_numbers = "4903176582"

orin_symbols = "!@#$%^&*()_+-=[]{}|;:',.<>?/~`"
x_symbols = "~`!@#$%^&*()_+-=[]{}|;:',.<>?/"

choice = input("Encode or Decode (e/d): ").lower()

if choice == "e" or choice == "encode":
    text = input("Text?: ")
    new = ""
    for letter in text:
        if letter == " ":
            new += " "
        elif letter in orin_lower:
            x = orin_lower.index(letter)
            new += x_lower[x]
        elif letter in orin_upper:
            x = orin_upper.index(letter)
            new += x_upper[x]
        elif letter in orin_numbers:
            x = orin_numbers.index(letter)
            new += x_numbers[x]
        elif letter in orin_symbols:
            x = orin_symbols.index(letter)
            new += x_symbols[x]
        else:
            new += letter
    print("Encoded Text:", new)

elif choice == "d" or choice == "decode":
    text = input("Text?: ")
    new = ""
    for letter in text:
        if letter == " ":
            new += " "
        elif letter in x_lower:
            x = x_lower.index(letter)
            new += orin_lower[x]
        elif letter in x_upper:
            x = x_upper.index(letter)
            new += orin_upper[x]
        elif letter in x_numbers:
            x = x_numbers.index(letter)
            new += orin_numbers[x]
        elif letter in x_symbols:
            x = x_symbols.index(letter)
            new += orin_symbols[x]
        else:
            new += letter
    print("Decoded Text:", new)

else:
    print("Invalid choice! Please enter 'e' or 'd'.")
