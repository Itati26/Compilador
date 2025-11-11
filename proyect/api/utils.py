from antlr4 import *
import lenguage.GrammarLexer as GrammarLexer
import lenguage.GrammarParser as GrammarParser

import io
import sys
import lenguage.MyVisitor as MyVisitor

def run_code(code:str):
    input_stream=InputStream(code)
    lexer=GrammarLexer(input_stream)
    stream=CommonTokenStream(lexer)
    parser=GrammarParser(stream)
    tree=parser.progam()

    #Capturan la salidas
    old_stdout=sys.stdout()
    buf=io.StringIO()
    sys.stdout=buf

    # Creamos un objetos de nuestro visitor
    visitor=MyVisitor()
    # Visitamos el arbol del Visitor
    visitor.visit(tree)
    # Capturamos la salida
    output=buf.getvalue()

    return output