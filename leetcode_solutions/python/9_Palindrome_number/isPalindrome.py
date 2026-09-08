"""
LeetCode Problem #9: Palindrome Number

Problem: Given an integer x, return true if x is a palindrome, and false otherwise.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.

Approach: Reverse only half of the number and compare it with the first half.
This avoids potential overflow issues and reduces the number of operations.

Steps:
1. Handle edge cases:
   - Negative numbers: not palindromes.
   - Numbers ending with 0 (except 0 itself): cannot be palindromes because the reverse would have a leading zero.
2. Reverse the second half of the number by repeatedly:
   - Extracting the last digit (x % 10).
   - Appending it to reversed_half (reversed_half = reversed_half * 10 + last_digit).
   - Removing the last digit from x (x //= 10).
3. Stop when x becomes less than or equal to reversed_half, meaning we have processed at least half of the digits.
4. Compare:
   - For even-length numbers: x == reversed_half
   - For odd-length numbers: x == reversed_half // 10 (to ignore the middle digit)

Time complexity: O(log10(n)) – we process roughly half the digits.
Space complexity: O(1) – only a few integer variables are used.

Note: The provided code has the return statement inside the while loop, which will cause
the function to exit after the first iteration. The correct placement should be outside the loop.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determines whether an integer is a palindrome.

        Args:
            x (int): The integer to check.

        Returns:
            bool: True if x is a palindrome, False otherwise.
        """
        # Edge case: negative numbers are not palindromes.
        # Edge case: numbers ending with 0 (except 0 itself) cannot be palindromes
        # because the reverse would have a leading zero.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Reverse the second half of the number.
        # Continue until the original number (x) becomes less than or equal to reversed_half,
        # which means we have processed at least half of the digits.
        while x > reversed_half:
            # Append the last digit of x to reversed_half.
            reversed_half = reversed_half * 10 + x % 10
            # Remove the last digit from x.
            x //= 10

            # BUG: The return statement is inside the while loop.
            # It should be outside the loop to allow the loop to complete.
            # As written, this will return after only one iteration,
            # which is incorrect for numbers with more than two digits.
            return x == reversed_half or x == reversed_half // 10                                                    return x == reversed_half or x == reversed_half // 10
