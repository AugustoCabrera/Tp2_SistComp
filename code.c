#include "stdio.h"

extern int _float_int (float num);

int main() {
    float num = 14.29;
    int num_int = _float_int(num);
    printf("The integer value of %f is %d\n", num, num_int);
    return 0;
}

/*
To compile this code, execute: gcc -m32 -o convert code.c float_int.o
*/