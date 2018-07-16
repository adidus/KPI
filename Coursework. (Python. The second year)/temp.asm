0000     Data Segment
0000         var db 0fch
0001         VAR2 dw 0340h
0003         Var3 dd 0a7f5ch
0007         var4 db 23
0008         var5 db -23
0009     Data ends
0000     Code Segment
0000         and var, ah
0000         and ds:var, ah
N a m e        Size	      Length    Align	Combine Class
DATA......     32 Bit     0009     PARA	   NONE
N a m e        Type	   Value	 Attr
VAR.......     DB       0000     DATA
VAR2......     DW       0001     DATA
VAR3......     DD       0003     DATA
VAR4......     DB       0007     DATA
VAR5......     DB       0008     DATA
