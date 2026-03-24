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
// RAM[4] = D
  @R4
  M=D
// D = 0
  @0
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
// RAM[4 + 0] = D
  @R13
  M=D
  @R4
  D=M
  @0
  D=D+A
  @R14
  M=D
  @R13
  D=M
  @R14
  A=M
  M=D
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
// RAM[4 + 1] = D
  @R13
  M=D
  @R4
  D=M
  @1
  D=D+A
  @R14
  M=D
  @R13
  D=M
  @R14
  A=M
  M=D
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
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[2 + 0] = D
  @R13
  M=D
  @R2
  D=M
  @0
  D=D+A
  @R14
  M=D
  @R13
  D=M
  @R14
  A=M
  M=D
(FibonacciSeries.main$LOOP)
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
// if-goto FibonacciSeries.main$COMPUTE_ELEMENT
  @FibonacciSeries.main$COMPUTE_ELEMENT
  D;JNE
// goto FibonacciSeries.main$END
  @FibonacciSeries.main$END
  0;JMP
(FibonacciSeries.main$COMPUTE_ELEMENT)
// D = RAM[4 + 0]
  @R4
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
// D = RAM[4 + 1]
  @R4
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
// RAM[4 + 2] = D
  @R13
  M=D
  @R4
  D=M
  @2
  D=D+A
  @R14
  M=D
  @R13
  D=M
  @R14
  A=M
  M=D
// D = RAM[4]
  @R4
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
// RAM[4] = D
  @R4
  M=D
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
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[2 + 0] = D
  @R13
  M=D
  @R2
  D=M
  @0
  D=D+A
  @R14
  M=D
  @R13
  D=M
  @R14
  A=M
  M=D
// goto FibonacciSeries.main$LOOP
  @FibonacciSeries.main$LOOP
  0;JMP
(FibonacciSeries.main$END)
// END
(END)
  @END
  0;JMP