"Modulo com classes e funcoes auxiliares para o projeto"

from __future__ import annotations
from typing import Any

class Matriz:
    "Classe com metodos e atributos relacionados a matrizes"
    __slots__= ("_name", "_matriz","numero_linhas", "numero_colunas")
    def __init__(self, matriz: list[list[Any]] = \
        [[0 for _ in range(3)] for _ in range(3)], name: str="matriz") -> None:
        self._matriz: list[list[Any]] = matriz
        self._name = name
        if self._matriz != []:
            self.numero_linhas = self.get_numero_linhas()
            self.numero_colunas = self.get_numero_colunas()
        else:
            self.numero_linhas = 0
            self.numero_colunas = 0

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


    def transposta(self) -> Matriz:
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
        "Retorna o numero de ocorrencia de 'valor' dentro da matriz"
        numero_ocorrencias: int = 0
        for linha in self._matriz:
            for coluna in linha:
                if coluna == valor:
                    numero_ocorrencias+= 1
        return numero_ocorrencias

    def maximo_ocorrencias_linha(self, valor: Any) -> int:
        "Retorna o numero maximo de vezes que 'valor' aparece em cada linha"
        numero_maximo_ocorrencias: int = 0
        for linha in self._matriz:
            numero_ocorrencias:int  = 0
            for coluna in linha:
                if coluna == valor:
                    numero_ocorrencias+= 1

            numero_maximo_ocorrencias = \
                maior(numero_ocorrencias, numero_maximo_ocorrencias)

        return numero_maximo_ocorrencias

    def maximo_ocorrencias_coluna(self, valor: Any) -> int:
        "Retorna o numero maximo de vezes que 'valor' aparece em cada coluna"
        numero_maximo_ocorrencias: int

        matriz_transposta: Matriz = self.transposta()
        numero_maximo_ocorrencias = \
            matriz_transposta.maximo_ocorrencias_linha(valor)

        return numero_maximo_ocorrencias

    def verifica_limites_matriz(self, index_i: int, index_j: int) -> bool:
        "Retorna True se os indices estao dentro dos limites da matriz e False caso contrario"
        dentro_limites: bool

        dentro_limites = (index_i < self.numero_linhas and index_j < self.numero_colunas) and \
            (index_i >= 0 and index_j >= 0)
        return dentro_limites

    def maximo_ocorrencias_diagonal_principal(self, valor: Any) -> int:
        """Retorna o numero de maximo de vezes que 'valor'
        aparece em cada diagonal principal"""

        elementos_origem: list[ tuple[int,int] ] = []
        for index_i, linha in enumerate(self._matriz):
            for index_j, _ in enumerate(linha):
                if index_i == 0 or index_j == 0:
                    elementos_origem.append((index_i, index_j))

        maximo_ocorrencias: int = 0
        for (index_i_inicial, index_j_inicial) in elementos_origem:
            numero_ocorrencias:int = 0

            index_i = index_i_inicial
            index_j = index_j_inicial
            while self.verifica_limites_matriz(index_i, index_j) is True:
                valor_posicao: int = self._matriz[index_i][index_j]
                if valor_posicao == valor:
                    numero_ocorrencias+= 1
                index_i+=1
                index_j+=1

            maximo_ocorrencias = maior(maximo_ocorrencias, numero_ocorrencias)



        return maximo_ocorrencias

    def maximo_ocorrencias_diagonal_secundaria(self, valor: Any) -> int:
        """Retorna o numero de maximo de vezes que 'valor'
        aparece em cada diagonal secundaria"""

        elementos_origem: list[ tuple[int,int] ] = []
        for index_i, linha in enumerate(self._matriz):
            for index_j, _ in enumerate(linha):
                if index_i == 0 or index_j == self.numero_colunas-1:
                    elementos_origem.append((index_i, index_j))


        maximo_ocorrencias: int = 0
        for (index_i_inicial, index_j_inicial) in elementos_origem:
            numero_ocorrencias:int = 0
            index_i = index_i_inicial
            index_j = index_j_inicial
            while self.verifica_limites_matriz(index_i, index_j) is True:
                valor_posicao: int = self._matriz[index_i][index_j]
                if valor_posicao == valor:
                    numero_ocorrencias+= 1
                index_i+=1
                index_j-=1

            maximo_ocorrencias = maior(maximo_ocorrencias, numero_ocorrencias)


        return maximo_ocorrencias

def maior(valor_a: Any, valor_b: Any) -> Any:
    "Retorna o maior entre dois valores"
    maior_valor: Any
    if valor_a >= valor_b:
        maior_valor = valor_a
    else:
        maior_valor = valor_b

    return maior_valor
