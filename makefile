
go: test lint mypy

run:
	python oito_rainhas.py

test:
	pytest -v testa_oito_rainhas.py

lint:
	pylint oito_rainhas.py 
	pylint testa_oito_rainhas.py

mypy:
	mypy oito_rainhas.py
	mypy testa_oito_rainhas.py

# abre todos os arquivos no sublime
open:
	subl oito_rainhas.py
	subl testa_oito_rainhas.py
	subl makefile
	subl README.md
	subl .gitignore