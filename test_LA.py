import pytest
import LA

#test variables
vector_01 = [1, 2, 4]
vector_02 = [3, 1, 2]
vector_03 = [0, 2, 5]
vector_04 = [5, 7, 2]

scalor_01 = 2

matrix_01 = [vector_01, vector_02, vector_03]
matrix_02 = [vector_02, vector_04, vector_01]
matrix_03 = [vector_04, vector_01, vector_02]

def test_add_vectors():
    assert LA.add_vectors(vector_01, vector_02) == [4,3,6] 
    assert LA.add_vectors(vector_02, vector_03) == [3,3,7]
def test_scalor_vector_mult():
    assert LA.scalor_vector_mult(scalor_01, vector_01) == [2,4,8]
    assert LA.scalor_vector_mult(scalor_01, vector_03) == [0,4,10]
def test_scalor_matrix_mult():
    assert LA.scalor_matrix_mult(scalor_01, matrix_01) == [[2,4,8],[6,2,4],[0,4,10]]
    assert LA.scalor_matrix_mult(scalor_01, matrix_02) == [[6,2,4],[10,14,4],[2,4,8]]
def test_matrix_add():
    assert LA.matrix_add(matrix_01, matrix_02) == [[4,3,6],[8,8,4],[1,4,9]]
    assert LA.matrix_add(matrix_01, matrix_03) == [[6,9,6],[4,3,6],[3,3,7]]
def test_matrix_vector_mult():
    assert LA.matrix_vector_mult(vector_01, matrix_01) == [7,12,28]
    assert LA.matrix_vector_mult(vector_03, matrix_02) == [15,24,24]
def test_matrix_matrix_mult():
    assert LA.matrix_matrix_mult(matrix_01, matrix_02) == [[6,11,24],[26,21,44],[7,12,28]]
    assert LA.matrix_matrix_mult(matrix_02, matrix_01) == [[17,23,22],[16,14,16],[15,24,24]]
pytest.main()    

