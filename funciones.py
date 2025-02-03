def greet(name, lastname="No tiene apellido"):
    #En caso de que no le pasemos un valor al llamar a la función podemos
    #dejarle un valor predeterminado
    print("Hola", name, lastname)

#Siempre hay que mandar a llamar a la funcion
greet("angel", "Anchevida")


#Si la funcion espera algo siempre hay que llamarla dandole un valor
greet("Diego")


#Tambien se puede ejecutar una funcion dandole de manera especifica los valores
greet(lastname="Anchevida", name="Angel")




