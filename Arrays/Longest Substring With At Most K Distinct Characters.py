class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> dict:
        l = 0
        seen = {}        
        max_len = 0

        for r, ch in enumerate(s):

            seen[ch] = seen.get(ch, 0) + 1

            while len(seen) > k:
                left_char = s[l]
                seen[left_char] -= 1
                if seen[left_char] == 0:
                    del seen[left_char]
                l += 1

            current_window = (r - l) + 1
            max_len = max(max_len, current_window)



        return max_len


c1 = Solution()
print(c1.lengthOfLongestSubstringKDistinct(s = "ecekw", k = 2))
