import Normas


def silabar(palabra_dada):  # Función que silabea la palabra dada por el usuario
    palabra = palabra_dada.lower()  # Me aseguro de que la palabra esté en minusculas para evitar problemas
    if not any(v in palabra for v in "aeiouáéíóúü") and not palabra.endswith("y"):
        raise ValueError("La palabra no contiene vocales")
    largo = len(palabra)  # Obtengo el largo de la palabra para recorrerla
    pos = 0  # La posición en la que estamos
    m = Normas.er.search(palabra, pos)
    if m is None:
        return palabra
    solucion = palabra[0:m.start()]
    final = 0
    while m:
        if final > m.start():
            largos1 = len(m['S1'])
            solucion += palabra[final:m.start() + largos1] + '-' + m['S2']
        else:
            solucion += m['S1'] + '-' + m['S2']
        pos = m.end() - 1
        final = m.end()
        m = Normas.er.search(palabra, pos)
    solucion += palabra[final:largo]
    lista = solucion.split(sep='-')
    return lista
