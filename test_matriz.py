"modulo que testa as funcionalidades do modulo matriz.py"

from __future__ import annotations
from matriz import Matriz

def test_compara_matrizes() -> None:
    "Testa se dois objetos matrizes sao iguais"

    matriz_a: Matriz = Matriz([[1,2,3],[4,5,6]])
    matriz_b: Matriz = Matriz([[4,5,6],[1,2,3]])
    matriz_c: Matriz = Matriz([[1,2,3],[4,5,6]])
    assert matriz_a == matriz_c
    assert matriz_a != matriz_b

def test_matriz_transposta() -> None:
    "Testa se a matriz foi transposta corretamente"
    matriz: Matriz = Matriz([[1,2,3],[4,5,6]])

    assert matriz.transposta() == Matriz( [[1,4],[2,5],[3,6]] )


def test_conta_ocorrencias() -> None:
    "testa se o metodo testa_ocorrencias contou a quantidade correta"

    lista: list[list[int]] = [[6, 2, 2],[6,5,2]]
    matriz: Matriz = Matriz(lista)

    assert matriz.conta_ocorrencias(10) == 0
    assert matriz.conta_ocorrencias(5) == 1
    assert matriz.conta_ocorrencias(6) == 2
    assert matriz.conta_ocorrencias(2) == 3


def test_maximo_ocorrencias_linha() -> None:
    "testa o numero maximo da ocorrencia de uma valor nas linhas da matriz"
    lista: list[list[int]] = [[5,2,3],\
                              [7,6,7],\
                              [4,4,4]]
    matriz: Matriz = Matriz(lista)

    assert matriz.maximo_ocorrencias_linha(7) == 2
    assert matriz.maximo_ocorrencias_linha(2) == 1
    assert matriz.maximo_ocorrencias_linha(10) == 0
    assert matriz.maximo_ocorrencias_linha(4) == 3


def test_maximo_ocorrencias_coluna() -> None:
    "testa o numero maximo da ocorrencia de uma valor nas colunas da matriz"
    lista: list[list[int]] = [[5,7,4],\
                               [2,6,4],\
                               [3,7,4]]
    matriz: Matriz = Matriz(lista)

    assert matriz.maximo_ocorrencias_coluna(7) == 2
    assert matriz.maximo_ocorrencias_coluna(2) == 1
    assert matriz.maximo_ocorrencias_coluna(10) == 0
    assert matriz.maximo_ocorrencias_coluna(4) == 3

def test_maximo_ocorrencias_diagonal_principal() -> None:
    "testa o numero maximo de ocorrencias de um valor em todas as diagonais principais"

    lista: list[list[int]] = [[5,1,3],
                              [4,5,1],
                              [9,8,5]]

    matriz: Matriz = Matriz(lista)

    assert matriz.maximo_ocorrencias_diagonal_principal(3) == 1
    assert matriz.maximo_ocorrencias_diagonal_principal(1) == 2
    assert matriz.maximo_ocorrencias_diagonal_principal(5) == 3
    assert matriz.maximo_ocorrencias_diagonal_principal(4) == 1
    assert matriz.maximo_ocorrencias_diagonal_principal(8) == 1
    assert matriz.maximo_ocorrencias_diagonal_principal(9) == 1
    assert matriz.maximo_ocorrencias_diagonal_principal(10) == 0

def test_maximo_ocorrencias_diagonal_secundaria() -> None:
    "testa o numero maximo de ocorrencias de um valor em todas as diagonais secundarias"

    lista: list[list[int]] = [[3,1,5],
                              [1,5,8],
                              [5,4,9]]

    matriz: Matriz = Matriz(lista)

    assert matriz.maximo_ocorrencias_diagonal_secundaria(3) == 1
    assert matriz.maximo_ocorrencias_diagonal_secundaria(1) == 2
    assert matriz.maximo_ocorrencias_diagonal_secundaria(5) == 3
    assert matriz.maximo_ocorrencias_diagonal_secundaria(8) == 1
    assert matriz.maximo_ocorrencias_diagonal_secundaria(4) == 1
    assert matriz.maximo_ocorrencias_diagonal_secundaria(9) == 1
    assert matriz.maximo_ocorrencias_diagonal_secundaria(10) == 0
    