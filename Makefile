PIP3=$(shell which pip3)
host=127.0.0.1
port=5000
threaded=True
url=$(host):$(port)

run: ## FLASK_APP=./main.py flask run
	FLASK_APP=./main.py flask run

