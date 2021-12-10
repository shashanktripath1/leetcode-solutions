#Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        max_length=start=0
        map={}
        for i in range(len(s)):
            if s[i] in map and start<=map[s[i]]:
                start=map[s[i]]+1
            else:
                max_length=max(max_length,i-start+1)
            map[s[i]]=i
        return(max_length)
                

