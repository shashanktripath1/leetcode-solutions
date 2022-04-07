class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=[str(x) for x in digits]
        s=""
        for x in digits:
            s+=x
        n=int(s)+1
        return list(str(n))
        