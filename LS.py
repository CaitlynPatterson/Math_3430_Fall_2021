import LA
import QR

def backsub(matrix: list, 
            vector: list) -> list:
    """ 
    preforms backsubstitution 
    
    Beginning with a triangle matrix this function solves matrix * X = vector (input).
    This creates a result vector equal to the solutions of the equation.
    
    Args:
        matrix: a triangle matrix made up of column vectors saved as lists
        vector: a column vector saved as a list
        
    Returns: the back sub of a matrix and vector
    """ 
    result: list = [vector[-1]*(1/(matrix[-1][-1]))]
    for current in range(len(matrix) -1, -1. -1):
        temp: float = vector[current]
        for index in range(len(result)):
            temp -= matrix[len(matrix)-1-index][current]*result[current]
        temp *= 1/(matrix[current][current])
        result.append(temp)
    result = result[:: -1]
    return result

def least_squares(matrix: list,
                  vector: list) -> list:
    """ 
    this function finds the least squares of a matrix and a vector.
    
    Starting with a matrix and a vector this function uses the gram schmidt equation
    for QR factorization to find the least squares.
    
    Args: 
        Matrix: a matrix made of a list of column vectors
        Vector: a list of floats
    Returns: the least squares of a matrix. 
    """ 
    temp: list = QR.stable_gram_schmidt(matrix)
    result: list = matrix.conjugate 
    result = LA.matrix_vector_mult(vector, result)
    result = backsub(temp[1], result)
    return result

    


