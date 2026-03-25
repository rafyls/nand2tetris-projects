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

  def process(self, str):
    if self.tokenizer.currentToken == str:
      if self.tokenizer.tokenType() == JackTokenizer.KEYWORD:
        print("  <keyword> ", file=self.outfile, end='')
        print(self.tokenizer.currentToken, file=self.outfile, end='')
        print(" </keyword>", file=self.outfile)
      elif self.tokenizer.tokenType() == JackTokenizer.SYMBOL:
        print("  <symbol> ", file=self.outfile, end='')
        if self.tokenizer.currentToken == '<':
          print("&lt;", file=self.outfile, end='')
        elif self.tokenizer.currentToken == '>':
          print("&gt;", file=self.outfile, end='')
        elif self.tokenizer.currentToken == '&':
          print("&amp;", file=self.outfile, end='')
        else:
          print(self.tokenizer.currentToken, file=self.outfile, end='')
        print(" </symbol>", file=self.outfile)
      elif self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
        print("  <identifier> ", file=self.outfile, end='')
        print(self.tokenizer.currentToken, file=self.outfile, end='')
        print(" </identifier>", file=self.outfile)
      elif self.tokenizer.tokenType() == JackTokenizer.INT_CONST:
        print("  <integerConstant> ", file=self.outfile, end='')
        print(self.tokenizer.currentToken, file=self.outfile, end='')
        print(" </integerConstant>", file=self.outfile)
      elif self.tokenizer.tokenType() == JackTokenizer.STRING_CONST:
        print("  <stringConstant> ", file=self.outfile, end='')
        print(self.tokenizer.currentToken, file=self.outfile, end='')
        print(" </stringConstant>", file=self.outfile)
    else:
      print(f"In file {self.infile}: Syntax Error - Unexpected token: {str}")
    if self.tokenizer.hasMoreTokens():
      self.tokenizer.advance()

  def compileClass(self):
    print("<class>", file=self.outfile)
    self.process("class")
    if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)
    self.process("{")
    while self.tokenizer.currentToken == 'static' or self.tokenizer.currentToken == 'field':
      self.compileClassVarDec()
    while self.tokenizer.currentToken == 'constructor' or self.tokenizer.currentToken == 'function' or self.tokenizer.currentToken == 'method':
      self.compileSubroutine()
    self.process("}")
    print("</class>", file=self.outfile)

  def compileClassVarDec(self):
    print("<classVarDec>", file=self.outfile)
    keyword = self.tokenizer.keyword()
    self.process(keyword)
    if self.tokenizer.currentToken == 'int' or self.tokenizer.currentToken == 'char' or self.tokenizer.currentToken == 'boolean':
      keyword = self.tokenizer.keyword()
      self.process(keyword)
    elif self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)
    if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)
    while self.tokenizer.currentToken == ',':
      symbol = self.tokenizer.symbol()
      self.process(symbol)
      if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
        identifier = self.tokenizer.identifier()
        self.process(identifier)
    self.process(";")
    print("</classVarDec>", file=self.outfile)

  def compileSubroutine(self):
    print("<subroutineDec>", file=self.outfile)
    keyword = self.tokenizer.keyword()
    self.process(keyword)
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
    self.process('(')
    self.compileParameterList()
    self.process(')')
    self.compileSubroutineBody()
    print("</subroutineDec>", file=self.outfile)

  def compileParameterList(self):
    print("<parameterList>", file=self.outfile)
    if self.tokenizer.currentToken == 'int' or self.tokenizer.currentToken == 'char' or self.tokenizer.currentToken == 'boolean':
      keyword = self.tokenizer.keyword()
      self.process(keyword)
    elif self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)
    if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)
    while self.tokenizer.currentToken == ',':
      symbol = self.tokenizer.symbol()
      self.process(symbol)
      if self.tokenizer.currentToken == 'int' or self.tokenizer.currentToken == 'char' or self.tokenizer.currentToken == 'boolean':
        keyword = self.tokenizer.keyword()
        self.process(keyword)
      elif self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
        identifier = self.tokenizer.identifier()
        self.process(identifier)
      if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
        identifier = self.tokenizer.identifier()
        self.process(identifier)
    print("</parameterList>", file=self.outfile)
  
  def compileSubroutineBody(self):
    print("<subroutineBody>", file=self.outfile)
    self.process("{")
    while self.tokenizer.currentToken == 'var':
      self.compileVarDec()
    self.compileStatements()
    self.process("}")
    print("</subroutineBody>", file=self.outfile)

  def compileVarDec(self):
    print("<varDec>", file=self.outfile)
    keyword = self.tokenizer.keyword()
    self.process(keyword)
    if self.tokenizer.currentToken == 'int' or self.tokenizer.currentToken == 'char' or self.tokenizer.currentToken == 'boolean':
      keyword = self.tokenizer.keyword()
      self.process(keyword)
    elif self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)
    if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)
    while self.tokenizer.currentToken == ',':
      symbol = self.tokenizer.symbol()
      self.process(symbol)
      if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
        identifier = self.tokenizer.identifier()
        self.process(identifier)
    self.process(";")
    print("</varDec>", file=self.outfile)
  
  def compileStatements(self):
    print("<statements>", file=self.outfile)
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
    print("</statements>", file=self.outfile)

  def compileLet(self):
    print("<letStatement>", file=self.outfile)
    keyword = self.tokenizer.keyword()
    self.process(keyword)
    if self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)
    if self.tokenizer.currentToken == '[':
      self.process("[")
      self.compileExpression()
      self.process("]")
    self.process("=")
    self.compileExpression()
    self.process(";")
    print("</letStatement>", file=self.outfile)

  def compileIf(self):
    print("<ifStatement>", file=self.outfile)
    keyword = self.tokenizer.keyword()
    self.process(keyword)
    self.process("(")
    self.compileExpression()
    self.process(")")
    self.process("{")
    self.compileStatements()
    self.process("}")
    if self.tokenizer.currentToken == 'else':
      keyword = self.tokenizer.keyword()
      self.process(keyword)
      self.process("{")
      self.compileStatements()
      self.process("}")
    print("</ifStatement>", file=self.outfile)

  def compileWhile(self):
    print("<whileStatement>", file=self.outfile)
    keyword = self.tokenizer.keyword()
    self.process(keyword)
    self.process("(")
    self.compileExpression()
    self.process(")")
    self.process("{")
    self.compileStatements()
    self.process("}")
    print("</whileStatement>", file=self.outfile)

  def compileDo(self):
    print("<doStatement>", file=self.outfile)
    keyword = self.tokenizer.keyword()
    self.process(keyword)
    identifier = self.tokenizer.identifier()
    self.process(identifier)
    if self.tokenizer.currentToken == '(':
      self.process("(")
      self.compileExpressionList()
      self.process(")")
    elif self.tokenizer.currentToken == '.':
      self.process(".")
      identifier = self.tokenizer.identifier()
      self.process(identifier)
      self.process("(")
      self.compileExpressionList()
      self.process(")")
    self.process(";")
    print("</doStatement>", file=self.outfile)

  def compileReturn(self):
    print("<returnStatement>", file=self.outfile)
    keyword = self.tokenizer.keyword()
    self.process(keyword)
    if self.tokenizer.currentToken != ";":
      self.compileExpression()
    self.process(";")
    print("</returnStatement>", file=self.outfile)

  def compileExpression(self):
    print("<expression>", file=self.outfile)
    self.compileTerm()
    while self.tokenizer.currentToken == '+' or self.tokenizer.currentToken == '-' or self.tokenizer.currentToken == '*' or self.tokenizer.currentToken == '/' or self.tokenizer.currentToken == '&' or self.tokenizer.currentToken == '|' or self.tokenizer.currentToken == '<' or self.tokenizer.currentToken == '>' or self.tokenizer.currentToken == '=':
      symbol = self.tokenizer.symbol()
      self.process(symbol)
      self.compileTerm()
    print("</expression>", file=self.outfile)

  def compileTerm(self):
    print("<term>", file=self.outfile)
    if self.tokenizer.tokenType() == JackTokenizer.INT_CONST:
      intConstant = self.tokenizer.intVal()
      self.process(str(intConstant))
    elif self.tokenizer.tokenType() == JackTokenizer.STRING_CONST:
      stringConstant = self.tokenizer.stringVal()
      self.process(stringConstant)
    elif self.tokenizer.currentToken == 'true' or self.tokenizer.currentToken == 'false' or self.tokenizer.currentToken == 'null' or self.tokenizer.currentToken == 'this':
      keyword = self.tokenizer.keyword()
      self.process(keyword)
    elif self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
      identifier = self.tokenizer.identifier()
      self.process(identifier)
      if self.tokenizer.currentToken == '[':
        self.process("[")
        self.compileExpression()
        self.process("]")
      elif self.tokenizer.currentToken == '(':
        self.process("(")
        self.compileExpressionList()
        self.process(")")
      elif self.tokenizer.currentToken == '.':
        self.process(".")
        identifier = self.tokenizer.identifier()
        self.process(identifier)
        self.process("(")
        self.compileExpressionList()
        self.process(")")
    elif self.tokenizer.currentToken == '(':
      self.process("(")
      self.compileExpression()
      self.process(")")
    elif self.tokenizer.currentToken == '-' or self.tokenizer.currentToken == '~':
      symbol = self.tokenizer.symbol()
      self.process(symbol)
      self.compileTerm()
    print("</term>", file=self.outfile)

  def compileExpressionList(self):
    print("<expressionList>", file=self.outfile)
    numExpressions = 0
    if self.tokenizer.currentToken == ')':
      print("</expressionList>", file=self.outfile)
      return numExpressions
    self.compileExpression()
    numExpressions += 1
    while self.tokenizer.currentToken == ',':
      self.process(",")
      self.compileExpression()
      numExpressions += 1
    print("</expressionList>", file=self.outfile)
    return numExpressions

def main(argv):
  if len(argv) != 2:
    raise SystemExit("Usage: ./JackAnalyzer [path/to/FileName.jack | path/to/FolderName]")
  
  if not os.path.isdir(argv[1]):
    filepath, ext = os.path.splitext(argv[1])
    if ext != '.jack':
      raise SystemExit("Error: " + filepath + " is not an jack file.")
    
    jackfilepath, jackfilename = os.path.split(filepath)
    if jackfilename[0].islower():
      raise SystemExit("Error: " + "The first character of \"" + jackfilename + "\" must be in uppercase.")
    
    outfilepath = jackfilepath + "/" + jackfilename + "Parsed.xml"

    outfilepath = Path(outfilepath)
    outfilepath.parent.mkdir(exist_ok=True, parents=True)

    outfile = open(outfilepath, "wt")

    compilationEngine = CompilationEngine(argv[1], outfile)

    compilationEngine.compileClass()
    
    compilationEngine.tokenizer.infile.close()
    outfile.close()
  else:
    dirpath = Path(argv[1])
    jackfilepaths = []
    for c in dirpath.iterdir():
      if c.suffix == '.jack':
        jackfilepaths.append(c)

    if len(jackfilepaths) == 0:
      raise SystemExit("Error: " + argv[1] + " does not contain any .jack file.")

    for p in jackfilepaths:
      _, jackfilename = os.path.split(p)
      if jackfilename[0].islower():
        raise SystemExit("Error: " + "The first character of \"" + jackfilename + "\" must be in uppercase.")

    for jackfile in jackfilepaths:
      f, _ = os.path.splitext(jackfile)
      outfilepath =  f + "Parsed.xml"
      outfile = open(outfilepath, "wt")
      
      compilationEngine = CompilationEngine(jackfile, outfile)

      compilationEngine.compileClass()

      outfile.close()
      compilationEngine.tokenizer.infile.close()
    
if __name__ == '__main__':
  import sys
  main(sys.argv)