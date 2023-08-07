class Solution:
    def searchMatrix(self, matrix, target):
        rowLength = len(matrix)
        columnLength = len(matrix[0])
        L = 0
        R = columnLength - 1
        prev_L = -1
        prev_R = -1
        vertDirection = 0
        midRow = rowLength // 2
        midCol = columnLength // 2

        while L != prev_L or R != prev_R or vertDirection != 0 and midRow < rowLength and midRow >= 0:
            
            prev_L = L
            prev_R = R

            #target is in lower row
            if matrix[midRow][midCol] > target and matrix[midRow][L] > target:
                if vertDirection != 1:
                    vertDirection = -1
                    midRow -= 1
                else:
                    return False

            #target is in current row
            elif matrix[midRow][midCol] > target and matrix[midRow][L] < target:
                vertDirection = 0
                R = midCol

            #target is in higher row
            elif matrix[midRow][midCol] < target and matrix[midRow][R] < target:
                if vertDirection != -1:
                    vertDirection = 1
                    midRow += 1
                else:
                    return False

            #target is in current row
            elif matrix[midRow][midCol] < target and matrix[midRow][R] > target:
                vertDirection = 0
                L = midCol
                
            #otherwise we reached target index
            else:
                return True
            
            midCol = (R + L) // 2
        
        return False

#example cases
solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
