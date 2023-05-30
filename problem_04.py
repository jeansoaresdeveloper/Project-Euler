def find_palindrome():
    factor_1 = 999
    factor_2 = 999
    maior = 0
    while factor_1 > 100:
        for num in range(factor_2, 99, - 1):
            result = factor_1 * num
            result_str = str(result)
            if result_str == result_str[::-1]:
                if result > maior:
                    print(str(factor_1) + " * " + str(num) + " = " + result_str + ", Maior: " + str(maior))
                    maior = result
        factor_1 -= 1

    return maior


print(find_palindrome())
