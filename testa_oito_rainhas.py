"modulo com os testes necessarios para o modulo oito_rainhas"
from oito_rainhas import OitoRainhas

def test_criacao_classes() -> None:
    "testa se a classe foi criada e instanciada"
    oito_rainhas: OitoRainhas = OitoRainhas()

    assert str(oito_rainhas) == "Classe oito rainhas vazia"


def test_tabuleiro_vazio() -> None:
    """testa se o tabuleiro(matriz) fornecido para o objeto
    oito_rainhas e vazio"""
    oito_rainhas: OitoRainhas = OitoRainhas()

    assert oito_rainhas.verifica_tabuleiro() == -1
