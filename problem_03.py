def find_largest_prime_factor(search):
    rest = search
    cont = 3
    for cont in range(cont, search, 2):
        if rest % cont == 0:
            for num in range(2, cont):
                if cont % num == 0:
                    break
                else:
                    rest = rest / cont
                    result = cont
                    if rest == 1:
                        return result
                    break


number = find_largest_prime_factor(600851475143)
print(number)