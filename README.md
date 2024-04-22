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



## Interfaceando ASM con C

Esta interfaz proporciona una conexión entre un programa en lenguaje C y una función escrita en lenguaje ensamblador NASM (Assembler). La función en ensamblador `_float_int` toma un número en punto flotante (representado como un `float` en C) y devuelve su valor entero + 1.

En el programa en C, se incluye la función `_float_int` como externa. Luego, se define la función `main`, que declara un número en punto flotante `num`, lo pasa a la función `_float_int` y luego imprime el número original junto con su valor entero devuelto por la función ensambladora + 1.

El ensamblador NASM define la función `_float_int`. Primero, guarda el estado del marco actual en la pila (push ebp, mov ebp, esp), luego carga el argumento de punto flotante de la pila (`fld dword [ebp + 8]`) y lo convierte a un entero (`fistp dword [num]`). Luego, incrementa el valor entero en uno y lo devuelve.

El código NASM también utiliza una variable `num` definida en la sección `.data` para almacenar temporalmente el valor entero convertido.

Para compilar este código, primero necesitas compilar el código en C usando GCC y el archivo objeto generado por NASM. Luego, ensamblas el código NASM. El comando de compilación dado para el código C y el ensamblador indica que se está compilando para una arquitectura de 32 bits (`-m32`).

## 32 bits vs 64 bits 

La interfaz entre el ensamblador y C está diseñada para una arquitectura de 32 bits (x86), mientras que el compilador de Python más reciente está optimizado para una arquitectura de 64 bits. Esto genera una discrepancia al intentar combinar estos archivos, ya que operan en arquitecturas diferentes. Para resolver esta discrepancia, se optó por migrar Python a una arquitectura más antigua de 32 bits. Esto permite que tanto la interfaz de ensamblador en C como Python operen en un entorno de 32 bits coherente, facilitando el enlace entre los archivos y garantizando su compatibilidad.
¿La solución? CONDA.

### CONDA

Conda es una herramienta de gestión de paquetes y un sistema de gestión de entornos ampliamente utilizada en el ecosistema de Python y en otras áreas de desarrollo de software. Su función principal es facilitar la instalación, actualización y administración de paquetes, bibliotecas y dependencias de software, así como la gestión de entornos virtuales.Conda nos permite instalar versiones específicas de Python, incluidas las versiones de 32 bits. Puedes crear un entorno de Conda utilizando una versión de Python de 32 bits, lo que te permite desarrollar y ejecutar tus aplicaciones en un entorno de 32 bits.


#### Instalación de Conda para Python de 32 bits

### Paso 1: Descargar Miniconda

Primero, descarga el archivo de instalación de Miniconda desde la [página oficial de Miniconda](https://docs.anaconda.com/free/miniconda/). Asegúrate de seleccionar la versión adecuada para tu sistema operativo y arquitectura (32 bits).

### Paso 2: Instalación de Miniconda

Una vez descargado el archivo, abre una terminal y navega hasta la carpeta donde se descargó. Luego, ejecuta el siguiente comando para iniciar la instalación:

<p align="center">
  <a href="https://example.com/">
    <img src="/image/image4.png" alt="UML">
  </a>
</p>


```bash
$ bash Miniconda3-latest-Linux-x86_64.sh
```

Se deben seguir todos los pasos que se muestran por consola y aceptar los términos de uso y condiciones de la misma.

Una vez instalado, se debe reiniciar la IDE en la cual se programa para restablecer el bash. Con el comando

```bash
$ conda
```






