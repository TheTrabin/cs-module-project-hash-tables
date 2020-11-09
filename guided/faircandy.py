"""
Understand
Input: A = [1,1], B = [2,2]
Output [1,2] 

Input: A = [1], B = [2,3]
Output [1,3]  --> A = [3], B = [2,1]

A = [1] B = [1]
[1,1]

Plan
sum(A) - x + y = xum(B) - y + x
2y = sum(B) - sum(A) = 2x
y = (sum(bob) - sum(A) / 2) + x


runtime: O(len(A) + len(B))
space: O(len(b))
https://leetcode.com/problems/fair-candy-swap/
"""


class Solution:
    def fairCandySwap(self, A:List[int], B:List[int]) -> List[int]:
        bCandies = set(B)
        bSum, aSum = sum(B), sum(A)
        for x in A:
            y = ((bSum - aSum)/ 2) + x
            if y in bCandies:
                return [x, y]
        return []

    