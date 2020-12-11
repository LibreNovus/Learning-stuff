global _start

section .text
_start:
  mov ebx, 1
  mov ecx, 4   ;number of iterations
label:
  add ebx, ebx ;ebx = 2, ebx = 4, ebx = 8, ebx = 16
  dec ecx      ;decrement. more efficient than subtraction
  cmp ecx, 0
  jg label     ;jump if greater
  mov eax, 1
  int 0x80
