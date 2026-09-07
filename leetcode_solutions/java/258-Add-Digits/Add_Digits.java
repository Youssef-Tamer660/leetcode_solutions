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
	        	                	                            
	        	                
	        

