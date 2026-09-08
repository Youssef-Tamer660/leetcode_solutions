"""
LeetCode Problem #1929: Concatenation of Array

Problem: Given an integer array nums of length n, create an array ans of length 2n
where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n.
In other words, ans is the concatenation of two copies of nums.

This problem tests basic array/list manipulation and indexing.

Approach:
- Determine the length n of the input list.
- Create a new list ans of size 2*n, initialized with zeros (placeholder).
- Loop through each index i from 0 to n-1:
  - Copy nums[i] to ans[i] (first half).
    - Copy nums[i] to ans[i + n] (second half).
    - Return the resulting list.

    Time complexity: O(n) – we iterate over the list once.
    Space complexity: O(n) – we create a new list of size 2n (the output list).
"""


class Solution:
    def getConcatenation(self, nums):
        """
        Constructs a list that is the concatenation of the input list with itself.

                Args:
                            nums (List[int]): The original integer list.

                                    Returns:
                                                List[int]: A new list of length 2*n containing two copies of nums.

                                                        Note:
                                                                    The original code had the return statement inside the for loop,
                                                                                which would cause the function to exit after the first iteration.
                                                                                            The correct placement is outside the loop, as shown below.
        """
        # Store the length of the input list.
        n = len(nums)

        # Create a new list twice the size, initialized with zeros.
        # The zeros will be overwritten in the loop.
        ans = [0] * (n * 2)

        # Fill the new list by copying each element into both halves.
        for i in range(n):
            # Copy to the first half at index i.
            ans[i] = nums[i]
            # Copy to the second half at index i + n.
        ans[i + n] = nums[i]

        # Return the concatenated list. This must be outside the loop!
        return ans
