class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1 / x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif n == 2:
            return x ** 2
        t = self.myPow(x, n // 2)
        if n % 2 == 0:
            return t * t
        else:
            return x * t * t


s = Solution()
print(s.myPow(2, -2))
