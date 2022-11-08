#!/usr/bin/env python3
""" Bloco de notas

$ notes.py new "Minha nota"
tag: tech
text:
Anotacao geral sobre carreira de tecnologia

$ notes.py read --tag=tech
"""

__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.tsv")
arguments = sys.argv[1:]
if not arguments:
    print(f"Invalid usage, you should specify subcommand: {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    # leitura de notas
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()


if arguments[0] == "new":
    # criancao da anotacao
    title = arguments[1] # TODO: tratar excecao
    text = [
        f"{title}",
        input("tag: ").strip(),
        input("text: \n").strip() + "\n"
    ]
    with open(filepath, "a") as file_:
        file_.write("\t".join(text))