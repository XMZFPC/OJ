class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s) + 1)             # DP Array of size (n+1) initialized to 1
        if s[0] == "0": dp[1] = 0           # Check s[0] is valid encoding

        for i in range(2, len(s) + 1):
            dp[i] = (dp[i - 1] if 1 <= int(s[i - 1]) <= 26 else 0) + (dp[i - 2] if 10 <= int(s[i - 2] + s[i - 1]) <= 26 else 0)
        return dp[-1]