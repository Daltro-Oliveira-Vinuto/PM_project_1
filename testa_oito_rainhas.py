"modulo com os testes necessarios para o modulo oito_rainhas"
from oito_rainhas import OitoRainhas

def test_criacao_classes() -> None:
    "testa se a classe foi criada e instanciada"
    oito_rainhas: OitoRainhas = OitoRainhas()

    assert str(oito_rainhas) == "Classe oito rainhas vazia"


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
