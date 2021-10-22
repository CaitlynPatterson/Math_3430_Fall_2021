import pytest
import LA

#test variables
vector_01 = [1, 2, 4]
vector_02 = [3, 1, 2]
vector_03 = [0, 2, 5]
vector_04 = [5, 7, 2]
vector_05 = [0+1j, 1-2j, 3]

scalor_01 = 2
scalor_02 = -7+1j
scalor_03 = -27

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
def test_absolute_value():
    assert LA.absolute_value(scalor_02) == 7.0710678118654755+0j
    assert LA.absolute_value(scalor_03) == 27
def test_p_norm():
    assert LA.p_norm(vector_01) ==  4.58257569495584+0j
    assert LA.p_norm(vector_05) == 3.872983346207417+0j
def test_infinity_norm():
    assert LA.infinity_norm(vector_01) == 16
    assert LA.infinity_norm(vector_04) == 49
def test_infinity_p_norm():
    assert LA.infinity_p_norm(vector_01) == 4.58257569495584+0j
    assert LA.infinity_p_norm(vector_01, TRUE) == 16
def test_inner_product():
    assert LA.inner_product(vector_01, vector_02) == 13
    assert LA.inner_product(vector_02, vector_03) == 12
    
    
pytest.main()    

