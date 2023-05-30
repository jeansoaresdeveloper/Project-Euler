def prime_number(num: int = 3, cont: int = 1):
    while cont < 10001:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        num += 2
        if is_prime:
            cont += 1

    return num - 2


print(prime_number())
