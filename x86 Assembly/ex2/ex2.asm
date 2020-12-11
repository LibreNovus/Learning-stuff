global _start

section .data
  msg db "Hello World", 0x0a; 0x0a=10, newline
  len equ $ - msg

section .text
_start:
  mov eax, 4 ;sys_write system call
  mov ebx, 1 ;stdout 
  mov ecx, msg
  mov edx, len
  int 0x80
  mov eax, 1
  mov ebx, 0
  int 0x80
