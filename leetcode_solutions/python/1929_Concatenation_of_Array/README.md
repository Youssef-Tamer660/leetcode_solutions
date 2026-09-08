Concatenation of Array (LeetCode #1929)

Problem Statement

Given an integer array nums of length n, create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed by concatenating [1,2,1] with [1,2,1].

Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]

Approach

The solution is straightforward:

1. Store the length n of the input list.
2. Create a new list ans of size 2 * n, initialized with zeros as placeholders.
3. Iterate over the input list once. For each index i (0 to n-1):
   · Assign nums[i] to ans[i] (first half).
   · Assign nums[i] to ans[i + n] (second half).
4. Return the resulting list.

This approach uses a single pass and directly constructs the result without additional overhead.

Note: In the original code, the return ans statement was mistakenly placed inside the for loop, causing the function to exit after the first iteration. The corrected version places the return statement outside the loop.

Complexity

· Time complexity: O(n) – we iterate through the input list once.
· Space complexity: O(n) – we allocate a new list of size 2n (the output list). No extra space is used besides the output.

Code

The implementation is in concatenation.py and includes detailed comments explaining each step.

```python
class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (n * 2)

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans
```

How to Run

You can run the code by creating a simple test script:

```python
# test.py
from concatenation import Solution

sol = Solution()
nums = [1, 2, 1]
result = sol.getConcatenation(nums)
print(result)  # Output: [1, 2, 1, 1, 2, 1]
```

Then execute:

```bash
python test.py
```

Alternatively, you can run it interactively in a Python shell.

Notes

· This problem is often used to test basic list manipulation and indexing.
· The solution is optimal for time and space.
· Python’s list multiplication simplifies initialization, but the manual loop keeps the logic explicit and easy to understand.

---

Author: Youssef Tamer
GitHub: Youssef-Tamer660
Email: pqy96872@gmail.com
Date: September 2026
