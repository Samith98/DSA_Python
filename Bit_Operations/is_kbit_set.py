from typing import Type


def is_kbit_set(n: int, k: int) -> bool:
    """
    This functions check if the kth bit of the number 'n' is set or not, i.e., if kth bit of 'n' is '1' or '0'.
    :param n: Number for which the bit check must be performed or not
    :param k: Bit position oto be checked
    :return: True, if kth bit is SET. False if kth bit is NOT SET
    """
    temp = 1 << (k - 1)
    if n & temp:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_kbit_set(79, 3))
