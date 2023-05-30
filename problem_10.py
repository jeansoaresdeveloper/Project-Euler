def sum_primes(prime: int = 3):
    list_prime = [2]
    while prime < 2000000:
        is_Prime = True
        for i in list_prime:
            rest = prime % i
            if rest < i:
                if rest == 0:
                    is_Prime = False
                    break

        if is_Prime:
            print(prime)
            list_prime.append(prime)

        prime += 2

    return sum(list_prime)


print(sum_primes())
