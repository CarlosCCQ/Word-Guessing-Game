class AdivinarPalabra:
    def __init__(self, palabra):
        self.palabra = palabra.lower()
        self.letras_adivinadas = set()
    def adivinar_letra(self, letra):
        letra = letra.lower()
        if letra in self.letras_adivinadas:
            return ("Ya has adivinado esa letra. Intenta con otra.")

        self.letras_adivinadas.add(letra)

        if letra in self.palabra:
            return (f"¡Correcto! La letra '{letra}' está en la palabra.")
        else:
            return (f"¡Incorrecto! La letra '{letra}' no está en la palabra.")

    def progreso_actual(self):
        return ''.join([letra if letra in self.letras_adivinadas else '_' for letra in self.palabra])
    
    def todas_las_letras_adivinadas(self):
        return all(letra in self.letras_adivinadas for letra in self.palabra)