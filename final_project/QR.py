import LA

# Stable Gram - Schmidt 
def stable_gram_schmidt(matrix_01: list) -> list:
    """
    Finds the QR Factorization of a Matrix
    
    The function starts with setting V = matrix_01. Then it takes the P-norm of each
    coloumn in matrix 01 and stores it in R. Then it creates Q = product of 
    1/norm of coloumns * each coloumn. Then it prints the rows and columns. Then 
    the function takes the inner product of Q and matrix_01(V).  We then find the
    real portion of the R and stores these in r.  Next we multiply elements in negR *
    Q rows .  Lastly, we subtract the coloumns in V - the product of R elements * Q rows. 
    
    Args: 
        matrix_01: a matrix stored as a list of columns vectors(lists)
        
    Returns: [Q,R] factorization
    """
    V: list = matrix_01
    R: list = []
    for j in range(len(V)):
        R[j][j]: list = LA.p_norm(V[j], 2)
        Q: list = LA.scalor_vector_mult(1/R[j][j], V[j])
        for i in range(j, len(V)):
            R[i][j] = LA.inner_product(Q[i], V[j]).real
            V[i] = LA.add_vectors(V[i], LA.scalor_vector_mult(-R[i][j], Q[j])) 
    return [Q,R]

#Orthonormal Vectors
def orthonormal_vectors(matrix_01: list) -> list:
    """ 
    Finds an orthonormal set of vectors of same span as input set of vectors.
    
    This function finds the Q from QR factorization and returns it.  As it is an orthonormal
    span of the matrix_01.
    
    Args: 
        matrix_01: a set of vectors stored as a list of column vectors in matrix_01.
    
    Returns:
        A list of vectors as a matrix that is an orthonmormal set of vectors of the same
        span as input matrix.
    """
    return stable_gram_schmidt(matrix_01)[0]
    