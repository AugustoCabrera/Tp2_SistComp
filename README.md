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
Para la segunda fase (con ensamblador), se incorpora la interzas Assembler para que desarrolle la operacion aritmetica.

A través de estos diagramas, se obtuvo una visión más clara del camino a seguir. Esto permitió comenzar a desarrollar los códigos, que se resumen a continuación.

##### ` APIconsumer.py ` 

El código proporcionado es un script en Python que realiza las siguientes acciones:

1. **Importa bibliotecas**: Las bibliotecas `requests` y `ctypes` se importan al principio del script. `requests` se utiliza para realizar solicitudes HTTP a la API de World Bank, mientras que `ctypes` se utiliza para llamar a funciones de una biblioteca compartida en C desde Python.

2. **Función `_float_int`**: Esta función toma un número de coma flotante como argumento y utiliza la biblioteca compartida `libfloat_int.so` para convertirlo en un número entero. La biblioteca compartida es cargada usando `ctypes.CDLL`, luego se especifican los tipos de argumentos y el tipo de retorno de la función `_float_int`, y finalmente se llama a la función con el número flotante dado.

3. **Función `obtener_indice_gini`**: Esta función toma el código de país y el año como entrada, y utiliza la API de World Bank para obtener el índice GINI del país para el año especificado. Utiliza la biblioteca `requests` para realizar una solicitud GET a la API y procesa la respuesta para encontrar el valor del índice GINI correspondiente al país y año dados.

4. **Bloque principal**: Si el script se ejecuta como el programa principal, solicita al usuario que ingrese el código del país y el año. Luego, llama a la función `obtener_indice_gini` para obtener el índice GINI correspondiente. Si se encuentra el valor del índice GINI, lo imprime. Luego, convierte este índice GINI a un número entero utilizando la función `_float_int` y muestra el resultado.

Este script podría ser útil para obtener y procesar datos del índice GINI de diferentes países y años a través de la API de World Bank, y realizar más análisis o cálculos con esos datos convertidos en números enteros.


##### ` code.c y float_int.asm ` 

El código C proporcionado es un programa simple que convierte un número de coma flotante en un entero utilizando una función externa llamada `_float_int` de codigo assembler. Luego imprime el valor original y el valor convertido.

1. **Inclusión de bibliotecas**: Se incluye la biblioteca estándar `stdio.h`, que proporciona funciones para entrada y salida estándar.

2. **Declaración de la función `_float_int`**: Se declara una función `_float_int` que espera un argumento de tipo `float` y devuelve un entero. Esta función se define en lenguaje ensamblador.

3. **Función `main`**: Esta es la función principal del programa. Define una variable `num` de tipo `float` con el valor `14.29`. Luego, llama a la función `_float_int` con `num` como argumento y almacena el resultado en la variable `num_int`. Finalmente, imprime el valor de `num` y `num_int` utilizando la función `printf`.

4. **Instrucciones de compilación**: Se proporciona un comentario que indica cómo compilar este código C junto con el código en ensamblador. Se debe usar el compilador `gcc` para compilar el código C y el ensamblador `nasm` para compilar el código en lenguaje ensamblador. El código en ensamblador se ensambla en un objeto de 32 bits (`-f elf32`) para que sea compatible con la arquitectura de 32 bits.

El código en lenguaje ensamblador proporcionado es la implementación de la función `_float_int`. Toma el argumento pasado en la pila, lo convierte a un entero y luego le suma 1. La conversión de punto flotante a entero se realiza utilizando las instrucciones `fld` y `fistp` para cargar el valor de punto flotante en la pila de FPU y luego almacenar el entero en la dirección de memoria especificada. Luego, se incrementa el valor del entero y se devuelve como resultado.

Este programa C y su implementación en ensamblador forman un ejemplo de cómo se puede integrar código en C y en ensamblador en un mismo proyecto. La ejecucion se resuelve con el siguiente `runAssC.sh`

##### `runAssC.sh`

El comando `nasm -f elf32 float_int.asm` ensambla el archivo `float_int.asm` en un objeto de formato ELF32, que es compatible con la arquitectura de 32 bits.

El comando `gcc -m32 -o convert code.c float_int.o` compila el archivo `code.c` junto con el archivo objeto `float_int.o` (generado previamente por `nasm`) en un ejecutable llamado `convert`. La opción `-m32` indica que se debe compilar para una arquitectura de 32 bits.

Finalmente, `./convert` ejecuta el programa compilado `convert`.

Estos comandos se utilizan para compilar el programa en C junto con su implementación en ensamblador y luego ejecutar el programa resultante.
A continuacion, se explica el uso de la interfaz.

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

<p align="center">
  <a href="https://example.com/">
    <img src="/image/image5.png" alt="UML">
  </a>
</p>

Se puede verificar la correcta instalación del mismo.

Luego, se debe crear el environment de 32 bits para poder comenzar a trabajar:

**Inicializar conda:**

```bash
$ conda init 
```

Inicializa el sistema de gestión de paquetes Conda en el entorno.

**Crear un entorno de conda llamado py32 con Python 3.7 para Linux de 32 bits:**

```bash
$ conda create -n py32 python=3.7 -c https://repo.anaconda.com/pkgs/main/linux-32/ --override-channels
Crea un entorno de conda llamado `py32` con Python 3.7 específicamente para sistemas Linux de 32 bits.
```

**Activar el entorno de conda py32:**

```bash
$ conda activate py32 
```

Activa el entorno de conda llamado `py32`, lo que asegura que las instalaciones de paquetes se realicen en este entorno.

**Compilar el archivo float_int.asm a formato ELF de 32 bits:**

```bash
$ nasm -f elf32 float_int.asm
```

Compila el archivo de ensamblador `float_int.asm` en formato ELF de 32 bits.


**Compilar el código C y generar un archivo ejecutable llamado code:**

```bash
$ gcc -m32 -o code float_int.o code.c
```
Compila el código C y genera un archivo ejecutable llamado `code`.

**Crear una biblioteca compartida (shared object) de 32 bits a partir de float_int.o:**

```bash
$ gcc -m32 -shared -o libfloat_int.so float_int.o
```
Crea una biblioteca compartida (shared object) de 32 bits llamada `libfloat_int.so` a partir del archivo `float_int.o`.

**Instalar el módulo requests usando pip en el entorno conda py32:**

El comando `pip install requests` instala el módulo `requests` utilizando el gestor de paquetes pip en el entorno de conda `py32`.



De esta manera, se establece un entorno funcional que permite el desarrollo de la segunda parte del laboratorio, que implica la incorporación de C con una interfaz de ensamblador. A continuación, se muestra material visual para observar la correcta funcionalidad de lo antes mencionado:

<p align="center">
  <a href="https://example.com/">
    <img src="/image/image6.png" alt="UML">
  </a>
</p>

<p align="center">
  <a href="https://example.com/">
    <img src="/image/image7.png" alt="UML">
  </a>
</p>

<p align="center">
  <a href="https://example.com/">
    <img src="/image/image8.png" alt="UML">
  </a>
</p>

<p align="center">
  <a href="https://example.com/">
    <img src="/image/image9.png" alt="UML">
  </a>
</p>

[Aquí tienes un video de cómo funciona todo](https://drive.google.com/file/d/1e9j1No5NToEb21ZFDsmaLv0QEEdEE25V/view?usp=sharing)


El video en cuestión es una excelente forma de respaldar y demostrar el correcto funcionamiento de la experiencia desarrollada, sin necesidad de configurar el entorno CONDA.

## Testeo y Coverage

El test se lleva a cabo con el codigo `test.c`. 

Este código es un conjunto de pruebas unitarias escritas en C utilizando el framework de pruebas Unity. Aquí está una explicación detallada de cada parte:

- Directiva de inclusión `#include <unity.h>:` Esta línea incluye la biblioteca Unity, que es un framework de pruebas unitarias para C.

- `Declaración externa extern int _float_int(float num)`: Esta declaración externa indica que hay una función llamada _float_int que acepta un argumento de tipo float y devuelve un entero. Es probable que esta función esté implementada en algún otro lugar, como en un archivo de código en lenguaje ensamblador.
- `Funciones setUp y tearDown`: Estas funciones se utilizan para configurar y limpiar el entorno antes y después de cada prueba. En el ejemplo proporcionado, ambas funciones están vacías, pero se pueden usar para inicializar variables o recursos antes de cada prueba y limpiarlos después de cada prueba, respectivamente.
- `Función testFloatToIntConversion`: Esta es una prueba unitaria que verifica la conversión de un número de coma flotante a un entero utilizando la función `_float_int`. En esta prueba, se define un número de entrada (14.29f) y se espera que la función `_float_int` devuelva 15 como resultado. La macro `TEST_ASSERT_EQUAL_INT` se utiliza para verificar si el resultado de la función `_float_int` es igual al valor esperado.

- `Función main:` Esta es la función principal del programa de prueba. Aquí es donde se ejecutan todas las pruebas definidas anteriormente. La función `UNITY_BEGIN()` inicializa el framework de pruebas, luego se agregan todas las pruebas utilizando `RUN_TEST`, y finalmente se ejecutan todas las pruebas con `UNITY_END()`. La función main devuelve el resultado de las pruebas.

En resumen, el código proporcionado implementa pruebas unitarias para verificar la precisión de la función `_float_int`, que convierte un número de coma flotante en un entero. Estas pruebas están organizadas y ejecutadas eficientemente mediante el uso del framework de pruebas Unity.

Para ejecutar este código, se utiliza el script `runTestCov.sh`. Además de ejecutar las pruebas unitarias, este script genera una página HTML que muestra el porcentaje de cobertura del código.

<p align="center">
  <a href="https://example.com/">
    <img src="/image/image10.png" alt="UML">
  </a>
</p>
