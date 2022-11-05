#!/usr/bin/env python3
""" Calculadora infix.
Funcionamento:
[operacao] [n1] [n2]

Operacoes:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7
$ infixcalc.py mul 10 5
50
$ infixcalc.py
operacao: sum
n1: 5
n2: 4
9
"""

import os
import click
from datetime import datetime


__version__ = "v0.1.0"

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(__version__)
    ctx.exit()

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
@click.option(
    "--operation", "-o", default="None", 
    help="Operation option", prompt=True,
    required=True, show_default=True,
    type=click.Choice(['sum', 'sub', 'mul', 'div'], case_sensitive=False))
@click.option(
    "--number1", "-n1", default="None", 
    help="First value for operation", prompt=True, 
    required=True, type=float, show_default=True)
@click.option(
    "--number2", "-n2", default="None", 
    help="Second value for operation", prompt=True, 
    required=True, type=float, show_default=True)
def main(operation, number1, number2):
    """ Script to calculate operations for the given numbers

    Usage: python3 infixcalc.py -o mul -n1 2 -n2 3 
    """
    path = os.curdir
    timestamp = datetime.now().isoformat()
    user = os.getenv("USER", "anonymous")
    filepath = os.path.join(path, "infixcalc.log")
    # Check type of operation
    if operation == "sum":
        result = number1 + number2
    elif operation == "sub":
        result = number1 - number2
    elif operation == "mul":
        result = number1 * number2
    elif operation == "div":
        result = number1 / number2
    else:
        print(f"Operation not found: {operation}")
        exit()
    # print(f"{operation},{number1},{number2} = {result}\n", file=open(filepath, "a"))
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp}_{user}: {operation},{number1},{number2} = {result}\n")
    print(result)
if __name__ == "__main__":
    main()