from src.lexer import Lexer
from src.parser_ import Parser
from src.interpreter import Interpreter

def resolver(texto):
    lexer = Lexer(texto)
    tokens = lexer.generar_tokens()
    # print(list(tokens)) # TOKENS
    parser = Parser(tokens)
    tree = parser.parse()
    # print(tree) # Arbol
    if not tree:
        return
    value = Interpreter().visit(tree)
    print(value)