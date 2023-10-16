# Bitwise AND
result_and = 5 & 3  # Result: 1 (binary 0101 & 0011)

# Bitwise OR
result_or = 5 | 3   # Result: 7 (binary 0101 | 0011)

# Bitwise XOR
result_xor = 5 ^ 3  # Result: 6 (binary 0101 ^ 0011)

# Bitwise NOT
result_not = ~5     # Result: -6 (binary ~0101)

# Left Shift
result_left_shift = 5 << 2  # Result: 20 (binary 0101 << 2)

# Right Shift
result_right_shift = 16 >> 2  # Result: 4 (binary 10000 >> 2)

# Set a bit at a specific position


def set_bit(num, position):
    return num | (1 << position)

# Clear a bit at a specific position


def clear_bit(num, position):
    return num & ~(1 << position)

# Check if a bit is set at a specific position


def is_bit_set(num, position):
    return (num & (1 << position)) != 0


def count_set_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count


def find_missing_number(nums):
    n = len(nums)
    missing = n
    for i in range(n):
        missing ^= i ^ nums[i]
    return missing
