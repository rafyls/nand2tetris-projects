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
// function Class1.set 0
(Class1.set)
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
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[static 0] = D
  @Class1.0
  M=D
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
// RAM[static 1] = D
  @Class1.1
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
// function Class1.get 0
(Class1.get)
  @0
  D=A
($1)
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
  @$1
  D;JGT
// D = RAM[static 0]
  @Class1.0
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = RAM[static 1]
  @Class1.1
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
// function Sys.init 0
(Sys.init)
  @0
  D=A
($2)
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
  @$2
  D;JGT
// D = 6
  @6
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 8
  @8
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
  @2
  D=A
  @R13
  D=M-D
  @ARG
  M=D
  @SP
  D=M
  @LCL
  M=D
  @Class1.set
  0;JMP
(Sys.init$ret.1)
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[5 + 0] = D
  @R13
  M=D
  @5
  D=A
  @0
  D=D+A
  @R14
  M=D
  @R13
  D=M
  @R14
  A=M
  M=D
// D = 23
  @23
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = 15
  @15
  D=A
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
  @Sys.init$ret.2
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
  @2
  D=A
  @R13
  D=M-D
  @ARG
  M=D
  @SP
  D=M
  @LCL
  M=D
  @Class2.set
  0;JMP
(Sys.init$ret.2)
// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1
// RAM[5 + 0] = D
  @R13
  M=D
  @5
  D=A
  @0
  D=D+A
  @R14
  M=D
  @R13
  D=M
  @R14
  A=M
  M=D
  @Sys.init$ret.3
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
  @0
  D=A
  @R13
  D=M-D
  @ARG
  M=D
  @SP
  D=M
  @LCL
  M=D
  @Class1.get
  0;JMP
(Sys.init$ret.3)
  @Sys.init$ret.4
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
  @0
  D=A
  @R13
  D=M-D
  @ARG
  M=D
  @SP
  D=M
  @LCL
  M=D
  @Class2.get
  0;JMP
(Sys.init$ret.4)
(Sys.init$END)
// goto Sys.init$END
  @Sys.init$END
  0;JMP
// function Class2.set 0
(Class2.set)
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
// RAM[static 0] = D
  @Class2.0
  M=D
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
// RAM[static 1] = D
  @Class2.1
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
// function Class2.get 0
(Class2.get)
  @0
  D=A
($4)
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
  @$4
  D;JGT
// D = RAM[static 0]
  @Class2.0
  D=M
// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1
// D = RAM[static 1]
  @Class2.1
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
