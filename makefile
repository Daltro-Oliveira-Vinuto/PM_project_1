
go: test lint mypy

run:
	python oito_rainhas.py

test:
	pytest -v testa_oito_rainhas.py
	pytest -v

lint:
	pylint oito_rainhas.py 
	pylint testa_oito_rainhas.py
	pylint modulo_auxiliar.py

mypy:
	mypy oito_rainhas.py
	mypy testa_oito_rainhas.py
	mypy modulo_auxiliar.py

# abre todos os arquivos no editor de código Sublime
open:
	subl oito_rainhas.py
	subl testa_oito_rainhas.py
	subl modulo_auxiliar.py 

	subl makefile
	subl README.md
	subl .gitignore