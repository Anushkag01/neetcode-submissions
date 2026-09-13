class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # arr = list(s)
        # arr2 = list(t)
        # arr.sort()
        # arr2.sort()
        # return(arr == arr2)

        return (sorted(s) == sorted(t))