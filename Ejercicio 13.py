class Matriz:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for _ in tange(columns)] for _ in range(rows)]
    
        def getNumberRows(self):
            return self.rows
        
        def getNumberColumns(self):
            return self.columns
    
    def setElement(self, x, y, element):
        if 0 <= x < self.rows and 0 <= y < self.columns:
            self.matrix[x][y] = element
        else:
            print("Índices fuera del rango permitido")
    
    def addMatrix(self, otherMatrix):
        if len(otherMatrix) == self.rows and len(itherMatrix[0]) == self.columns:
            for i in range(self.rows):
                for j in range (self.columns):
                    self.matrix[i][j] += otherMatrix[i][j]
        else:
            print("No se puede realizar la suma. Las dimensiones no coinciden.")
    
    def maultMatrix(self, otherMatrix):
        if len(otherMatrix) == self.columns:
            result = [[0 for _ in range(len(otherMatrix[0]))] for _ in range(self.rows)]
            for i in range(len(otherMatrix[0])):
                for j in range(len(otherMatrix[0])):
                    for k in range(self.columns):
                        result[i][j] += self.matrix[i][k] * otherMatrix[k][j]
            self.columns = len(otherMatrix[0])
            self.matrix = result
        else:
            print("No se puede realizar la multiplicacion. Las dimensiones no coinciden.")