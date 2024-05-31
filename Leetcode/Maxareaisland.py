def findAllOnesUsingDFS( row, col, grid, n, m):
        if min(row, col) < 0 or row >= n or col >= m or grid[row][col] == 0:
            return 0 
 
        result = 1 
        grid[row][col] = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
 
        for index in range(4):
            newRow = row + dx[index]
            newCol = col + dy[index]
            result += findAllOnesUsingDFS(newRow, newCol, grid, n, m)
        return result
def findAllOnesUsingBFS( row, col, grid, n, m):
        Q = [[row, col]]
        result = 1
        grid[row][col] = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
 
        while Q:
            curr = Q.pop(0)
            row, col = curr[0], curr[1]
 
            for index in range(4):
                newRow = row + dx[index]
                newCol = col + dy[index]
                if min(newRow, newCol) < 0 or newRow >= n or newCol >= m or grid[newRow][newCol] == 0:
                    continue
                grid[newRow][newCol] = 0
                result += 1
                Q.append([newRow, newCol])
 
        return result
 

def maxAreaOfIsland( grid) :
        n = len(grid)
        m = len(grid[0])
        result = 0 
 
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    current =findAllOnesUsingBFS(row, col, grid, n, m)
                    result = max(result, current)
        return result            
        return result
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         def flood(i, j):
#             nonlocal area
#             if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
#                 return
#             area += 1
#             grid[i][j] = -1
#             flood(i+1, j)
#             flood(i-1, j)
#             flood(i, j+1)
#             flood(i, j-1)
        
#         max_area = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     area = 0
#                     flood(i, j)
#                     max_area = max(max_area, area)
#         return max_area 
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(grid))