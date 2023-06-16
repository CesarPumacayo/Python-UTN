# Diccionario vacío
dicctionary_empty= {}

print(f"Diccionario vacío: {dicctionary_empty}")
print()

#Diccionario homogéneo

dictionary_ages = {"Juan": 32,
                   "Gerardo":21,
                   "Luis":25
                   }

print(f"Diccionario de edades: {dictionary_ages}")
print()

# Dicionario heterogéneo

dictionary_dates = {"name": "Brenda",
                    "Last name":"Flores",
                    "age": 22
                    }

print(f"Diccionario de edades: {dictionary_dates}")
print()

# Diccionario puede almacenar listas y diccionarios
dictionary_list= {"a": {"a": 1},
                  "b": [0,1,2],
                  }
print(f"Diccionario con lista y diccionario: {dictionary_list}")
print()

# Diccionario puede tener claves numéricas
dictionary_keys_num = {4:1,
                       5:2,
                       6:3
                       }
print(f"Diccionario con claves numéricas {dictionary_keys_num}")

# Diccionario no puede tener claves repetidas
dictionary_repeated_keys = {"Juan": 20,
                            "Gerardo":30,
                            "Juan":15
                            }
print(f"Diccionario con claves repetidas: {dictionary_repeated_keys}")
print()

# Diccionario puede tener claves numericas o de tipo texto
dictionary= {1:23,
             "Juan":5,
             -2:"hola"
             }
print(f"Diccionario con claves numéricas o de tipo texto: {dictionary})")
print()
