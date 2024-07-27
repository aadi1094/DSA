class Solution(object):
        def myPow(self, x, n):
            if n == 0:
                return 1
            if n < 0:
                x = 1 / x
                n = -n
            if n % 2 == 0:
                half = self.myPow(x, n // 2)
                return half * half
            else:
                return x * self.myPow(x, n - 1)
            
            
pow=Solution()
print(pow.myPow(2,-2))