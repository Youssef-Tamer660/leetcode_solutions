/**
 * LeetCode Problem #1929: Concatenation of Array
  *
   * Problem: Given an integer array nums of length n, create an array ans of length 2n
    * where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n.
     * In other words, ans is the concatenation of two copies of nums.
      *
       * This problem tests basic array manipulation and indexing.
        *
         * Approach:
          * - Determine the length n of the input array.
           * - Create a new array ans of size 2 * n.
            * - Loop through each index i from 0 to n-1:
             *   - Copy nums[i] to ans[i] (first half).
              *   - Copy nums[i] to ans[i + n] (second half).
               * - Return the resulting array.
                *
                 * Time complexity: O(n) – we iterate over the array once.
                  * Space complexity: O(n) – we create a new array of size 2n.
                   */
                   class Solution {
                   	    /**
                   	         * Constructs an array that is the concatenation of the input array with itself.
                   	              *
                   	                   * @param nums the original integer array
                   	                        * @return a new array of length 2*n containing two copies of nums
                   	                             */
                   	                                 public int[] getConcatenation(int[] nums) {
                   	                                 	        // Store the length of the input array.
                   	                                 	                int n = nums.length;

                   	                                 	                        // Create a new array twice the size to hold both copies.
                   	                                 	                                int[] ans = new int[n * 2];

                   	                                 	                                        // Fill the new array by copying each element into both halves.
                   	                                 	                                                for (int i = 0; i < n; i++) {
                   	                                 	                                                	            // Copy to the first half.
                   	                                 	                                                	                        ans[i] = nums[i];
                   	                                 	                                                	                                    // Copy to the second half (offset by n).
                   	                                 	                                                	                                                ans[i + n] = nums[i];
                   	                                 	                                                	                                                        }

                   	                                 	                                                	                                                                // Return the concatenated array.
                   	                                 	                                                	                                                                        return ans;
                   	                                 	                                                	                                                                            }
                   	                                 	                                                	                                                                            }
                   	                                 	                                                }
                   	                                 }
                   }
