#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.1"

########################################################
#      ATENçÃO: MODIFIQUE ESSE CÓDIGO!                 #
#   Tente utilizar dicionários onde achar conveniente  #
########################################################

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades.items():
  
    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)
    
    # sala1 que tem interseção com a atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)
    
    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)
    
    print()
    print("#" * 40)