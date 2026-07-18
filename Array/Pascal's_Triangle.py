class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]

        """
        result = []
        for i in range(numRows):
            row = [1] * (i+1)

            for j in range(1,i):
                row[j] = row[j - 1] * (i - j + 1) // j
            
            result.append(row)

        return result
 
        