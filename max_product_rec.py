import sys

number = sys.argv[1]
distance = int(sys.argv[2])

try:
    int(number)
except:
    raise ValueError('El primer argumento ha de ser un entero')

if distance >= len(number):
    raise ValueError('El segundo argumento no puede ser mayor que el primero')

if distance <= 0:
    raise ValueError('El segundo argumento no puede ser menor o igual a 0')

def max_product(number: str, distance: int, i: int, max_res: int):
    res = 1
    for n in number[i:i+distance]:
        res *= int(n)
    if res > max_res: 
        max_res = res
    i += 1  
    return max_product(number, distance, i, max_res) if (len(number) - i >= distance) else max_res

print(max_product(number, distance, 0, 0))

# def max_res(number: int, distance: int):
#     max_res = 0
#     for i in range(len(number) - distance + 1):
#         res = 1
#         for n in number[i:i+distance]:
#             res *= int(n)
#         if res > max_res: 
#             max_res = res
#     return max_res