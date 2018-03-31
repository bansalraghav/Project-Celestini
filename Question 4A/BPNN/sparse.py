# function to multiply two sparse matrices
def sparseMultiply(mat1,mat2):
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            for k in range(len(mat1)):
                c[i][j] += mat1[i][k]*mat2[k][j]
    return c


# function to calculate convolution of two matrices
# def sparseConvolution():




a = [[0,2,0],
     [1,0,0],
     [0,0,5]]

b = [[100,0,0],
     [0,100,0],
     [0,0,100]]

c = [[0,0,0],
     [0,0,0],
     [0,0,0]]
print(sparseMultiply(a,b))
# transpose(a)
