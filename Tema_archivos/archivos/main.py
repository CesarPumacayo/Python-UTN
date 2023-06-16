import csv
import json

#binarios
#texto
#csv -> coma separated value
#json -> java script objetc notation

# leer -> r/r+
# escribir -> w/w+ ()
# añadir info -> a

# archivo = open(ruta, 'r')
# print(archivo)
# archivo.close()


def leer_csv(ruta:str):
    lista_retorno = []
    with open(ruta, 'r') as archivo:
        # segunda_lista_aux = archivo.readlines() esto es una etapa intermedia en lugar de iterar el objeto file de forma directa
        for usuario in archivo:
            usuario = usuario.replace("\n", "")
            lista_aux = usuario.split(',')
            lista_retorno.append(lista_aux)
    return lista_retorno

def guardar_csv(ruta:str, lista_usuarios:list):
    with open(ruta, 'w') as archivo:
        for usuario in lista_usuarios:
            archivo.write(",".join(usuario)+'\n')

def leer_json(ruta:str)->list:
    with open(ruta, 'r') as archivo:
        diccionario_usuarios = json.load(archivo)
    return diccionario_usuarios["usuarios"]
    
def guardar_json(ruta:str, lista_usuarios:list)->None:
    with open(ruta, 'w') as archivo:
        json.dump(lista_usuarios, archivo, indent=4)


rutaCSV = "Archivos\\usuarios.csv"
rutaJSON = "Archivos\\usuarios.json"


# Leer y Escribir en JSON
# lista_usuarios = leer_json(rutaJSON)
# guardar_json('prueba.json', lista_usuarios)

# Leer y Escribir en CSV
lista_usuarios = leer_csv(rutaCSV)
guardar_csv("prueba.csv", lista_usuarios)

print(lista_usuarios)
