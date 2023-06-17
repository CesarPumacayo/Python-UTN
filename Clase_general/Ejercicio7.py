string= input("Introduce un string para invertirlo: ")
substring= ""

for character in string:
    substring= character + substring

print(substring)
