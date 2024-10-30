import random
import string

class Pistas:
    def obtener_pista(palabra):
        letras = set()
        for letra in palabra:
            if letra.lower() in string.ascii_lowercase:
                letras.add(letra.lower())
        return list(letras)
    
    def dar_pista(letras, letras_adivinadas):
        letras_no_adivinadas = [letra for letra in letras if letra not in letras_adivinadas]
        if len(letras_no_adivinadas) < 1:
            return None
        pista = random.choice(letras_no_adivinadas)
        return pista