# A palindrome is a series of characters which when read from front to the end or end to the front becomes the same letter
# eg racecar

from typing import List
def is_palindrome(s : str) -> bool:
    cleaned_s = "".join(filter(str.isalnum,s)).lower()
    start = 0
    end = len(cleaned_s) - 1

    while start < end:
        if cleaned_s[start] != cleaned_s[end]:
            return False
        start += 1
        end -= 1

    return True
print(f"Test 1 (True): {is_palindrome('A man, a plan, a canal: Panama')}")
print(f"Test 2 (False): {is_palindrome('race a car')}")
