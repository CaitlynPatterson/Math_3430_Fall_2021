"""
For this homework assignment we will take our work from HW01 and use it to
prepare a python script which will implement our algoirthms as python functions. 

For Problems #0-5 from HW01, Do the following.



1) Write your answer from HW01 in a comment.

2) Below the comment write a function which implements the algorithm from your
comment. If you find that you need to change your algorithm for your python
code, you must edit your answer in the comment. 

3) Test each of your functions on at least 2 inputs. 

4) Upload your .py file to a github repo named "Math_3430_Fall_2021"

This assignment is due by 11:59pm 09/27/2021. Do NOT upload an updated version to github
after that date. 
"""


#Example:

#Problem 00

"""
-The Three Questions

Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 

-PsuedoCode

def add_vectors(vector_a,vector_b):

Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

Return the desired result.
"""

def add_vectors(vector_a,vector_b):
  result = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result

#End Example


#Problem 01
"""Write an algorithm to implement scalar-vector multiplication.

Q1: What do we have?

A1: A scalor stored as scalor_01 and a vector stored as a list as vector_01 on a computer. 

Q2: What do we want?

A2: A new vector that has components equal to the scalor multiplied by the original vector; the new vector will be stored as a list. 

Q3: How will we get there?

A3: We will create an empty vector of same size as the original vector - vector_01 and store the product of the scalor multiplied by the original vector - vector_01.


def scalor_vector_mult(scalor_01,vector_01):

# Initializing result as a list containing 0 the same length os vector_01
result = []

# Set each element of result to be equal to the desired product.
for index in range(length(result)):
  result[index] = scalor_01 * vector_01[index]

# Return the desired result.
return result
"""
def scalor_vector_mult(scalor_01, vector_01):
    result = [0 for element in vector_01]
    for index in range(len(result)):
        result[index] = scalor_01 * vector_01[index]
    return result

#Problem 02
"""
Write an algorithm to implement scalar-matrix multiplication.

Q1: What do we have?

A1: A scalor stored as scalor_01 and a matrix stored as a list of column vectors as matrix_01 on a computer. 

Q2: What do we want?

A2: A new matrix that has corresponding components equal to the scalor multiplied by each component in the original matrix; the new matrix will be stored as a list of column vectors. 

Q3: How will we get there?

A3: We will create an empty matrix of same size as the original matrix - matrix_01 and store the product of the scalor multiplied by each component of matrix_01.


def scalor_matrix_mult(scalor_01,matrix_01):

# Initializing result containing 0 the same length as matrix_01
result = []

# Using previous algorithm scalor_vector_mult, run this algorithm on each vector in result.

For index in range(length(result)):
	result[index] = scalor_vector_mult(scalor_01, matrix_01[index]

# Return the desired result.
return result
"""
def scalor_matrix_mult(scalor_01, matrix_01):
    result = [0 for element in matrix_01]
    for index in range(len(result)):
        result[index] = scalor_vector_mult(scalor_01, matrix_01[index])
    return result

#Problem 03
"""
Write an algorithm to implement matrix addition.


Q1: What do we have?

A1: 2 matricies stored as a lists of column vectors as matrix_01 and matrix_02 on a computer. 

Q2: What do we want?

A2: A new matrix that has corresponding components equal to the addition of corresponding elements in matrix_01 and matrix_02. 

Q3: How will we get there?

A3: We will create an empty matrix of same size as the original matrix - matrix_01 and store the product of the scalor multiplied by each component of matrix_01.


def matrix_add(matrix_01, matrix_02):

# Initializing result as a list containg 0 equal length to matrix_01
result = []

# Using previous algorithm add_vectors, run this algorithm on each corresponding vectors of inputs and place output in corresoponding vector of result. 

For index in range(length(result)):
	result[index] = add_vectors(matrix_01[index], matrix_02[index])

# Return the desired result.
return result

"""
def matrix_add(matrix_01, matrix_02):
    result = [0 for element in matrix_01]
    for index in range(len(result)):
        result[index] = add_vectors(matrix_01[index], matrix_02[index])
    return result

#Problem 04
"""Write an algorithm to implement matrix-vector multiplication using the linear
combination of columns method. You must use the algorithms from Problem #0 and
Problem #1.  

Q1: What do we have?

A1: A vector stored as a list and a matrix stored as a list of column vectors as matrix_01.  Both stored on a computer. 

Q2: What do we want?

A2: A new vector that has elements equal to the scalor x matrix multiplication.  

Q3: How will we get there?

A3: We will create an empty vector of size equal to vector_01.  First we will multiply each column vector in Matrix_01 by the corresponding element in the vector to create 3 new vectors. Then using the algorithm from #0 we will add the vectors together to create the desired vector.


def matrix_vector_mult(vector_01, matrix_01):

# Initializing result as a list containg 0 equal length to vector_01
result = [0 for element matrix_01]

# Using previous algorithm scalor_vector_mult, run this algorithm on each vector in matrix_01 using corresponding element of Vector_01 storing result in result. 

For index in range(length(result)):
	result[index] = scalor_vector_mult(vector_01[index], matrix_01[index])

#intialize result vector as a list:
result_02 = [0 for element vector_01]

# run add_vectors on each vector in result_01
for index in range(length(result)):
	result_02[index] = add_vectors(result_01[index])

# Return the desired result.
return result_02
"""
def matrix_vector_mult(vector_01, matrix_01):
    result = [0 for element in matrix_01]
    for index in range(len(result)):
        result[index] = scalor_vector_mult(vector_01[index], matrix_01[index])
    result_02 = [0 for element in vector_01]
    for index in range(len(result_02)):
        result_02[index] = add_vectors(result[index], result[index+1])
    return result_02
#Problem 05



#Test Inputs

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
test_vector_03 = [0, 2, 5]
test_vector_04 = [5, 7, 2]
test_vector_05 = [1,2]

test_scalor_01 = 2

test_matrix_01 = [test_vector_01, test_vector_02, test_vector_03]
test_matrix_02 = [test_vector_02, test_vector_04, test_vector_01]
#Problem 0: tests
# add_vectors(test_vector_01,test_vector_02) should output [4,3,6]
print('Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_02)))
print('Should have been [4,3,6]')
# add_vectors(test_vector_01, test_vector_030) should output [1,4,9]
print('Test Output 2 for add_vectors: ' + str(add_vectors(test_vector_01, test_vector_03)))
print('Should have been [1,4,9]')

#Problem 1: tests
# scalor_vector_mult(test_scalor_01, test_vector_01) should output [2,4,8]
print('Test Output for scalor_vector_mult:'+ str(scalor_vector_mult(test_scalor_01, test_vector_01)))
print('Should have been [2,4,8]')
# scalor_vector_mult(test_scalor_01, test_vector_03) should output [0,4,10]
print('Test Output for scalor_vector_mult:'+ str(scalor_vector_mult(test_scalor_01, test_vector_03)))
print('Should have been [0,4,10]')

#Problem 2: tests
# scalor_matrix_mult(test_scalor_01, test_matrix_01) should output [[2,4,8],[6,2,4],[0,4,10]]
print('Test Output for scalor_matrix_mult:'+ str(scalor_matrix_mult(test_scalor_01, test_matrix_01)))
print('Should have been [[2,4,8],[6,2,4],[0,4,10]]')
# scalor_matrix_mult(test_scalor_01, test_matrix_02) should output [[6,2,4], [10,14,4],[2,4,8]]
print('Test Output for scalor_matrix_mult:'+ str(scalor_matrix_mult(test_scalor_01, test_matrix_02)))
print('Should have been [[6,2,4],[10,14,4],[2,4,8]]')

#Problem 3: tests
# matrix_add(test_matrix_01, test_matrix_02) should output [[4,3,6],[8,8,4],[1,4,9]]
print('Test Output for matrix_add:'+ str(matrix_add(test_matrix_01, test_matrix_02)))
print('Should have been [[4,3,6],[8,8,4],[1,4,9]]')

#Problem 4: tests
# matrix_vector_mult(test_vector, test_matrix_02) should output
print('Test Output for matrix_vector_mult:'+ str(matrix_vector_mult(test_vector_01, test_matrix_01)))

