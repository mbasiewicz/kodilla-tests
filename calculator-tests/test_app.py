import subprocess


def test_addition():
    """sprawdzenie poprawności dodawania"""
    result = subprocess.run(
        ["python", "main.py", "2", "+", "3"], stdout=subprocess.PIPE
    )
    assert result.stdout.decode("utf-8").strip() == "5"


def test_too_many_args():
    """sprawdzenie czy przyjmuje więcej niż 3 argumenty"""
    result = subprocess.run(
        ["python", "main.py", "2", "+", "3", "+", "5"], stdout=subprocess.PIPE
    )
    assert result.returncode != 0


def test_not_enough_args():
    """sprawdzenie czy przyjmuje mniej niż 3 argumenty"""
    result = subprocess.run(["python", "main.py", "2", "+"], stdout=subprocess.PIPE)
    assert result.returncode != 0


def test_no_args():
    """sprawdznie braku argumentów"""
    result = subprocess.run(["python", "main.py"], stdout=subprocess.PIPE)
    assert result.returncode != 0


def test_string_instead_int():
    """sprawdzenie czy przyjmuje string jako argument"""
    result = subprocess.run(
        ["python", "main.py", "dwa", "+", "dwa"], stdout=subprocess.PIPE
    )
    assert result.returncode != 0


def test_float_instead_int():
    """sprawdzenie czy przyjmuje float jako argument"""
    result = subprocess.run(
        ["python", "main.py", "2.5", "+", "1.5"], stdout=subprocess.PIPE
    )
    assert result.returncode != 0


def test_wrong_math_operator():
    """sprawdzenie czy przyjmuje inny operator matematyczny niż + - x /"""
    result = subprocess.run(
        ["python", "main.py", "2", "%", "2"], stdout=subprocess.PIPE
    )
    assert result.returncode != 0


def test_substraction():
    """sprawdzenie poprawności odejmowania"""
    result = subprocess.run(
        ["python", "main.py", "2", "-", "3"], stdout=subprocess.PIPE
    )
    assert result.stdout.decode("utf-8").strip() == "-1"


def test_multiplication():
    """sprawdzenie poprawności mnożenia"""
    result = subprocess.run(
        ["python", "main.py", "3", "x", "5"], stdout=subprocess.PIPE
    )
    assert result.stdout.decode("utf-8").strip() == "15"


def test_division():
    """sprawdzenie poprawności dzielenia
    BUG FOUND:
    według wymagań z readme działa tylko na INT a wynik dzielenia zwracany jest jako FLOAT
    Expected: '2'
    Actual: '2.0'"""
    result = subprocess.run(
        ["python", "main.py", "4", "/", "2"], stdout=subprocess.PIPE
    )
    assert result.stdout.decode("utf-8").strip() == "2"


# PRZYPADKI Z ZEREM W DZIAŁANIU


def test_addition_with_zero():
    """sprawdzenie dodawania z zerem"""
    result = subprocess.run(
        ["python", "main.py", "0", "+", "2"], stdout=subprocess.PIPE
    )
    assert result.stdout.decode("utf-8").strip() == "2"


def test_multiplication_by_zero():
    """sprawdzenie mnożenia przez zero"""
    result = subprocess.run(
        ["python", "main.py", "5", "x", "0"], stdout=subprocess.PIPE
    )
    assert result.stdout.decode("utf-8").strip() == "0"


def test_substraction_with_zero():
    """sprawdzenie odejmowania z zerem"""
    result = subprocess.run(
        ["python", "main.py", "2", "-", "0"], stdout=subprocess.PIPE
    )
    assert result.stdout.decode("utf-8").strip() == "2"


def test_zero_minus_number():
    """sprawdzenie odejmowania od zera"""
    result = subprocess.run(
        ["python", "main.py", "0", "-", "2"], stdout=subprocess.PIPE
    )
    assert result.stdout.decode("utf-8").strip() == "-2"


def test_division_by_zero():
    """sprawdzenie dzielenia przez 0"""
    result = subprocess.run(
        ["python", "main.py", "3", "/", "0"], stdout=subprocess.PIPE
    )
    assert result.returncode != 0
