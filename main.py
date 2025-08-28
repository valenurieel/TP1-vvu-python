import funciones as f

def ahorcado():
    estado_inicio={"palabras":f.palabras_random(), "letrasOK":[], "letrasMAL":[], "errores":0, "gano":False}
    fallos_max= len("AHORCADO")

    bandera= True
    while bandera:
        f.limpiar()
        print("---------- Estado actual de Juego ----------")
        print("Palabra:", f.proceso_OK(estado_inicio["palabras"], estado_inicio["letrasOK"]))
        print("Errores:", f.errores(estado_inicio["errores"]))
        print("Letras Utilizadas:", estado_inicio["letrasOK"] + estado_inicio["letrasMAL"])
        print("Te quedan", fallos_max - estado_inicio["errores"], "intentos")

        valor= input("Ingresa una Letra o escribí '!' para arriesga la Palabra Completa: ").strip().lower()

        if valor == "!":
#            f.limpiar()
            print("Atención, si te equivocas perderás el juego. ¡Muchas Suerte!") #Arriesgando la palabra completa.1
            intento= f.escribir_palabra()
            if intento == estado_inicio["palabras"]:
                estado_inicio["gano"]= True
            else:
                print("¡Palabra Incorrecta, al final sos un Burro!")
                estado_inicio["errores"] = fallos_max
        else:
            ingresado= estado_inicio["letrasOK"] + estado_inicio["letrasMAL"]
            letra= f.escribir_letras(ingresado,valor)
            if letra in estado_inicio["palabras"]:
                estado_inicio["letrasOK"].append(letra)
                completo=True
                for letra in estado_inicio["palabras"]:
                    if letra not in estado_inicio["letrasOK"]:
                        completo=False
                estado_inicio["gano"]= completo #No gano.
            else:
                estado_inicio["letrasMAL"].append(letra)
                estado_inicio["errores"] += 1
        f.limpiar()
        if estado_inicio["gano"] or estado_inicio["errores"] == fallos_max:
            bandera= False
    
    if estado_inicio["gano"]:
        print("¡Ganaste Crackk! La palabra era:", estado_inicio["palabras"])
    else:
        print("¡Perdiste Burroooo! La palabra era:", estado_inicio["palabras"])

#función que muestra el menú principal del juego.
def menu():
    bandera=True
    f.limpiar()
    while bandera:
        print("-- Bienvenido al Juego del Ahorcado, donde veremos que tan burro eres o nos callaras la boca --")
        print("1. Jugar")
        print("2. Salir")
        opcion= input("Ingrese una opción: ").strip()
        if opcion == "1":
            ahorcado()
        elif opcion == "2":
            bandera= False
        else:
            print("Seleccioná una opción de las mencionadas, no la compliques pibe...")

#inicializador.
if __name__ == "__main__":
    menu()