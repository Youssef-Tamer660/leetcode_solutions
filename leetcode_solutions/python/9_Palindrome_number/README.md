Palindrome Number (LeetCode #9)

Problem Statement

Given an integer x, return true if x is a palindrome, and false otherwise.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.

Examples

Input Output Explanation
121 true 121 reads as 121 from both ends
-121 false Negative numbers are not palindromes
10 false Ends with 0, cannot be a palindrome (except 0 itself)

Approach

The solution uses the reverse half of the number technique:

1. Handle edge cases: negative numbers and numbers ending with 0 (except 0 itself) are not palindromes.
2. Reverse the second half of the number by repeatedly:
   · Extracting the last digit (x % 10).
   · Appending it to reversed_half (reversed_half = reversed_half * 10 + last_digit).
   · Removing the last digit from x (x //= 10).
3. Stop when x becomes less than or equal to reversed_half, meaning we have processed at least half of the digits.
4. Compare:
   · For even-length numbers: x == reversed_half
   · For odd-length numbers: x == reversed_half // 10 (ignoring the middle digit)

This method avoids overflow and runs in O(log₁₀(n)) time.

⚠️ Important Note: The provided code has the return statement inside the while loop. This causes the function to exit after the first iteration, which is incorrect for numbers with more than two digits. The return statement should be outside the loop to allow the loop to complete its iterations.

Complexity

· Time complexity: O(log₁₀(n)) – we process roughly half the digits.
· Space complexity: O(1) – only a few integer variables are used.

Code

The implementation is in palindrome.py and includes detailed comments explaining the logic.

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
            # BUG: return inside loop; should be outside the while
            return x == reversed_half or x == reversed_half // 10
```

How to Run

You can test the solution with a simple script:

```python
# test.py
from palindrome import Solution

sol = Solution()
print(sol.isPalindrome(121))   # True (but current code will return after first iteration)
print(sol.isPalindrome(-121))  # False (edge case works)
print(sol.isPalindrome(10))    # False (edge case works)
```

Run:

```bash
python test.py
```

For a correct implementation, move the return statement to the outside of the loop.

Notes

· The algorithm is efficient but the current code contains a bug due to the misplaced return.
· The edge case handling is correct.
· The reverse-half technique is a common interview solution.

---

Author: Youssef Tamer
GitHub: Youssef-Tamer660
Email: pqy96872@gmail.com
Date: September 2026
