#!/usr/bin/env python3

import os.path
from pathlib import Path
import re

class Parser:
  A_INSTRUCTION = 0
  C_INSTRUCTION = 1
  L_INSTRUCTION = 2

  def __init__(self, file):
    self.infile = open(file, "rt")
    self.currentInstruction = ""
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
    self.currentInstruction = currentLine
    self.currentLineIndex += 1

  def instructionType(self):
    if self.currentInstruction[0] == '@':
      return Parser.A_INSTRUCTION
    elif self.currentInstruction[0] == '(':
      return Parser.L_INSTRUCTION
    else:
      return Parser.C_INSTRUCTION
    
  def symbol(self):
    if self.currentInstruction[0] == '@':
      return self.currentInstruction[1:len(self.currentInstruction)]
    elif self.currentInstruction[0] == '(':
      return self.currentInstruction[1:len(self.currentInstruction)-1]
  
  def dest(self):
    if "=" in self.currentInstruction:
      r = self.currentInstruction.split("=")[0]
      return r
    else:
      return None

  def comp(self):
    if "=" in self.currentInstruction:
      r = re.split(r"=|;", self.currentInstruction)[1]
      return r
    elif ";" in self.currentInstruction:
      r = re.split(r"=|;", self.currentInstruction)[0]
      return r
    else:
      return None

  def jump(self):
    if ";" in self.currentInstruction:
      if "=" in self.currentInstruction:
        r = re.split(r"=|;", self.currentInstruction)[2]
      else:
        r = r = re.split(r"=|;", self.currentInstruction)[1]
      return r
    else:
      return None

class Code:

  dest_mnemonics_binary = {
    "null": "000",
    "M": "001",
    "D": "010",
    "DM": "011",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "MA": "101",
    "AD": "110",
    "DA": "110",
    "ADM": "111",
    "AMD": "111",
    "DMA": "111",
    "DAM": "111",
    "MAD": "111",
    "MDA": "111",
  }

  jump_mnemonics_binary = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
  }

  comp_mnemonics_binary = {
    "0": "101010",
    "1": "111111",
    "-1": "111010",
    "D": "001100",
    "A": "110000",
    "!D": "001101",
    "!A": "110001",
    "-D": "001111",
    "-A": "110011",
    "D+1": "011111",
    "A+1": "110111",
    "D-1": "001110",
    "A-1": "110010",
    "D+A": "000010",
    "D-A": "010011",
    "A-D": "000111",
    "D&A": "000000",
    "D|A": "010101",
    "M": "110000",
    "!M": "110001",
    "-M": "110011",
    "M+1": "110111",
    "M-1": "110010",
    "D+M": "000010",
    "D-M": "010011",
    "M-D": "000111",
    "D&M": "000000",
    "D|M": "010101",
  }

  def dest(self, s):
    return Code.dest_mnemonics_binary[s]
  def comp(self, s):
    return Code.comp_mnemonics_binary[s]
  def jump(self, s):
    return Code.jump_mnemonics_binary[s]

class SymbolTable:

  def __init__(self):
    self.current_variable_address = 16
    self.symbol_table = {}
    self.symbol_table["R0"] = 0 
    self.symbol_table["R1"] = 1
    self.symbol_table["R2"] = 2
    self.symbol_table["R3"] = 3
    self.symbol_table["R4"] = 4
    self.symbol_table["R5"] = 5
    self.symbol_table["R6"] = 6
    self.symbol_table["R7"] = 7
    self.symbol_table["R8"] = 8
    self.symbol_table["R9"] = 9
    self.symbol_table["R10"] = 10
    self.symbol_table["R11"] = 11
    self.symbol_table["R12"] = 12
    self.symbol_table["R13"] = 13
    self.symbol_table["R14"] = 14
    self.symbol_table["R15"] = 15
    self.symbol_table["SP"] = 0
    self.symbol_table["LCL"] = 1
    self.symbol_table["ARG"] = 2
    self.symbol_table["THIS"] = 3
    self.symbol_table["THAT"] = 4
    self.symbol_table["SCREEN"] = 16384
    self.symbol_table["KBD"] = 24576

  def addEntry(self, symbol, address):
    self.symbol_table[symbol] = address

  def contains(self, symbol):
    if symbol in self.symbol_table.keys():
      return True
    return False

  def getAddress(self, symbol):
    return self.symbol_table[symbol]

def main(argv):
  if len(argv) != 2:
    raise SystemExit("Usage: ./HackAssembler [path/to/file.asm]")
  
  filepath, ext = os.path.splitext(argv[1])
  if ext != '.asm':
    raise SystemExit("Error: " + filepath + " is not an asm file.")
  
  asmfilepath, asmfilename = os.path.split(filepath)
  
  outfilepath = asmfilepath + "/" + asmfilename + ".hack"

  outfilepath = Path(outfilepath)
  outfilepath.parent.mkdir(exist_ok=True, parents=True)

  output_file = open(outfilepath, 'wt')

  # First pass
  parser = Parser(argv[1])
  symbol_table = SymbolTable()
  lineNumber = 0
  while parser.hasMoreLines():
    parser.advance()
    if parser.instructionType() == Parser.A_INSTRUCTION or parser.instructionType() == Parser.C_INSTRUCTION:
      lineNumber += 1
    else:
      symbol = parser.symbol()
      symbol_table.addEntry(symbol, lineNumber)
    
  # Second pass
  parser = Parser(argv[1])
  code = Code()
  while parser.hasMoreLines():
    parser.advance()
    if parser.instructionType() == Parser.A_INSTRUCTION:
      binaryInstruction = "0"

      symbol = parser.symbol()
      s = ""

      if symbol.isnumeric():
        s = bin(int(symbol))[2:]
      else:
        if symbol_table.contains(symbol):
            s = bin(symbol_table.getAddress(symbol))[2:]
        else:
            symbol_table.addEntry(symbol, symbol_table.current_variable_address)
            symbol_table.current_variable_address += 1
            s = bin(symbol_table.getAddress(symbol))[2:]
      
      for _ in range(0, 15-len(s)):
        binaryInstruction += "0"
      
      binaryInstruction += s

      binaryInstruction += '\n'
      output_file.write(binaryInstruction)
      
    elif parser.instructionType() == Parser.C_INSTRUCTION:
      dest = parser.dest()
      comp = parser.comp()
      jump = parser.jump()

      binaryInstruction = "111"

      if "M" in comp:
        binaryInstruction += "1"
      else:
        binaryInstruction += "0"

      if comp is not None:
        comp_bin = code.comp(comp)
      binaryInstruction += comp_bin

      if dest is not None:
        dest_bin = code.dest(dest)
      else:
        dest_bin = code.dest("null")
      binaryInstruction += dest_bin

      if jump is not None:
        jump_bin = code.jump(jump)
      else:
        jump_bin = code.jump("null")
      binaryInstruction += jump_bin

      binaryInstruction += '\n'
      output_file.write(binaryInstruction)
  
  parser.infile.close()
  output_file.close()

if __name__ == '__main__':
  import sys
  main(sys.argv)