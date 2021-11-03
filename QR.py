import LA


# Unstable Gram - Schmidt
def unstable_gram_schmidt(matrix_01: list) -> list:
    for i in range(1, n+1):
        V: list = matrix_01[i]
        for j in range(1,j):
            Q: list = [0 for element in matrix_01]
            R[j][i]: list = LA.inner_product(Q[j], V)
            V = LA.add_vectors(V, LA.scalor_matrix_mult(R[j][i], Q[j]))
            R[i][i] = LA.p_norm(V[j])
            Q[i] = LA.scalor_vector_mult(1/(r[i][i]), V[j])
    return[Q,R]
            
    

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
    for j in range(len(V)):
        R[j][j]: list = LA.p_norm(V[j], 2)
        Q: list = LA.scalor_vector_mult(1/R[j][j], V[j])
        for i in range(j+1, len(V)):
            print(i)
            print(j)
            R[i][j] = LA.inner_product(Q[i], V[j]).real
            V[j] = LA.add_vectors(V[j], LA.scalor_vector_mult(-R[j][i], Q[i]))
    return[Q,R]