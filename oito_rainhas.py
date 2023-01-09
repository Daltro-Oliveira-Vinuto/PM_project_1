"modulo principal"

from __future__ import annotations
from typing import Union, Any
from matriz import Matriz

class OitoRainhas:
    """classe com os metodos e atributos
    esperados para verificar/resolver o
    problema das oito rainhas"""
    __slots__ = ["_tabuleiro"]
    dimensao: int = 8
    def __init__(self, matriz: Union[ list[list[int]], Any] = None ) -> None:
        self._tabuleiro: Matriz
        if matriz is None:
            self._tabuleiro = Matriz()
        else:
            self._tabuleiro = Matriz(matriz)

    @property
    def tabuleiro(self) -> Matriz:
        "retorna o objeto da classe Matriz que corresponde ao tabuleiro"
        return self._tabuleiro

    def __del__(self) -> None:
        "desaloca recursos"
        return None

    def __str__(self) -> str:
        expression: str
        if self._tabuleiro == Matriz():
            expression = "A classe oito rainhas esta vazia"
        else:
            expression = \
            f"A classe oito rainhas tem o seguinte tabuleiro -> {self._tabuleiro}\n"
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
            elif self._checa_ataque_horizontal() is False:
                solucao = 0
            elif self._checa_ataque_diagonal_principal() is False:
                solucao = 0
            elif self._checa_ataque_diagonal_secundaria() is False:
                solucao = 0
            else:
                solucao = 1

        return solucao

    def _checa_ataque_diagonal_principal(self) -> bool:
        """Retorna False se as rainhas se atacam na diagonal principal
        e True caso contrario"""
        ataque_impossivel: bool
        ataque_impossivel = \
            self._tabuleiro.maximo_ocorrencias_diagonal_principal(1) == 1

        return ataque_impossivel

    def _checa_ataque_diagonal_secundaria(self) -> bool:
        """Retorna False se as rainhas se atacam na diagonal secundaria
        e True caso contrario"""
        ataque_impossivel: bool
        ataque_impossivel = \
            self._tabuleiro.maximo_ocorrencias_diagonal_secundaria(1) == 1

        return ataque_impossivel

    def _checa_ataque_horizontal(self) -> bool:
        "Retorna True se as rainhas nao se atacam na horizontal e False caso contrario"
        ataque_impossivel: bool
        ataque_impossivel = self._tabuleiro.maximo_ocorrencias_linha(1) == 1

        return ataque_impossivel

    def _checa_ataque_vertical(self) -> bool:
        """Funcao retorna True as rainhas nao se atacam na vertical
        e retorna False caso ao menos uma delas se ataquem"""
        ataque_impossivel: bool

        ataque_impossivel = self._tabuleiro.maximo_ocorrencias_coluna(1) == 1
        return ataque_impossivel

    def _checa_validade(self) -> bool:
        "verifica se a matriz e valida ou nao"
        verifica_tabuleiro: bool
        if isinstance(self._tabuleiro, Matriz):
            if self._tabuleiro == Matriz() or self._tabuleiro.matriz == []:
                verifica_tabuleiro = False
            elif self._checa_numero_linhas() is False:
                verifica_tabuleiro = False
            elif self._checa_numero_colunas() is False:
                verifica_tabuleiro = False
            elif self._checa_numero_rainhas() is False:
                verifica_tabuleiro = False
            else:
                verifica_tabuleiro = True
        else:
            verifica_tabuleiro = False

        return verifica_tabuleiro

    def _checa_numero_rainhas(self) -> bool:
        """Retorna True se a matriz do tabuleiro contem 8 rainhas(0)
        caso contrario retorna False """

        numero_rainhas_valido: bool = self._tabuleiro.conta_ocorrencias(1) == OitoRainhas.dimensao

        return numero_rainhas_valido

    def _checa_numero_linhas(self) -> bool:
        """retorna True se a matriz do tabuleiro possui 8 linhas
        e False caso contrario """
        numero_linhas_valido: bool = self._tabuleiro.get_numero_linhas() == OitoRainhas.dimensao

        return numero_linhas_valido

    def _checa_numero_colunas(self) -> bool:
        """Retorna True se a matriz do tabuleiro tem 8 colunas
        e False caso contrario"""
        numero_colunas_valido: bool = True

        matriz: list[list[int]] = self._tabuleiro.matriz
        for linha in matriz:
            if len(linha) != OitoRainhas.dimensao:
                numero_colunas_valido = False

        return numero_colunas_valido

    def carrega_tabuleiro(self, matriz: list[list[int]]) -> None:
        "carrega um novo tabuleiro no objeto da classe OitoRainhas"
        self._tabuleiro = Matriz(matriz)

    def carrega_string(self, string: str) -> None:
        "Recebe uma string e carrega ela na forma de matriz no objeto OitoRainhas"
        novo_tabuleiro: list[list[int]] = []
        nova_linha: list[int] = []

        for caractere in string:
            nova_linha.append(int(caractere))

            if len(nova_linha) == 8:
                novo_tabuleiro.append(nova_linha.copy())
                nova_linha.clear()

        self.carrega_tabuleiro(novo_tabuleiro)


def main() -> None:
    "funcao principal"

    oito_rainhas: OitoRainhas = OitoRainhas()

    caracteres: str = input("Digite os caracteres correspondentes ao tabuleiro: ")
    oito_rainhas.carrega_string(caracteres)
    solucao_valida: int = oito_rainhas.verifica_tabuleiro()

    print()

    if solucao_valida == -1:
        print("O tabuleiro fornecido é inválido")
    elif solucao_valida == 0:
        print("O tabuleiro fornecido não é uma solução para o problema")
    elif solucao_valida == 1:
        print("O tabuleiro fornecido é uma solução para o problema")

if __name__ == "__main__":
    main()
