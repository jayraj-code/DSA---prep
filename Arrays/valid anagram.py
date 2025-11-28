def isAnagram(s, t):
    # Different lengths can't be anagrams
    if len(s) != len(t):
        return False

    # Count characters in s
    count_s = {}
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    # Count characters in t
    count_t = {}
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    # Compare the counts
    return count_s == count_t


# Test
print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))  # False

# Let's trace it:
s = "rat"
t = "car"

# After counting:
# count_s = {'r': 1, 'a': 1, 't': 1}
# count_t = {'c': 1, 'a': 1, 'r': 1}
# They're different! → False