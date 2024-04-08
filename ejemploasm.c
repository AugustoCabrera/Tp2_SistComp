#include <stdio.h>

// Prototipo de la función escrita en ensamblador
extern int suma_asm(int a, int b);

int main() {
    int num1, num2, suma;

    // Solicitar al usuario dos números
    printf("Ingrese el primer número: ");
    scanf("%d", &num1);

    printf("Ingrese el segundo número: ");
    scanf("%d", &num2);

    // Llamar a la función escrita en ensamblador para sumar los números
    suma = suma_asm(num1, num2);

    // Mostrar el resultado
    printf("La suma es: %d\n", suma);

    return 0;
}
