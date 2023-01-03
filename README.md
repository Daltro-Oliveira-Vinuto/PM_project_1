<h1>
	Projeto 1 da disciplina Métodos de Programação
</h1>

<h2>
	Aluno: Daltro Oliveira Vinuto , Matrícula: 160025966
</h2>

<p> 
	O pré-requisito inicial é que o usuário deve estar na pasta contendo esse README.md no terminal de comandos do seu SO.
</p>

<p>
	 Esse projeto deve ser executado preferencialmente em um computador com SO Windows com makefile instalado, ou em computador com SO Linux. Para isso siga as seguintes instruções.
</p>
<ul> Obs.: O python 3.10, pytest e pylint necessitam estar instalados no SO.
	<li> Para executar o programa digite: make run </li>
	<li> Para realizar os testes digite: make test </li>
	<li> Para executar o analisador estático de código: make lint </li>
	<ul> Obs.: Para executar as próximas duas instruções o módulo mypy necessita estar instalado
		<li> Para realizar a verificação de tipos com o mypy: make mypy </li>
		<li> Para executar os testes, analisador estático e o mypy digite: make </li>
	</ul>
</ul>


<p>
	Se o seu SO nao suporta makefile ou ele não está instalado então siga as seguintes instruções:
</p> 

<p> Obs.: O python 3.10, pytest e pylint necessitam estar instalados no SO.
	<ul>
		<li> Para executar o programa digite: python oito_rainhas.py </li>
		<li> Para realizar os testes digite: pytest -v testa_oito_rainhas.py </li>
		<li> Para executar o analisador estático de código: pylint oito_rainhas.py </li>
	</ul>
</p>





