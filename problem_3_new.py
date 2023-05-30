def find_largest_prime_factor(search):
    cont = 3
    result = 0
    while search > 1:
        if search % cont == 0:
            for num in range(3, cont, 2):
                if cont % num == 0:
                    break
                else:
                    search = search / cont
                    result = cont
                    break
        cont += 2
    return result


number = find_largest_prime_factor(600851475143)
print(number)
