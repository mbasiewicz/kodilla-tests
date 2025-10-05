def prime_factors_result(number):
    """funkcja rozkłada liczbę na czynniki pierwsze:
    zwraca liczbę pierwszą lub jej czynniki w tabeli"""
    factors = []
    divisor = 2

    while number != 1:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1

    return factors


print(prime_factors_result(21))
