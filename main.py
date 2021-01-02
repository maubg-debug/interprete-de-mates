from src import resolver

while True:
    try:
        texto = input("Calculadora: ")
        resolver(texto)
    except Exception as e:
        print(e)