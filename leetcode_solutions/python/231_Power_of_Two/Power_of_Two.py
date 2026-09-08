"""
LeetCode Problem #231: Power of Two

Problem: Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two if there exists an integer x such that n == 2^x.

Examples:
    Input: n = 1   -> Output: true  (2^0 = 1)
    Input: n = 16  -> Output: true  (2^4 = 16)
    Input: n = 3   -> Output: false

Approach (bit manipulation):
    A power of two in binary has exactly one bit set to 1, and all other bits are 0.
    For a positive integer n, performing n & (n - 1) clears the lowest set bit.
    If n is a power of two, it has only one set bit, so clearing it results in 0.
    Therefore, the condition `n > 0 and (n & (n - 1)) == 0` correctly identifies powers of two.

Time complexity: O(1) - constant time bitwise operation.
Space complexity: O(1) - no extra space used.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Determines whether the given integer is a power of two.

        Args:
            n (int): The input integer.

        Returns:
            bool: True if n is a power of two, False otherwise.

        Note:
            - n must be strictly positive (n > 0); zero and negative numbers are not powers of two.
            - The expression `n & (n - 1)` clears the least significant 1-bit.
              For a power of two, this yields 0 because there is only one 1-bit.
        """
        # Check that n is positive and that clearing its lowest set bit results in zero.
        return n > 0 and (n & (n - 1)) == 0
