Data Segment
    VAR2 dw 0340h
    Var3 dd 0a7f5ch
    var4 db 254
    var5 db -23
Data ends
Code Segment
    and dword ptr [eax*4], eax
    and dword ptr cs:[esi*4], eax
    and [esi*4], edi
    inc VAR2
    inc Var3
    inc var4
    inc dword ptr ds: [esi*4]
    inc dword ptr ds: [esi*4]
    inc dword ptr ds: [esi*4]
    inc byte ptr ds: [esi*4]
    inc byte ptr ds: [esi*4]
    inc byte ptr ds: [esi*4]
    mov byte ptr ds:[edi*8], 5+2
    mov edi, dword ptr ds:[esi*8]
    mov ebx, dword ptr ds:[esi*8]
    mov ah, byte ptr ds:[esi*8]
    cmp ah, dl
    and ds:[esi*4], eax
    and dword ptr [eax*4], eax
    and dword ptr cs:[esi*4], eax
    and [esi*4], edi
    sti
    pop eax
    pop edx
    inc dword ptr ds:[edi*8]
    sti
    inc byte ptr ds:[esi*4]
    mov dword ptr ds:[esi*8], 0f564h*4
    sti
label3:
    cmp ah, dl
    cmp al, dh
    jnz label3
    cmp eax, esi
    cmp edi, ebx
    jnz label9
    cmp esi, edi 
    jnz label1
    and ds:[ebx*2], ecx
    and dword ptr ds:[esi*8], edx
    jnz label1
label1:
    jnz label1
    xor al, -2
    xor edi, 0f564h*2
    xor ah, 00001000b*2
    xor al, 00001000b*4
    xor eax, 00001000h*2
    xor edx, 00001000h*4
label9:
Code ends
End