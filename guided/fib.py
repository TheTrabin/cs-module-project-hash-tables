class Solution:
    """
    Input: 2
    Output: 1
    Fib(2) = Fib(1) + Fib(0) = 1 + 0 = 1

    Input: 2
    Output: 1
    Fib(2) = Fib(1) + Fib(0) = 1 + 0 = 1

    Input: 2
    Output: 1
    Fib(2) = Fib(1) + Fib(0) = 1 + 0 = 1

    https://leetcode.com/problems/fibonacci-number/
    """
    def fib(self, N: int) -> int:
        computedValues = {1: 1, 0: 0}
        return self.memoizedFib(N, computedValues)

    def memoizedFib(self, N, computedValues):
        if N in computedValues:
            return computedValues[N]
        computedValues[N] = self.memoizedFib(N - 1, computedValues) + self.memoizedFib(N - 2, computedValues)
        return computedValues[N]

    
