#!/bin/bash no ejecutar, copiar comandos.

# Inicializar conda
conda init

# Crear un entorno de conda llamado py32 con Python 3.7 para Linux de 32 bits
conda create -n py32 python=3.7 -c https://repo.anaconda.com/pkgs/main/linux-32/ --override-channels

# Activar el entorno de conda py32
conda activate py32

# Compilar el archivo float_int.asm a formato ELF de 32 bits
nasm -f elf32 float_int.asm

# Compilar el código C y generar un archivo ejecutable llamado code
gcc -m32 -o code float_int.o code.c

# Crear una biblioteca compartida (shared object) de 32 bits a partir de float_int.o
gcc -m32 -shared -o libfloat_int.so float_int.o

# Instalar el módulo requests usando pip en el entorno conda py32
pip install requests

# NOTA: Asegúrate de ejecutar este script en el mismo directorio donde se encuentran los archivos float_int.asm y float_int.o
