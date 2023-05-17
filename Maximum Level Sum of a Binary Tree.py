# Maximum Level Sum of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        def levelSum(root, levelSumArray, level, depth):

            if not root:
                return 
            
            #increment maximum depth if current level is greater then current depth
            if level > depth[0]:
                depth[0] = level

            #add current node value to the current level index in array
            levelSumArray[level] += root.val

            levelSum(root.right, levelSumArray, level + 1, depth)
            levelSum(root.left, levelSumArray, level + 1, depth)

        
        
        levelSumArray = [0] * 1000
        depth = [0]
        levelSum(root, levelSumArray, 0, depth)

        #return index of largest sum
        return levelSumArray.index(max(levelSumArray[: depth[0] + 1])) + 1



# Create an instance of the Solution class
solution = Solution()

# Example usage
root = [989,null,10250,98693,-89388,null,null,null,-32127]
max_level_sum = solution.maxLevelSum(root)
print(max_level_sum)
