nasm -f elf32 float_int.asm

gcc -m32 -o convert code.c float_int.o

./convert