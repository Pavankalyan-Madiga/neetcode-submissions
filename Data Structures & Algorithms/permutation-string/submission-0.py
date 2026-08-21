class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = {}

        for ch in s1:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        window = {}

        for i in range(len(s1)):
            ch = s2[i]

            if ch in window:
                window[ch] += 1
            else:
                window[ch] = 1

        if window == freq:
            return True

        left = 0

        for right in range(len(s1), len(s2)):
            ch = s2[right]

            if ch in window:
                window[ch] += 1
            else:
                window[ch] = 1

            old = s2[left]
            window[old] -= 1

            if window[old] == 0:
                del window[old]

            left += 1

            if window == freq:
                return True

        return False
        