def dif_sum_of_the_squares(sum_square: int = 0, square_sum: int = 0):
    for i in range(1, 101):
        sum_square += i ** 2
        square_sum += i

    square_sum *= square_sum
    return square_sum - sum_square


result = dif_sum_of_the_squares()
print(result)
