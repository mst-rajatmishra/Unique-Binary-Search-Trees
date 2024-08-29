class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        
        # Initialize the dp array where dp[i] will be storing the number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # An empty tree
        dp[1] = 1  # A tree with only one node
        
        # Fill the dp array
        for i in range(2, n + 1):
            dp[i] = 0
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]
