#!/usr/bin/env python3

import os.path
from pathlib import Path

class Parser:
  C_ARITHMETIC = 0
  C_PUSH = 1
  C_POP = 2
  C_LABEL = 3
  C_GOTO = 4
  C_IF = 5
  C_FUNCTION = 6
  C_RETURN = 7
  C_CALL = 8

  binarycommands = {"add", "sub", "eq", "gt", "lt", "and", "or"}
  unarycommands = {"neg", "not"}
  arithmeticcommands = binarycommands | unarycommands

  def __init__(self, file):
    self.infile = open(file, "rt")
    self.currentCommand = ""
    self.infilelines = self.infile.read().splitlines()
    if (len(self.infilelines) == 0):
      self.infile.close()
      raise SystemExit("Error: \"" + file + "\" is an empty file.")
    else:
      self.currentLineIndex = 0

  def hasMoreLines(self):
    if self.currentLineIndex < len(self.infilelines):
      return True
    else:
      return False

  def advance(self):
    currentLine = self.infilelines[self.currentLineIndex].strip()
    while len(currentLine) == 0 or currentLine[0] == '/':
      self.currentLineIndex += 1
      currentLine = self.infilelines[self.currentLineIndex].strip()
    self.currentCommand = currentLine
    self.currentLineIndex += 1

  def commandType(self):
    command = self.currentCommand.split()[0]
    if command in Parser.arithmeticcommands:
      return Parser.C_ARITHMETIC
    elif command == "push":
      return Parser.C_PUSH
    elif command == "pop":
      return Parser.C_POP
    elif command == "label":
      return Parser.C_LABEL
    elif command == "goto":
      return Parser.C_GOTO
    elif command == "if-goto":
      return Parser.C_IF
    elif command == "function":
      return Parser.C_FUNCTION
    elif command == "call":
      return Parser.C_CALL
    elif command == "return":
      return Parser.C_RETURN

  def arg1(self):
    command = self.currentCommand.split()[0]
    if command in Parser.arithmeticcommands:
      return command
    else:
      return self.currentCommand.split()[1]

  def arg2(self):
    return self.currentCommand.split()[2]

class CodeWriter:

  label_number = 0
  base_addresses = {
    "local": 1,
    "argument": 2,
    "this": 3,
    "that": 4,
    "temp": 5,
  }
  filename = ""
  currentFunctionName = ""
  numberCallCommands = {}

  def __init__(self, file):
    self.outfile = open(file, 'wt')
    _, f = os.path.split(file)
    CodeWriter.filename, _ = os.path.splitext(f)

    a = f"""// Bootstrap code
// SP = 256
  @256
  D=A
  @SP
  M=D\n"""
    b = f"""// call Sys.init
  @LCL
  D=M\n"""
    c = self.genPushAsmCode()
    d = f"""  @ARG
  D=M\n"""
    e = self.genPushAsmCode()
    g = f"""  @THIS
  D=M\n"""
    h = self.genPushAsmCode()
    i = f"""  @THAT
  D=M\n"""
    j = self.genPushAsmCode()
    k = f"""  @5
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
  0;JMP\n"""
    print(a + b + c + d + e + g + h + i + j + k, file=self.outfile, end='')

  def writeArithmetic(self, command):
    if command == "add":
      pop1 = self.genPopAsmCode()
      y = """// RAM[14] = D
  @R14
  M=D\n"""
      pop2 = self.genPopAsmCode()
      x = """// RAM[13] = D
  @R13
  M=D\n"""
      add = self.genAddAsmCode()
      push = self.genPushAsmCode()
      print(pop1 + y + pop2 + x + add + push, file=self.outfile, end='')
    elif command == "sub":
      pop1 = self.genPopAsmCode()
      y = """// RAM[14] = D
  @R14
  M=D\n"""
      pop2 = self.genPopAsmCode()
      x = """// RAM[13] = D
  @R13
  M=D\n"""
      sub = self.genSubAsmCode()
      push = self.genPushAsmCode()
      print(pop1 + y + pop2 + x + sub + push, file=self.outfile, end='')
    elif command == "neg":
      pop1 = self.genPopAsmCode()
      y = """// RAM[14] = D
  @R14
  M=D\n"""
      neg = self.genNegAsmCode()
      push = self.genPushAsmCode()
      print(pop1 + y + neg + push, file=self.outfile, end='')
    elif command == "eq":
      pop1 = self.genPopAsmCode()
      y = """// RAM[14] = D
  @R14
  M=D\n"""
      pop2 = self.genPopAsmCode()
      x = """// RAM[13] = D
  @R13
  M=D\n"""
      eq = self.genEqAsmCode()
      push = self.genPushAsmCode()
      print(pop1 + y + pop2 + x + eq + push, file=self.outfile, end='')
    elif command == "gt":
      pop1 = self.genPopAsmCode()
      y = """// RAM[14] = D
  @R14
  M=D\n"""
      pop2 = self.genPopAsmCode()
      x = """// RAM[13] = D
  @R13
  M=D\n"""
      gt = self.genGtAsmCode()
      push = self.genPushAsmCode()
      print(pop1 + y + pop2 + x + gt + push, file=self.outfile, end='')
    elif command == "lt":
      pop1 = self.genPopAsmCode()
      y = """// RAM[14] = D
  @R14
  M=D\n"""
      pop2 = self.genPopAsmCode()
      x = """// RAM[13] = D
  @R13
  M=D\n"""
      lt = self.genLtAsmCode()
      push = self.genPushAsmCode()
      print(pop1 + y + pop2 + x + lt + push, file=self.outfile, end='')
    elif command == "and":
      pop1 = self.genPopAsmCode()
      y = """// RAM[14] = D
  @R14
  M=D\n"""
      pop2 = self.genPopAsmCode()
      x = """// RAM[13] = D
  @R13
  M=D\n"""
      andasm = self.genAndAsmCode()
      push = self.genPushAsmCode()
      print(pop1 + y + pop2 + x + andasm + push, file=self.outfile, end='')
    elif command == "or":
      pop1 = self.genPopAsmCode()
      y = """// RAM[14] = D
  @R14
  M=D\n"""
      pop2 = self.genPopAsmCode()
      x = """// RAM[13] = D
  @R13
  M=D\n"""
      orasm = self.genOrAsmCode()
      push = self.genPushAsmCode()
      print(pop1 + y + pop2 + x + orasm + push, file=self.outfile, end='')
    elif command == "not":
      pop1 = self.genPopAsmCode()
      y = """// RAM[14] = D
  @R14
  M=D\n"""
      notasm = self.genNotAsmCode()
      push = self.genPushAsmCode()
      print(pop1 + y + notasm + push, file=self.outfile, end='')
      
  def writePushPop(self, command, segment, index):
    if command == "push":
      if segment == "constant":
        c = self.genConstantAsmCode(index)
      elif segment == "local" or segment == "argument" or  segment == "this" or segment == "that":
        c = self.genLclArgThisThatAsmCode(CodeWriter.base_addresses[segment], index)
      elif segment == "temp":
        c = self.genTempAsmCode(index)
      elif segment == "pointer":
        c = self.genPointerAsmCode(index)
      elif segment == "static":
        c = self.genStaticAsmCode(index)

      push = self.genPushAsmCode()
      print(c + push, file=self.outfile, end='')

    elif command == "pop":
      pop = self.genPopAsmCode()
      if segment == "local" or segment == "argument" or  segment == "this" or segment == "that":
        y = self.genLclArgThisThatPopAsmCode(CodeWriter.base_addresses[segment], index)
      elif segment == "temp":
        y = self.genTempPopAsmCode(index)
      elif segment == "pointer":
        y = self.genPointerPopAsmCode(index)
      elif segment == "static":
        y = self.genStaticPopAsmCode(index)
      
      print(pop + y, file=self.outfile, end='')

  def writeLabel(self, label):
    if CodeWriter.currentFunctionName == "":
      a = f"{CodeWriter.filename}.main${label}"
      l = f"({a})\n"
    else:
      a = f"{CodeWriter.currentFunctionName}${label}"
      l = f"({a})\n"
    print(l, file=self.outfile, end='')

  def writeGoto(self, label):
    if CodeWriter.currentFunctionName == "":
      a = f"{CodeWriter.filename}.main${label}"
    else:
      a = f"{CodeWriter.currentFunctionName}${label}"
    j = f"""// goto {a}
  @{a}
  0;JMP\n"""
    print(j, file=self.outfile, end='')

  def writeIf(self, label):
    p = self.genPopAsmCode()
    if CodeWriter.currentFunctionName == "":
      a = f"{CodeWriter.filename}.main${label}"
    else:
      a = f"{CodeWriter.currentFunctionName}${label}"
    j = f"""// if-goto {a}
  @{a}
  D;JNE\n"""
    print(p + j, file=self.outfile, end='')

  def writeFunction(self, functionName, nVars):
    CodeWriter.currentFunctionName = functionName
    l = self.genDynamicLabelAsmCode()
    r = f"""// function {functionName} {nVars}
({functionName})
  @{nVars}
  D=A
({l})
  @R13
  M=D
  D=0\n"""
    p = self.genPushAsmCode()
    s = f"""  @R13
  MD=M-1\n"""
    q = f"""  @{l}
  D;JGT\n"""
    print(r + p + s + q, file=self.outfile, end='')

  def writeCall(self, functionName, nArgs):
    if CodeWriter.currentFunctionName not in CodeWriter.numberCallCommands.keys():
      CodeWriter.numberCallCommands[CodeWriter.currentFunctionName] = 1
    else:
      CodeWriter.numberCallCommands[CodeWriter.currentFunctionName] += 1
      
    a = f"""  @{CodeWriter.currentFunctionName}$ret.{CodeWriter.numberCallCommands[CodeWriter.currentFunctionName]}
  D=A\n"""
    b = self.genPushAsmCode()
    c = f"""  @LCL
  D=M\n"""
    d = self.genPushAsmCode()
    e = f"""  @ARG
  D=M\n"""
    f = self.genPushAsmCode()
    g = f"""  @THIS
  D=M\n"""
    h = self.genPushAsmCode()
    i = f"""  @THAT
  D=M\n"""
    j = self.genPushAsmCode()
    k = f"""  @5
  D=A
  @R13
  M=D
  @SP
  D=M
  @R13
  M=D-M
  @{nArgs}
  D=A
  @R13
  D=M-D
  @ARG
  M=D
  @SP
  D=M
  @LCL
  M=D
  @{functionName}
  0;JMP
({CodeWriter.currentFunctionName}$ret.{CodeWriter.numberCallCommands[CodeWriter.currentFunctionName]})\n"""
    print(a + b + c + d + e + f + g + h + i + j + k, file=self.outfile, end='')

  def writeReturn(self):
    a = f"""// return
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
  M=D\n"""
    p = self.genPopAsmCode()
    b = f"""  @ARG
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
  0;JMP\n"""
    print(a + p + b, file=self.outfile, end='')

  def setFileName(self, fileName):
    _, f = os.path.split(fileName)
    CodeWriter.filename, _ = os.path.splitext(f)

  def close(self):
    self.outfile.close()

  def genPushAsmCode(self):
    """Returns the Hack assembly code that pushes a value 
    in the D register into the stack.
    """
    return """// Push: RAM[SP++] = D
  @SP
  A=M
  M=D
  @SP
  M=M+1\n"""
  
  def genPopAsmCode(self):
    """Returns the Hack assembly code that pops a value 
    off the stack into the D register.
    """
    return """// Pop: D = RAM[--SP]
  @SP
  A=M-1
  D=M
  M=0
  @SP
  M=M-1\n"""

  def genAddAsmCode(self):
    """Returns the Hack assembly code that performs the following
    operation: D = RAM[13] + RAM[14].
    """
    return """// D = RAM[13] + RAM[14]
  @R13
  D=M
  @R14
  D=D+M\n"""

  def genSubAsmCode(self):
    """Returns the Hack assembly code that performs the following
    operation: D = RAM[13] - RAM[14].
    """
    return """// D = RAM[13] - RAM[14]
  @R13
  D=M
  @R14
  D=D-M\n"""

  def genNegAsmCode(self):
    """Returns the Hack assembly code that performs the following
    operation: D = - RAM[14].
    """
    return """// D = - RAM[14]
  @R14
  D=-M\n"""

  def genEqAsmCode(self):
    """Returns the Hack assembly code that performs the following
    operation: D = RAM[13] == RAM[14].
    """
    label1 = self.genDynamicLabelAsmCode()
    label2 = self.genDynamicLabelAsmCode()
    return f"""// D = RAM[13] == RAM[14]
  @R13
  D=M
  @R14
  D=D-M
  @{label1}
  D;JEQ
  D=0
  @{label2}
  0;JMP
({label1})
  D=-1
({label2})\n"""

  def genGtAsmCode(self):
    """Returns the Hack assembly code that performs the following
    operation: D = RAM[13] > RAM[14].
    """
    label1 = self.genDynamicLabelAsmCode()
    label2 = self.genDynamicLabelAsmCode()
    return f"""// D = RAM[13] > RAM[14]
  @R13
  D=M
  @R14
  D=D-M
  @{label1}
  D;JGT
  D=0
  @{label2}
  0;JMP
({label1})
  D=-1
({label2})\n"""
  
  def genLtAsmCode(self):
    """Returns the Hack assembly code that performs the following
    operation: D = RAM[13] < RAM[14].
    """
    label1 = self.genDynamicLabelAsmCode()
    label2 = self.genDynamicLabelAsmCode()
    return f"""// D = RAM[13] < RAM[14]
  @R13
  D=M
  @R14
  D=D-M
  @{label1}
  D;JLT
  D=0
  @{label2}
  0;JMP
({label1})
  D=-1
({label2})\n"""

  def genAndAsmCode(self):
    """Returns the Hack assembly code that performs the following
    operation: D = RAM[13] And RAM[14].
    """
    return """// D = RAM[13] And RAM[14]
  @R13
  D=M
  @R14
  D=D&M\n"""

  def genOrAsmCode(self):
    """Returns the Hack assembly code that performs the following
    operation: D = RAM[13] Or RAM[14].
    """
    return """// D = RAM[13] Or RAM[14]
  @R13
  D=M
  @R14
  D=D|M\n"""

  def genNotAsmCode(self):
    """Returns the Hack assembly code that performs the following
    operation: D = Not RAM[14].
    """
    return """// D = Not RAM[14]
  @R14
  D=!M\n"""

  def genConstantAsmCode(self, value):
    """Returns the Hack assembly code that performs the following
    operation: D = value.
    """
    return f"""// D = {value}
  @{value}
  D=A\n"""

  def genLclArgThisThatAsmCode(self, base_address, value):
    """Returns the Hack assembly code that performs the following
    operation: D = RAM[base_address + value].
    """
    return f"""// D = RAM[{base_address} + {value}]
  @R{base_address}
  D=M
  @{value}
  D=D+A
  A=D
  D=M\n"""

  def genTempAsmCode(self, value):
    """Returns the Hack assembly code that performs the following
    operation: D = RAM[5 + value].
    """
    return f"""// D = RAM[5 + {value}]
  @5
  D=A
  @{value}
  D=D+A
  A=D
  D=M\n"""

  def genLclArgThisThatPopAsmCode(self, base_address, value):
    """Returns the Hack assembly code that performs the following
    operation: RAM[base_address + value] = D.
    """
    return f"""// RAM[{base_address} + {value}] = D
  @R13
  M=D
  @R{base_address}
  D=M
  @{value}
  D=D+A
  @R14
  M=D
  @R13
  D=M
  @R14
  A=M
  M=D\n"""

  def genTempPopAsmCode(self, value):
    """Returns the Hack assembly code that performs the following
    operation: RAM[5 + value] = D.
    """
    return f"""// RAM[5 + {value}] = D
  @R13
  M=D
  @5
  D=A
  @{value}
  D=D+A
  @R14
  M=D
  @R13
  D=M
  @R14
  A=M
  M=D\n"""

  def genPointerAsmCode(self, value):
    """Returns the Hack assembly code that performs the following
    operation: D = RAM[value], where value is either 3 or 4.
    """
    if value == '0':
      return f"""// D = RAM[3]
  @R3
  D=M\n"""
    else:
      return f"""// D = RAM[4]
  @R4
  D=M\n"""
    
  def genPointerPopAsmCode(self, value):
    """Returns the Hack assembly code that performs the following
    operation: RAM[value] = D, where value is either 3 or 4.
    """
    if value == '0':
      return f"""// RAM[3] = D
  @R3
  M=D\n"""
    else:
      return f"""// RAM[4] = D
  @R4
  M=D\n"""

  def genStaticAsmCode(self, value):
    """Returns the Hack assembly code that translates
    static variables into Hack variable assembly symbols that
    begins from RAM[16] and onward and that performs the operation:
    D = RAM[value].
    """
    return f"""// D = RAM[static {value}]
  @{CodeWriter.filename}.{value}
  D=M\n"""
  
  def genStaticPopAsmCode(self, value):
    """Returns the Hack assembly code that translates
    static variables into Hack variable assembly symbols that
    begins from RAM[16] and onward and that performs the operation:
    RAM[value] = D.
    """
    return f"""// RAM[static {value}] = D
  @{CodeWriter.filename}.{value}
  M=D\n"""

  def genDynamicLabelAsmCode(self):
    """Returns a dynamically-generated label to add and refer to
    in a Hack assembly program.
    """
    label = "$" + str(CodeWriter.label_number)
    CodeWriter.label_number += 1
    return label

  def genInfiniteLoop(self):
    """Returns the Hack assembly code that performs an infinite
    loop, to add at the end of Hack assembly programs.
    """
    e = """// END
(END)
  @END
  0;JMP"""
    print(e, file=self.outfile, end='')

def main(argv):
  if len(argv) != 2:
    raise SystemExit("Usage: ./VMTranslator [path/to/FileName.vm | path/to/FolderName]")
  
  if not os.path.isdir(argv[1]):
    filepath, ext = os.path.splitext(argv[1])
    if ext != '.vm':
      raise SystemExit("Error: " + filepath + " is not an .vm file.")
    
    vmfilepath, vmfilename = os.path.split(filepath)
    if vmfilename[0].islower():
      raise SystemExit("Error: " + "The first character of \"" + vmfilename + "\" must be in uppercase.")
    
    outfilepath = vmfilepath + "/" + vmfilename + ".asm"

    outfilepath = Path(outfilepath)
    outfilepath.parent.mkdir(exist_ok=True, parents=True)

    parser = Parser(argv[1])
    codewriter = CodeWriter(outfilepath)

    while parser.hasMoreLines():
      parser.advance()
      
      if parser.commandType() == Parser.C_PUSH or parser.commandType() == Parser.C_POP:
        codewriter.writePushPop(parser.currentCommand.split()[0], parser.arg1(), parser.arg2())
      elif parser.commandType() == Parser.C_ARITHMETIC:
        codewriter.writeArithmetic(parser.arg1())
      elif parser.commandType() == Parser.C_LABEL:
        codewriter.writeLabel(parser.arg1())
      elif parser.commandType() == Parser.C_GOTO:
        codewriter.writeGoto(parser.arg1())
      elif parser.commandType() == Parser.C_IF:
        codewriter.writeIf(parser.arg1())
      elif parser.commandType() == Parser.C_FUNCTION:
        codewriter.writeFunction(parser.arg1(), parser.arg2())
      elif parser.commandType() == Parser.C_RETURN:
        codewriter.writeReturn()
      elif parser.commandType() == Parser.C_CALL:
        codewriter.writeCall(parser.arg1(), parser.arg2())

    codewriter.genInfiniteLoop()

    parser.infile.close()
    codewriter.close()
  else:
    dirpath = Path(argv[1])
    vmfilepaths = []
    for c in dirpath.iterdir():
      if c.suffix == '.vm':
        vmfilepaths.append(c)

    if len(vmfilepaths) == 0:
      raise SystemExit("Error: " + argv[1] + " does not contain any .vm file.")

    for p in vmfilepaths:
      _, vmfilename = os.path.split(p)
      if vmfilename[0].islower():
        raise SystemExit("Error: " + "The first character of \"" + vmfilename + "\" must be in uppercase.")

    vmfilepath, _ = os.path.split(vmfilepaths[0])
    _, dirname = os.path.split(vmfilepath)

    outfilepath = vmfilepath + "/" + dirname + ".asm"

    outfilepath = Path(outfilepath)
    outfilepath.parent.mkdir(exist_ok=True, parents=True)

    codewriter = CodeWriter(outfilepath)

    for vmfile in vmfilepaths:
      parser = Parser(vmfile)
      codewriter.setFileName(vmfile)
      while parser.hasMoreLines():
        parser.advance()
        
        if parser.commandType() == Parser.C_PUSH or parser.commandType() == Parser.C_POP:
          codewriter.writePushPop(parser.currentCommand.split()[0], parser.arg1(), parser.arg2())
        elif parser.commandType() == Parser.C_ARITHMETIC:
          codewriter.writeArithmetic(parser.arg1())
        elif parser.commandType() == Parser.C_LABEL:
          codewriter.writeLabel(parser.arg1())
        elif parser.commandType() == Parser.C_GOTO:
          codewriter.writeGoto(parser.arg1())
        elif parser.commandType() == Parser.C_IF:
          codewriter.writeIf(parser.arg1())
        elif parser.commandType() == Parser.C_FUNCTION:
          codewriter.writeFunction(parser.arg1(), parser.arg2())
        elif parser.commandType() == Parser.C_RETURN:
          codewriter.writeReturn()
        elif parser.commandType() == Parser.C_CALL:
          codewriter.writeCall(parser.arg1(), parser.arg2())

if __name__ == '__main__':
  import sys
  main(sys.argv)