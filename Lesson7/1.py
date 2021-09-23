class Matrix:

    def __init__(self, mtrx1: list[list, list, list], mtrx2: list[list, list, list]):
        self.mtrx1 = mtrx1
        self.mtrx2 = mtrx2

    def __add__(self):
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(self.mtrx1)):

            for j in range(len(self.mtrx2[i])):

                matrix[i][j] = self.mtrx1[i][j] + self.mtrx2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))

    def __str__(self, matrix):
       return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))
    
lol = Matrix([[132, 111, 111], 
            [567, 143, 21113], 
            [10001, 1444, 99]], 
            
            [[1, 566, 12], 
            [543, 345, 0], 
            [333, 555, 777]])

print(lol.__add__())