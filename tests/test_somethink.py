import requests

rom configuration import SERVICE_URL
def test_getting_post():
    response = requests.get(url=SERVICE_URL)

'''test_example.py
def test_addition():
 assert 1 + 1 == 2

def test_subtraction():
    result = 5 - 3
    assert result == 2, f"Expected 2, but got {result}" '''


'''import pytest

@pytest.mark.smoke
def test_smoke_example():
    assert True

@pytest.mark.integration
def test_integration_example():
    assert True'''


'''import pytest

@pytest.mark.parametrize("input_data, expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_parametrized_example(input_data, expected):
    result = input_data * 2
    assert result == expected'''

'''# Код, который требуется протестировать
def add(a, b):
    return a + b

# Тесты для функции add
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_mixed_numbers():
    assert add(2, -3) == -1 '''


'''class Calculator:
    def add(self, a, b):
        return a + b

# Тесты для класса Calculator
def test_calculator_add_positive_numbers():
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5, f"Expected 5, but got {result}"

def test_calculator_add_negative_numbers():
    calc = Calculator()
    result = calc.add(-2, -3)
    assert result == -5, f"Expected -5, but got {result}"'''



'''import pytest

# Код, который требуется протестировать
def process_data(data):
    # Логика обработки данных
    return data.upper()

# Фикстура для создания тестовых данных
@pytest.fixture
def test_data():
    return "test data"

# Тест с использованием фикстуры
def test_process_data_with_fixture(test_data):
    result = process_data(test_data)
    assert result == "TEST DATA"'''



'''# прибавляет 2 к каждому элементу коллекции
def plus2(nums):
    result = []
    for num in nums:
        result.append(num + 2)
    return result

# умножает на 2 каждый элемент коллекции
def multiply2(nums):
    result = []
    for num in nums:
        result.append(num * 2)
    return result

# возводит в степень 2 каждый элемент коллекции
def exponent2(nums):
    result = []
    for num in nums:
        result.append(num ** 2)
    return result'''







