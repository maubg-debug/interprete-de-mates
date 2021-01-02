from lexer import Lexer
from parser_ import Parser

while True:
    texto = input("Calculadora: ")
    lexer = Lexer(texto)
    tokens = lexer.generar_tokens()
    # print(list(tokens))
    parser = Parser(tokens)
    tree = parser.parse()
    print(tree)