class Counter:
    count = 0

    @classmethod
    def increment(cls):
        #Se puede modificar una variable de una clase usandola como atributo
        #Para eso sirve @classmethod
        cls.count += 1

Counter.increment()
Counter.increment()

print(Counter.count)