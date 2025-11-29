from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        new_start, new_end = newInterval

        # Phase 1: Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1

        # Phase 2: Merge all intervals that overlap with the new interval
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1

        # Add the merged interval
        res.append([new_start, new_end])

        # Phase 3: Add all remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
