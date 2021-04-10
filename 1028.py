class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        i = 0
        n = len(S)
        val = 0
        while i < n and S[i] != '-':
            val = val * 10 + int(S[i])
            i += 1
        head = TreeNode(val)
        stk = [[0, head]]
        while i < n:
            ctr = 0
            while i < n and S[i] == '-':
                ctr += 1
                i += 1
            val = 0
            while i < n and S[i] != '-':
                val = val * 10 + int(S[i])
                i += 1
            p = TreeNode(val)
            if ctr > stk[-1][0]:
                stk[-1][1].left = p
            else:
                while stk[-1][0] >= ctr:
                    stk.pop()
                stk[-1][1].right = p
            stk.append([ctr, p])
        return head
