Power of Two (LeetCode #231)

Problem Statement

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two if there exists an integer x such that n == 2^x.

Examples:

Input Output Explanation
1 true 2^0 = 1
16 true 2^4 = 16
3 false No integer x satisfies 2^x = 3
0 false Not a positive integer
-8 false Negative numbers are not powers of two

Approach

The solution uses bit manipulation to achieve constant-time performance.

A power of two in binary representation has exactly one bit set to 1, and all other bits are 0. For example:

· 1 (2^0) → 0001
· 2 (2^1) → 0010
· 4 (2^2) → 0100
· 8 (2^3) → 1000

For any positive integer n, the expression n & (n - 1) clears the lowest set bit. If n is a power of two, it has only one set bit, so clearing that bit results in 0.

Therefore, the condition:

```python
n > 0 and (n & (n - 1)) == 0
```

correctly identifies powers of two.

Complexity

· Time complexity: O(1) – constant time bitwise operation.
· Space complexity: O(1) – no extra space used.

Code

The implementation is in power_of_two.py and includes detailed comments explaining the logic.

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
```

How to Run

You can test the solution with a simple script:

```python
# test.py
from power_of_two import Solution

sol = Solution()
print(sol.isPowerOfTwo(1))    # True
print(sol.isPowerOfTwo(16))   # True
print(sol.isPowerOfTwo(3))    # False
print(sol.isPowerOfTwo(0))    # False
print(sol.isPowerOfTwo(-8))   # False
```

Then execute:

```bash
python test.py
```

Notes

· The solution is optimal and widely used due to its simplicity and efficiency.
· It correctly handles edge cases: zero and negative numbers return False.
· Bitwise operations are extremely fast and preferred for such problems.
· Alternative approaches include logarithmic checks or loop division, but they are less efficient.

---

Author: Youssef Tamer
GitHub: Youssef-Tamer660
Email: pqy96872@gmail.com
Date: September 2026
