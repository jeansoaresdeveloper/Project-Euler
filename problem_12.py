import math
import timeit


def first_triangle_number(num: int):
    triangle_number = 0
    cont = 1
    divisors = 1
    while True:
        for i in range(1, int(math.sqrt(triangle_number))):
            if triangle_number % i == 0:
                divisors += 1 if triangle_number / i == i else 2

        if divisors > num:
            return triangle_number

        triangle_number = triangle_number + cont
        cont += 1
        divisors = 1


inicio = timeit.default_timer()
result = first_triangle_number(500)
print(result)
fim = timeit.default_timer()
print('duracao: %f' % (fim - inicio))

