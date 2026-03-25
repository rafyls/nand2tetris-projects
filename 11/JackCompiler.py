#!/usr/bin/env python3

import os.path
from pathlib import Path

class JackTokenizer:
  KEYWORD = 0
  SYMBOL = 1
  IDENTIFIER = 2
  INT_CONST = 3
  STRING_CONST = 4

  keyword_tokens = {
    'class', 'constructor', 'function', 'method', 'field',
    'static', 'var', 'int', 'char', 'boolean', 'void', 'true',
    'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return',
  }

  symbols_tokens = {
    '{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-',
    '*', '/', '&', '|', '<', '>', '=', '~',
  }

  def __init__(self, file):
    self.infile = open(file, "rt")
    self.currentToken = ""
    self.infilecontents = self.infile.read()
    self.infilecontents += ' '
    if (len(self.infilecontents) == 0):
      self.infile.close()
      raise SystemExit("Error: \"" + file + "\" is an empty file.")
    else:
      self.currentCharIndex = 0

  def ignoreCommentsSpaces(self):
    try:
      while self.infilecontents[self.currentCharIndex].isspace():
        self.currentCharIndex += 1

      while self.infilecontents[self.currentCharIndex] == '/' and self.infilecontents[self.currentCharIndex + 1] == '/':
        while self.infilecontents[self.currentCharIndex] != '\n':
          self.currentCharIndex += 1
        while self.infilecontents[self.currentCharIndex].isspace():
          self.currentCharIndex += 1

      while self.infilecontents[self.currentCharIndex] == '/' and self.infilecontents[self.currentCharIndex + 1] == '*':
        self.currentCharIndex += 2
        if self.infilecontents[self.currentCharIndex] == '*':
          self.currentCharIndex += 1
        while self.infilecontents[self.currentCharIndex] != '*' or self.infilecontents[self.currentCharIndex + 1] != '/':
          self.currentCharIndex += 1
        self.currentCharIndex += 2
        while self.infilecontents[self.currentCharIndex].isspace():
          self.currentCharIndex += 1
      
      while self.infilecontents[self.currentCharIndex].isspace():
        self.currentCharIndex += 1
        
        return True
    except IndexError:
      return False
    
  def hasMoreTokens(self):
    self.ignoreCommentsSpaces()
    if self.currentCharIndex == len(self.infilecontents):
      return False
    else:
      return True

  def advance(self):
    startTokenIndex = self.currentCharIndex
    if self.infilecontents[self.currentCharIndex].isdecimal():
      self.currentCharIndex += 1
      while self.infilecontents[self.currentCharIndex].isdecimal():
        self.currentCharIndex += 1
      self.currentToken = self.infilecontents[startTokenIndex:self.currentCharIndex]
    elif self.infilecontents[self.currentCharIndex] == "\"":
      self.currentCharIndex += 1
      while self.infilecontents[self.currentCharIndex] != "\"":
        self.currentCharIndex += 1
      self.currentToken = self.infilecontents[startTokenIndex+1:self.currentCharIndex]
      self.currentCharIndex += 1
    elif self.infilecontents[self.currentCharIndex].isalpha() or self.infilecontents[self.currentCharIndex] == "_":
      self.currentCharIndex += 1
      while self.infilecontents[self.currentCharIndex].isalpha() or self.infilecontents[self.currentCharIndex].isdecimal() or self.infilecontents[self.currentCharIndex] == "_":
        self.currentCharIndex += 1
      self.currentToken = self.infilecontents[startTokenIndex:self.currentCharIndex]
    elif self.infilecontents[self.currentCharIndex] in JackTokenizer.symbols_tokens:
      self.currentToken = self.infilecontents[startTokenIndex]
      self.currentCharIndex += 1
      
  def tokenType(self):
    if self.currentToken in JackTokenizer.keyword_tokens:
      return JackTokenizer.KEYWORD
    elif self.currentToken in JackTokenizer.symbols_tokens:
      return JackTokenizer.SYMBOL
    elif self.currentToken[0].isdecimal():
      return JackTokenizer.INT_CONST
    elif self.infilecontents[self.currentCharIndex-1] == "\"":
      return JackTokenizer.STRING_CONST
    else:
      return JackTokenizer.IDENTIFIER

  def keyword(self):
    return self.currentToken

  def symbol(self):
    return self.currentToken

  def identifier(self):
    return self.currentToken

  def intVal(self):
    return int(self.currentToken)

  def stringVal(self):
    return self.currentToken

class CompilationEngine:
  def __init__(self, inputFile, outputFile):
    self.infile = inputFile
    self.outfile = outputFile
    self.tokenizer = JackTokenizer(inputFile)
    if self.tokenizer.hasMoreTokens():
      self.tokenizer.advance()
    self.vmwriter = VMWriter(outputFile)
    self.classSymbolTable = SymbolTable()
    self.subroutineSymbolTable = SymbolTable()
    self.className = ""
    self.currentSubroutineName = ""
    self.numlocalVars = 0
    self.currentSubroutineIsMethod = False
    self.currentSubroutineIsConstructor = False

  def process(self, str):
    if self.tokenizer.currentToken == str:
      if self.tokenizer.tokenType() == JackTokenizer.KEYWORD:
        if self.tokenizer.hasMoreTokens():
          self.tokenizer.advance()
      elif self.tokenizer.tokenType() == JackTokenizer.SYMBOL:
        if self.tokenizer.hasMoreTokens():
          self.tokenizer.advance()
      elif self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
        if self.tokenizer.hasMoreTokens():
          self.tokenizer.advance()
      elif self.tokenizer.tokenType() == JackTokenizer.INT_CONST:
        if self.tokenizer.hasMoreTokens():
          self.tokenizer.advance()
      elif self.tokenizer.tokenType() == JackTokenizer.STRING_CONST:
        if self.tokenizer.hasMoreTokens():
          self.tokenizer.advance()
    else:
      print(f"In file {self.infile}: Syntax Error - Unexpected token: {str}")
    
  def compileClass(self):
    self.process("class")
    if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)
      self.className = identifier
    self.process("{")
    while self.tokenizer.currentToken == 'static' or self.tokenizer.currentToken == 'field':
      self.compileClassVarDec()
    while self.tokenizer.currentToken == 'constructor' or self.tokenizer.currentToken == 'function' or self.tokenizer.currentToken == 'method':
      self.compileSubroutine()
    self.process("}")

  def compileClassVarDec(self):
    keyword = self.tokenizer.keyword()
    self.process(keyword)

    if keyword == 'static':
      varsKind = self.classSymbolTable.STATIC
    elif keyword == 'field':
      varsKind = self.classSymbolTable.FIELD

    if self.tokenizer.currentToken == 'int' or self.tokenizer.currentToken == 'char' or self.tokenizer.currentToken == 'boolean':
      keyword = self.tokenizer.keyword()
      self.process(keyword)

      varsType = keyword

    elif self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)

      varsType = identifier

    if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)
      
      self.classSymbolTable.define(identifier, varsType, varsKind)
      
    while self.tokenizer.currentToken == ',':
      symbol = self.tokenizer.symbol()
      self.process(symbol)
      if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
        identifier = self.tokenizer.identifier()
        self.process(identifier)

        self.classSymbolTable.define(identifier, varsType, varsKind)

    self.process(";")

  def compileSubroutine(self):
    self.subroutineSymbolTable.reset()

    keyword = self.tokenizer.keyword()
    self.process(keyword)

    self.currentSubroutineIsMethod = False
    self.currentSubroutineIsConstructor = False

    if keyword == 'method':
      self.subroutineSymbolTable.define("this", self.className, SymbolTable.ARG)
      self.currentSubroutineIsMethod = True
    elif keyword == 'constructor':
      self.currentSubroutineIsConstructor = True

    if self.tokenizer.currentToken == 'void':
      keyword = self.tokenizer.keyword()
      self.process(keyword)
    elif self.tokenizer.currentToken == 'int' or self.tokenizer.currentToken == 'int' or self.tokenizer.currentToken == 'char' or self.tokenizer.currentToken == 'boolean':
      keyword = self.tokenizer.keyword()
      self.process(keyword)
    elif self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)
    if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)
      self.currentSubroutineName = identifier
    self.process('(')
    self.compileParameterList()
    self.process(')')
    self.compileSubroutineBody()

  def compileParameterList(self):
    if self.tokenizer.currentToken == 'int' or self.tokenizer.currentToken == 'char' or self.tokenizer.currentToken == 'boolean':
      keyword = self.tokenizer.keyword()
      self.process(keyword)

      varsType = keyword

    elif self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)

      varsType = identifier

    if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)

      self.subroutineSymbolTable.define(identifier, varsType, SymbolTable.ARG)

    while self.tokenizer.currentToken == ',':
      symbol = self.tokenizer.symbol()
      self.process(symbol)
      if self.tokenizer.currentToken == 'int' or self.tokenizer.currentToken == 'char' or self.tokenizer.currentToken == 'boolean':
        keyword = self.tokenizer.keyword()
        self.process(keyword)

        varsType = keyword

      elif self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
        identifier = self.tokenizer.identifier()
        self.process(identifier)

        varsType = identifier

      if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
        identifier = self.tokenizer.identifier()
        self.process(identifier)

        self.subroutineSymbolTable.define(identifier, varsType, SymbolTable.ARG)
  
  def compileSubroutineBody(self):
    self.process("{")
    while self.tokenizer.currentToken == 'var':
      self.compileVarDec()
    
    if self.currentSubroutineIsMethod:
      self.vmwriter.writeFunction(f"{self.className}.{self.currentSubroutineName}", self.numlocalVars)
      self.vmwriter.writePush(VMWriter.ARGUMENT, 0)
      self.vmwriter.writePop(VMWriter.POINTER, 0)
    elif self.currentSubroutineIsConstructor:
      self.vmwriter.writeFunction(f"{self.className}.{self.currentSubroutineName}", self.numlocalVars)
      self.vmwriter.writePush(VMWriter.CONSTANT, self.classSymbolTable.varCount(SymbolTable.FIELD))
      self.vmwriter.writeCall("Memory.alloc", 1)
      self.vmwriter.writePop(VMWriter.POINTER, 0)
    else:
      self.vmwriter.writeFunction(f"{self.className}.{self.currentSubroutineName}", self.numlocalVars)
    self.compileStatements()
    self.process("}")

  def compileVarDec(self):
    keyword = self.tokenizer.keyword()
    self.process(keyword)
    if self.tokenizer.currentToken == 'int' or self.tokenizer.currentToken == 'char' or self.tokenizer.currentToken == 'boolean':
      keyword = self.tokenizer.keyword()
      self.process(keyword)

      varsType = keyword

    elif self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)

      varsType = identifier

    if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)

      self.subroutineSymbolTable.define(identifier, varsType, SymbolTable.VAR)

    while self.tokenizer.currentToken == ',':
      symbol = self.tokenizer.symbol()
      self.process(symbol)
      if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
        identifier = self.tokenizer.identifier()
        self.process(identifier)

        self.subroutineSymbolTable.define(identifier, varsType, SymbolTable.VAR)
    
    self.process(";")
    self.numlocalVars = self.subroutineSymbolTable.varCount(SymbolTable.VAR)
  
  def compileStatements(self):
    while self.tokenizer.currentToken == 'let' or self.tokenizer.currentToken == 'if' or self.tokenizer.currentToken == 'while' or self.tokenizer.currentToken == 'do' or self.tokenizer.currentToken == 'return':
      if self.tokenizer.currentToken == 'let':
        self.compileLet()
      elif self.tokenizer.currentToken == 'if':
        self.compileIf()
      elif self.tokenizer.currentToken == 'while':
        self.compileWhile()
      elif self.tokenizer.currentToken == 'do':
        self.compileDo()
      elif self.tokenizer.currentToken == 'return':
        self.compileReturn()

  def compileLet(self):
    keyword = self.tokenizer.keyword()
    self.process(keyword)
    if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)
    if self.tokenizer.currentToken == '[':
      kind = self.subroutineSymbolTable.kindOf(identifier)
      if kind != None:
        index = self.subroutineSymbolTable.indexOf(identifier)
        if kind == SymbolTable.STATIC:
          self.vmwriter.writePush(VMWriter.STATIC, index)
        elif kind == SymbolTable.FIELD:
          self.vmwriter.writePush(VMWriter.THIS, index)
        elif kind == SymbolTable.VAR:
          self.vmwriter.writePush(VMWriter.LOCAL, index)
        elif kind == SymbolTable.ARG:
          self.vmwriter.writePush(VMWriter.ARGUMENT, index)
      else:
        kind = self.classSymbolTable.kindOf(identifier)
        if kind != None:
          index = self.classSymbolTable.indexOf(identifier)
          if kind == SymbolTable.STATIC:
            self.vmwriter.writePush(VMWriter.STATIC, index)
          elif kind == SymbolTable.FIELD:
            self.vmwriter.writePush(VMWriter.THIS, index)
          elif kind == SymbolTable.VAR:
            self.vmwriter.writePush(VMWriter.LOCAL, index)
          elif kind == SymbolTable.ARG:
            self.vmwriter.writePush(VMWriter.ARGUMENT, index)
        else:
          raise SystemExit(f"Syntax error in file {self.infile}: identifier \"{identifier}\" is not declared.")

      self.process("[")
      self.compileExpression()
      self.process("]")

      self.vmwriter.writeArithmetic(VMWriter.ADD)
      
      self.process("=")
      self.compileExpression()
      self.process(";")

      self.vmwriter.writePop(VMWriter.TEMP, 0)
      self.vmwriter.writePop(VMWriter.POINTER, 1)
      self.vmwriter.writePush(VMWriter.TEMP, 0)
      self.vmwriter.writePop(VMWriter.THAT, 0)
    else:
      self.process("=")
      self.compileExpression()
      self.process(";")
      kind = self.subroutineSymbolTable.kindOf(identifier)
      if kind != None:
        index = self.subroutineSymbolTable.indexOf(identifier)
        if kind == SymbolTable.STATIC:
          self.vmwriter.writePop(VMWriter.STATIC, index)
        elif kind == SymbolTable.FIELD:
          self.vmwriter.writePop(VMWriter.THIS, index)
        elif kind == SymbolTable.VAR:
          self.vmwriter.writePop(VMWriter.LOCAL, index)
        elif kind == SymbolTable.ARG:
          self.vmwriter.writePop(VMWriter.ARGUMENT, index)
      else:
        kind = self.classSymbolTable.kindOf(identifier)
        if kind != None:
          index = self.classSymbolTable.indexOf(identifier)
          if kind == SymbolTable.STATIC:
            self.vmwriter.writePop(VMWriter.STATIC, index)
          elif kind == SymbolTable.FIELD:
            self.vmwriter.writePop(VMWriter.THIS, index)
          elif kind == SymbolTable.VAR:
            self.vmwriter.writePop(VMWriter.LOCAL, index)
          elif kind == SymbolTable.ARG:
            self.vmwriter.writePop(VMWriter.ARGUMENT, index)
        else:
          raise SystemExit(f"Syntax error in file {self.infile}: identifier \"{identifier}\" is not declared.")

  def compileIf(self):
    keyword = self.tokenizer.keyword()
    self.process(keyword)
    self.process("(")
    self.compileExpression()
    self.process(")")

    self.vmwriter.writeArithmetic(VMWriter.NOT)
    label1 = self.vmwriter.generateLabel()
    self.vmwriter.writeIf(label1)

    self.process("{")
    self.compileStatements()
    self.process("}")

    label2 = self.vmwriter.generateLabel()
    self.vmwriter.writeGoto(label2)
    self.vmwriter.writeLabel(label1)

    if self.tokenizer.currentToken == 'else':
      keyword = self.tokenizer.keyword()
      self.process(keyword)
      self.process("{")
      self.compileStatements()
      self.process("}")
    
    self.vmwriter.writeLabel(label2)

  def compileWhile(self):
    keyword = self.tokenizer.keyword()
    self.process(keyword)

    label1 = self.vmwriter.generateLabel()
    self.vmwriter.writeLabel(label1)

    self.process("(")
    self.compileExpression()
    self.process(")")

    self.vmwriter.writeArithmetic(VMWriter.NOT)
    label2 = self.vmwriter.generateLabel()
    self.vmwriter.writeIf(label2)

    self.process("{")
    self.compileStatements()
    self.process("}")
    
    self.vmwriter.writeGoto(label1)
    self.vmwriter.writeLabel(label2)

  def compileDo(self):
    keyword = self.tokenizer.keyword()
    self.process(keyword)
    self.compileExpression()
    self.process(";")
    self.vmwriter.writePop(VMWriter.TEMP, 0)

  def compileReturn(self):
    keyword = self.tokenizer.keyword()
    self.process(keyword)
    if self.tokenizer.currentToken != ";":
      self.compileExpression()
      self.process(";")
    else:
      self.process(";")
      self.vmwriter.writePush(VMWriter.CONSTANT, 0)
    self.vmwriter.writeReturn()
    
  def compileExpression(self):
    self.compileTerm()
    while self.tokenizer.currentToken == '+' or self.tokenizer.currentToken == '-' or self.tokenizer.currentToken == '*' or self.tokenizer.currentToken == '/' or self.tokenizer.currentToken == '&' or self.tokenizer.currentToken == '|' or self.tokenizer.currentToken == '<' or self.tokenizer.currentToken == '>' or self.tokenizer.currentToken == '=':
      symbol = self.tokenizer.symbol()
      self.process(symbol)
      self.compileTerm()
      if symbol == '+':
        self.vmwriter.writeArithmetic(VMWriter.ADD)
      elif symbol == '-':
        self.vmwriter.writeArithmetic(VMWriter.SUB)
      elif symbol == '=':
        self.vmwriter.writeArithmetic(VMWriter.EQ)
      elif symbol == '<':
        self.vmwriter.writeArithmetic(VMWriter.LT)
      elif symbol == '>':
        self.vmwriter.writeArithmetic(VMWriter.GT)
      elif symbol == '|':
        self.vmwriter.writeArithmetic(VMWriter.OR)
      elif symbol == '&':
        self.vmwriter.writeArithmetic(VMWriter.AND)
      elif symbol == '*':
        self.vmwriter.writeCall("Math.multiply", 2)
      elif symbol == '/':
        self.vmwriter.writeCall("Math.divide", 2)

  def compileTerm(self):
    if self.tokenizer.tokenType() == JackTokenizer.INT_CONST:
      intConstant = self.tokenizer.intVal()
      self.process(str(intConstant))

      self.vmwriter.writePush(VMWriter.CONSTANT, intConstant)

    elif self.tokenizer.tokenType() == JackTokenizer.STRING_CONST:
      stringConstant = self.tokenizer.stringVal()
      self.process(stringConstant)

      self.vmwriter.writePush(VMWriter.CONSTANT, len(stringConstant))
      self.vmwriter.writeCall("String.new", 1)
      for i in range(0, len(stringConstant)):
        self.vmwriter.writePush(VMWriter.CONSTANT, ord(stringConstant[i]))
        self.vmwriter.writeCall("String.appendChar", 2)

    elif self.tokenizer.currentToken == 'true' or self.tokenizer.currentToken == 'false' or self.tokenizer.currentToken == 'null' or self.tokenizer.currentToken == 'this':
      keyword = self.tokenizer.keyword()
      self.process(keyword)
      if keyword == 'false' or keyword == 'null':
        self.vmwriter.writePush(VMWriter.CONSTANT, 0)
      elif keyword == 'true':
        self.vmwriter.writePush(VMWriter.CONSTANT, 1)
        self.vmwriter.writeArithmetic(VMWriter.NEG)
      else:
        self.vmwriter.writePush(VMWriter.POINTER, 0)
      
    elif self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier1 = self.tokenizer.identifier()
      self.process(identifier1)

      if self.tokenizer.currentToken == '[':
        kind = self.subroutineSymbolTable.kindOf(identifier1)
        if kind != None:
          index = self.subroutineSymbolTable.indexOf(identifier1)
          if kind == SymbolTable.STATIC:
            self.vmwriter.writePush(VMWriter.STATIC, index)
          elif kind == SymbolTable.FIELD:
            self.vmwriter.writePush(VMWriter.THIS, index)
          elif kind == SymbolTable.VAR:
            self.vmwriter.writePush(VMWriter.LOCAL, index)
          elif kind == SymbolTable.ARG:
            self.vmwriter.writePush(VMWriter.ARGUMENT, index)
        else:
          kind = self.classSymbolTable.kindOf(identifier1)
          if kind != None:
            index = self.classSymbolTable.indexOf(identifier1)
            if kind == SymbolTable.STATIC:
              self.vmwriter.writePush(VMWriter.STATIC, index)
            elif kind == SymbolTable.FIELD:
              self.vmwriter.writePush(VMWriter.THIS, index)
            elif kind == SymbolTable.VAR:
              self.vmwriter.writePush(VMWriter.LOCAL, index)
            elif kind == SymbolTable.ARG:
              self.vmwriter.writePush(VMWriter.ARGUMENT, index)
          else:
            raise SystemExit(f"Syntax error in file {self.infile}: identifier \"{identifier1}\" is not declared.")

        self.process("[")
        self.compileExpression()
        self.process("]")

        self.vmwriter.writeArithmetic(VMWriter.ADD)

        self.vmwriter.writePop(VMWriter.POINTER, 1)
        self.vmwriter.writePush(VMWriter.THAT, 0)
      elif self.tokenizer.currentToken == '(':
        if self.currentSubroutineIsConstructor or self.currentSubroutineIsMethod:
          self.vmwriter.writePush(VMWriter.POINTER, 0)
        self.process("(")
        n = self.compileExpressionList()
        self.process(")")
        if self.currentSubroutineIsConstructor or self.currentSubroutineIsMethod:
          self.vmwriter.writeCall(f"{self.className}.{identifier1}", n+1)
        else:
          self.vmwriter.writeCall(f"{self.className}.{identifier1}", n)
      elif self.tokenizer.currentToken == '.':
        self.process(".")
        identifier2 = self.tokenizer.identifier()
        self.process(identifier2)

        kind = self.subroutineSymbolTable.kindOf(identifier1)
        if kind != None:
          index = self.subroutineSymbolTable.indexOf(identifier1)
          typeId1 = self.subroutineSymbolTable.typeOf(identifier1)
          if kind == SymbolTable.STATIC:
            self.vmwriter.writePush(VMWriter.STATIC, index)
          elif kind == SymbolTable.FIELD:
            self.vmwriter.writePush(VMWriter.THIS, index)
          elif kind == SymbolTable.VAR:
            self.vmwriter.writePush(VMWriter.LOCAL, index)
          elif kind == SymbolTable.ARG:
            self.vmwriter.writePush(VMWriter.ARGUMENT, index)

          self.process("(")
          n = self.compileExpressionList()
          self.process(")")
          self.vmwriter.writeCall(f"{typeId1}.{identifier2}", n+1)
        else:
          kind = self.classSymbolTable.kindOf(identifier1)
          if kind != None:
            index = self.classSymbolTable.indexOf(identifier1)
            typeId1 = self.classSymbolTable.typeOf(identifier1)
            if kind == SymbolTable.STATIC:
              self.vmwriter.writePush(VMWriter.STATIC, index)
            elif kind == SymbolTable.FIELD:
              self.vmwriter.writePush(VMWriter.THIS, index)
            elif kind == SymbolTable.VAR:
              self.vmwriter.writePush(VMWriter.LOCAL, index)
            elif kind == SymbolTable.ARG:
              self.vmwriter.writePush(VMWriter.ARGUMENT, index)
          
            self.process("(")
            n = self.compileExpressionList()
            self.process(")")
            self.vmwriter.writeCall(f"{typeId1}.{identifier2}", n+1)
          else:
            self.process("(")
            n = self.compileExpressionList()
            self.process(")")
            self.vmwriter.writeCall(f"{identifier1}.{identifier2}", n)

      else:
        kind = self.subroutineSymbolTable.kindOf(identifier1)
        if kind != None:
          index = self.subroutineSymbolTable.indexOf(identifier1)
          if kind == SymbolTable.STATIC:
            self.vmwriter.writePush(VMWriter.STATIC, index)
          elif kind == SymbolTable.FIELD:
            self.vmwriter.writePush(VMWriter.THIS, index)
          elif kind == SymbolTable.VAR:
            self.vmwriter.writePush(VMWriter.LOCAL, index)
          elif kind == SymbolTable.ARG:
            self.vmwriter.writePush(VMWriter.ARGUMENT, index)
        else:
          kind = self.classSymbolTable.kindOf(identifier1)
          if kind != None:
            index = self.classSymbolTable.indexOf(identifier1)
            if kind == SymbolTable.STATIC:
              self.vmwriter.writePush(VMWriter.STATIC, index)
            elif kind == SymbolTable.FIELD:
              self.vmwriter.writePush(VMWriter.THIS, index)
            elif kind == SymbolTable.VAR:
              self.vmwriter.writePush(VMWriter.LOCAL, index)
            elif kind == SymbolTable.ARG:
              self.vmwriter.writePush(VMWriter.ARGUMENT, index)
          else:
            raise SystemExit(f"Syntax error in file {self.infile}: identifier \"{identifier1}\" is not declared.")

    elif self.tokenizer.currentToken == '(':
      self.process("(")
      self.compileExpression()
      self.process(")")
    
    elif self.tokenizer.currentToken == '-' or self.tokenizer.currentToken == '~':
      symbol = self.tokenizer.symbol()
      self.process(symbol)
      self.compileTerm()
      if symbol == '-':
        self.vmwriter.writeArithmetic(VMWriter.NEG)
      elif symbol == '~':
        self.vmwriter.writeArithmetic(VMWriter.NOT)

  def compileExpressionList(self):
    numExpressions = 0
    if self.tokenizer.currentToken == ')':
      return numExpressions
    self.compileExpression()
    numExpressions += 1
    while self.tokenizer.currentToken == ',':
      self.process(",")
      self.compileExpression()
      numExpressions += 1
    return numExpressions
    
class VMWriter:
  CONSTANT = 0
  ARGUMENT = 1
  LOCAL = 2
  STATIC = 3
  THIS = 4
  THAT = 5
  POINTER = 6
  TEMP = 7

  ADD = 10
  SUB = 11
  NEG = 12
  EQ = 13
  GT = 14
  LT = 15
  AND = 16
  OR = 17
  NOT = 18

  def __init__(self, file):
    self.outfile = file
    self.labelCounter = 0

  def generateLabel(self):
    a = f"L{self.labelCounter}"
    self.labelCounter += 1
    return a

  def writePush(self, segment, index):
    if segment == VMWriter.CONSTANT:
      seg = "constant"
    elif segment == VMWriter.ARGUMENT:
      seg = "argument"
    elif segment == VMWriter.LOCAL:
      seg = "local"
    elif segment == VMWriter.STATIC:
      seg = "static"
    elif segment == VMWriter.THIS:
      seg = "this"
    elif segment == VMWriter.THAT:
      seg = "that"
    elif segment == VMWriter.POINTER:
      seg = "pointer"
    elif segment == VMWriter.TEMP:
      seg = "temp"
    print(f"  push {seg} {index}", file=self.outfile)

  def writePop(self, segment, index):
    if segment == VMWriter.ARGUMENT:
      seg = "argument"
    elif segment == VMWriter.LOCAL:
      seg = "local"
    elif segment == VMWriter.STATIC:
      seg = "static"
    elif segment == VMWriter.THIS:
      seg = "this"
    elif segment == VMWriter.THAT:
      seg = "that"
    elif segment == VMWriter.POINTER:
      seg = "pointer"
    elif segment == VMWriter.TEMP:
      seg = "temp"
    print(f"  pop {seg} {index}", file=self.outfile)

  def writeArithmetic(self, command):
    if command == VMWriter.ADD:
      cmd = "add"
    elif command == VMWriter.SUB:
      cmd = "sub"
    elif command == VMWriter.NEG:
      cmd = "neg"
    elif command == VMWriter.EQ:
      cmd = "eq"
    elif command == VMWriter.GT:
      cmd = "gt"
    elif command == VMWriter.LT:
      cmd = "lt"
    elif command == VMWriter.AND:
      cmd = "and"
    elif command == VMWriter.OR:
      cmd = "or"
    elif command == VMWriter.NOT:
      cmd = "not"
    print(f"  {cmd}", file=self.outfile)
  
  def writeLabel(self, label):
    print(f"label {label}", file=self.outfile)
  
  def writeGoto(self, label):
    print(f"  goto {label}", file=self.outfile)

  def writeIf(self, label):
    print(f"  if-goto {label}", file=self.outfile)

  def writeCall(self, name, nArgs):
    print(f"  call {name} {nArgs}", file=self.outfile)
  
  def writeFunction(self, name, nVars):
    print(f"function {name} {nVars}", file=self.outfile)

  def writeReturn(self):
    print("  return", file=self.outfile)

  def close(self):
    self.outfile.close()

class SymbolTable:
  STATIC = 0
  FIELD = 1
  ARG = 2
  VAR = 3

  def __init__(self):
    self.symbolTable = {}
    self.indexStatic = 0
    self.indexField = 0
    self.indexArg = 0
    self.indexVar = 0

  def reset(self):
    self.symbolTable.clear()
    self.indexStatic = 0
    self.indexField = 0
    self.indexArg = 0
    self.indexVar = 0

  def define(self, name, type, kind):
    r = (type, kind, )
    if kind == SymbolTable.STATIC:
      r += (self.indexStatic, )
      self.indexStatic += 1
    elif kind == SymbolTable.FIELD:
      r += (self.indexField, )
      self.indexField += 1
    elif kind == SymbolTable.ARG:
      if name == "this":
        r += (0, )
      else:
        r += (self.indexArg, )
      self.indexArg += 1
    elif kind == SymbolTable.VAR:
      r += (self.indexVar, )
      self.indexVar += 1
    self.symbolTable[name] = r

  def varCount(self, kind):
    c = 0
    for item in self.symbolTable.values():
      if item[1] == kind:
        c += 1
    return c
    
  def kindOf(self, name):
    try:
      return self.symbolTable[name][1]
    except KeyError:
      return None
  
  def typeOf(self, name):
    try:
      return self.symbolTable[name][0]
    except KeyError:
      return None
    
  def indexOf(self, name):
    try:
      return self.symbolTable[name][2]
    except KeyError:
      return None

def main(argv):
  if len(argv) != 2:
    raise SystemExit("Usage: ./JackCompiler [path/to/FileName.jack | path/to/FolderName]")
  
  if not os.path.isdir(argv[1]):
    filepath, ext = os.path.splitext(argv[1])
    if ext != '.jack':
      raise SystemExit("Error: " + filepath + " is not an jack file.")
    
    jackfilepath, jackfilename = os.path.split(filepath)
    if jackfilename[0].islower():
      raise SystemExit("Error: " + "The first character of \"" + jackfilename + "\" must be in uppercase.")
    
    outfilepath = jackfilepath + "/" + jackfilename + ".vm"

    outfilepath = Path(outfilepath)
    outfilepath.parent.mkdir(exist_ok=True, parents=True)

    outfile = open(outfilepath, "wt")

    compilationEngine = CompilationEngine(argv[1], outfile)

    compilationEngine.compileClass()
    
    compilationEngine.tokenizer.infile.close()
  else:
    dirpath = Path(argv[1])
    jackfilepaths = []
    for c in dirpath.iterdir():
      if c.suffix == '.jack':
        jackfilepaths.append(c)

    if len(jackfilepaths) == 0:
      raise SystemExit("Error: " + argv[1] + " does not contain any jack file.")

    for p in jackfilepaths:
      _, jackfilename = os.path.split(p)
      if jackfilename[0].islower():
        raise SystemExit("Error: " + "The first character of \"" + jackfilename + "\" must be in uppercase.")

    for jackfile in jackfilepaths:
      f, _ = os.path.splitext(jackfile)
      outfilepath =  f + ".vm"
      outfile = open(outfilepath, "wt")
      
      compilationEngine = CompilationEngine(jackfile, outfile)

      compilationEngine.compileClass()

      compilationEngine.tokenizer.infile.close()
    
if __name__ == '__main__':
  import sys
  main(sys.argv)