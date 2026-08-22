class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need={}
        for ch in t:
            if ch in need:
                need[ch]+=1
            else:
                need[ch]=1
        
        window={}
        left=0
        count=0
        min_len=float("inf")
        start=0

        for right in range(len(s)):
            ch=s[right]

            if ch in window:
                window[ch]+=1
            else:
                window[ch]=1
            
            if ch in need and window[ch]<=need[ch]:
                count+=1

            while count==len(t):
                if right-left+1 < min_len:
                    min_len=right-left+1
                    start=left
                left_ch=s[left]

                if left_ch in need and window[left_ch]<=need[left_ch]:
                    count-=1

                window[left_ch]-=1
                left+=1

        if min_len==float("inf"):
            return ""
        return s[start:start+min_len]