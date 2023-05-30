def sum_fibonacci_even_valued(sum_value_fibo: int = 0, previous_value: int = 0):
    sum_even_value = 0
    while sum_value_fibo < 4000000:
        if sum_value_fibo > 1:
            sum_value_fibo = sum_value_fibo + previous_value
            previous_value = sum_value_fibo - previous_value
        else:
            sum_value_fibo += 1
            previous_value = sum_value_fibo - 1

        if sum_value_fibo % 2 == 0:
            sum_even_value += sum_value_fibo

    print(sum_even_value)


sum_fibonacci_even_valued()
