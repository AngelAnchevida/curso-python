from collections import Counter

def count_sales(products: list[str]) -> Counter:
    #Usa counter para contar cuántos productos de cada tipo de han vendido
    return Counter(products)

sales = ['laptop', 'smartphone', 'smartphone', 'laptop', 'tablet', 'smartwatch']
result = count_sales(sales)
print(result)  # Output: Counter({'laptop': 2, 'smartphone': 2, 'tablet': 1})

c = Counter(sales)
print(c)
 
#Imprime los que se repitan más veces
print(c.most_common())