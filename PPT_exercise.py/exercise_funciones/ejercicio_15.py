#Ejercicio 15
#Crear una función que recibe una lista de diccionarios con información de películas (título, género, director) y 
# devuelve un diccionario con la cantidad de películas por género.

def contar_peliculas_por_genero(lista_peliculas):
    dict_peliculas_por_genero = {} #Contador {'Drama': 2, 'Fantasía': 1, 'Ciencia ficción': 2, 'Comedia musical': 1}
    for pelicula in lista_peliculas:
        genero = pelicula["genero"] # Son las claves de los generos  
        if genero in dict_peliculas_por_genero:# Al principio te dice que no esta en el diccionario, pero en lin 85 cambia despues y le agrega "+= 1" como existente en el dict
            
            # Incremento de contador
            dict_peliculas_por_genero[genero] += 1
        else:
            # Creo la clave, y asigna "1" como primer valor
            dict_peliculas_por_genero[genero] = 1
    return dict_peliculas_por_genero

peliculas = [
    {
        "titulo": "El Padrino", 
        "genero": "Drama", 
        "director": "Francis Ford Coppola"
    },
    {
        "titulo": "El Señor de los Anillos", 
        "genero": "Fantasía", 
        "director": "Peter Jackson"
    },
    {
        "titulo": "Jurassic Park", 
        "genero": "Ciencia ficción", 
        "director": "Steven Spielberg"
    },
    {
        "titulo": "La La Land", 
        "genero": "Comedia", 
        "director": "Damien Chazelle"
    },
    {
        "titulo": "Titanic", 
        "genero": "Drama", 
        "director": "James Cameron"
    },    
    {
        "titulo": "Star Wars", 
        "genero": "Ciencia ficción", 
        "director": "George Lucas"
    }
]

resultado = contar_peliculas_por_genero(peliculas)


print(resultado)


