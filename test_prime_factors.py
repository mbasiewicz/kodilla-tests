from prime_factors import prime_factors_result


def test_prime_factors_result():
    """sprawdza czy można zaimportować funkcję"""
    try:
        from prime_factors import prime_factors_result

        assert callable(prime_factors_result), "prime_factors_result not callable"
    except ImportError as error:
        assert False, error


def test_prime_number():
    """dla liczby pierwszej zwraca listę z tą liczbą"""
    result = prime_factors_result(2)
    assert result == [2], f"Expected [2], got {result}"


if __name__ == "__main__":
    for test in (test_prime_factors_result, test_prime_number):
        print(f"{test.__name__}: ", end="")
        try:
            test()
            print("OK")
        except AssertionError as error:
            print(error)
