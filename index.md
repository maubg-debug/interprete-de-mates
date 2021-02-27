# interprete-de-mates
 Un  robot que te resuelve 1 + 2

![img](https://raw.githubusercontent.com/maubg-debug/interprete-de-mates/main/img/img1.png)

# ¿Como funciona?

* Ejemplo (`1 + 2 * 6`)

* Primero creamos un generador con los tokens.
    * Y nos devolveria los tipos de los tokens gracias al `lexer`
    ```
    Calculadora: 1 + 2 * 6
    [NUMBER:1.0, PLUS, NUMBER:2.0, MULTIPLY, NUMBER:6.0]
    ```

* Luego el `parser` nos devuelve un arbol
    ```
    Calculadora: 1 + 2 * 6
    (2.0+5.0)
    ```

* Por ultimo nos da el resultado
    ```
    Calculadora: 1 + 2 * 6
    7.0
    ```

# ¿Para que sirve esto?

* Esto es un ejemplo muy basico para la gente que quiera aprender a como hacer un lenguage de programaciones
* Tambien para ver como los ordenadores traducen la data
* Y de mas

# Mas cosas
* Esta maquina respeta las reglas de BIDMAS (BODMAS)
    * Puedes poner parentesis `()` para que el interprete aga primero esa expresion
* No da un error si intentas dividir por 0
    * EJ: `1 / 0`
* Tokens `+ - NUMEROS / * ( )`

# TODO:
* Algebra
