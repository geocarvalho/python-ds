#!/usr/bin/env python3
"""Hello world multi linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execucao:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "George Carvalho"
__license__ = "Unlicense"

import os


current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, world!"

if current_language == "pt_BR":
    msg = "Ola, mundo!"
elif current_language == "it_IT":
    msg = "Ciao, mondo!"
elif current_language == "es_SP":
    msg = "Hola, mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, monde!"

print(msg)