from CompruebaTilde import hayTilde
from EntonarConTilde import entonacion_tilde
from EntonarSinTilde import entonacion_sin_tilde
from Justificacion import justifica
from Rimar import rimas
from Silabear import silabar

if __name__ == '__main__':
    estado = 0
    archivo = open('BBDD.csv', 'w', encoding='latin1')
    diccionario = {}
    dicc_asonante = {}
    dicc_consonante = {}
    lista_entonada = []
    palabra_silabeada = []
    print('¡Bienvenido al Silabeador+!\n')
    while estado != 5:
        estado = input(
            'Por favor, indica qué deseas hacer:\n- Pulsa 1 si quieres silabear una palabra.\n- Pulsa 2 si quieres entonar una palabra\n- Pulsa 3 si quieres las rimas de una palabra.\n- Pulsa 4 si quieres justificar un texto.\n- Pulsa 5 para salir.\n\nNúmero introducido: ')
        try:
            estado = int(estado)
        except:
            print('Has introducido un valor inválido. Debe ser un número entre 1 y 5')
            print()
            continue
        if estado == 1:
            palabra = input('Palabra: ')
            if palabra == '':
                print('Necesito una palabra válida.')
                print()
                pass
            else:
                try:
                    palabra_silabeada = silabar(palabra)
                except:
                    print('La palabra introducida no es válida')
                    print()
                    continue
                if palabra in diccionario:
                    pass
                else:
                    if hayTilde(palabra) == 2:
                        print('La palabra introducida no es válida ya que tiene más de una tilde')
                        print()
                        continue
                    elif hayTilde(palabra):
                        lista_entonada = entonacion_tilde(palabra_silabeada)
                    else:
                        lista_entonada = entonacion_sin_tilde(palabra_silabeada)
                    diccionario_rimas = rimas(lista_entonada, palabra, dicc_asonante, dicc_consonante)
                    diccionario_palabra = {
                        palabra: [palabra_silabeada, lista_entonada, diccionario_rimas[2], diccionario_rimas[3]]}
                    diccionario.update(diccionario_palabra)
                print('La palabra silabeada es: ', palabra_silabeada)
                print()
            continue
        elif estado == 2:
            palabra = input('Palabra: ')
            if palabra == '':
                print('Necesito una palabra válida.')
                print()
                pass
            else:
                try:
                    palabra_silabeada = silabar(palabra)
                except:
                    print('La palabra introducida no es válida')
                    print()
                    continue
                if hayTilde(palabra) == 2:
                    print('La palabra introducida no es válida ya que tiene más de una tilde')
                    print()
                    continue
                if hayTilde(palabra):
                    lista_entonada = entonacion_tilde(palabra_silabeada)
                else:
                    lista_entonada = entonacion_sin_tilde(palabra_silabeada)
                if palabra in diccionario:
                    pass
                else:
                    diccionario_rimas = rimas(lista_entonada, palabra, dicc_asonante, dicc_consonante)
                    diccionario_palabra = {
                        palabra: [palabra_silabeada, lista_entonada, diccionario_rimas[2], diccionario_rimas[3]]}
                    diccionario.update(diccionario_palabra)
                print('La palabra entonada es: ', lista_entonada)
            print()
            continue
        elif estado == 3:
            palabra = input('Palabra: ')
            if palabra == '':
                print('Necesito una palabra válida.')
                print()
                pass
            else:
                try:
                    palabra_silabeada = silabar(palabra)
                except:
                    print('La palabra introducida no es válida')
                    print()
                    continue
                if hayTilde(palabra) == 2:
                    print('La palabra introducida no es válida ya que tiene más de una tilde')
                    print()
                    continue
                if hayTilde(palabra):
                    lista_entonada = entonacion_tilde(palabra_silabeada)
                else:
                    lista_entonada = entonacion_sin_tilde(palabra_silabeada)
            diccionario_rimas = rimas(lista_entonada, palabra, dicc_asonante, dicc_consonante)
            if palabra in diccionario:
                pass
            else:
                diccionario_palabra = {
                    palabra: [palabra_silabeada, lista_entonada, diccionario_rimas[2], diccionario_rimas[3]]}
                diccionario.update(diccionario_palabra)
            dicc_asonante.update(diccionario_rimas[0])
            dicc_consonante.update(diccionario_rimas[1])
            rima_asonante = dicc_asonante.get(diccionario_rimas[2])
            rima_consonante = dicc_consonante.get(diccionario_rimas[3])
            print('Las rimas asonantes y consonantes de la palabra son: ', diccionario_rimas[2], ' : ', rima_asonante,
                  '\n', diccionario_rimas[3], ' : ', rima_consonante)
            print()
            continue
        elif estado == 4:
            justifica()
            print()
            continue
        elif estado == 5:
            print('¡Adiós!')
            print()
            print(diccionario, file=archivo)
            archivo.close()
            break
        else:
            print('No has puesto ninguna de las opciones establecidas. Por favor introduce un número válido')
            print()
            continue