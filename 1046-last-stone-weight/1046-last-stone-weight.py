from sortedcontainers import SortedList
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a=SortedList(stones)
        while len(a)>=2:
            y=a.pop()
            x=a.pop()
            if y>x:
                a.add(y-x)
        return a.pop() if len(a) else 0
        