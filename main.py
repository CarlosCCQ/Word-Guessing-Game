from src.palabraAleatoria import seleccionar_palabra
from src.pistasPalabra import Pistas
from src.adividarPalabra import AdivinarPalabra

def main():
    print("Bienvenido al juego de Adivinanza de Palabras")
    print("La configuración inicial del juego se ha completado")
    palabra = seleccionar_palabra()
    juego = AdivinarPalabra(palabra)

    print("La palabra ha sido seleccionada. ¡Comienza a adivinar!")

    pistas_dadas = 0
    contador_intentos = 0

    while True:
        print(f"Palabra: {juego.progreso_actual()} (progreso actual)")
        letra = input('Adivina una letra: ').lower()

        mensaje = juego.adivinar_letra(letra)
        print(mensaje)

        if juego.todas_las_letras_adivinadas():
            print(f"¡Felicidades! Has adivinado la palabra: '{palabra}'")
            break

        if contador_intentos >= 10:
            print(f"Lo siento, has perdido. La palabra era: '{palabra}'")
            break

        if pistas_dadas < 3:
            condicional = input("¿Necesitas una pista? (s/n): ")
            if condicional.lower() == "s":
                letras = Pistas.obtener_pista(palabra)
                pista = Pistas.dar_pista(letras, juego.letras_adivinadas)
                if pista:
                    print(f"Pista: Una de las letras en la palabra es '{pista}'.")
                    pistas_dadas += 1
                else:
                    print("No quedan más letras para dar como pista.")
        else:
            print("Ya se han dado todas las pistas posibles.")
        contador_intentos += 1

if __name__ == '__main__':
    main()