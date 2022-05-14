

def binary_to_decimal(binary: str) -> int:
    """Converts a binary string to its decimal representation.

    Parameters
    -----------
    binary: :class:`str`
        A sequence of 0s and 1s to be converted.

    Returns an :class:`int` representing the decimal value of a binary string.
    """

    result: int = 0
    for (index, value) in enumerate(reversed(binary)):
        result += (int(value) * (2 ** index))

    return result


if __name__ == '__main__':
    print(binary_to_decimal('01010101'))  # 85
    print(binary_to_decimal('11110000'))  # 240
    print(binary_to_decimal('00001111'))  # 15
    print(binary_to_decimal('10110110'))  # 182
    print(binary_to_decimal('11111111'))  # 255
