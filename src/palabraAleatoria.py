import random

def seleccionar_palabra():
    with open("./words.txt") as archivo:
        listaPalabras = archivo.readlines()
        tamañoLista = len(listaPalabras)
        indiceAleatorio = random.randint(0, tamañoLista - 1)
        palabraAleatoria = listaPalabras[indiceAleatorio].strip()
        return palabraAleatoria