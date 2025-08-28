import random
import os

#Tupla que contiene palabras que rotarán en el juego.
Palabras_Ahorcado= ("python", "hola mundo", "programacion", "desarrollador", "algoritmo", "pc", "monitor", "pelota", "lionel messi", "lunes")

#función que elege palabra al azar de la tupla.
def palabras_random():
    palabra = random.choice(Palabras_Ahorcado)
    return palabra

#función que arma palabra "AHORCADO" con los errores que haya en el juego.
def errores(error):
    perdio = "AHORCADO"
    if error < 0: error = 0
    if error > len(perdio): error = len(perdio)
    return perdio[:error]

#función que valida si la Letra ingresada es correcta (band False) o incorrecta (band True).
def escribir_letras(letras, intento_uno=None):
    bandera= True
    letra=""
    while bandera:
        if intento_uno is None:
            letra= input("Ingrese una Letra: ").lower().strip()
        else:
            letra= intento_uno.lower().strip()
            intento_uno= None
        valida= (len(letra) ==1) and letra.isalpha()
        repite= (letra not in letras)
        if valida and repite:
            bandera= False
        else:
            print("Error, ingrese una Letra válida y que no haya repetido")
    return letra

#función que permite arriesgar la palabra completa en un intento.
def escribir_palabra():
    bandera= True
    palabra=""
    while bandera:
        palabra= input("Ingrese la Palabra Completa: ").lower().strip()
        valida= len(palabra) >0
        if valida:
            bandera= False
        else:
            print("Error, ingrese una Palabra válida")
    return palabra

#función que muestra proceso OK del juego armando la palabra.
def proceso_OK(palabra, letras):
    texto= ""
    for letra in palabra:
        if letra in letras:
            texto += letra + " "
        else:
            texto += "_ "
    return texto.strip()

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')