from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key  = lambda x : x[0])
        merged = []

        for start , end in intervals:
            if not merged :
                merged.append([start, end])

            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)

            else :
                merged.append([start, end])
        return merged

c1 = Solution()
print(c1.merge([[1,2] , [2,3], [4,5]]))