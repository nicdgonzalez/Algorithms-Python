

def decimal_to_binary(decimal: int, *, total_length: int = 0) -> str:
    """Converts a decimal value to its binary representation.

    Parameters
    -----------
    decimal: :class:`int`
        The integer value to be converted to binary.
    total_length: :class:`int`
        The desired length of the final binary sequence. If the sequence
        is shorter than the total_length, it will be prefixed with
        the required 0s. If the length of the sequence is longer than
        the total_length provided, the total_length is ignored and the entire
        sequence will be returned. Defaults to :int:`0`.

    Returns a :class:`str` of the decimal value in its binary form.
    """

    def to_binary(_decimal: int, buffer: str = '') -> str:
        buffer += str(_decimal % 2)

        return (
            buffer
            if ((_decimal // 2) == 0)
            else to_binary((_decimal // 2), buffer)
        )

    binary: str = ''.join(reversed(to_binary(decimal, '')))

    return (('0' * (total_length - len(binary))) + binary)


if __name__ == '__main__':
    print(decimal_to_binary(85, total_length=8))  # 85
    print(decimal_to_binary(15, total_length=8))  # 15
    print(decimal_to_binary(240, total_length=8))  # 240
    print(decimal_to_binary(182, total_length=8))  # 182
    print(decimal_to_binary(255, total_length=8))  # 255
