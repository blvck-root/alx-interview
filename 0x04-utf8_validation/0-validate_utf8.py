def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing the byte sequence.

    Returns:
        True if the data is a valid UTF-8 encoding, False otherwise.
    """

    def check_continuation_bytes(n):
        """Checks for valid continuation bytes.

        Args:
            n: The number of continuation bytes to check.

        Returns:
            True if all bytes are valid continuation bytes, False otherwise.
        """
        for _ in range(n):
            byte = data.pop(0)
            if not (0b10000000 <= byte <= 0b10111111):
                return False
        return True

    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            # Check for starting byte
            if byte & 0b11100000 == 0b11000000:
                num_bytes = 2
            elif byte & 0b11110000 == 0b11100000:
                num_bytes = 3
            elif byte & 0b11111000 == 0b11110000:
                num_bytes = 4
            elif byte & 0b10000000 == 0b00000000:
                # Single-byte character
                continue
            else:
                return False
        else:
            # Check for continuation bytes
            if not check_continuation_bytes(num_bytes - 1):
                return False
            num_bytes -= 1
    return num_bytes == 0
