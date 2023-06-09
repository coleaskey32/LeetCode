# Container with most water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        MAX = 0
        left = 0
        right = len(height) - 1

        while left != right:
            MAX = max(MAX, (right - left) * min(height[left], height[right]))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return MAX

# Create an instance of the Solution class
solution = Solution()

# Example usage
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
max_area = solution.maxArea(heights)
print(max_area)
