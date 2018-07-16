Data Segment
    var db 0fch
    VAR2 dw 0340h
    Var3 dd 0a7f5ch
    var4 db 23
    var5 db -23
Code Segment
    jnz label2
    label 2:
    inc VAR2
    inc Var3
    inc var4
    inc ds:Var2 [esi*4]
    inc ds:Var3 [esi*4]
    inc ds:Var4 [esi*4]
    jnz label2
    inc dword ptr ds:Var2 [esi*4]
    inc dword ptr ds:Var3 [esi*4]
    inc dword ptr ds:Var4 [esi*4]
    inc byte ptr ds:Var2 [esi*4]
    inc byte ptr ds:Var3 [esi*4]
    inc byte ptr ds:Var4 [esi*4]
    mov byte ptr ds:[edi*8], 00001000b*2
    mov edi, dword ptr ds:[esi*8]
    mov ebx, dword ptr ds:[esi*8]
    mov ah, byte ptr ds:[esi*8]
    mov var, 00001000b*2
    cmp ah, dl
    and ds:Var3[esi*4], eax
    and dword ptr Var3[eax*4], eax
    and dword ptr cs:var[esi*4], eax
    and Var3[esi*4], edi
    inc Var3
    inc var4
    inc ds:Var3 [esi*4]
    sti
    pop eax
    pop esp
    inc dword ptr ds:[edi*8]
    sti
    inc byte ptr ds:[esi*4]
    mov dword ptr ds:[esi*8], 0f564h*4
    sti
    cmp al, dh
    cmp eax, esi
    cmp edi, ebx
    jnz label2
    cmp esi, edi 
    jnz label2
    and byte ptr ds:[si*4], dh
    and ds:[ebx*2], ecx
    and dword ptr ds:[esi*8], edx
label1:
    xor esi, 0f564h*2
    xor edi, 0f564h*2
    xor ah, 00001000b*2
    xor al, 00001000b*4
    xor eax, 00001000h*2
    xor edx, 00001000h*4
label2:
Code ends
End