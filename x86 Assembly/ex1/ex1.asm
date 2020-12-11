global _start
_start:
  mov eax, 1   ;set eax = 1
  mov ebx, 50  ;set ebx = 50
  sub ebx, 30  ;subtract 30 from ebx. 
  int 0x80     ;interrupt handler for system calls. eax 1 = system exit call. ebx = exit status
