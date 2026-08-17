from typing import List
def diagonalSum(mat: List[List[int]]) -> int:
    n=len(mat)
    s = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                s+=mat[i][j]
            if i + j == n-1:
                s += mat[i][j]
    if n % 2 == 1:
        s -= mat[n // 2][n // 2]
    return s

