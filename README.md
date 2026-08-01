# Silabeador+

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)

Herramienta CLI que trabaja con palabras del castellano: silabea palabras, marca la sílaba tónica (entonación), busca rimas y justifica textos.

## Autores

- **Ibrahim Cherif Barry** - [ibracb](https://github.com/ibracb)
- **Sofía Pérez Augusto** - [Arimoluk](https://github.com/Arimoluk)

**Asignatura:** Autómatas y Lenguajes Formales  
**Titulación:** Grado en Ingeniería Informática  
**Universidad:** Universidad de Murcia  
**Curso:** 2023/2024

## Estructura del proyecto

```
silabeador-castellano/
├── code/                      # Código fuente
│   ├── Main.py                # Menú principal y coordinación de funcionalidades
│   ├── Silabear.py            # silabar(): divide una palabra en sílabas
│   ├── Normas.py              # Expresiones regulares y reglas de separación silábica
│   ├── EntonarConTilde.py     # entonacion_tilde(): marca la vocal tónica con tilde
│   ├── EntonarSinTilde.py     # entonacion_sin_tilde(): marca la vocal tónica sin tilde
│   ├── Rimar.py               # rimas(): calcula las rimas asonante y consonante
│   ├── CompruebaTilde.py      # hayTilde(): comprueba si una palabra lleva tilde
│   ├── Justificacion.py       # justifica(): justifica el texto de un fichero
│   └── SeparacionPalabras.py  # separarPalabras(): divide un párrafo en palabras
├── ejemplos/
│   └── prueba.txt             # Extracto del Quijote (ejemplo de entrada)
├── requirements.txt           # Dependencias del proyecto
└── README.md
```

## Requisitos

- Python 3
- Dependencias listadas en [`requirements.txt`](requirements.txt)

## Instalación y ejecución <a id="instalacion"></a>

```bash
# Clonar el repositorio
git clone https://github.com/ibracb/silabeador-castellano.git
cd silabeador-castellano

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar desde la carpeta del proyecto
python code/Main.py
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

Al elegir la opción 3 (rimas):

```
Número introducido: 3
Palabra: canción
Las rimas asonantes y consonantes de la palabra son:  O :  ['canción'] 
 On :  ['canción']
```

Al elegir la opción 4 (justificar) con el fichero de ejemplo `ejemplos/prueba.txt`:

```
Número introducido: 4
Anchura máxima: 30
Espacios mínimos: 2
Introduzca el fichero que desea justificar: ejemplos/prueba.txt
30  En  un  lugar  de  la
29  Mancha,  de  cuyo
...
```

Al elegir la opción 5 (salir):

```
Número introducido: 5
¡Adiós!
```

## Notas

- En la opción 4 (justificar), si el fichero indicado no existe se muestra un mensaje y se pide de nuevo la ruta; si se introduce una línea vacía, se cancela y se vuelve al menú. Puedes usar `ejemplos/prueba.txt` (un extracto del Quijote) como fichero de ejemplo.
- Los datos acumulados durante la sesión se guardan en `BBDD.csv` al salir del programa. Al ejecutar desde la raíz del proyecto (tal como se indica en [Instalación y ejecución](#instalacion)), el archivo se crea en esa raíz.
