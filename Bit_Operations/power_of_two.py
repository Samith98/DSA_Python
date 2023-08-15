from typing import Type


def check_two_power(n=Type[int]) -> bool:
    """
    This function uses bitwise operation to determine if the number is a power of 2, or not.
    Performs bitwise AND operations with 1 lesser value than the number to check the bits.
    :param n: Input parameter
    :return: True, if the number is a power of 2, False if the number is not a power of 2
    """
    if n and (n & (n - 1)):
        return False
    else:
        return True


if __name__ == '__main__':
    print(check_two_power(4))
