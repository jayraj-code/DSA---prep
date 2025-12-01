class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        max_len = 0

        for r, ch in enumerate(s):
            seen[ch] = seen.get(ch, 0) + 1

            while seen[ch] > 1:
                left_char = s[l]
                seen[left_char] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len

c1 = Solution()
print(c1.lengthOfLongestSubstring( s = "abcabcbb"))
print(c1.lengthOfLongestSubstring( s = "bbbbb"))
print(c1.lengthOfLongestSubstring(s = "pwwkew"))