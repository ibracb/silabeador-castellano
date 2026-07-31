import regex as re

er_espacios = re.compile(r'\s+')

def separarPalabras(parrafo):
    parrafo = parrafo.strip()
    indice = 0
    listaPalabras = []
    for m in er_espacios.finditer(parrafo):
        listaPalabras.append(parrafo[indice:m.start()])
        indice = m.end()
    listaPalabras.append(parrafo[indice:])
    return listaPalabras