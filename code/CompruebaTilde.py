from Normas import vocales_acentuadas


def hayTilde(palabra):  # Comprobación de si hay una tilde en la palabra.
    vocales = 0
    for letra in palabra:
        if vocales_acentuadas.search(letra):
            vocales += 1
    if vocales > 1:
        return 2
    elif vocales == 1:
        return True
    else:
        return False
