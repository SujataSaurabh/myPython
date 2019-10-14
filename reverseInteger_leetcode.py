class Solution:
    def reverse(self, x: int) -> int:
        m = 0 if x > 0 else 1
        x=int(str(abs(x))[::-1])
        if m:
            x*=-1
        return x if abs(x)<2**31 else 0
