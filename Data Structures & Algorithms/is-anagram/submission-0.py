class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

        for ch in t:
            if ch not in freq:
                return False

            freq[ch] -= 1

            if freq[ch] < 0:
                return False

        for count in freq.values():
            if count != 0:
                return False

        return True