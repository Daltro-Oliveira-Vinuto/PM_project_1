"modulo principal"

from typing import Union, Any

class OitoRainhas:
    """classe com os metodos e atributos
    esperados para verificar/resolver o
    problema das oito rainhas"""
    __slots__ = ["_matriz"]
    def __init__(self, matriz: Union[ (list[list[int]], Any) ] = None ) -> None:
        self._matriz: list[list[int]] = matriz

    def __del__(self) -> None:
        "nao precisa desalocar nenhum recurso"
        return None

    def __str__(self) -> str:
        return "Classe oito rainhas"

def main() -> None:
    "funcao principal"
    oito_rainhas: OitoRainhas = OitoRainhas()

    print(oito_rainhas)

if __name__ == "__main__":
    main()
