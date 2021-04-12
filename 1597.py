class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def expTree(self, s: str) -> Node:
        flag = False
        for c in s:
            if c in ["+", "-", "*", "/"]:
                flag = True
                break

        if not flag:
            return Node(s)

        cnt = 0
        for i in range(len(s) - 1, -1, -1):
            c = s[i]

            if c == ")":
                cnt += 1
            elif c == "(":
                cnt -= 1

            if cnt == 0 and (c == "-" or c == "+"):
                n1, n2 = self.expTree(s[:i]), self.expTree(s[i + 1:])
                root = Node(c, n1, n2)

                return root

        cnt = 0
        for i in range(len(s) - 1, -1, -1):
            c = s[i]

            if c == ")":
                cnt += 1
            elif c == "(":
                cnt -= 1

            if cnt == 0 and (c == "*" or c == "/"):
                n1, n2 = self.expTree(s[:i]), self.expTree(s[i + 1:])
                root = Node(c, n1, n2)
                return root

        return self.expTree(s[1:-1])
    
    