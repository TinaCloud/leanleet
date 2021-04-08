class Solution:
    def isValidSerialization1(self, preorder: str) -> bool:
        """
        O(n) time, O(n) space
        """
        valid=1
        for node in preorder.split(","):
            valid-=1
            if valid<0: return False
            if node!="#": valid+=2
        return True if valid==0 else False
