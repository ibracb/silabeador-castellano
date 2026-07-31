from SeparacionPalabras import separarPalabras
from Silabear import silabar


def justifica():
    while True:
        try:
            anchuraMaxima = int(input("Anchura máxima: "))
        except ValueError:
            print("Debe ser un número entero.")
            continue
        if anchuraMaxima <= 0:
            print("La anchura máxima debe ser un número positivo.")
            continue
        break

    while True:
        try:
            minimo = int(input("Espacios mínimos: "))
        except ValueError:
            print("Debe ser un número entero.")
            continue
        if minimo <= 0:
            print("Los espacios mínimos deben ser un número positivo.")
            continue
        if minimo >= anchuraMaxima:
            print("Los espacios mínimos deben ser menores que la anchura máxima.")
            continue
        break
    espaciosMinimos = " " * minimo

    ruta = ""
    fichero = None
    while fichero is None:
        ruta = input("Introduzca el fichero que desea justificar: ")
        if ruta == "":
            print("Necesito un fichero.")
            print()
            return
        try:
            fichero = open(ruta, encoding='utf8')
        except FileNotFoundError:
            print("Fichero inválido. Intente de nuevo")
            print()

    parrafo = fichero.read()
    fichero.close()

    listaPalabras = separarPalabras(parrafo)
    listaLineas = []

    linea = ""

    for indice, palabra in enumerate(listaPalabras):
        if len(linea) + minimo + len(palabra) <= anchuraMaxima:
            if indice == 0:
                linea += palabra
            else:
                linea += espaciosMinimos + palabra
        else:
            palabraSilabada = silabar(palabra)
            ultimasSilabasCortadas = palabraSilabada[-1]
            parteJunta = palabraSilabada[:-1]
            for silaba in reversed(parteJunta):
                if len(linea) + minimo + len("".join(parteJunta)) + 1 <= anchuraMaxima:
                    linea += espaciosMinimos + "".join(parteJunta) + "-"
                    break
                else:
                    ultimasSilabasCortadas = silaba + ultimasSilabasCortadas
                    parteJunta = parteJunta[:-1]
            listaLineas.append(linea)
            linea = ultimasSilabasCortadas
    listaLineas.append(linea)
    for lineaJustificada in listaLineas:
        print(len(lineaJustificada), lineaJustificada)