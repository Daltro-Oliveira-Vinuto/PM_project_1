"modulo com os testes necessarios para o modulo oito_rainhas"

from __future__ import annotations
from oito_rainhas import OitoRainhas
#from modulo_auxiliar import Matriz

def test_criacao_da_classe() -> None:
    "testa se a classe foi criada e instanciada"
    oito_rainhas: OitoRainhas = OitoRainhas()

    assert isinstance(oito_rainhas, OitoRainhas)
    assert str(oito_rainhas) == "A classe oito rainhas esta vazia"


def test_tabuleiro_ausente() -> None:
    """testa se o tabuleiro(matriz) foi de fato fornecido para o objeto
    oito_rainhas"""
    oito_rainhas: OitoRainhas = OitoRainhas()

    assert oito_rainhas.verifica_tabuleiro() == -1

def test_tabuleiro_vazio() -> None:
    """ testa se o tabuleiro fornecido esta vazio """

    tabuleiro: list[list[int]]
    tabuleiro = []
    oito_rainhas: OitoRainhas = OitoRainhas(tabuleiro)

    assert oito_rainhas.verifica_tabuleiro() == -1


def test_tabuleiro_numero_linhas() -> None:
    """testa se o tabuleiro fornecido contem 8 linhas"""

    tabuleiro: list[list[int]] = [ [] for _ in range(7) ]
    oito_rainhas: OitoRainhas = OitoRainhas(tabuleiro)

    assert oito_rainhas.verifica_tabuleiro() == -1

    tabuleiro = [ [] for _ in range(6) ]
    oito_rainhas.carrega_tabuleiro(tabuleiro)
    assert oito_rainhas.verifica_tabuleiro() == -1

    tabuleiro = [ [] for _ in range(9) ]
    oito_rainhas.carrega_tabuleiro(tabuleiro)
    assert oito_rainhas.verifica_tabuleiro() == -1

    tabuleiro = [ [] for _ in range(10) ]
    oito_rainhas.carrega_tabuleiro(tabuleiro)
    assert oito_rainhas.verifica_tabuleiro() == -1

def test_tabuleiro_numero_colunas() -> None:
    "Testa se o tabuleiro fornecido contem 8 colunas"

    tabuleiro: list[list[int]] = [[0 for _ in range(7)] for _ in range(8)]
    oito_rainhas: OitoRainhas = OitoRainhas(tabuleiro)
    assert oito_rainhas.verifica_tabuleiro() == -1

    tabuleiro = [ [0 for _ in range(6) ] for _ in range(8) ]
    oito_rainhas.carrega_tabuleiro(tabuleiro)
    assert oito_rainhas.verifica_tabuleiro() == -1

    tabuleiro = [ [0 for _ in range(9) ] for _ in range(8) ]
    oito_rainhas.carrega_tabuleiro(tabuleiro)
    assert oito_rainhas.verifica_tabuleiro() == -1


    tabuleiro = [ [0 for _ in range(10) ] for _ in range(8) ]
    oito_rainhas.carrega_tabuleiro(tabuleiro)
    assert oito_rainhas.verifica_tabuleiro() == -1


def insere_oito_rainhas(tabuleiro: list[list[int]]) -> list[list[int]]:
    "insere 8 rainhas no tabuleiro, isso e, transforma a primeira coluna em 1s"
    for index_i, _ in enumerate(tabuleiro):
        for index_j, _ in enumerate(tabuleiro[index_i]):
            if index_j == 0:
                tabuleiro[index_i][index_j] = 1
    return tabuleiro

def test_numero_rainhas() -> None:
    "Verifica se existem 8 rainhas no tabuleiro"

    tabuleiro: list[list[int]] = [[0 for _ in range(8)] for _ in range(8)]
    oito_rainhas: OitoRainhas = OitoRainhas(tabuleiro)

    assert oito_rainhas.verifica_tabuleiro() == -1

    tabuleiro = [[1 for _ in range(8)] for _ in range(8)]
    oito_rainhas.carrega_tabuleiro(tabuleiro)
    assert oito_rainhas.verifica_tabuleiro() == -1


    tabuleiro_invalido: list[list[int]] = [ [0 for _ in range(8) ] for _ in range(8) ]
    tabuleiro_valido = insere_oito_rainhas(tabuleiro_invalido.copy())
    oito_rainhas.carrega_tabuleiro(tabuleiro_valido)
    assert oito_rainhas.verifica_tabuleiro() != -1

def test_rainhas_atacam_vertical() -> None:
    "Verifica se alguma das rainhas ataca as outras na vertical"

    #as rainhas das linhas 2 e 8 se atacam na verti
    tabuleiro: list[list[int]] = [
        [0,0,0,0,1,0,0,0],
        [0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,1,0],
        [0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,1,0,0],
        [0,1,0,0,0,0,0,0]
    ]

    oito_rainhas: OitoRainhas = OitoRainhas(tabuleiro)

    assert oito_rainhas.verifica_tabuleiro() == 0

def test_rainhas_atacam_horizontal() -> None:
    "Verifica se alguma das rainhas ataca as outras na horizontal"

    # as duas rainhas na linha 1 se atacam
    tabuleiro: list[list[int]] = [
        [1,0,0,0,1,0,0,0],
        [0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,1,0],
        [0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0]
    ]

    oito_rainhas: OitoRainhas = OitoRainhas(tabuleiro)

    assert oito_rainhas.verifica_tabuleiro() == 0

def test_rainhas_atacam_diagonal_principal() -> None:
    "Verifica se alguma das rainhas ataca outra na diagonal principal"

    # as duas rainhas nas posicoes 7x6 e 8x7 se atacam na diagonal principal
    tabuleiro: list[list[int]] = [
        [0,0,0,0,1,0,0,0],
        [0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [1,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,1,0]
    ]

    oito_rainhas: OitoRainhas = OitoRainhas(tabuleiro)

    assert oito_rainhas.verifica_tabuleiro() == 0

def test_rainhas_atacam_diagonal_secundaria() -> None:
    "Verifica se alguma das rainhas ataca outra na diagonal secundaria"

    # as duas rainhas nas posicoes 7x6 e 8x5 se atacam na diagonal secundaria
    tabuleiro: list[list[int]] = [
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,1],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,1,0],
        [0,0,1,0,0,0,0,0],
        [0,1,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0],
        [1,0,0,0,0,0,0,0]
    ]

    oito_rainhas: OitoRainhas = OitoRainhas(tabuleiro)

    assert oito_rainhas.verifica_tabuleiro() == 0

def test_verifica_tabuleiro_contem_solucao() -> None:
    "Verifica se uma possivel solucao do problema das 8 rainhas é reconhecida"

    tabuleiro: list[list[int]] = [
        [0,0,0,0,1,0,0,0],
        [0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,1,0],
        [0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,1,0,0],
        [1,0,0,0,0,0,0,0]
    ]


    oito_rainhas: OitoRainhas = OitoRainhas(tabuleiro)

    assert oito_rainhas.verifica_tabuleiro() == 1
