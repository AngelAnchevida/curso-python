# Uso de la coma en print
# La coma dentro de la función print se usa para separar varios argumentos. Al hacerlo, Python añade automáticamente un espacio entre los argumentos. Esto es diferente a concatenar cadenas con el operador +, que no añade espacios adicionales.

# print("Nunca", "pares", "de", "aprender")

# Por otro lado, al concatenar cadenas con el operador +, los elementos se unen sin ningún espacio adicional, a menos que lo añadas explícitamente.

# print("Nunca" + "pares" + "de" + "aprender")
# Resultado:

# Nuncaparesdeaprender

# Para añadir un espacio explícitamente cuando concatenas cadenas, debes incluirlo dentro de las comillas.

# print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")
# Resultado:

# Nunca pares de aprender

# Uso de sep
# El parámetro sep permite especificar cómo separar los elementos al imprimir. En este ejemplo, los elementos “Nunca”, “pares”, “de” y “aprender” se imprimirán con una coma y un espacio entre ellos, resultando en “Nunca, pares, de, aprender”. Puedes cambiar sep por cualquier cadena de caracteres que desees usar como separador.

# print("Nunca", "pares", "de", "aprender", sep=", ")
# Resultado:

# Nunca, pares, de, aprender

# Uso de end
# El parámetro end cambia lo que se imprime al final de la llamada a print. En lugar de imprimir cada mensaje en una nueva línea, end="" asegura que “Nunca” y “pares” se impriman en la misma línea, resultando en “Nunca pares”. Por defecto, end es un salto de línea ("\n"), lo que hace que cada llamada a print comience en una nueva línea.

# print("Nunca", end=" ")
# print("pares de aprender")
# Resultado:

# Nunca pares de aprender



# Impresión de variables
# Puedes usar print para mostrar el valor de las variables. En este ejemplo, imprimirá “Frase: Nunca pares de aprender” y “Autor: Platzi”. Esto es útil para depurar y ver los valores de las variables en diferentes puntos de tu programa.

# frase = "Nunca pares de aprender"
# author = "Platzi"
# print("Frase:", frase, "Autor:", author)
# Resultado:

# Frase: Nunca pares de aprender Autor: Platzi

# Uso de formato con f-strings

# Este uso de strings nos sirve para usar cualquier variable en una cadena de strings poniendo una f al inicio de la cadena y usando las llaves {} para poner una variable dentro 

# frase = "Nunca pares de aprender"
# author = "Platzi"
# print(f"Frase: {frase}, Autor: {author}")
# Resultado:

# Frase: Nunca pares de aprender, Autor: Platzi


# Uso de formato con format
# El método format permite usar el contenido de una variable en una cadena. 
# El punto .format que sigue después de una cadena está compuesto por la variables de las que se va a tomar el contenido y ponerlo en las llaves {}, estas se representan en las llaves de la cadena y van en orden.

# frase = "Nunca pares de aprender"
# author = "Platzi"
# print("Frase: {}, Autor: {}".format(frase, author))
# Resultado:

# Frase: Nunca pares de aprender, Autor: Platzi

# Impresión con formato específico
# Sirve para darle un formato a los números, una variable que tenga 10 decimales se le puede aplicar de esta manera:

# valor = 3.14159
# print("Valor: {:.2f}".format(valor))
# Resultado:

# Valor: 3.14

# Saltos de línea y caracteres especiales
# Los saltos de línea en Python se indican con la secuencia de escape \n. Por ejemplo, para imprimir “Hola\nmundo”, que aparecerá en dos líneas:

# print("Hola\nmundo")
# Resultado:

# Hola
# mundo
# Para imprimir comillas doble o simples dentro de una cadena se debe hacer de la siguiente manera

# print('Hola soy \'Angel\'')
# Resultado:

# Hola soy 'Angeli'
# Para imprimir una ruta de un archivo necesitas poner una barra extra a la ruta para que se imprima correctamente.

# print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")
# Resultado:
# La ruta de archivo es: C:\Users\Usuario\Desktop\archivo.txt

# En Python, estas secuencias de escape te permiten manejar caracteres especiales y estructurar la salida de texto según sea necesario, asegurando que la salida se formatee correctamente en la consola o en cualquier otro medio donde se imprima.
