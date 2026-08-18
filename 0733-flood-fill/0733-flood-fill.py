class Solution:
    def floodFill(self,image:List[List[int]],sr:int,sc:int,color:int)->List[List[int]]:
        old=image[sr][sc]
        if old==color:
            return image
        rt=[]
        rt.append([sr,sc])
        image[sr][sc]=color
        while len(rt)>0:
            cell=rt.pop(0)
            i=cell[0]
            j=cell[1]
            if i+1<len(image) and image[i+1][j]==old:
                image[i+1][j]=color
                rt.append([i+1,j])
            if i-1>=0 and image[i-1][j]==old:
                image[i-1][j]=color
                rt.append([i-1,j])
            if j+1<len(image[0]) and image[i][j+1]==old:
                image[i][j+1]=color
                rt.append([i,j+1])
            if j-1>=0 and image[i][j-1]==old:
                image[i][j-1]=color
                rt.append([i,j-1])
        return image