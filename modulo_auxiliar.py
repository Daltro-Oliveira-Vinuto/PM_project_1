"Modulo com classes e funcoes auxiliares para o projeto"

from __future__ import annotations
from typing import Any

class Matriz:
    "Classe com metodos e atributos relacionados a matrizes"
    __slots__= ("_name", "_matriz")
    def __init__(self, matriz: list[list[Any]] = \
        [[0 for _ in range(3)] for _ in range(3)], name: str="matriz") -> None:
        self._matriz: list[list[Any]] = matriz
        self._name = name

    def __del__(self) -> None:
        pass

    def __str__(self) -> str:
        string: str = ""

        string += f"{self._name}: \n\n"
        for index_i, linha in enumerate(self._matriz):
            for index_j, coluna in enumerate(linha):
                if index_j == len(linha)-1:
                    string +=f"{coluna} \n"
                else:
                    string += f"{coluna}, "
            if index_i == len(self._matriz)-1:
                string+= "\n"

        return string

    def __repr__(self) -> str:
        return self.__str__()

    def get_numero_linhas(self) -> int:
        "retorna numero de linhas da matriz"
        return len(self._matriz)

    def get_numero_colunas(self) -> int:
        "retorna numero de colunas da matriz"
        return len(self._matriz[0])

    @property
    def matriz(self) -> list[list[Any]]:
        "Encapsula o acesso a variavel protected _matriz"
        return self._matriz

    @matriz.setter
    def matriz(self, new_matriz: list[list[Any]]) -> None:
        self._matriz = new_matriz


    def transposta(self) -> matriz:
        "Retorna uma matriz transposta a matriz fornecida"

        numero_linhas_transposta = self.get_numero_colunas()
        numero_colunas_transpota = self.get_numero_linhas()

        matriz_transposta: list[list[Any]] = \
            [ [0 for _ in range(numero_colunas_transpota)] \
                for _ in range(numero_linhas_transposta)]

        for index_i, linha in enumerate(self._matriz):
            for index_j, coluna in enumerate(linha):
                matriz_transposta[index_j][index_i] = coluna

        return Matriz(matriz_transposta)

    def __eq__(self,other) -> bool:
        "Retorna True se as duas matrizes sao iguais e falso caso contrario"

        encontrou_diferenca: bool = False

        if self.get_numero_linhas() == other.get_numero_linhas() and\
            self.get_numero_colunas() == other.get_numero_colunas():


            for index_i, linha in enumerate(self._matriz):
                for index_j, _ in enumerate(linha):
                    if self._matriz[index_i][index_j] != other.matriz[index_i][index_j]:
                        encontrou_diferenca = True

        else:
            encontrou_diferenca = True

        return not encontrou_diferenca

    def __ne__(self, other) -> bool:
        "Retorna True se as duas matrizes forem diferentes e False caso contrario"
        return not self.__eq__(other)


    def conta_ocorrencias(self, valor: Any) -> int:
        numero_ocorrencias: int = 0

        for index_i, linha in enumerate(self._matriz):
            for index_j, coluna in enumerate(linha):
                if coluna == valor:
                    numero_ocorrencias+= 1


        return numero_ocorrencias