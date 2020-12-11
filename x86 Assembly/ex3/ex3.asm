global _start

section .text
_start:
  mov ecx, 99
  mov ebx, 42
  mov eax, 1
  cmp ecx, 100
  jl skip ; jump if less than. je = if equal, jne = if not equal, jg if greater, jge ig greater or equal, jl if less, jle if less or equal
  mov ebx, 13
skip:
  int 0x80

