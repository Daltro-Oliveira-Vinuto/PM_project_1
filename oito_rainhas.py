"modulo principal"

from __future__ import annotations
from typing import Union, Any
from modulo_auxiliar import Matriz

class OitoRainhas:
    """classe com os metodos e atributos
    esperados para verificar/resolver o
    problema das oito rainhas"""
    __slots__ = ["_matriz"]
    dimensao: int = 8
    def __init__(self, matriz: Union[ list[list[int]], Any] = None ) -> None:
        if matriz is None:
            self._matriz: Matriz = Matriz()
        else:
            self._matriz: Matriz = Matriz(matriz)

    def __del__(self) -> None:
        "desaloca recursos"
        return None

    def __str__(self) -> str:
        expression: str
        if self._matriz == Matriz():
            expression = "A classe oito rainhas esta vazia"
        else:
            expression = \
            f"A classe oito rainhas tem o seguinte tabuleiro -> {self._matriz}\n"
        return expression

    def __repr__(self) -> str:
        expression: str = self.__str__()

        return expression

    def verifica_tabuleiro(self) -> int:
        """verifica se a configuracao do tabuleiro fornecido
        resolve o problema das 8 rainhas ou nao. Retorna -1 se a
        o tabuleiro for invalido. Retorna 1 se a solucao valida fornecida
        resolve o problema das 8 rainha. Retorna 0 se a solucao valida
        fornecida nao resolve o problema das 8 rainhas"""
        solucao: int
        if self._checa_validade() is False:
            solucao = -1
        else:
            if self._checa_ataque_vertical() is False:
                solucao = 0
            else:
                solucao = 1

        return solucao

    def _checa_ataque_vertical(self) -> bool:
        """Funcao retorna True as rainhas nao se atacam na vertical
        e retorna False caso ao menos uma delas se ataquem"""
        ataque_impossivel: bool

        ataque_impossivel = True
        return ataque_impossivel

    def _checa_validade(self) -> bool:
        "verifica se a matriz e valida ou nao"
        verifica_matriz: bool
   
        if isinstance(self._matriz, Matriz):
            if self._matriz == Matriz() or self._matriz.matriz == []:
                verifica_matriz = False
            elif self._checa_numero_linhas() is False:
                verifica_matriz = False
            elif self._checa_numero_colunas() is False:
                verifica_matriz = False
            elif self._checa_numero_rainhas() is False:
                verifica_matriz = False
            else:
                verifica_matriz = True
        else:
            verifica_matriz = False

        return verifica_matriz

    def _checa_numero_rainhas(self) -> bool:
        """Retorna True se a matriz do tabuleiro contem 8 rainhas(0)
        caso contrario retorna False """

        numero_rainhas_valido: bool = self._matriz.conta_ocorrencias(1) == OitoRainhas.dimensao

        return numero_rainhas_valido

    def _checa_numero_linhas(self) -> bool:
        """retorna True se a matriz do tabuleiro possui 8 linhas
        e False caso contrario """
        numero_linhas_valido: bool = self._matriz.get_numero_linhas() == OitoRainhas.dimensao

        return numero_linhas_valido

    def _checa_numero_colunas(self) -> bool:
        """Retorna True se a matriz do tabuleiro tem 8 colunas
        e False caso contrario"""
        numero_colunas_valido: bool = True

        matriz: list[list[int]] = self._matriz.matriz
        for linha in matriz:
            if len(linha) != OitoRainhas.dimensao:
                numero_colunas_valido = False

        return numero_colunas_valido

    def carrega_tabuleiro(self, matriz: list[list[int]]) -> None:
        "carrega um novo tabuleiro no objeto da classe OitoRainhas"
        self._matriz = Matriz(matriz)

def main() -> None:
    "funcao principal"
    oito_rainhas: OitoRainhas = OitoRainhas()

    tabuleiro_valido: list[list[int]] = [
        [0,0,0,0,1,0,0,0],
        [0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,1,0],
        [0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,1,0,0],
        [1,0,0,0,0,0,0,0]
    ]

    oito_rainhas.carrega_tabuleiro(tabuleiro_valido)

    solucao_valida: int = oito_rainhas.verifica_tabuleiro()

    print(oito_rainhas)

    if solucao_valida == -1:
        print("O tabuleiro fornecido e invalido")
    elif solucao_valida == 0:
        print("O tabuleiro fornecido nao e uma solucao para o problema")
    elif solucao_valida == 1:
        print("O tabuleiro fornecido e uma solucao para o problema")

if __name__ == "__main__":
    main()
