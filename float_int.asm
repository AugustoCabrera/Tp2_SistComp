section .data
    num dd 0

global _float_int
section .text

;to compile: nasm -f elf32 float_int.asm
_float_int:
    push ebp
    mov ebp,esp

    fld dword [ebp + 8] 

    fistp dword [num]

    mov eax, [num]
    add eax, 1
    mov [num], eax

    mov esp, ebp 
    pop ebp
    ret