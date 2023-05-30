def smallest_number():
    result = False
    cont = 20
    while not result:
        print(result)
        print("Valor cont " + str(cont))
        result = True
        for num in range(1, 20):
            if cont % num != 0:
                result = False
                break

        cont += 20
    return cont - 20


print(smallest_number())


