// Bootstrap code
// SP = 256
  @256
  D=A
  @SP
  M=D
// call Sys.init
  @LCL
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @ARG
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @THIS
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @THAT
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @5
  D=A
  @R13
  M=D
  @SP
  D=M
  @R13
  M=D-M
  @ARG
  M=D
  @SP
  D=M
  @LCL
  M=D
  @Sys.init
  0;JMP
// function Main.fibonacci 0
(Main.fibonacci)
  @0
  D=A
($0)
  @R13
  M=D
  D=0
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @R13
  MD=M-1
  @$0
  D;JGT
// D = RAM[2 + 0]
  @R2
  D=M
  @0
  D=D+A
  A=D
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 2
  @2
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
  @$1
  D;JLT
  D=0
  @$2
  0;JMP
($1)
  D=-1
($2)
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
// if-goto Main.fibonacci$N_LT_2
  @Main.fibonacci$N_LT_2
  D;JNE
// goto Main.fibonacci$N_GE_2
  @Main.fibonacci$N_GE_2
  0;JMP
(Main.fibonacci$N_LT_2)
// D = RAM[2 + 0]
  @R2
  D=M
  @0
  D=D+A
  A=D
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// return
  @LCL
  D=M
  @R14
  M=D
  @5
  D=A
  @R14
  A=M-D
  D=M
  @R15
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
  @ARG
  A=M
  M=D
  @ARG
  D=M
  @SP
  M=D+1
  @R14
  A=M-1
  D=M
  @THAT
  M=D
  @2
  D=A
  @R14
  A=M-D
  D=M
  @THIS
  M=D
  @3
  D=A
  @R14
  A=M-D
  D=M
  @ARG
  M=D
  @4
  D=A
  @R14
  A=M-D
  D=M
  @LCL
  M=D
  @R15
  A=M
  0;JMP
(Main.fibonacci$N_GE_2)
// D = RAM[2 + 0]
  @R2
  D=M
  @0
  D=D+A
  A=D
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 2
  @2
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
  @Main.fibonacci$ret.1
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @LCL
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @ARG
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @THIS
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @THAT
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @5
  D=A
  @R13
  M=D
  @SP
  D=M
  @R13
  M=D-M
  @1
  D=A
  @R13
  D=M-D
  @ARG
  M=D
  @SP
  D=M
  @LCL
  M=D
  @Main.fibonacci
  0;JMP
(Main.fibonacci$ret.1)
// D = RAM[2 + 0]
  @R2
  D=M
  @0
  D=D+A
  A=D
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 1
  @1
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
  @Main.fibonacci$ret.2
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @LCL
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @ARG
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @THIS
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @THAT
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @5
  D=A
  @R13
  M=D
  @SP
  D=M
  @R13
  M=D-M
  @1
  D=A
  @R13
  D=M-D
  @ARG
  M=D
  @SP
  D=M
  @LCL
  M=D
  @Main.fibonacci
  0;JMP
(Main.fibonacci$ret.2)
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
// return
  @LCL
  D=M
  @R14
  M=D
  @5
  D=A
  @R14
  A=M-D
  D=M
  @R15
  M=D
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
  @ARG
  A=M
  M=D
  @ARG
  D=M
  @SP
  M=D+1
  @R14
  A=M-1
  D=M
  @THAT
  M=D
  @2
  D=A
  @R14
  A=M-D
  D=M
  @THIS
  M=D
  @3
  D=A
  @R14
  A=M-D
  D=M
  @ARG
  M=D
  @4
  D=A
  @R14
  A=M-D
  D=M
  @LCL
  M=D
  @R15
  A=M
  0;JMP
// function Sys.init 0
(Sys.init)
  @0
  D=A
($3)
  @R13
  M=D
  D=0
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @R13
  MD=M-1
  @$3
  D;JGT
// D = 4
  @4
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @Sys.init$ret.1
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @LCL
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @ARG
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @THIS
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @THAT
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @5
  D=A
  @R13
  M=D
  @SP
  D=M
  @R13
  M=D-M
  @1
  D=A
  @R13
  D=M-D
  @ARG
  M=D
  @SP
  D=M
  @LCL
  M=D
  @Main.fibonacci
  0;JMP
(Sys.init$ret.1)
(Sys.init$END)
// goto Sys.init$END
  @Sys.init$END
  0;JMP
