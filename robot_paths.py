def dp_fn(mat, i, j):
    if i == 0 or j == 0:
        return 1
    else:
        return mat[j][i-1] + mat[j-1][i]
    return

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initialize matrix
        mat = []
        for _ in range(n):
            mat.append([0]* m)

        # build the matrix
        for j in range(n):
            for i in range(m):
                mat[j][i] = dp_fn(mat, i, j)
        
        return mat[-1][-1]

# zombiekillerwhale
# just do n choose R after calculating n total steps
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = (m-1)+(n-1) # The total number of steps the robot must take
        R = n - 1  # The number of steps the robot moves to the right
        # nCr: Out of N total steps, choose R steps to move to the right. 
        # The order in which we choose those R steps doesn't matter
        return math.factorial(N) // (math.factorial(R) * math.factorial(N - R))