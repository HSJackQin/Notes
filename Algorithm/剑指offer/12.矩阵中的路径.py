# 12.矩阵中的路径

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if matrix == None or rows < 1 or cols < 1 or path == None:
            return False
        pathLength = 0
        visited = [0]*(rows*cols)
        for row in xrange(rows):
            for col in xrange(cols):
                if self.hasPathRecu(matrix, rows, cols, row, col, path, pathLength, visited):
                    return True
        return False
    def hasPathRecu(self,matrix,rows,cols,row,col,path,pathLength,visited):
        if pathLength == len(path):
            return True
        hasPath = False
        if row >= 0 and col >= 0 and row < rows and col < cols and path[pathLength] == matrix[row*cols+col] and not visited[row*cols+col]:
            pathLength += 1
            visited[row*cols+col] = 1
            hasPath = self.hasPathRecu(matrix, rows, cols, row-1, col, path, pathLength, visited) or \
                      self.hasPathRecu(matrix, rows, cols, row+1, col, path, pathLength, visited) or \
                      self.hasPathRecu(matrix, rows, cols, row, col-1, path, pathLength, visited) or \
                      self.hasPathRecu(matrix, rows, cols, row, col+1, path, pathLength, visited)
            if not hasPath:
                pathLength -= 1
                visited[row*cols+col] = 0
        return hasPath