### 13.机器人的运动范围

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows < 1 or cols < 1:
            return 0
        visited = [0]*(rows*cols)
        return self.movingCountRecu(threshold,rows,cols,0,0,visited)
    def movingCountRecu(self,threshold,rows,cols,row,col,visited):
        count = 0
        if row >=0 and col >= 0 and row < rows and col < cols and \
        self.getDigitSum(row)+self.getDigitSum(col)<=threshold and \
        not visited[row*cols+col]:
            visited[row*cols+col] = 1
            count = 1 + self.movingCountRecu(threshold,rows,cols,row-1,col,visited) \
                      + self.movingCountRecu(threshold,rows,cols,row+1,col,visited) \
                      + self.movingCountRecu(threshold,rows,cols,row,col-1,visited) \
                      + self.movingCountRecu(threshold,rows,cols,row,col+1,visited)
        return count
    def getDigitSum(self, number):
        res = 0
        while number:
            res += number%10
            number = number//10
        return res