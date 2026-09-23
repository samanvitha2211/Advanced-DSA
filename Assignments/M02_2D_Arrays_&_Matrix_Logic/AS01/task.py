from typing import List

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    res = [[rStart, cStart]]
    total_cells = rows * cols
    
    # Directions: East (0, 1), South (1, 0), West (0, -1), North (-1, 0)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0  # Start facing East
    steps = 1
    
    r, c = rStart, cStart
    
    while len(res) < total_cells:
        # Perform 2 direction changes per step length increment
        for _ in range(2):
            dr, dc = directions[d]
            for _ in range(steps):
                r += dr
                c += dc
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
                    if len(res) == total_cells:
                        return res
            # Turn right
            d = (d + 1) % 4
        steps += 1
        
    return res

if __name__ == '__main__':
    rows, cols, rStart, cStart = map(int, input().split())
    print(spiralMatrixIII(rows, cols, rStart, cStart))