from typing import List

def diagonalBoundarySum(arr: List[List[int]]) -> int:
    n = len(arr)
    visited = set()
    total_sum = 0
    
    for i in range(n):
        for j in range(n):
            # Check if cell is on the primary diagonal, secondary diagonal, or boundary
            if i == j or i + j == n - 1 or i == 0 or i == n - 1 or j == 0 or j == n - 1:
                if (i, j) not in visited:
                    visited.add((i, j))
                    total_sum += arr[i][j]
                    
    return total_sum

if __name__ == '__main__':
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))
    print(diagonalBoundarySum(mat))