#Leaf-Similar Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def findLeafs(root, arr):
            
            if not root:
                return
            
            if not root.right and not root.left:
                arr.append(root.val)

            findLeafs(root.right, arr)
            findLeafs(root.left, arr)
        

        arr1 = []
        arr2 = []

        findLeafs(root1, arr1)
        findLeafs(root2, arr2)
        
        if len(arr1) != len(arr2):
            return False

        for i in range(0, len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        
        return True
    

# Create an instance of the Solution class
solution = Solution()

# Example usage
root1 = [3,5,1,6,2,9,8,null,null,7,4]
root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
isSimilarLeaves = solution.leafSimilar(root1, root2)
print(isSimilarLeaves )
