class Solution:
    def merge_intervals(self, intervals):
        if not intervals:
            return []

        intervals.sort(key = lambda x : x[0])

        current_interval = 0
        next_interval = 1

        while next_interval < len(intervals):
            if intervals[current_interval][1] >= intervals[next_interval][0]:
                new_interval = [intervals[current_interval][0], max(intervals[next_interval][1], intervals[current_interval][1])]
                intervals[current_interval] = new_interval
                del intervals[next_interval]
                intervals.sort(key = lambda x : x[0])

            else:
                current_interval += 1
                next_interval += 1


        return intervals

c1 = Solution()
print(c1.merge_intervals( intervals = [[1,3],[2,6],[8,10],[15,18]]))
print(c1.merge_intervals(intervals = [[1,4],[4,5]]))
print(c1.merge_intervals([[4,7],[1,4]]))
print(c1.merge_intervals([[1,4], [2,3]]))

