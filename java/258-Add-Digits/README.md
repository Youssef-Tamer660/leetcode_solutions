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

The solution uses an iterative digit‑summing method:

1. Convert the absolute value of the number to a string to easily check the digit count.
2. If the number already has one digit, return it immediately.
3. Otherwise, enter a loop that continues as long as the number has more than one digit:
   · Extract the last digit: num % 10
      · Remove the last digit from the original number: num / 10
         · Sum these two parts and assign the result to sum
            · Update num with this sum and repeat
            4. Once the number is reduced to a single digit, return the final sum.

            This approach is straightforward and easy to follow, making it a good demonstration of basic loop and integer manipulation.

            Alternative Optimal Solution

            A constant‑time solution exists using the digital root formula:


            if (num == 0) return 0;
            return 1 + (num - 1) % 9;


            This version runs in O(1) time and O(1) space. I have chosen the iterative approach here to illustrate the underlying logic; however, I am aware of the more efficient formula and can discuss it if needed.

            Complexity

            · Time complexity: O(log₁₀(num)) – the number of iterations is proportional to the number of digits.
            · Space complexity: O(log₁₀(num)) – due to the string conversion used to check the digit count.

            Code

            The implementation is in AddDigitsTest.java and includes detailed comments explaining each step.


            class Solution {
            	    public int sum;

            	        public int addDigits(int num) {
            	        	        String str = Integer.toString(Math.abs(num));
            	        	                if (str.length() == 1) {
            	        	                	            return num;
            	        	                	                    }

            	        	                	                            while (str.length() != 1) {
            	        	                	                            	            int num1 = num % 10;
            	        	                	                            	                        int num2 = num / 10;
            	        	                	                            	                                    sum = num1 + num2;
            	        	                	                            	                                                num = sum;
            	        	                	                            	                                                            str = Integer.toString(Math.abs(num));
            	        	                	                            	                                                                    }
            	        	                	                            	                                                                            return sum;
            	        	                	                            	                                                                                }
            	        	                	                            	                                                                                }


            	        	                	                            	                                                                                How to Run

            	        	                	                            	                                                                                Compile and run the test class included in the same folder:


            	        	                	                            	                                                                                javac AddDigitsTest.java
            	        	                	                            	                                                                                java AddDigitsTest


            	        	                	                            	                                                                                The output will show results for several test cases, e.g.:


            	        	                	                            	                                                                                addDigits(38) = 2
            	        	                	                            	                                                                                addDigits(0) = 0
            	        	                	                            	                                                                                addDigits(12345) = 6


            	        	                	                            	                                                                                Notes

            	        	                	                            	                                                                                · The solution handles negative inputs by taking the absolute value; the problem assumes non‑negative integers, but this adds a layer of safety.
            	        	                	                            	                                                                                · The iterative approach demonstrates how to extract and recombine digits, which is a common pattern in many programming challenges.



            	        	                	                            	                                                                                Author: Youssef Tamer
            	        	                	                            	                                                                                GitHub: Youssef-Tamer660
            	        	                	                            	                                                                                Email: pqy96872@gmail.com
            	        	                	                            	                                                                                Date: February 2026
            	        	                	                            
            	        	       
