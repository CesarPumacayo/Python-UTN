string= "0123456789"
substring=""

print(f"Cadena principal: {string}")

substring = string[0]
print(f"\nSubcadena con indice en la posicion [0] es: {substring}")

substring = string[5]
print(f"\nSubcadena con indice en la posicion [5] es: {substring}")

substring = string[-4]
print(f"\nSubcadena con indice en la posicion [-4] es: {substring}")

substring = string[0:3]
print(f"\nSubcadena con indices en la posiciones [0:3] es: {substring}")

substring = string[:3]
print(f"\nSubcadena con indices en la posiciones [:3] es: {substring}")

substring = string[5:]
print(f"\nSubcadena con indices en la posiciones [5:] es: {substring}")

substring = string[-4:-1]
print(f"\nSubcadena con indices en la posiciones [-4:-1] es: {substring}")

substring = string[:]
print(f"\nSubcadena con indices en la posiciones [:] es: {substring}")

substring = string[1:6:2]
print(f"\nSubcadena con indices en la posiciones y salto [1:6:2] es: {substring}")

substring = string[::3]
print(f"\nSubcadena con indices en la posiciones y salto [::3] es: {substring}")
