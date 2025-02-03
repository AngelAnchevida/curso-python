#Leer un archivo linea por linea
with open('manejo_archivos\cuento.txt', 'r') as file:
    #Si estan en la misma ruta podemos hacer referencia al archivo simplemente poniendo el nombre
    for lineas in file:
        print(lineas.strip())
        #Strip elimina los espacios y saltos de linea, lo hace más legibles


#Leer todas las lineas en una lista
with open('manejo_archivos\cuento.txt', 'r') as file:
    lines = file.readlines()
    #Crea una lista con todas las lineas del texto
    print(lines)


#Añadir texto
with open('manejo_archivos\cuento.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")

#Sobreescribir el texto
with open('manejo_archivos\cuento.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")


#Leer el número de lineas en una lista
with open('manejo_archivos\cuento.txt', 'r') as file:
    lines = file.readlines()
    #Crea una lista con todas las lineas del texto
    print(len(lines))