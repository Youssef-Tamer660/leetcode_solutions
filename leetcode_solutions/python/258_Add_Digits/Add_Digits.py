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

                return total
