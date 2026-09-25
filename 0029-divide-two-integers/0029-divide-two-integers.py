class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        result = 0

        while a >= b:
            shift = a.bit_length() - b.bit_length()

            if a < (b << shift):
                shift -= 1

            result += 1 << shift
            a -= b << shift

        return -result if negative else result