
go: test lint mypy

run:
	python oito_rainhas.py

run3:
	python3 oito_rainhas.py

test:
	pytest -vv test_matriz.py
	pytest -vv testa_oito_rainhas.py

lint:
	pylint oito_rainhas.py 
	pylint testa_oito_rainhas.py
	pylint matriz.py
	pylint test_matriz.py

mypy:
	mypy oito_rainhas.py
	mypy testa_oito_rainhas.py
	mypy matriz.py
	mypy test_matriz.py

# abre todos os arquivos no editor de código Sublime
open:
	subl oito_rainhas.py
	subl testa_oito_rainhas.py
	subl matriz.py
	subl test_matriz.py

	subl makefile
	subl README.md
	subl .gitignore