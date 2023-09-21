
def max_product(number: str, distance: str):
    try:
        int(number)
        distance = int(distance)
    except:
        raise ValueError('Los argumentos han de ser numéricos')
    if distance >= len(number):
        raise ValueError('El segundo argumento no puede ser mayor que el primero')
    if distance <= 0:
        raise ValueError('El segundo argumento no puede ser menor o igual a 0')
    
    max_res = 0
    for i in range(len(number) - distance + 1):
        res = 1
        for n in number[i:i+distance]:
            res *= int(n)
        if res > max_res: 
            max_res = res
    return max_res


# acepta la distancia como entero
print(max_product('2357898', 3)) 

# print(max_product('2357898', '3'))
# print(max_product('23578985', '3'))
# print(max_product('2357898', '15'))
# print(max_product('2357898', 'a'))
# print(max_product('23578b98', '5'))
# print(max_product(2357898, '3'))
# print(max_product(2357898, 3))