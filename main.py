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

    while True:
        print(f"Palabra: {juego.progreso_actual()} (progreso actual)")
        letra = input('Adivina una letra: ').lower()

        mensaje = juego.adivinar_letra(letra)
        print(mensaje)

        condicional = input("¿Necesitas una pista? (s/n): ")

        if condicional.lower() == "s":
            if pistas_dadas < 3:
                letras = Pistas.obtener_pista(palabra)
                pista = Pistas.dar_pista(letras, juego.letras_adivinadas)
                if pista:
                    print(f"Pista: Una de las letras en la palabra es '{pista}'.")
                    pistas_dadas += 1
                else:
                    print("No quedan más letras para dar como pista.")
            else:
                print("Ya se han dado todas las pistas posibles.")

if __name__ == '__main__':
    main()