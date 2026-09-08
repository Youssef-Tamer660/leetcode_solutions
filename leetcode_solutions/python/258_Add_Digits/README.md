Add Digits (LeetCode #258)

Problem Statement

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example:
Input: 38
Output: 2
Explanation: 3 + 8 = 11 → 1 + 1 = 2

Additional Examples

Input Output Explanation
0 0 Already a single digit
9 9 Single digit, return as is
12345 6 1+2+3+4+5 = 15 → 1+5 = 6

Approach

The solution uses an iterative digit‑summing method (with a known bug; see Notes):

1. Take the absolute value of num to handle negative inputs safely.
2. Convert the number to a string to easily check its digit count.
3. If the number already has one digit, return it immediately.
4. Otherwise, enter a loop intended to continue until the number becomes a single digit:
   · Extract the last digit: num % 10
   · Remove the last digit from the original number: num // 10
   · Sum these two parts and assign the result to total
   · Update num with this sum and repeat
5. Once the loop finishes (intended), return the final total.

⚠️ Important Note: The current code has the return total statement inside the while loop. This causes the function to exit after the first iteration, always returning the sum of the last digit and the remaining part, instead of repeating until a single digit remains. The return statement should be outside the loop to work correctly.

Alternative Optimal Solution

A constant‑time solution exists using the digital root formula:

```python
if num == 0:
    return 0
return 1 + (num - 1) % 9
```

This version runs in O(1) time and O(1) space. The iterative approach illustrated here is more intuitive but less efficient.

Complexity

· Time complexity (intended): O(log₁₀(num)) – iterations proportional to number of digits.
· Space complexity: O(log₁₀(num)) – due to string conversion for digit count checking.

Code

The implementation is in add_digits.py and includes detailed comments explaining each step.

```python
class Solution:
    def addDigits(self, num):
        num = abs(num)
        s = str(num)
        if len(s) == 1:
            return num

        total = 0
        while len(s) != 1:
            num1 = num % 10
            num2 = num // 10
            total = num1 + num2
            num = total
            s = str(abs(num))
            return total  # BUG: return inside loop
```

How to Run

You can run a quick test with the following script:

```python
# test.py
from add_digits import Solution

sol = Solution()
print(sol.addDigits(38))    # Expected 2, but due to bug may output 11
print(sol.addDigits(0))     # 0 (works correctly)
print(sol.addDigits(12345)) # Expected 6, but may output 15
```

Then execute:

```bash
python test.py
```

Notes

· The code handles negative inputs by taking the absolute value; the problem normally assumes non‑negative integers.
· The iterative approach demonstrates how to extract and recombine digits, which is a common pattern in many programming challenges.
· Bug Alert: The return total is currently inside the while loop, preventing repeated summing. For a correct solution, move the return outside the loop.

---

Author: Youssef Tamer
GitHub: Youssef-Tamer660
Email: pqy96872@gmail.com
Date: September 2026
