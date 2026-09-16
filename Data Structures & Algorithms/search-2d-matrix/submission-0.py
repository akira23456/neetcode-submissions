class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        count = 0

        while count < len(matrix):
            if matrix[count][-1] == target:
                return True

            elif matrix[count][-1] < target:
                count += 1

            else:
                for num in matrix[count]:
                    if num == target:
                        return True

                return False  

        return False