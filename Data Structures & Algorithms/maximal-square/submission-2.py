class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Idea:
        1,1,1.     1,1,1
        1,1,1.     1,2,2
        1,1,1.     1,2,3

        1,1,1.     1,1,1
        1,1,1.     1,2,2
        1,1,0.     1,2,0


        1,1,1.     1,1,1
        1,1,0.     1,2,0
        1,1,1.     1,2,1


        1,1,1.     1,1,1
        1,0,1.     1,0,1
        1,1,1.     1,1,1


        1,0
        0,1


        """
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            dp[i][0] = int(matrix[i][0])
        for j in range(len(matrix[0])):
            dp[0][j] = int(matrix[0][j])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
        return max(max([row for row in dp])) ** 2
        