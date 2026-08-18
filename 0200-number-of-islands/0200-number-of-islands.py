class Solution:
    def numIslands(self,grid:List[List[str]])->int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    rt=[]
                    rt.append([i,j])
                    grid[i][j]="0"
                    while len(rt)>0:
                        cell=rt.pop(0)
                        r=cell[0]
                        c=cell[1]
                        if r+1<len(grid) and grid[r+1][c]=="1":
                            grid[r+1][c]="0"
                            rt.append([r+1,c])
                        if r-1>=0 and grid[r-1][c]=="1":
                            grid[r-1][c]="0"
                            rt.append([r-1,c])
                        if c+1<len(grid[0]) and grid[r][c+1]=="1":
                            grid[r][c+1]="0"
                            rt.append([r,c+1])
                        if c-1>=0 and grid[r][c-1]=="1":
                            grid[r][c-1]="0"
                            rt.append([r,c-1])
        return count