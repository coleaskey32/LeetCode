# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]

        def goodN(root, MaxBeforeNode):
            if not root:
                return

            if root.val >= MaxBeforeNode:
                count[0] += 1
                MaxBeforeNode = root.val

            goodN(root.right, MaxBeforeNode)
            goodN(root.left, MaxBeforeNode)

        goodN(root, root.val)
        return count[0]

# Create an instance of the Solution class
solution = Solution()

# Example usage
good_nodes_count = solution.goodNodes([3,1,4,3,null,1,5])
print(good_nodes_count)
