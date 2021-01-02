from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
    try:
        texto = input("Calculadora: ")
        lexer = Lexer(texto)
        tokens = lexer.generar_tokens()
        # print(list(tokens))
        parser = Parser(tokens)
        tree = parser.parse()
        print(tree)
        if not tree:
            continue
        value = Interpreter().visit(tree)
        print(value)
    except Exception as e:
        print(e)