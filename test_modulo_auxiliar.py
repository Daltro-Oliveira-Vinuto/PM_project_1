
from __future__ import annotations
from modulo_auxiliar import Matriz

def test_compara_matrizes():
	matriz_a: Matriz = Matriz([[1,2,3],[4,5,6]])
	matriz_b: Matriz = Matriz([[4,5,6],[1,2,3]])
	matriz_c: Matriz = Matriz([[1,2,3],[4,5,6]])
	
	assert matriz_a == matriz_c
	assert matriz_a != matriz_b

def test_matriz_transposta():
	matriz: Matriz = Matriz([[1,2,3],[4,5,6]])

	assert matriz.transposta() == Matriz( [[1,4],[2,5],[3,6]] )
