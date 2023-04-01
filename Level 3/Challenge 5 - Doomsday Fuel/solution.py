from fractions import Fraction
from fractions import gcd

def sumValues(m):
    sumList=list(map(sum,m))             
    return sumList       
 
def findProbabilityFraction(m):
    probability=[[0 for _ in range(len(m[0]))] for _ in range(len(m))] 
    s= sumValues(m)     
    for i in range(len(m)):
        for x,j in enumerate(m[i]):
            if(j != 0):            
                probability[i][x]=Fraction(j,s[i])            
    return probability 

def submatrix(m, r, c):
    newMatrix = []
    for row in r:
        currentRow = []
        for column in c:
            currentRow.append(m[row][column])
        newMatrix.append(currentRow)
    return newMatrix

def Q(m, nonabsorbingIndices):
    return submatrix(m, nonabsorbingIndices, nonabsorbingIndices)
def R(m, nonabsorbingIndices, absorbingIndices):
    return submatrix(m, nonabsorbingIndices, absorbingIndices)        
def I(m):      
    rowQ=len(Q(m,nonabsorbingIndices)) 
    mI=[[0 for _ in range(rowQ)] for _ in range(rowQ)]    
    for x in range(rowQ):
        mI[x][x]= 1         
    return mI

def subtract(m1,m2):
    result =[[0 for _ in range(len(m1))] for _ in range(len(m1))]          
    for i in range(len(m1)):      
       for j in range(len(m1[0])): 
           result[i][j] = m1[i][j] - m2[i][j]                    
    return result

def multiply(a, b):
    a_rows = len(a)
    a_cols = len(a[0])
    b_cols = len(b[0])
    rows = a_rows
    cols = b_cols
    c = twoDimensionlist(rows, cols)
    for row in range(rows):
        for col in range(cols):
            dot_product = Fraction(0, 1)
            for i in range(a_cols):
                dot_product += a[row][i]*b[i][col]
            c[row][col] = dot_product
    return c
def mulSquareMatrix(m, row, k):
    n = len(m)
    row_operator = make_identity(n)
    row_operator[row][row] = k
    return multiply(row_operator, m)
def twoDimensionlist(rows, cols):
    a = []
    for row in range(rows):
        a += [[0] * cols]
    return a
def make_identity(n):
    result = twoDimensionlist(n, n)
    for i in range(n):
        result[i][i] = Fraction(1, 1)
    return result
def addMultiSquareMatrix(m, source_row, k, target_row):
    n = len(m)
    row_operator = make_identity(n)
    row_operator[target_row][source_row] = k
    return multiply(row_operator, m)
def getMatrixInverse(m):
    n = len(m)
    assert(len(m) == len(m[0]))
    inverse = make_identity(n)
    for col in range(n):
        diagonal_row = col
        assert(m[diagonal_row][col] != 0)
        k = Fraction(1, m[diagonal_row][col])
        m = mulSquareMatrix(m, diagonal_row, k)
        inverse = mulSquareMatrix(inverse, diagonal_row, k)
        source_row = diagonal_row
        for target_row in range(n):
            if source_row != target_row:
                k = -m[target_row][col]
                m = addMultiSquareMatrix(m, source_row, k, target_row)
                inverse = addMultiSquareMatrix(inverse, source_row, k, target_row)   
    return inverse

def FR(m1,m2):
    fr=multiply(m1,m2)
    return fr

def lcm(a, b):
    result = a * b / gcd(a, b)
    return result

def lcm_for_arrays(args):
    array_length = len(args)
    if array_length <= 2:
        return lcm(*args)
    initial = lcm(args[0], args[1])
    i = 2
    while i < array_length:
        initial = lcm(initial, args[i])
        i += 1
    return initial

def extractFractions(m):
    nonabsorbingIndices=[]
    absorbingIndices=[]
    for index, row in enumerate(m):  
        if sum(row) == 0:
            absorbingIndices.append(index)            
        else:
            nonabsorbingIndices.append(index)
    if len(absorbingIndices) == 1:        
        return [1, 1] 
    m=findProbabilityFraction(m)    
    q = Q(m, nonabsorbingIndices)
    r = R(m, nonabsorbingIndices, absorbingIndices)
    final=[]              
    f=getMatrixInverse(subtract(make_identity(len(q)), q))
    fr=FR(f,r)    
    denominator = lcm_for_arrays([item.denominator for item in fr[0]])    
    fr = [item.numerator * denominator / item.denominator for item in fr[0]]    
    fr.append(denominator)
    for x,v in enumerate(fr):
        v=int(v) 
        final.append(v)
    return final 
    
def solution(m):         
    return extractFractions(m)
