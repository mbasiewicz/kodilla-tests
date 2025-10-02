def is_palindrome(data):
    """funkcja sprawdza czy podane słowo jest palindromem
    Args:
        data: dane wejściowe do funkcji
    Returns:
        bool: True jeśli jest palindromem, False jeśli nie
    Raises:
        TypeError: data nie jest stringiem
        ValueError: data jest pustym stringiem"""

    # weryfikacja czy jest stringiem
    if not isinstance(data, str):
        raise TypeError("błędny typ danych, oczekiwano str")

    # obsługa pustego stringa
    if data == "":
        raise ValueError("pusty string")

    # normalizacja dostarczonego stringa, usunięcie spacji i znaków specjalnych
    normalized = "".join(char.lower() for char in data if char.isalnum())
    if normalized == "":
        raise ValueError("Brak znaków alfanumerycznych")
    if normalized == normalized[::-1]:
        return True
    else:
        return False


test_cases = {
    "kajak": True,
    "Kajak": True,
    "abc": False,
    "alla": True,
    "ala ala": True,
    "al.a.ala": True,
    123: TypeError,
    123.321: TypeError,
    ("a", "b"): TypeError,
    "": ValueError,
    ".!.": ValueError,
}

passed = 0
for word, expect_result in test_cases.items():
    if isinstance(expect_result, type) and issubclass(expect_result, Exception):
        try:
            result = is_palindrome(word)
            print(f"test FAIL - {word!r} nie rzucił błędu")
        except (TypeError, ValueError):
            print(f"test OK - {word!r}")
            passed += 1
    else:
        result = is_palindrome(word)
        if result == expect_result:
            print(f"test OK - {word!r}")
            passed += 1
        else:
            print(f"test FAIL - {word!r}")

print(f"Z {len(test_cases)} testów, {passed} pozytywnych")
