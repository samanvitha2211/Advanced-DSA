from collections import defaultdict
from typing import List

def diagonalSort(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    diagonals = defaultdict(list)
    
    # Group elements by diagonal index (r - c)
    for r in range(m):
        for c in range(n):
            diagonals[r - c].append(mat[r][c])
            
    # Sort each diagonal in descending order so we can pop small elements from the end
    for k in diagonals:
        diagonals[k].sort(reverse=True)
        
    # Reconstruct the matrix with sorted values
    for r in range(m):
        for c in range(n):
            mat[r][c] = diagonals[r - c].pop()
            
    return mat

if __name__ == '__main__':
    m, n = map(int, input().split())
    mat = []
    for i in range(m):
        mat.append(list(map(int, input().split())))
    print(diagonalSort(mat))