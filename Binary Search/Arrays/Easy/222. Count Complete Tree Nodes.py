# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # getting the height of binary tree
        # taking the leftmost length as the leftmost path always reaches the maximum depth (height)
        def getHeight(node):
            h = 0
            while node.left:
                h += 1
                node = node.left
            return h

        # checking if the node exists at index or not
        def exists(idx, h, node):
            left = 0
            right = (2**h) - 1

            for _ in range(h):
                # not using a variable cos we wont be needing it anywhere, just need to run this loop h times
                # why h times? cos we already know a complete binary tree is full at all levels except the last so we just need to know how many nodes are present at the last level
                mid = (left + right) // 2

                if idx <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return node is not None

        h = getHeight(root)

        # if root exists
        if h == 0:
            return 1

        # applying binary search on last level
        left = 0
        right = (2**h) - 1
        while left <= right:
            mid = (left + right) // 2

            if exists(mid, h, root):
                left = mid + 1
            else:
                right = mid - 1
        return (2**h - 1) + left
