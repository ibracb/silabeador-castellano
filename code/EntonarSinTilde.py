from Normas import letra_final_aguda, vocal_sin_acentuar, vocal_abierta, triptongo, diptongo_abierto, diptongo_cerrado, \
    vocal_cerrada


def entonacion_sin_tilde(lista_silabas):  # Función para entonar la palabra sin tilde
    separador = ""  # la cadena vacía
    palabra_entonacion = separador.join(
        lista_silabas)  # Juntamos la palabra para obtener la ultima letra de manera sencilla
    ultima_letra = palabra_entonacion[-1]  # Obtenemos la última letra
    lista_salida = []  # Creamos la lista del resultado
    if type(lista_silabas) == str:
        cantidad_silabas = 1
        ultima_silaba = lista_silabas
        penultima_silaba = None
        lista_silabas = [ultima_silaba]
    else:
        cantidad_silabas = len(
            lista_silabas)  # La cantidad de sílabas para obtener la última silaba y penultima de manera sencilla
        penultima_silaba = lista_silabas[cantidad_silabas - 2]  # Penúltima sílaba
        ultima_silaba = lista_silabas[cantidad_silabas - 1]  # Última sílaba
    if letra_final_aguda.search(
            ultima_letra):  # Comprobamos que la última letra sea "a, e, i, o, u, n ó s ya que si la ultima letra es una de ellas y la palabra no tiene acento significa que es llana por lo que la vocal tónica está en la penúltima sílaba"
        i = 0  # Contador
        if diptongo_abierto.search(penultima_silaba):
            for letra_abierta in penultima_silaba:
                i = i + 1
                if vocal_abierta.search(letra_abierta):
                    silaba_entonada = penultima_silaba[0:i - 1] + letra_abierta.upper() + penultima_silaba[
                                                                                          i:]  # Añadimos a la sílaba la vocal entonada
                    lista_salida = lista_silabas[0:cantidad_silabas - 2] + [silaba_entonada] + lista_silabas[
                                                                                               cantidad_silabas - 1:]  # Añadimos a la palabra la sílaba entonada
                    return lista_salida  # No necesitamos recorrer nada más por lo que devolvemos la palabra entonada
        elif diptongo_cerrado.search(penultima_silaba):
            j = 0
            for letra_cerrada in penultima_silaba:
                i = i + 1
                if vocal_cerrada.search(letra_cerrada):
                    j = j + 1
                    if j == 2:
                        silaba_entonada = penultima_silaba[0:i - 1] + letra_cerrada.upper() + penultima_silaba[
                                                                                              i:]  # Añadimos a la sílaba la vocal entonada
                        lista_salida = lista_silabas[0:cantidad_silabas - 2] + [silaba_entonada] + lista_silabas[
                                                                                                   cantidad_silabas - 1:]  # Añadimos a la palabra la sílaba entonada
                        return lista_salida  # No necesitamos recorrer nada más por lo que devolvemos la palabra entonada
        elif triptongo.search(penultima_silaba):
            for letra_abierta in penultima_silaba:
                i = i + 1
                if vocal_abierta.search(letra_abierta):
                    silaba_entonada = penultima_silaba[0:i - 1] + letra_abierta.upper() + penultima_silaba[
                                                                                          i:]  # Añadimos a la sílaba la vocal entonada
                    lista_salida = lista_silabas[0:cantidad_silabas - 2] + [silaba_entonada] + lista_silabas[
                                                                                               cantidad_silabas - 1:]  # Añadimos a la palabra la sílaba entonada
                    return lista_salida  # No necesitamos recorrer nada más por lo que devolvemos la palabra entonada
        else:
            for letra in penultima_silaba:  # Recorremos la sílaba
                i = i + 1  # Contamos la letra en la que estamos
                if vocal_sin_acentuar.search(letra):  # Comprobamos que la letra sea una vocal sin acentuar
                    silaba_entonada = penultima_silaba[0:i - 1] + letra.upper() + penultima_silaba[
                                                                                  i:]  # Añadimos a la sílaba la vocal entonada
                    lista_salida = lista_silabas[0:cantidad_silabas - 2] + [silaba_entonada] + lista_silabas[
                                                                                               cantidad_silabas - 1:]  # Añadimos a la palabra la sílaba entonada
                    return lista_salida  # No necesitamos recorrer nada más por lo que devolvemos la palabra entonada
    else:  # En el caso de que la última letra no sea ninguna de esas, la palabra es aguda por lo que tenemos que evaluar la última sílaba
        i = 0  # Contador
        if diptongo_abierto.search(ultima_silaba):
            for letra_abierta in ultima_silaba:
                i = i + 1
                if vocal_abierta.search(letra_abierta):
                    silaba_entonada = ultima_silaba[0:i - 1] + letra_abierta.upper() + ultima_silaba[
                                                                                       i:]  # Añadimos a la sílaba la vocal entonada
                    lista_salida = lista_silabas[0:cantidad_silabas - 1] + [silaba_entonada] + lista_silabas[
                                                                                               cantidad_silabas:]  # Añadimos a la palabra la sílaba entonada
                    return lista_salida  # No necesitamos recorrer nada más por lo que devolvemos la palabra entonada
        elif diptongo_cerrado.search(ultima_silaba):
            j = 0
            for letra_cerrada in ultima_silaba:
                i = i + 1
                if vocal_cerrada.search(letra_cerrada):
                    j = j + 1
                    if j == 2:
                        silaba_entonada = ultima_silaba[0:i - 1] + letra_cerrada.upper() + ultima_silaba[
                                                                                           i:]  # Añadimos a la sílaba la vocal entonada
                        lista_salida = lista_silabas[0:cantidad_silabas - 1] + [silaba_entonada] + lista_silabas[
                                                                                                   cantidad_silabas:]  # Añadimos a la palabra la sílaba entonada
                        return lista_salida  # No necesitamos recorrer nada más por lo que devolvemos la palabra entonada
        elif triptongo.search(ultima_silaba):
            for letra_abierta in ultima_silaba:
                i = i + 1
                if vocal_abierta.search(letra_abierta):
                    silaba_entonada = ultima_silaba[0:i - 1] + letra_abierta.upper() + ultima_silaba[
                                                                                       i:]  # Añadimos a la sílaba la vocal entonada
                    lista_salida = lista_silabas[0:cantidad_silabas - 1] + [silaba_entonada] + lista_silabas[
                                                                                               cantidad_silabas:]  # Añadimos a la palabra la sílaba entonada
                    return lista_salida  # No necesitamos recorrer nada más por lo que devolvemos la palabra entonada
        else:
            for letra in ultima_silaba:  # Recorremos la sílaba
                i = i + 1  # Contamos la letra en la que estamos
                if vocal_sin_acentuar.search(letra):  # Comprobamos que la letra sea una vocal sin acentuar
                    silaba_entonada = ultima_silaba[0:i - 1] + letra.upper() + ultima_silaba[
                                                                               i:]  # Añadimos a la sílaba la vocal entonada
                    lista_salida = lista_silabas[0:cantidad_silabas - 1] + [silaba_entonada] + lista_silabas[
                                                                                               cantidad_silabas:]  # Añadimos a la palabra la sílaba entonada
                    return lista_salida  # No necesitamos recorrer nada más por lo que devolvemos la palabra entonada