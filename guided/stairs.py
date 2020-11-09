class Solution:
    """
    n = 2
    output = 2
    1. 1 step + 1 step
    2. 2 steps

    n = 3
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 steps

    n = 1
    output = 1

    Plan
    Cookie monster eating cookies.

    https://leetcode.com/problems/climbing-stairs/
    """
    def climbStairs(self, n: int) -> int:
        computedValues = {0 : 0, 1: 1, 2:2}
        return self.climbStairsHelper(n, computedValues)

    def climbStairsHelper(self, N, computedValues):
        if N in computedValues:
            return computedValues[N]
        computedValues[N] = self.climbStairsHelper(N - 1, computedValues) + self.climbStairsHelper(N - 2, computedValues)
        return computedValues[N]

        