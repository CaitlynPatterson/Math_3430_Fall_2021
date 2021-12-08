# Problem #0

def add_vectors(vector_a: list,
                vector_b: list) -> list:
    """Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
    """ 
    result = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result

# Problem #1

def scalor_vector_mult(scalor_01: float, 
                       vector_01: list) -> list:
    """Multiplies the vector input by the scalor input. 
    
    Creates a result vector stored as a list of 0' s the same length as the input
    vector_01 then overwrites each element of the result vector with the correspoding 
    element of the product of the input vector and scalor.  Achieves this for loop
    over the length of result.
    
    Args:
        scalor_01: A scalor stored as a number(float)
        vector_01: A vector stored as a list
        
    Returns:
        The product of the input vector by the scalor input stored as a list.
    """
    result: list = [0 for element in vector_01]
    for index in range(len(result)):
        result[index] = scalor_01 * vector_01[index]
    return result

# Problem #2

def scalor_matrix_mult(scalor_01: float,
                       matrix_01: list) -> list:
    """Multiplies the matrix input by the scalor input.
    
    Creates a result matrix stored as a list of 0's the same length as the input
    matrix_01. Then overwrites each element of the result matrix with the corresponding
    scalor vector muliplication of the scalor and each column vector in matrix_01.
    Repeats this over the length of result.
    
    Args:
        scalor_01: A scalor stored as a number(float)
        matrix_01: A matrix stored as a list of lists that represent column vectors
        
    Returns: A matrix equal to the product of the scalor and matrix that is stored as
        a list of lists that respresent column vectos.
    """
    result: list = [0 for element in matrix_01]
    for index in range(len(result)):
        result[index] = scalor_vector_mult(scalor_01, matrix_01[index])
    return result

# Problem #3

def matrix_add(matrix_01: list,
               matrix_02: list) -> list:
    """Adds the imput matricies together.
    
    Creates a result matrix stored as a list of 0's the same length as the input
    matrix_01.  Then overwrites each element of the result matrix with the corresponding
    addition of the column vectors in the inputs.  Repeats this over the lenth of result
    
    Args: 
        matrix_01: A matrix stored as a list of lists that represent column vectors.
        matrix_02: A matrix stored as a list of lists that represent column vectors
            of the same size to matrix_01.
            
    Returns: A matrix equal to the addition of the inputs - stored as a list of 
        lists which represent column vectors.
    """
    result: list = [0 for element in matrix_01]
    for index in range(len(result)):
        result[index] = add_vectors(matrix_01[index], matrix_02[index])
    return result

# Problem #4

def matrix_vector_mult(vector_01: list, 
                       matrix_01: list) -> list:
    """Multiples matrix by a vector
    
    Creates a result matrix stored as a list of 0's the same length as the input 
    matrix_01.  Then overwrites each element of the result matrix with the addition 
    of the result and the scalor_vector_multiplication the first element of vector_01
    and the first element of matrix_01.  This continues for each element of vector_01.
    
    Args:
        vector_01: A vector stored as a list, that has the same number of rows as
            matrix_01 has columns. 
        matrix_01: A matrix stored as a list of lists that represent column vectors.
    
    Returns: A vector qual to the matrix vector multiplication, stored as a 
        list of lists that represent column vectors. 
    """
    result: list = [0 for element in matrix_01]
    for index in range(len(vector_01)):
        result = add_vectors(result, scalor_vector_mult(vector_01[index], matrix_01[index]))
    return result

# Problem #5
def matrix_matrix_mult(matrix_01: list, 
                       matrix_02: list) -> list:
    """Mutliplies the input matricies
    
    Creates a result matrix stored as a list of 0's the same length as the input
    matrix_01.  Then overwrites each element of the result matrix with the 
    matrix_vector_mult of the first vector in matrix_02 and matrix_01. This will
    continue for the length of matrix_01.
    
    Args:
        matrix_01: A matrix stored as a list of lists that represent column vectors.
        matrix_02: A matrix stored as a list of lists that represent column vectors,
            that has the same number of rows as matrix_01 has columns.
    
    Returns: A matrix stored as a list of lists that represent column vectors. 
    """
    result: list = [0 for element in matrix_01]
    for index in range(len(result)):
        result[index] = matrix_vector_mult(matrix_02[index], matrix_01)
    return result

# Problem #6

def absolute_value(scalor: complex) -> float:
    """ 
    Finds the absolute value of any number.
    
    This will create a result number that is equal to the conjugate of the scalor 
    * scalor and then takes the square root of the result. 
    
    Args:
        scalor: A scalor stored as a complex number. (python will convert any 
                numbers that are not stored as complex into complex)
    
    Returns: The absolute value of the input.
    """ 
    result: float = scalor*scalor.conjugate()
    result = result**(1/2)
    return result

# Problem #7

def p_norm(vector: list,
           scalor: float = 2) -> float:
    """
    Finds the p_norm of a vector(list).
    
    This function will create a result list of equal length to input vector.
    It then adds together the absolute values of each element in the vector to 
    the power of the scalor.  the result is then to the power of 1/scalor.
    
    Args:
        vector: stored as a list of complex, float, or ints.
        scalor: stored as a float, defaults to 2
    
    Returns: The p_norm of the vector that is input. 
    """
    result: float = 0
    for index in range(len(vector)):
        result += absolute_value(vector[index])**scalor
    result = result**(1/scalor)
    return result

# Problem #8

def infinity_norm(vector: list) -> float:
    """ 
    Finds the infinity norm of a vector(list)
    
    The function first creates a result equal to 0 and then checks it against 
    each absolute value of each element and replace it with each larger element.  
    
    Args: 
        vector: stored as a list.
        
    Returns: the infinity norm of the vector that is input. 
    """
    result: list = 0
    for index in range(len(vector)):
        if absolute_value(index) >= result:
            result = absolute_value[index]
            return result

# Problem #9

def infinity_p_norm(vector: list,
                    scalor: float = 2,
                    inf_flag: bool = False) -> float:
    """ 
    Find the infinity norm or p norm of a vector
    
    This function finds the p_norm of a vector if true and the infinity norm if
    false,  
    
    Args: 
        vector: a vector stored as a list
        scalor: a scalor stored as a float set to default to 2
        boolean: a boolean value set to default FALSE
        
    Returns: the p_norm or infinity norm respectively
    """ 
    if inf_flag:
        result = infinity_norm(vector)
    else: 
        result = p_norm(vector, scalor)
    return result

# Problem #10

def inner_product(vector_01: list,
                  vector_02: list) -> float:
    """
    Finds the inner product of 2 vectors(lists)
    
    This functin finds the inner product of two vectors by taking the conjugate
    of the first vector and then multiplies the vectors against each other and adds
    the new elements. 
    
    Args:
        vector_01: a vector stored as a list
        vector_02: a vector stored as a list
    Returns: the inner product of the two vectors
    """ 
    result: float = [0 for element in vector_01]
    for index in range(len(result)):
        result[index] = vector_01[index].conjugate()
        result = sum(result[index]*vector_02[index])
    return result











