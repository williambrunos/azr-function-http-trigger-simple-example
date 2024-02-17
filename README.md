# About this project

This project has the goal to store the necessary artifacts to run a simple HTTP triggered azure function locally.

## About function app

The azure function is a simple hello world function that will be ran locally on your computer.

## How to run the function locally

Follow this documentation:

[Create your first python function on azure functions](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-decorators)

[Azure functions python developer guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Capplication-level&pivots=python-mode-decorators)

* Install azure core tools
* Install azure functions extension
* Run and debug python function (F5 on vs code)

## How to run the function tests

After deploying locally the azure function, open another python terminal and run the following commands:

````bash
.\venv\Scripts\activate
pip install -r requirements.txt
cd tests/function_app_test
pytest http_example_test.py
````

