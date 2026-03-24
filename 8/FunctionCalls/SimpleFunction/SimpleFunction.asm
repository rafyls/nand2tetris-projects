// function SimpleFunction.test 2
(SimpleFunction.test)
  @2
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
// D = RAM[1 + 0]
  @R1
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
// D = RAM[1 + 1]
  @R1
  D=M
  @1
  D=D+A
  A=D
  D=M
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
// D = RAM[2 + 1]
  @R2
  D=M
  @1
  D=D+A
  A=D
  D=M
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
// END
(END)
  @END
  0;JMP