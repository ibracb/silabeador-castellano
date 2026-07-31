from Normas import vocal_sin_acentuar


def rimas(palabra_entonada, palabra, dicc_asonante, dicc_consonante):
    letras_rima_asonante = []
    letras_rima_consonante = []
    encontrado = 0
    contador_silabas = 0

    for silaba in palabra_entonada:
        contador_silabas = contador_silabas + 1
        contador_letras = 0
        for letra in silaba:
            contador_letras = contador_letras + 1
            if (encontrado == 0):
                if (letra == letra.upper()):
                    letras_rima_consonante = [silaba[contador_letras - 1:]] + palabra_entonada[contador_silabas:]
                    letras_rima_asonante.append(letra)
                    encontrado = 1
            elif (encontrado == 1):
                if (vocal_sin_acentuar.search(letra)):
                    letras_rima_asonante.append(letra)
    separador = ""  # la cadena vacía
    letras_rima_asonante_juntas = separador.join(letras_rima_asonante)
    letras_rima_consonante_juntas = separador.join(letras_rima_consonante)
    if letras_rima_asonante_juntas in dicc_asonante:
        lista_palabras = dicc_asonante.get(letras_rima_asonante_juntas)
        lista_palabras.append(palabra)
        dicc_asonante[letras_rima_asonante_juntas] = lista_palabras
    else:
        lista_palabras = [palabra]
        dicc_asonante = {letras_rima_asonante_juntas: lista_palabras}
    if letras_rima_consonante_juntas in dicc_consonante:
        lista_palabras = dicc_consonante.get(letras_rima_consonante_juntas)
        lista_palabras.append(palabra)
        dicc_consonante[letras_rima_consonante_juntas] = lista_palabras
    else:
        lista_palabras = [palabra]
        dicc_consonante = {letras_rima_consonante_juntas: lista_palabras}
    return dicc_asonante, dicc_consonante, letras_rima_asonante_juntas, letras_rima_consonante_juntas