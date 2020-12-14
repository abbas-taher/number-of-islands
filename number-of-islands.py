"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
 """

# The proposed Solution is quite simple and does not use recurssion.
# Simply we traverse the grid line by line and item by item to check for a given item if
# the preceeding item or the one above belong to an island - if so then add it to that island

 class Grid(object):
    def __init__(self, mat):
        self.mat = mat
        self.islandLst =[]     # list of dictionaries (islands)
    
    # for a given (i,j) check that preceeding item belongs to an island; if so add it to that island
    def isBefore(self, i,j):      
        for island in self.islandLst:
            if j != 0 and (i,j-1) in island:   # assuming grid is surrounded by water, then for j == 0 (1st entry in line) there are no before entry  
                island[(i,j)] = None
                return (True) 
        return (False)
    
    # for a given (i,j) check that above item belongs to an island; if so add it to that island
    def isAbove(self, i,j):
        for island in self.islandLst:
            if i != 0 and (i-1,j) in island:
                island[(i,j)] = None      # adding the item keys into the island dictionary
                return (True)
        return (False)
    
        
    def numof_Islands(self): 
        for i in range (len(self.mat)):
            for j in range (len(self.mat[0])):
             if self.mat[i][j] == '1':
                 if not self.isBefore(i,j) and not self.isAbove(i,j):
                     self.islandLst.append({(i,j):None})                # if item does not belong to any island then create an island for it  
                     
        return (len(self.islandLst))
    
mat = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]


grid = Grid(mat)
print (grid.numof_Islands())  # 1


mat = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

grid = Grid(mat)
print (grid.numof_Islands())   # 3
