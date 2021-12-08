import LA
import QR
import LS

print("My name is Caitlyn Patterson.  This is a library of basic linear algebra.")

print("LA.py contains a large number of functions for performing basic linear algebra tasks.")

print("The first function in LA.py is add_vectors. It will take in two vectors as its arguments and return their sum.")
print("For example, if a = [1,2] and b = [3,4], then add_vectors(a,b) will return")
a = [1,2]
b = [3,4]
print(LA.add_vectors(a,b))

print("The next function is scalor_vector_mult It will take a vector and a scalor as its arguments and return their product.")
print("For example, if a = [1,2, 4] and b = 2, then scalor_vector_mult(b, a) will return")
a = [1, 2, 4]
b = 2
print(LA.scalor_vector_mult(b, a))
      
print("The next function is scalor_matrix_mult It will take a matrix and a scalor as its arguments and return their product.")
print("For example, if a = [[1, 2, 4]. [3, 1, 2], [0, 2, 5]] and b = 2, then scalor_matrix_mult(b, a) will return")
a = [[1, 2, 4], [3, 1, 2], [0, 2, 5]]
b = 2
print(LA.scalor_matrix_mult(b, a))
      
print("The next function is matrix_add It will take two matricies as its arguments and return their sum.")
print("For example, if a = [[1, 2, 4]. [3, 1, 2], [0, 2, 5]] and b = [[0, 2, 5],[1, 2, 4]. [3, 1, 2]], then matrix_add(a,b) will return")
a = [[1, 2, 4], [3, 1, 2], [0, 2, 5]]
b = [[0, 2, 5], [1, 2, 4], [3, 1, 2]]
print(LA.matrix_add(a, b))

print("The next function is matrix_vector_mult It will take a matrix and a vector as its arguments and return their product.")
print("For example, if a = [1, 2, 4] and b = [[0, 2, 5],[1, 2, 4]. [3, 1, 2]], then matrix_vector_mult(a,b) will return")
a = [1, 2, 4]
b = [[0, 2, 5], [1, 2, 4], [3, 1, 2]]
print(LA.matrix_vector_mult(a, b))

print("The next function is matrix_matrix_mult It will take two matricies as its arguments and return their product.")
print("For example, if a = [[1, 2, 4]. [3, 1, 2], [0, 2, 5]] and b = [[0, 2, 5],[1, 2, 4]. [3, 1, 2]], then matrix_matrix_mult(a,b) will return")
a = [[1, 2, 4], [3, 1, 2], [0, 2, 5]]
b = [[0, 2, 5], [1, 2, 4], [3, 1, 2]]
print(LA.matrix_matrix_mult(a, b))

print("The next function is absolute value. It will take a scalor as its argument and return it's absolute value.")
print("For example, if a = -3, absolute_value(a) will return")
a = -3
print(LA.absolute_value(a))

print("The next function is p_norm. It will take a vector as its argument and return it's p_norm.")
print("For example, if a = [1, 2, 4], p_norm(a) will return")
a = [1, 2, 4]
print(LA.p_norm(a))

print("The next function is infinity_norm. It will take a vector as its argument and return it's infinity norm.")
print("For example, if a = [1, 2, 4], infinity_norm(a) will return")
a = [1, 2, 4]
print(LA.infinity_norm(a))

print("The next function is infinity_p_norm. It will take a vector, and boolean value as its argument and return it's infinity norm when true and p norm when false.")
print("For example, if a = [1, 2, 4], infinity_p_norm(a) will return")
a = [1, 2, 4]
print(LA.infinity_p_norm(a))

print("The next function is inner_product. It will take two vectors as its argument and return it's inner product.")
print("For example, if a = [1, 2, 4] b = [3, 1, 2], inner_product(a,b) will return")
a = [1, 2, 4]
b = [3, 1, 2]
print(LA.inner_product(a,b))


print("QR.py contains a few functions that perfrom various forms of QR factorization.")

print("The first function is stable_gram_schmidt. It will take a matrix as its argument and return it's QR factorization.")
print("For example, if a = [[1, 2, 4], [3, 1, 2], [0, 2, 5]], stable_gram_schmidt(a) will return")
a = [[1, 2, 4], [3, 1, 2], [0, 2, 5]]
print(QR.stable_gram_schmidt(a))

print("The next function is orthonormal_vectors. It will take a matrix as its argument and return a list of vectors as a matrix that is an orthonmormal set of vectors of the same span as input matrix..")
print("For example, if a = [[1, 2, 4], [3, 1, 2], [0, 2, 5]], orthonormal_vectors(a) will return")
a = [[1, 2, 4], [3, 1, 2], [0, 2, 5]]
print(QR.orthonormal_vectors(a))


print("LS.py contains a function that finds the least squares of a matrix and vector.")

print("The least_squares function will take a matrix and a vector as its arguments and return it's least squares.")
print("For example, if a = [[1, 2, 4], [3, 1, 2], [0, 2, 5]] b = [3, 1, 2], least_squares(a,b) will return")
a = [[1, 2, 4], [3, 1, 2], [0, 2, 5]]
b = [3, 1, 2]
print(LS.least_squares(a,b))



