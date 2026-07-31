from Normas import vocales_acentuadas


def entonacion_tilde(lista_silabas):  # Función para entonar la palabra con tilde
    lista_salida = []  # Creamos la variable final
    contador_silabas = 0  # Creo un contador para poder volver a montar la palabra una vez tenga la sílaba con la vocal entonada
    if type(lista_silabas) == str:
        lista_silabas = [lista_silabas]
    for silaba in lista_silabas:  # Recorremos la lista de silabas
        contador_silabas = contador_silabas + 1  # Cuento que vamos por la silaba "i"
        cotador_letras = 0  # Creo un contador para poder volver a montar la silaba una vez tenga la vocal entonada
        for letra in silaba:  # Recorremos la silaba
            cotador_letras = cotador_letras + 1  # Cuento que vamos por la letra "i"
            if vocales_acentuadas.search(
                    letra):  # Compruebo si la letra es del gurpo de expresión regular de las vocales acentuadas
                if letra == "á":  # Comprobamos qué vocal de las 5 es
                    silaba_cambiada = silaba[:cotador_letras - 1] + "A" + silaba[
                                                                          cotador_letras:]  # Añado la vocal entonada a la sílaba
                    lista_salida = lista_silabas[:contador_silabas - 1] + [silaba_cambiada] + lista_silabas[
                                                                                              contador_silabas:]  # Añado la sílaba entonada a la palabra
                    return lista_salida  # No es necesario recorrer nada más por lo que devuelvo la lista con la palabra entonada
                elif letra == "é":  # Comprobamos qué vocal de las 5 es
                    silaba_cambiada = silaba[:cotador_letras - 1] + "E" + silaba[
                                                                          cotador_letras:]  # Añado la vocal entonada a la sílaba
                    lista_salida = lista_silabas[:contador_silabas - 1] + [silaba_cambiada] + lista_silabas[
                                                                                              contador_silabas:]  # Añado la sílaba entonada a la palabra
                    return lista_salida  # No es necesario recorrer nada más por lo que devuelvo la lista con la palabra entonada
                elif letra == "í":  # Comprobamos qué vocal de las 5 es
                    silaba_cambiada = silaba[:cotador_letras - 1] + "I" + silaba[
                                                                          cotador_letras:]  # Añado la vocal entonada a la sílaba
                    lista_salida = lista_silabas[:contador_silabas - 1] + [silaba_cambiada] + lista_silabas[
                                                                                              contador_silabas:]  # Añado la sílaba entonada a la palabra
                    return lista_salida  # No es necesario recorrer nada más por lo que devuelvo la lista con la palabra entonada
                elif letra == "ó":  # Comprobamos qué vocal de las 5 es
                    silaba_cambiada = silaba[:cotador_letras - 1] + "O" + silaba[
                                                                          cotador_letras:]  # Añado la vocal entonada a la sílaba
                    lista_salida = lista_silabas[:contador_silabas - 1] + [silaba_cambiada] + lista_silabas[
                                                                                              contador_silabas:]  # Añado la sílaba entonada a la palabra
                    return lista_salida  # No es necesario recorrer nada más por lo que devuelvo la lista con la palabra entonada
                elif letra == "ú":  # Comprobamos qué vocal de las 5 es
                    silaba_cambiada = silaba[:cotador_letras - 1] + "U" + silaba[
                                                                          cotador_letras:]  # Añado la vocal entonada a la sílaba
                    lista_salida = lista_silabas[:contador_silabas - 1] + [silaba_cambiada] + lista_silabas[
                                                                                              contador_silabas:]
                    return lista_salida  # No es necesario recorrer nada más por lo que devuelvo la lista con la palabra entonada