"modulo com os testes necessarios para o modulo oito_rainhas"
from oito_rainhas import OitoRainhas

def test_criacao_classes() -> None:
    "testa se a classe foi criada e instanciada"
    oito_rainhas: OitoRainhas = OitoRainhas()

    assert str(oito_rainhas) == "Classe oito rainhas"
