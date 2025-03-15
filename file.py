import time

orin_lower = "abcdefghijklmnopqrstuvwxyz"
x_lower = "nopqrstuvwxyzabcdefghijklm"

orin_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x_upper = "NOPQRSTUVWXYZABCDEFGHIJKLM"

orin_numbers = "0123456789"
x_numbers = "4903176582"

orin_symbols = "!@#$%^&*()_+-=[]{}|;:',.<>?/~`"
x_symbols = "~`!@#$%^&*()_+-=[]{}|;:',.<>?/"

choice = input("Encode or Decode (e/d): ").lower()

if choice == "e":
   file1 = input("File Name (include extension e.g: .txt, .py): ")
   s = time.perf_counter()
   with open (file1, "r") as file:
       z = file.read()
   new = ""
   for letter in z:
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
   e = time.perf_counter()
   l = e-s
   file.close()
   with open (file1 , "w") as file:
      file.write(" ")
      file.write(new)
   print(f"Encoded Text, {l}s")
elif choice == "d":
   file1 = input("File Name (include extension e.g: .txt, .py): ")
   s = time.perf_counter()
   with open (file1, "r") as file:
       z = file.read()
   new = ""
   for letter in z:
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
   e = time.perf_counter()
   l = e-s
   file.close()
   with open (file1 , "w") as file:
      file.write(" ")
      file.write(new)
   print(f"Decoded Text, {l}s")
