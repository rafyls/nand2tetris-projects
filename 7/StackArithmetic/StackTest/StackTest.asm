// D = 17
  @17
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 17
  @17
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[13] = D
  @R13
  M=D
// D = RAM[13] == RAM[14]
  @R13
  D=M
  @R14
  D=D-M
  @$0
  D;JEQ
  D=0
  @$1
  0;JMP
($0)
  D=-1
($1)
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 17
  @17
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 16
  @16
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[13] = D
  @R13
  M=D
// D = RAM[13] == RAM[14]
  @R13
  D=M
  @R14
  D=D-M
  @$2
  D;JEQ
  D=0
  @$3
  0;JMP
($2)
  D=-1
($3)
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 16
  @16
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 17
  @17
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[13] = D
  @R13
  M=D
// D = RAM[13] == RAM[14]
  @R13
  D=M
  @R14
  D=D-M
  @$4
  D;JEQ
  D=0
  @$5
  0;JMP
($4)
  D=-1
($5)
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 892
  @892
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 891
  @891
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[13] = D
  @R13
  M=D
// D = RAM[13] < RAM[14]
  @R13
  D=M
  @R14
  D=D-M
  @$6
  D;JLT
  D=0
  @$7
  0;JMP
($6)
  D=-1
($7)
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 891
  @891
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 892
  @892
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[13] = D
  @R13
  M=D
// D = RAM[13] < RAM[14]
  @R13
  D=M
  @R14
  D=D-M
  @$8
  D;JLT
  D=0
  @$9
  0;JMP
($8)
  D=-1
($9)
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 891
  @891
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 891
  @891
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[13] = D
  @R13
  M=D
// D = RAM[13] < RAM[14]
  @R13
  D=M
  @R14
  D=D-M
  @$10
  D;JLT
  D=0
  @$11
  0;JMP
($10)
  D=-1
($11)
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 32767
  @32767
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 32766
  @32766
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[13] = D
  @R13
  M=D
// D = RAM[13] > RAM[14]
  @R13
  D=M
  @R14
  D=D-M
  @$12
  D;JGT
  D=0
  @$13
  0;JMP
($12)
  D=-1
($13)
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 32766
  @32766
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 32767
  @32767
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[13] = D
  @R13
  M=D
// D = RAM[13] > RAM[14]
  @R13
  D=M
  @R14
  D=D-M
  @$14
  D;JGT
  D=0
  @$15
  0;JMP
($14)
  D=-1
($15)
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 32766
  @32766
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 32766
  @32766
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[13] = D
  @R13
  M=D
// D = RAM[13] > RAM[14]
  @R13
  D=M
  @R14
  D=D-M
  @$16
  D;JGT
  D=0
  @$17
  0;JMP
($16)
  D=-1
($17)
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 57
  @57
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 31
  @31
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 53
  @53
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[13] = D
  @R13
  M=D
// D = RAM[13] + RAM[14]
  @R13
  D=M
  @R14
  D=D+M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 112
  @112
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[13] = D
  @R13
  M=D
// D = RAM[13] - RAM[14]
  @R13
  D=M
  @R14
  D=D-M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// D = - RAM[14]
  @R14
  D=-M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[13] = D
  @R13
  M=D
// D = RAM[13] And RAM[14]
  @R13
  D=M
  @R14
  D=D&M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 82
  @82
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[13] = D
  @R13
  M=D
// D = RAM[13] Or RAM[14]
  @R13
  D=M
  @R14
  D=D|M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[14] = D
  @R14
  M=D
// D = Not RAM[14]
  @R14
  D=!M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// END
(END)
  @END
  0;JMP