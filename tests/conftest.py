'''import pytest
@pytest.fixture()
def get_prime_nums():
    prime_nums = []
    for num in range(1, 50):
        for div in range(2, num):
            if num % div == 0:
                break
        else:
            prime_nums.append(num)
    return prime_nums'''




