# Silabeador+

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)

Herramienta CLI que trabaja con palabras del castellano: silabea palabras, marca la sílaba tónica (entonación), busca rimas y justifica textos.

## Autores

- **Ibrahim Cherif Barry** - [ibracb](https://github.com/ibracb)
- **Sofía Pérez Augusto** - [Arimoluk](https://github.com/Arimoluk)

**Asignatura:** Autómatas y Lenguajes Formales  
**Grado:** Ingeniería Informática  
**Universidad:** Universidad de Murcia  
**Curso:** 2023/2024

## Requisitos

- Python 3
- Paquete [`regex`](https://pypi.org/project/regex/), usado en el silabeo y la separación de palabras:

```bash
pip install regex
```

## Instalación y ejecución

```bash
cd code
python Main.py
```

Al iniciarse se muestra un menú con las siguientes opciones:

```
Pulsa 1 si quieres silabear una palabra.
Pulsa 2 si quieres entonar una palabra.
Pulsa 3 si quieres las rimas de una palabra.
Pulsa 4 si quieres justificar un texto.
Pulsa 5 para salir.
```

## Funcionalidades

| Opción | Función | Descripción |
|---|---|---|
| 1 | **Silabear** | Divide una palabra en sus sílabas. |
| 2 | **Entonar** | Marca en mayúscula la vocal tónica (la sílaba que se acentúa). |
| 3 | **Rimas** | Devuelve las rimas asonantes y consonantes de una palabra. |
| 4 | **Justificar** | Justifica el texto de un fichero según una anchura máxima y un mínimo de espacios. |
| 5 | **Salir** | Guarda los datos acumulados en `BBDD.csv` y cierra el programa. |

## Estructura del proyecto

| Archivo | Descripción |
|---|---|
| `Main.py` | Menú principal y coordinación de las funcionalidades. |
| `Silabear.py` | `silabar()` divide una palabra en sílabas. |
| `Normas.py` | Expresiones regulares y reglas de separación silábica. |
| `EntonarConTilde.py` | `entonacion_tilde()` marca la vocal tónica en palabras con tilde. |
| `EntonarSinTilde.py` | `entonacion_sin_tilde()` marca la vocal tónica en palabras sin tilde. |
| `Rimar.py` | `rimas()` calcula las rimas asonante y consonante. |
| `CompruebaTilde.py` | `hayTilde()` comprueba si una palabra lleva tilde. |
| `Justificacion.py` | `justifica()` justifica el texto de un fichero. |
| `SeparacionPalabras.py` | `separarPalabras()` divide un párrafo en palabras. |

## Ejemplo de uso

Al elegir la opción 1 (silabear):

```
Número introducido: 1
Palabra: hola
La palabra silabeada es:  ['ho', 'la']
```

Al elegir la opción 2 (entonar):

```
Número introducido: 2
Palabra: canción
La palabra entonada es:  ['can', 'ciOn']
```

## Notas

- En la opción 4 (justificar), si el fichero indicado no existe se muestra un mensaje y se pide de nuevo la ruta; si se introduce una línea vacía, se cancela y se vuelve al menú.
- Los datos acumulados durante la sesión se guardan en `BBDD.csv` al salir del programa. Si dicho fichero no existe, se crea al inicio de la sesión.
