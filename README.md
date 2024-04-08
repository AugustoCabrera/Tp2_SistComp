<p align="center">
  <a href="https://example.com/">
    <img src="/image/image1.png" alt="Logo">
  </a>


***TRABAJO PRACTICO 2***

**Titulo:** STACK FRAME

**Asignatura:** Sistemas de Computación

**Integrantes:**
   - Cabrera, Augusto Gabriel 
   - Moroz, Esteban Mauricio 
   - Britez, Fabio

**Fecha:** 7/4/2024
   

---------------

  <p align="center">
  

El presente Trabajo Práctico aborda la interacción entre lenguajes de alto nivel (C) y bajo nivel (Assembler) en sistemas compuestos por hardware y software. Se implementa una interfaz que muestra el índice GINI utilizando una API REST para obtener datos del Banco Mundial. Utilizando Python y API REST para la capa superior, mientras que la capa intermedia en C convoca rutinas en ensamblador para cálculos específicos.
   
</p>


## Tabla de Contenidos

- [Enunciado](#Enunciado)
- [Desarrollo](#Desarrollo)
- [What's included](#whats-included)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Contributing](#contributing)
- [Creators](#creators)
- [Thanks](#thanks)
- [Copyright and license](#copyright-and-license)


## Enunciado

Diseña e implementa una interfaz que muestre el índice GINI. Recupera la información del [Banco Mundial](https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22) en la capa superior. Transfiere los datos de consulta a un programa en C (capa intermedia) que invocará rutinas en ensamblador para realizar los cálculos de conversión de float a enteros. Devuelve el índice de un país, como Argentina u otro seleccionado, sumando uno (+1). Luego, muestra los datos obtenidos en el programa en C. Utiliza el stack para invocar funciones, enviar parámetros y recibir resultados, siguiendo las convenciones de llamadas de lenguajes de alto nivel a bajo nivel.

En la primera iteración, resuelve todo el trabajo práctico utilizando C con Python, sin ensamblador. En la siguiente iteración, utiliza los conocimientos de ensamblador para completar el proyecto.

En esta segunda iteración, muestra los resultados con gdb. Puedes usar un programa de C puro. Durante la depuración, muestra el estado del área de memoria que contiene el stack antes, durante y después de la función.

### Desarrollo

En la etapa inicial, se han ideado diagramas para visualizar los distintos bloques que se incorporarán en la estructura de los códigos. La siguiente imagen representa la interacción de los distintos actores:

<p align="center">
  <a href="https://example.com/">
    <img src="/image/image2.png" alt="bloques">
  </a>
  </p>
Para la primera fase (sin ensamblador), se ha elaborado el siguiente diagrama de secuencias.
<p align="center">
  <a href="https://example.com/">
    <img src="/image/image3.png" alt="UML">
  </a>
</p>
Para la segunda fase (con ensamblador), se ha elaborado el siguiente diagrama de secuencias.
<p align="center">
  <a href="https://example.com/">
    <img src="/image/image4.png" alt="UML">
  </a>
</p>
A través de estos diagramas, se obtuvo una visión más clara del camino a seguir. Esto permitió comenzar a desarrollar los códigos, que se resumen a continuación.

##### ` runlab.sh ` 

- `gcc -c Process.c -o Process.o`: Este comando compila el archivo `Process.c` y genera un archivo objeto (`Process.o`). La opción `-c` indica a GCC que solo compile el código fuente y genere el archivo objeto sin realizar la vinculación. El argumento `-o` especifica el nombre del archivo de salida.

- `ar rcs libprocess.a Process.o`: Este comando crea una biblioteca estática llamada `libprocess.a` utilizando el archivo objeto `Process.o`. La utilidad `ar` es un archiver que se utiliza para crear, modificar y extraer archivos de biblioteca. La opción `rcs` indica que se deben realizar las siguientes operaciones: crear (`c`) un archivo, agregar (`r`) el archivo objeto al archivo de biblioteca y guardar (`s`) el índice de la biblioteca para una búsqueda más rápida.

- `gcc -shared -o libprocess.so Process.c`: Este comando compila el archivo `Process.c` y genera una biblioteca compartida llamada `libprocess.so`. La opción `-shared` indica a GCC que genere una biblioteca compartida en lugar de un ejecutable. El argumento `-o` especifica el nombre del archivo de salida.

- `python3 APIconsumer.py`: Este comando ejecuta el script Python `APIconsumer.py` utilizando Python 3. Ejecutar este script probablemente realizará alguna operación relacionada con consumir una API, como recuperar datos de la web o realizar solicitudes HTTP a un servidor.

##### ` APIconsumer.py ` 




## What's included

Some text

```text
folder1/
└── folder2/
    ├── folder3/
    │   ├── file1
    │   └── file2
    └── folder4/
        ├── file3
        └── file4
```



