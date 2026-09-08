"""
LeetCode Problem #258: Add Digits

Problem: Given an integer num, repeatedly add all its digits until the result has only
one digit, and return it.
For example, 38 -> 3 + 8 = 11 -> 1 + 1 = 2, so the answer is 2.

This is a classic coding challenge that tests understanding of loops and number manipulation.

Approach (as implemented):
- Take the absolute value of the input number to handle negative values gracefully.
- Convert the number to a string to easily check the number of digits.
- If the number already has one digit, return it.
- Otherwise, enter a loop that repeatedly:
    - Extracts the last digit (`num % 10`) and the remaining part (`num // 10`).
    - Sums them and assigns the result to `total`.
    - Updates `num` with this sum and updates the string representation.
    - The loop is intended to continue until the number becomes a single digit.

Note on the algorithm: Summing the last digit with the remaining integer part is
equivalent to summing all digits in stages, and it does converge to the digital root.
However, this implementation is not the most efficient; a constant-time solution exists
using the digital root formula (num == 0 ? 0 : 1 + (num - 1) % 9).

Bug alert: The `return total` statement is placed inside the `while` loop. This causes
the function to exit after the first iteration, always returning the sum of the last
digit and the rest of the number, rather than repeating until a single digit remains.
The correct placement would be outside the loop.

Time complexity (intended): O(log10(num)) – number of iterations proportional to digit count.
Space complexity: O(log10(num)) – due to string conversion for digit count.
"""

class Solution:
    def addDigits(self, num):
        """
        Reduces an integer to a single digit by repeatedly summing its digits.

        Args:
            num (int): The input integer (negative values are converted to positive).

        Returns:
            int: The single-digit result after the digit summation process.
                 Due to the misplaced return, this will actually return the sum after
                 only one iteration.
        """
        # Convert to absolute value to handle negative inputs.
        num = abs(num)
        # Convert to string to easily check the number of digits.
        s = str(num)

        # If the number already has only one digit, return it immediately.
        if len(s) == 1:
            return num

        # Initialize total to store the sum of digit parts.
        total = 0

        # Intended loop: continue until the number becomes a single digit.
        while len(s) != 1:
            # Extract the last digit.
            num1 = num % 10
            # Remove the last digit to get the remaining part.
            num2 = num // 10

            # Sum the last digit and the remaining part.
            total = num1 + num2

            # Update num for the next iteration.
            num = total

            # Update the string representation for the digit-count check.
            s = str(abs(num))

            # BUG: This return statement causes the function to exit after the first
            # iteration. It should be placed outside the while loop to allow repeated
            # summing until a single digit remains.
            return total
