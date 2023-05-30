def multiples_3_and_5(sum: int = 0, cont: int = 1000):
    for number in range(cont):
        if number % 3 == 0 or number % 5 == 0:
            sum += number
            print("Sum: " + str(sum) + ", Number: " + str(number))

    return sum


print(multiples_3_and_5())