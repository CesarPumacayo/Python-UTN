#Strip()

cadena = "\tHola Ernesto\n"
print(cadena)


cadena = cadena.strip("s tHo")
"""si pones \t y \n dentro del parentesis alli lo modifica"""
print(cadena)
#rstrip()

cadena = cadena.rstrip("s tHo\t\n")
print(cadena)


#lstrip()


cadena= cadena.lstrip("s tHo\t\n")
print(cadena)
