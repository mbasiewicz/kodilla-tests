def prime_factors(number):
    """Funkcja rozkłada podaną liczbę na czynniki
    Args:
        number: dane wejściowe do funkcji (INT)
    Returns:
        list: lista z wypisanymi czynnikami
    Raises:
        TypeError: number nie jest INT
        ValueError: number jest <0 lub =0 lub =1"""
    # weryfikacja czy jest intem"
    if not isinstance(number, int):
        raise TypeError("błędny typ danych, oczekiwano int")
    if number < 2:
        raise ValueError("błędna wartość")


test_cases = {
    # liczby pierwsze
    2: [2],
    13: [13],
    73: [73],
    # liczby złożone
    4: [2, 2],
    6: [2, 3],
    12: [2, 2, 3],
    100: [2, 2, 5, 5],
    # błędne typy danych (TypeError)
    3.5: TypeError,
    "dwa": TypeError,
    (10, 20): TypeError,
    # błędne wartości (ValueError)
    0: ValueError,
    1: ValueError,
    -1: ValueError,
}


passed = 0
for number, expect_result in test_cases.items():
    if isinstance(expect_result, type) and issubclass(expect_result, Exception):
        try:
            result = prime_factors(number)
            print(f"test FAIL - {number!r} nie rzucił błędu")
        except (TypeError, ValueError):
            print(f"test OK - {number!r}")
            passed += 1
    else:
        result = prime_factors(number)
        if result == expect_result:
            print(f"test OK - {number!r}")
            passed += 1
        else:
            print(f"test FAIL - {number!r}")

print(f"Z {len(test_cases)} testów, {passed} pozytywnych")
