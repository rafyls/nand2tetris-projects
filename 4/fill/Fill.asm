// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.
    
(LOOP)
    @KBD
    D=M
    @BLACK
    D;JNE
    @WHITE
    0;JMP
(WHITE)
    @16384
    D=A
    @i
    M=D          // i = SCREEN
(WHITE_LOOP)
    @i
    D=M
    @24576
    D=D-A
    @LOOP
    D;JGE        
    @i
    A=M
    M=0          // Write white
    @i
    M=M+1
    @WHITE_LOOP
    0;JMP
(BLACK)
    @16384
    D=A
    @i
    M=D          // i = SCREEN
(BLACK_LOOP)
    @i
    D=M
    @24576
    D=D-A
    @LOOP
    D;JGE
    @i
    A=M
    M=-1         // Write black
    @i
    M=M+1
    @BLACK_LOOP
    0;JMP