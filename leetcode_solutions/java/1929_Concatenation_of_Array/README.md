Concatenation of Array (LeetCode #1929)

Problem Statement

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

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

1. Store the length n of the input array.
2. Create a new array ans of size 2 * n.
3. Iterate over the input array once. For each index i (0 to n-1):
   · Assign nums[i] to ans[i] (first half).
   · Assign nums[i] to ans[i + n] (second half).
4. Return the resulting array.

This approach uses a single pass and directly constructs the result without additional overhead.

Complexity

· Time complexity: O(n) – we iterate through the input array once.
· Space complexity: O(n) – we allocate a new array of size 2n (the output array). No extra space is used besides the output.

Code

The implementation is in GetConcatenation.java (or Main.java) and includes detailed comments explaining each step.

```java
class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n * 2];

        for (int i = 0; i < n; i++) {
            ans[i] = nums[i];
            ans[i + n] = nums[i];
        }

        return ans;
    }
}
```

How to Run

Compile and run the test class (if provided) or use this snippet in your own main method:

```bash
javac GetConcatenation.java
java GetConcatenation
```

Alternatively, you can run a quick test directly:

```java
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {1, 2, 1};
        int[] result = sol.getConcatenation(nums);
        // Print result: [1, 2, 1, 1, 2, 1]
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
```

Notes

· This problem is often used to test basic array manipulation and indexing.
· The solution is optimal; no further improvements are needed.
· The problem can also be solved using System.arraycopy() or Arrays.copyOf(), but the manual loop is clear and efficient.

---

Author: Youssef Tamer
GitHub: Youssef-Tamer660
Email: pqy96872@gmail.com
Date: September 2026

---

