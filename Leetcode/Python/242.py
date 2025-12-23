def isAnagram(self, s: str, t: str) -> bool:
    return True if sorted(s)==sorted(t) else False
print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))