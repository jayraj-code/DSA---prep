from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Left = 0
        total_length = 0
        seen = set()
        
