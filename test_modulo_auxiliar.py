
from __future__ import annotations
from modulo_auxiliar import Matriz

def test_compara_matrizes():
	"Testa se dois objetos matrizes sao iguais"

	matriz_a: Matriz = Matriz([[1,2,3],[4,5,6]])
	matriz_b: Matriz = Matriz([[4,5,6],[1,2,3]])
	matriz_c: Matriz = Matriz([[1,2,3],[4,5,6]])
	
	assert matriz_a == matriz_c
	assert matriz_a != matriz_b

def test_matriz_transposta():
	"Testa se a matriz foi transposta corretamente"
	matriz: Matriz = Matriz([[1,2,3],[4,5,6]])

	assert matriz.transposta() == Matriz( [[1,4],[2,5],[3,6]] )


def test_conta_ocorrencias():
	"testa se o metodo testa_ocorrencias contou a quantidade correta"

	lista: list[list[int]] = [[6, 2, 2],[6,5,2]]
	matriz: Matriz = Matriz(lista)

	assert matriz.conta_ocorrencias(10) == 0
	assert matriz.conta_ocorrencias(5) == 1
	assert matriz.conta_ocorrencias(6) == 2
	assert matriz.conta_ocorrencias(2) == 3


def test_maximo_ocorrencias_linha():
	"testa o numero maximo da ocorrencia de uma valor nas linhas da matriz"
	lista: list[list[int]] = [[5,2,3],\
							  [7,6,7],\
							  [4,4,4]]
	matriz: Matriz = Matriz(lista)

	assert matriz.conta_maximo_ocorrencias_linha(7) == 2
	assert matriz.conta_maximo_ocorrencias_linha(2) == 1
	assert matriz.conta_maximo_ocorrencias_linha(10) == 0
	assert matriz.conta_maximo_ocorrencias_linha(4) == 3


def test_maximo_ocorrencias_coluna():
	"testa o numero maximo da ocorrencia de uma valor nas colunas da matriz"
	lista: lista[list[int]] = [[5,7,4],\
	                           [2,6,4],\
	                           [3,7,4]]
	matriz: Matriz = Matriz(lista)

	assert matriz.conta_maximo_ocorrencias_coluna(7) == 2
	assert matriz.conta_maximo_ocorrencias_coluna(2) == 1
	assert matriz.conta_maximo_ocorrencias_coluna(10) == 0
	assert matriz.conta_maximo_ocorrencias_coluna(4) == 3