"modulo principal"

from typing import Union, Any

class OitoRainhas:
    """classe com os metodos e atributos
    esperados para verificar/resolver o
    problema das oito rainhas"""
    __slots__ = ["_matriz"]
    def __init__(self, matriz: Union[ (list[list[int]], Any) ] = None ) -> None:
        self._matriz: Union[ list[list[int]], Any ] = matriz

    def __del__(self) -> None:
        "nao precisa desalocar nenhum recurso"
        return None

    def __str__(self) -> str:
        expression: str
        if self._matriz is None:
            expression = "Classe oito rainhas vazia"
        return expression

    def verifica_tabuleiro(self) -> int:
        """verifica se a configuracao do tabuleiro fornecido
        resolve o problema das 8 rainhas ou nao. Retorna -1 se a
        o tabuleiro for invalido. Retorna 1 se a solucao valida fornecida
        resolve o problema das 8 rainha. Retorna 0 se a solucao valida
        fornecida nao resolve o problema das 8 rainhas"""
        solucao: int
        if self._checa_matriz() is False:
            solucao = -1
        else:
            solucao = 0

        return solucao

    def _checa_matriz(self) -> bool:
        "verifica se a matriz e valida ou nao"
        verifica_matriz: bool
        if self._matriz is None:
            verifica_matriz = False
        elif isinstance(self._matriz, list):
            if self._matriz == []:
                verifica_matriz = False
            elif self._checa_numero_linhas() is False:
                verifica_matriz = False
            else:
                verifica_matriz = True
        else:
            verifica_matriz = False

        return verifica_matriz

    def _checa_numero_linhas(self) -> bool:
        """retorna True se a matriz do tabuleiro possui 8 linhas
        e False caso contrario """
        numero_linhas_valido: bool = len(self._matriz) == 8

        return numero_linhas_valido

    def carrega_tabuleiro(self, matriz: list[list[int]]) -> None:
        "carrega um novo tabuleiro no objeto da classe OitoRainhas"
        self._matriz = matriz

def main() -> None:
    "funcao principal"
    oito_rainhas: OitoRainhas = OitoRainhas()


    solucao_valida: int = oito_rainhas.verifica_tabuleiro()

    if solucao_valida == -1:
        print("O tabuleiro fornecido e invalido")
    elif solucao_valida == 0:
        print("O tabuleiro fornecido nao e uma solucao para o problema")
    elif solucao_valida == 1:
        print("O tabuleiro fornecido e uma solucao para o problema")

if __name__ == "__main__":
    main()
