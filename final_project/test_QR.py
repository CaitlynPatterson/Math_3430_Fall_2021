# -*- coding: utf-8 -*-
import QR
import pytest

matrix_01 = [[1,0,2],[2,3,4],[2,5,1]]
matrix_02 = [[5,2,1],[3,3,4],[6,2,1]]

def test_stable_gram_schmidt():
    assert QR.stable_gram_schmidt(matrix_01) == [[[0.45,0,0.89],[0,1,0],[0.89,0,-0.5]],[[2.24,0,0],[4.47,3,0],[1.79,5,1.34]]]
    assert QR.stable_gram_schmidt(matrix_02) == [[[0.91,0.37,0.18],[-0.32,0.37,0.87],[0.25,-0.86,0.45]],[[5.48,0,0],[4.56,3.63,0],[6.39,-0.32,0.25]]]

def test_orthonormal_vectors():
    assert QR.orthonormal_vectors(matrix_01) == [[0.45,0,0.89],[0,1,0],[0.89,0,-0.5]]
    assert QR.orthonormal_vectors(matrix_02) == [[0.91,0.37,0.18],[-0.32,0.37,0.87],[0.25,-0.86,0.45]]
