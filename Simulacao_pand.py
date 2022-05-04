# PRIMEIRA FUNÇÃO DE TODAS!!!!!! ------ ACABADO
print()
print('\033[7;31mSIMULAÇÃO DE PANDEMIA\033[m')
print('Feito por Miguel Branco, Gonçalo Lopes e Simão Cardoso')
print('---------------------')
print()


import sys

pessoas = [{'Código': 0, 'Coordenadas': [15, 15], 'Faixa etária': 'Adulto', 'Sintomas': [], 'Infetado': 'Sim',
            'Semana do teste positivo': [], 'Semana de infeção': 1, 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []},
           {'Código': [], 'Coordenadas': [], 'Faixa etária': [], 'Sintomas': [], 'Infetado': [],
            'Semana do teste positivo': [], 'Semana de infeção': [], 'Lista de contacto social': []}]

import random


def criar_pessoas(pessoas):
    for i in range(1, len(pessoas)):
        x = random.randint(0, 30)
        y = random.randint(0, 30)
        pessoas[i]['Código'] = i
        pessoas[i]['Coordenadas'] = [x, y]
        pessoas[i]['Faixa etária'] = random.choice(['Jovem', 'Adulto', 'Idoso', 'Doente'])
        pessoas[i]['Sintomas'] = []
        pessoas[i]['Infetado'] = 'Não'
        pessoas[i]['Semana do teste positivo'] = []
        pessoas[i]['Semana de infeção'] = []
        pessoas[i]['Lista de contacto social'] = []

    return pessoas




# FUNÇÃO COORDENADAS ALEATÓRIAS ------- ACABADO

#------------------------------------------
import random


def movimento_pessoas(pessoas):
    coordenadas = []
    for i in range(len(pessoas)):
        x = random.randint(0,30)
        y = random.randint(0,30)
        pessoas[i]['Coordenadas'] = (x,y)
        coordenadas += [pessoas[i]['Código'],(x,y)]
    return coordenadas


# FUNÇÃO COMPARAR DISTÂNCIAS

import math
#-----------------------------------

def distância_infetados(pessoas):
    c = 2
    contactos = []
    for i in range(len(pessoas)):
        pessoas[i]['Lista de contacto social'] = []
        for k in range(len(pessoas)):
            p1 = pessoas[i]['Coordenadas']
            p2 = pessoas[k]['Coordenadas']
            if p1 != p2 and c >= round(math.dist(p1,p2)):
                pessoas[i]['Lista de contacto social'] += [pessoas[k]['Código']]


    for i in range(len(pessoas)):
            contactos += [pessoas[i]['Código'],pessoas[i]['Lista de contacto social']]


    return contactos
#-----------------------------------

def capacidadeContaminadora(pessoas, n):
    if (pessoas[n]['Faixa etária']) == 'Jovem':
        return 0.85
    if (pessoas[n]['Faixa etária']) == 'Adulto':
        return 0.70
    if (pessoas[n]['Faixa etária']) == 'Idoso':
        return 0.50
    if (pessoas[n]['Faixa etária']) == 'Doente':
        return 0.65


def threshold(pessoas, n):
    if (pessoas[n]['Faixa etária']) == 'Jovem':
        return 0.92
    if (pessoas[n]['Faixa etária']) == 'Adulto':
        return 0.60
    if (pessoas[n]['Faixa etária']) == 'Idoso':
        return 0.50
    if (pessoas[n]['Faixa etária']) == 'Doente':
        return 0.45


def crialista_infetados(pessoas):
    infetados = []
    for i in range(len(pessoas)):
        if pessoas[i]['Infetado'] == 'Sim':
            infetados += [pessoas[i]['Código']]
    return infetados


def crialista_naoinfetados(pessoas):
    nao_infetados = []
    for i in range(len(pessoas)):
        if pessoas[i]['Infetado'] == 'Não' or pessoas[i]['Infetado'] == 'Imune':
            nao_infetados += [pessoas[i]['Código']]
    return nao_infetados


def coef_virus(semana):
    if semana >= 5 and semana <= 21 or semana >= 39 and semana <= 47:
        n = 0.9375
    elif semana >= 22 and semana <= 38:
        n = 0.6375
    elif semana >= 1 and semana <= 4 or semana >= 48 and semana <= 52:
        n = 0.75
    return n


def ver_se_esta_infetado(pessoas, semana):
    for i in range(len(pessoas)):
        if pessoas[i]['Infetado'] != 'Imune':
            for k in pessoas[i]['Lista de contacto social']:
                if k in crialista_infetados(pessoas):
                    d = (capacidadeContaminadora(pessoas, k)) * coef_virus(semana)
                    t = (threshold(pessoas, i))
                    if d > t:
                        pessoas[i]['Infetado'] = 'Sim'
                        pessoas[i]['Semana de infeção'] = semana
    return pessoas

#------------------------------------------

def sintomas_random(pessoas, semana):
    for i in range(len(pessoas)):
        if pessoas[i]['Infetado'] == 'Sim' and pessoas[i]['Sintomas'] == [] and semana == pessoas[i][
            'Semana de infeção'] + 2:
            a = random.randint(1, 100)
            if a > 50:
                pessoas[i]['Sintomas'] += ['Tosse seca']
            b = random.randint(1, 100)
            if b > 50:
                pessoas[i]['Sintomas'] += ['Febre']
            c = random.randint(1, 100)
            if c > 60:
                pessoas[i]['Sintomas'] += ['Febre alta']
            d = random.randint(1, 100)
            if d > 95:
                pessoas[i]['Sintomas'] += ['Náuseas']
            e = random.randint(1, 100)
            if e > 95:
                pessoas[i]['Sintomas'] += ['Diarreia']
            f = random.randint(1, 100)
            if f > 95:
                pessoas[i]['Sintomas'] += ['Cefaléia']
            g = random.randint(1, 100)
            if g > 80:
                pessoas[i]['Sintomas'] += ['Dores musculares']
            h = random.randint(1, 100)
            if h > 20:
                pessoas[i]['Sintomas'] += ['Cansaço geral']
            u = random.randint(1, 100)
            if u > 60:
                pessoas[i]['Sintomas'] += ['Dificuldades respiratórias']
            j = random.randint(1, 100)
            if j > 20:
                pessoas[i]['Sintomas'] += ['Nariz entupido']
            k = random.randint(1, 100)
            if k > 30:
                pessoas[i]['Sintomas'] += ['Dores de garganta']
            l = random.randint(1, 100)
            if l > 30:
                pessoas[i]['Sintomas'] += ['Perda de apetite ou olfato']
            m = random.randint(1, 100)
            if m > 30:
                pessoas[i]['Sintomas'] += ['Dor no peito']
            n = random.randint(1, 100)
            if n > 95:
                pessoas[i]['Sintomas'] += ['Vômitos']
            o = random.randint(1, 100)
            if o > 10:
                pessoas[i]['Sintomas'] += ['Espirros']
            p = random.randint(1, 100)
            if p > 95:
                pessoas[i]['Sintomas'] += ['Olhos húmidos']

    return pessoas


# Função que dá a lista de sintomas




def lista_sintomas(pessoas):
    sintomas = []
    for i in range(len(pessoas)):
        sintomas += [pessoas[i]['Código'], pessoas[i]['Sintomas']]
    return sintomas


#------------------------------------------------

import random


def hospitalizado(pessoas, semana):
    hospitalizados = []
    s = ['Dificuldades respiratórias', 'Febre alta', 'Dor no peito']
    for i in range(len(pessoas)):
        for j in range(len(s)):
            if s[j] in pessoas[i]['Sintomas']:
                x = random.randint(0, 30)
                y = random.randint(0, 30)
                pessoas[i]['Coordenadas'] = (x, y)
                pessoas[i]['Semana do teste positivo'] = semana
                pessoas[i]['Infetado'] = 'Imune'
                pessoas[i]['Sintomas'] = []
                hospitalizados += [{'Código': pessoas[i]['Código'],
                                    'Semana do teste positivo': pessoas[i]['Semana do teste positivo']}]
    if hospitalizados == []:
        return ('Não há pessoas hospitalizadas')

    return hospitalizados


#------------------------------------------------

def quarentena(pessoas, semana):
    quarentena = []
    v = ['Dificuldades respiratórias', 'Febre alta', 'Dor no peito']

    for i in range(len(pessoas)):
        for j in v:
            if pessoas[i]['Sintomas'] != [] and j not in pessoas[i]['Sintomas']:
                pessoas[i]['Coordenadas'] = [40, 40]
                if pessoas[i]['Semana do teste positivo'] == []:
                    pessoas[i]['Semana do teste positivo'] = semana
                else:
                    pessoas[i]['Semana do teste positivo'] = pessoas[i]['Semana do teste positivo']

                quarentena += [{'Código': pessoas[i]['Código'],
                                'Semana do teste positivo': pessoas[i]['Semana do teste positivo']}]

    if quarentena == []:
        return ('Não há pessoas em quarentena')

    return remove_repetidos(quarentena)


def remove_sintomas(pessoas, semana):
    for i in range(len(pessoas)):
        if semana - 2 == pessoas[i]['Semana do teste positivo']:
            pessoas[i]['Sintomas'] = []
            pessoas[i]['Infetado'] = 'Imune'
    return pessoas


def remove_repetidos(l):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return res


#------------------------------------------------------------- RETRO
def hospitalizado_retrovirus(pessoas, semana):
    hospitalizados = []
    s = ['Linfadenopatia', 'Faringite', 'Dores articulares']
    for i in range(len(pessoas)):
        for j in range(len(s)):
            if s[j] in pessoas[i]['Sintomas']:
                x = random.randint(0, 30)
                y = random.randint(0, 30)
                pessoas[i]['Coordenadas'] = (x, y)
                pessoas[i]['Semana do teste positivo'] = semana
                pessoas[i]['Infetado'] = 'Imune'
                pessoas[i]['Sintomas'] = []
                hospitalizados += [{'Código': pessoas[i]['Código'],
                                    'Semana do teste positivo': pessoas[i]['Semana do teste positivo']}]
    if hospitalizados == []:
        return ('Não há pessoas hospitalizadas')

    return hospitalizados


def sintomas_retrovirus(pessoas, semana):
    for i in range(len(pessoas)):
        if pessoas[i]['Infetado'] == 'Sim' and pessoas[i]['Sintomas'] == [] and semana == pessoas[i]['Semana de infeção'] + 2:
            a = random.randint(1, 100)
            if a > 4:
                pessoas[i]['Sintomas'] += ['Febre']
            b = random.randint(1, 100)
            if b > 26:
                pessoas[i]['Sintomas'] += ['Linfadenopatia']
            c = random.randint(1, 100)
            if c > 30:
                pessoas[i]['Sintomas'] += ['Faringite']
            d = random.randint(1, 100)
            if d > 73:
                pessoas[i]['Sintomas'] += ['Náuseas']
            e = random.randint(1, 100)
            if e > 68:
                pessoas[i]['Sintomas'] += ['Diarreia']
            f = random.randint(1, 100)
            if f > 30:
                pessoas[i]['Sintomas'] += ['Irritação na pele']
            g = random.randint(1, 100)
            if g > 46:
                pessoas[i]['Sintomas'] += ['Dores musculares']
            h = random.randint(1, 100)
            if h > 46:
                pessoas[i]['Sintomas'] += ['Dores articulares']
            j = random.randint(1, 100)
            if j > 68:
                pessoas[i]['Sintomas'] += ['Dores de cabeça']
            k = random.randint(1, 100)
            if k > 73:
                pessoas[i]['Sintomas'] += ['Vômitos']

    return pessoas


def capacidadeContaminadora_retrovirus(pessoas, n):
    if (pessoas[n]['Faixa etária']) == 'Jovem':
        return 0.90
    if (pessoas[n]['Faixa etária']) == 'Adulto':
        return 0.80
    if (pessoas[n]['Faixa etária']) == 'Idoso':
        return 0.45
    if (pessoas[n]['Faixa etária']) == 'Doente':
        return 0.60


def threshold(pessoas, n):
    if (pessoas[n]['Faixa etária']) == 'Jovem':
        return 0.92
    if (pessoas[n]['Faixa etária']) == 'Adulto':
        return 0.60
    if (pessoas[n]['Faixa etária']) == 'Idoso':
        return 0.50
    if (pessoas[n]['Faixa etária']) == 'Doente':
        return 0.45


def coef_retrovirus(semana):
    if semana >= 5 and semana <= 21 or semana >= 39 and semana <= 47:
        n = 0.90
    elif semana >= 22 and semana <= 38:
        n = 0.75
    elif semana >= 1 and semana <= 4 or semana >= 48 and semana <= 52:
        n = 0.85
    return n


def ver_se_esta_infetado_retrovirus(pessoas, semana):
    for i in range(len(pessoas)):
        if pessoas[i]['Infetado'] != 'Imune':
            for k in pessoas[i]['Lista de contacto social']:
                if k in crialista_infetados(pessoas):
                    d = (capacidadeContaminadora_retrovirus(pessoas, k)) * (coef_retrovirus(semana))
                    t = (threshold(pessoas, i))
                    if d > t:
                        pessoas[i]['Infetado'] = 'Sim'
                        pessoas[i]['Semana de infeção'] = semana
    return pessoas


def quarentena_retrovirus(pessoas, semana):
    quarentena = []
    v = ['Linfadenopatia', 'Faringite', 'Dores articulares']

    for i in range(len(pessoas)):
        for j in v:
            if pessoas[i]['Sintomas'] != [] and j not in pessoas[i]['Sintomas']:
                pessoas[i]['Coordenadas'] = [40, 40]
                if pessoas[i]['Semana do teste positivo'] == []:
                    pessoas[i]['Semana do teste positivo'] = semana
                else:
                    pessoas[i]['Semana do teste positivo'] = pessoas[i]['Semana do teste positivo']

                quarentena += [{'Código': pessoas[i]['Código'],
                                'Semana do teste positivo': pessoas[i]['Semana do teste positivo']}]

    if quarentena == []:
        return ('Não há pessoas em quarentena')

    return remove_repetidos(quarentena)


def remove_sintomas(pessoas, semana):
    for i in range(len(pessoas)):
        if semana - 2 == pessoas[i]['Semana do teste positivo']:
            pessoas[i]['Sintomas'] = []
            pessoas[i]['Infetado'] = 'Imune'
    return pessoas


def remove_repetidos(l):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return res


###############################################################  #ADENO
def sintomas_adenovirus(pessoas,semana):
    for i in range(len(pessoas)):
        if pessoas[i]['Infetado'] == 'Sim' and pessoas[i]['Sintomas'] == [] and semana == pessoas[i]['Semana de infeção'] + 2:
            a = random.randint(1,100)
            if a > 10:
                pessoas[i]['Sintomas'] += ['Febre']
            b = random.randint(1,100)
            if b > 15:
                pessoas[i]['Sintomas'] += ['Nariz entupido']
            c = random.randint(1,100)
            if c > 30:
                pessoas[i]['Sintomas'] += ['Garganta inflamada']
            d = random.randint(1,100)
            if d > 43:
                pessoas[i]['Sintomas'] += ['Tosse']
            e = random.randint(1,100)
            if e > 47:
                pessoas[i]['Sintomas'] += ['Espirros']
            f = random.randint(1,100)
            if f > 21:
                pessoas[i]['Sintomas'] += ['Perda de olfato']
            g = random.randint(1,100)
            if g > 39:
                pessoas[i]['Sintomas'] += ['Dores musculares']
            h = random.randint(1,100)
            if h > 66:
                pessoas[i]['Sintomas'] += ['Bronquite']
            j = random.randint(1,100)
            if j > 50:
                pessoas[i]['Sintomas'] += ['Dores de cabeça']
            k = random.randint(1,100)
            if k > 69:
                pessoas[i]['Sintomas'] += ['Pneumonia']
            l = random.randint(1,100)
            if l > 63:
                pessoas[i]['Sintomas'] += ['Conjuntivite']
            m = random.randint(1,100)
            if m > 59:
                pessoas[i]['Sintomas'] += ['Gastroenterite']
            n = random.randint(1,100)
            if n > 89:
                pessoas[i]['Sintomas'] += ['Inflamação na bexiga']
            o = random.randint(1,100)
            if o > 98:
                pessoas[i]['Sintomas'] += ['Doenças neurológicas']
    return pessoas

def capacidadeContaminadora_adenovirus(pessoas,n):
    if (pessoas[n]['Faixa etária']) == 'Jovem':
        return 0.70
    if (pessoas[n]['Faixa etária']) == 'Adulto':
        return 0.70
    if (pessoas[n]['Faixa etária']) == 'Idoso':
        return 0.50
    if (pessoas[n]['Faixa etária']) == 'Doente':
        return 0.60


def threshold(pessoas,n):
    if (pessoas[n]['Faixa etária']) == 'Jovem':
        return 0.92
    if (pessoas[n]['Faixa etária']) == 'Adulto':
        return 0.60
    if (pessoas[n]['Faixa etária']) == 'Idoso':
        return 0.50
    if (pessoas[n]['Faixa etária']) == 'Doente':
        return 0.45

def coef_virus_adenovirus(semana):
    if semana >= 5 and semana <= 21 or semana >= 39 and semana <= 47:
        n = 0.75
    elif semana >= 22 and semana <= 38:
        n = 0.55
    elif semana >= 1 and semana <= 4 or semana >= 48 and semana <= 52:
        n = 0.70
    return n

def ver_se_esta_infetado_adenovirus(pessoas,semana):
    for i in range(len(pessoas)):
        if pessoas[i]['Infetado'] != 'Imune':
            for k in pessoas[i]['Lista de contacto social']:
                if k in crialista_infetados(pessoas):
                    d = (capacidadeContaminadora_adenovirus(pessoas,k)) * (coef_virus_adenovirus(semana))
                    t = (threshold(pessoas,i))
                    if d > t:
                        pessoas[i]['Infetado'] = 'Sim'
                        pessoas[i]['Semana de infeção'] = semana
    return pessoas


import random


def hospitalizado_adenovirus(pessoas, semana):
    hospitalizados = []
    s = ['Bronquite', 'Pneumonia', 'Conjuntivite', 'Gastroenterite', 'Inflamação na bexiga', 'Doenças neurológicas']
    for i in range(len(pessoas)):
        for j in range(len(s)):
            if s[j] in pessoas[i]['Sintomas']:
                x = random.randint(0, 30)
                y = random.randint(0, 30)
                pessoas[i]['Coordenadas'] = (x, y)
                pessoas[i]['Semana do teste positivo'] = semana
                pessoas[i]['Infetado'] = 'Imune'
                pessoas[i]['Sintomas'] = []
                hospitalizados += [{'Código': pessoas[i]['Código'],
                                    'Semana do teste positivo': pessoas[i]['Semana do teste positivo']}]
    if hospitalizados == []:
        return ('Não há pessoas hospitalizadas')

    return hospitalizados


def quarentena_adenovirus(pessoas, semana):
    quarentena = []
    v = ['Bronquite', 'Pneumonia', 'Conjuntivite', 'Gastroenterite', 'Inflamação na bexiga', 'Doenças neurológicas']

    for i in range(len(pessoas)):
        for j in v:
            if pessoas[i]['Sintomas'] != [] and j not in pessoas[i]['Sintomas']:
                pessoas[i]['Coordenadas'] = [60, 60]
                if pessoas[i]['Semana do teste positivo'] == []:
                    pessoas[i]['Semana do teste positivo'] = semana
                else:
                    pessoas[i]['Semana do teste positivo'] = pessoas[i]['Semana do teste positivo']

                quarentena += [{'Código': pessoas[i]['Código'],
                                'Semana do teste positivo': pessoas[i]['Semana do teste positivo']}]

    if quarentena == []:
        return ('Não há pessoas em quarentena')

    return remove_repetidos(quarentena)


def remove_sintomas(pessoas, semana):
    for i in range(len(pessoas)):
        if semana - 2 == pessoas[i]['Semana do teste positivo']:
            pessoas[i]['Sintomas'] = []
            pessoas[i]['Infetado'] = 'Imune'
    return pessoas


def remove_repetidos(l):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return res

################################################################
def menu_opcoes():
    print('-----------------')
    print('1 - Criar pessoas')
    print('2 - Sair')
    print('-----------------')
    opcao = input('=>')
    return opcao

def menu3():
    print('--------------------------------')
    print('1 - Próxima semana')
    print('2 - Mostrar posições das pessoas')
    print('3 - Sair')
    print('--------------------------------')
    op = input('=>')
    return op
def menuvirus():
    print('Selecione o Vírus')
    print('1 - Corona Vírus')
    print('2 - Adeno Vírus')
    print('3 - Retro Vírus')
    print('4 - Sair')
    opv = input('=>')
    return opv


# FUNÇÃO COORDENADAS ALEATÓRIAS -------


# FUNÇÃO COMPARAR DISTÂNCIAS   ---- POR ACABAR

import math


#################################################################

mt = [[]] * 41  # criar uma matriz vazia
for i in range(41):
    mt[i] = [' '] * 41

def cria_matriz(pessoas):
    limpa_matriz(mt)
    for i in range(len(mt)):
        for j in range(len(mt[0])):
            for k in range(len(pessoas)):
                x = pessoas[k]['Coordenadas'][0]
                y = pessoas[k]['Coordenadas'][1]
                if pessoas[k]['Infetado'] == 'Sim':
                    mt[x][y] = '\033[31m1\033[m'
                elif pessoas[k]['Infetado'] == 'Não':
                    mt[x][y] = '\033[32m2\033[m'
                elif pessoas[k]['Infetado']=='Imune':
                    mt[x][y] = '\033[38m0\033[m'


    return mt

def limpa_matriz(mt):
    for i in range(len(mt)):
        for j in range(len(mt[0])):
            mt[i][j] = ' '
    return mt


def matriz_bonita(mt):
    for i in range(len(mt)):
        for x in mt:
            print(x[i], end=' ')
        print()
    return ('')

#-------------------------------------------------------


opv= menuvirus()
while opv !='1' and opv !='2' and opv !='3' and opv !='4':
    print('\033[31mOpção inválida\033[m')
    opv=menuvirus()
    break
if opv =='1' and opv =='2' and opv =='3' and opv =='4':
    print('Nothing')                #Só uma maneira de evitar erros
else:
    while opv =='1' or opv =='2'or opv =='3' or opv =='4':
        if opv =='1':                                                                                         #corona
            oput = menu_opcoes()
            while oput != "1" and oput != "2":  # INICIA MENU_OPÇOES
                    print('\033[31mOpção inválida\033[m')
                    oput = menu_opcoes()
                    break
            if opv == '1' and opv == '2' and opv == '3' and opv == '4':
                print('Nothing')
            else:
                while oput == "1" or oput == "2":
                    if oput == "1":
                        print('Lista de pessoas')
                        print(criar_pessoas(pessoas))
                        print()
                        def menux():
                            print('---------------------')
                            print('1 - Iniciar simulação')
                            print('2 - Sair')
                            print('---------------------')
                            opt = input('=>')
                            return opt
                        opio = menux()  #####
                        if opio == '1':  # OPÇAO INICIAR SIMULAÇÃO===================================#INICIA MENUX
                            opt = menu3()  # inicio do ciclo das semanas
                            if opt != '1' and opt != '2' and opt != '3':
                                print('\033[31mOpção inválida\033[m')
                                opio = menux()
                                break
                            while opt == '1' or opt == '2' or opt== '3':
                                for semana in range(1, 53):
                                    print()
                                    if semana ==52:
                                        quit()
                                    else:
                                        if opt == '2':  # definir a primeira opção
                                            if semana < 52:
                                                print('=> Exibição da matriz')
                                                print(matriz_bonita(cria_matriz(pessoas)))
                                                print()
                                                print('___________')
                                                print('Legenda')
                                                print()
                                                print('1 = Infetado')
                                                print('2 = Não infetado')
                                                print('O - Imune')
                                                print('___________')
                                                print()
                                                opt = menu3()

                                            else:
                                                opt = menu3()
                                        elif opt == '1':
                                            print('Semana ' + str(semana))
                                            print()
                                            print('=> Coordenadas das pessoas')
                                            print(movimento_pessoas(pessoas))
                                            print()
                                            print('=> Contactos')
                                            print(distância_infetados(pessoas))
                                            print()
                                            print('=> Pessoas (lista atualizada)')
                                            print(ver_se_esta_infetado(pessoas, semana))
                                            print()
                                            print('=> Pessoas infetadas')
                                            print(crialista_infetados(pessoas))
                                            print()
                                            print('=> Pessoas não infetadas')
                                            print(crialista_naoinfetados(pessoas))
                                            print()
                                            print('Sintomas de cada pessoa')
                                            print(sintomas_random(pessoas, semana))
                                            print()
                                            print(lista_sintomas(pessoas))
                                            print()
                                            print('Listas de pessoas hospitalizadas com a semana de infeção')
                                            print(hospitalizado(pessoas, semana))
                                            print()
                                            print('Listas de pessoas em quarentena')
                                            print(quarentena(pessoas, semana))
                                            print()
                                            print('Lista de pessoas atualizada')
                                            print(remove_sintomas(pessoas, semana))
                                            print()
                                            opt = menu3()
                                        elif opt == '3':
                                            print('Saiu do menu')
                                            opio = menux()
                                            break
                                        else:
                                            print('\033[31mOpção inválida\033[m')
                                            opt = menu3()
                        elif opio == '2':  # OPCAO SAIR # ENCERRA MENUX
                            for i in range (0,12):
                                if i ==2:
                                    print('Saiu do menu')
                                    oput = menu_opcoes()
                                    break
                        while opio!='1' and opio !='2':                      #BUG DE PEDIR DUAS VEZES
                            print('\033[31mOpção inválida\033[m')
                            opio = menux()
                            break
                    elif oput == '2': # ENCERRA MENU_OPÇOES
                        print('Saiu do menu')
                        opv = menuvirus()
                        break
                    else:
                        print('=> Opção inválida')
                        oput = menu_opcoes()
                        break

        elif opv =='2':                                                       #adeno
            oput = menu_opcoes()
            while oput != "1" and oput != "2":  # INICIA MENU_OPÇOES
                    print('\033[31mOpção inválida\033[m')
                    oput = menu_opcoes()
                    break
            if opv == '1' and opv == '2' and opv == '3' and opv == '4':
                print('Nothing')
            else:
                while oput == "1" or oput == "2":
                    if oput == "1":
                        print('Lista de pessoas')
                        print(criar_pessoas(pessoas))
                        print()
                        def menux():
                            print('---------------------')
                            print('1 - Iniciar simulação')
                            print('2 - Sair')
                            print('---------------------')
                            opt = input('=>')
                            return opt

                        opio = menux()  #####
                        if opio == '1':  # OPÇAO INICIAR SIMULAÇÃO===================================#INICIA MENUX
                            opt = menu3()  # inicio do ciclo das semanas
                            if opt != '1' and opt != '2' and opt != '3':
                                print('\033[31mOpção inválida\033[m')
                                opio = menux()
                                break
                            while opt == '1' or opt == '2' and opt == '3':
                                for semana in range(1, 53):
                                    print()
                                    if opt == '2':  # definir a primeira opção

                                        if semana < 52:
                                            print('=> Exibição da matriz')
                                            print(matriz_bonita(cria_matriz(pessoas)))
                                            print()
                                            print('___________')
                                            print('Legenda')
                                            print()
                                            print('1 = Infetado')
                                            print('2 = Não infetado')
                                            print('O - Imune')
                                            print('___________')
                                            print()
                                            opt = menu3()
                                        elif semana == 52:
                                            print('Foi decorrido um ano')
                                            quit()
                                        else:
                                            opt = menu3()
                                    elif opt == '1':
                                        print('Semana ' + str(semana))
                                        print()
                                        print('=> Coordenadas das pessoas')
                                        print(movimento_pessoas(pessoas))
                                        print()
                                        print('=> Contactos')
                                        print(distância_infetados(pessoas))
                                        print()
                                        print('=> Pessoas (lista atualizada)')
                                        print(ver_se_esta_infetado_adenovirus(pessoas, semana))
                                        print()
                                        print('=> Pessoas infetadas')
                                        print(crialista_infetados(pessoas))
                                        print()
                                        print('=> Pessoas não infetadas')
                                        print(crialista_naoinfetados(pessoas))
                                        print()
                                        print('Sintomas de cada pessoa')
                                        print(sintomas_adenovirus(pessoas, semana))
                                        print()
                                        print(lista_sintomas(pessoas))
                                        print()
                                        print('Listas de pessoas hospitalizadas com a semana de infeção')
                                        print(hospitalizado_adenovirus(pessoas, semana))
                                        print()
                                        print('Listas de pessoas em quarentena')
                                        print(quarentena_adenovirus(pessoas, semana))
                                        print()
                                        print('Lista de pessoas atualizada')
                                        print(remove_sintomas(pessoas, semana))
                                        print()
                                        opt = menu3()
                                    elif opt == '3':
                                        print('Saiu do menu')
                                        quit()
                                        opio = menux()
                                        break
                                    else:
                                        print('\033[31mOpção inválida\033[m')
                                        opt = menu3()
                        elif opio == '2':  # OPCAO SAIR
                            for i in range (0,12):
                                if i ==2:
                                    print('Saiu do menu')
                                    oput = menu_opcoes()
                                    break

                        else:  # ENCERRA MENUX
                            print('\033[31mOpção inválida\033[m')
                            opio = menux()
                            break
                    elif oput == '2':# ENCERRA MENU_OPÇOES
                        print('Saiu do menu')
                        opv = menuvirus()
                        break
                    else:
                        print('=> Opção inválida')
                        oput = menu_opcoes()
                        break


        elif opv =='3':                                                                             #retro
            oput = menu_opcoes()
            while oput != "1" and oput != "2":  # INICIA MENU_OPÇOES
                print('\033[31mOpção inválida\033[m')
                oput = menu_opcoes()
                break
            if opv == '1' and opv == '2' and opv == '3' and opv == '4':
                print('Nothing')
            else:
                while oput == "1" or oput == "2":
                    if oput == "1":
                        print('Lista de pessoas')
                        print(criar_pessoas(pessoas))
                        print()
                        def menux():
                            print('---------------------')
                            print('1 - Iniciar simulação')
                            print('2 - Sair')
                            print('---------------------')
                            opt = input('=>')
                            return opt


                        opio = menux()  #####
                        if opio == '1':  # OPÇAO INICIAR SIMULAÇÃO===================================#INICIA MENUX
                            opt = menu3()  # inicio do ciclo das semanas
                            if opt != '1' and opt != '2' and opt != '3':
                                print('\033[31mOpção inválida\033[m')
                                opio = menux()
                                break
                            while opt == '1' or opt == '2' or opt== '3':
                                for semana in range(1, 53):
                                    print()
                                    if opt == '2':  # definir a primeira opção

                                        if semana < 52:
                                            print('=> Exibição da matriz')
                                            print(matriz_bonita(cria_matriz(pessoas)))
                                            print()
                                            print('___________')
                                            print('Legenda')
                                            print()
                                            print('1 = Infetado')
                                            print('2 = Não infetado')
                                            print('O - Imune')
                                            print('___________')
                                            print()
                                            opt = menu3()
                                        elif semana == 52:
                                            print()
                                            print('Foi percorrido um ano')
                                            quit()
                                        else:
                                            opt = menu3()
                                    elif opt == '1':
                                        print('Semana ' + str(semana))
                                        print()
                                        print('=> Coordenadas das pessoas')
                                        print(movimento_pessoas(pessoas))
                                        print()
                                        print('=> Contactos')
                                        print(distância_infetados(pessoas))
                                        print()
                                        print('=> Pessoas (lista atualizada)')
                                        print(ver_se_esta_infetado_retrovirus(pessoas, semana))
                                        print()
                                        print('=> Pessoas infetadas')
                                        print(crialista_infetados(pessoas))
                                        print()
                                        print('=> Pessoas não infetadas')
                                        print(crialista_naoinfetados(pessoas))
                                        print()
                                        print('Sintomas de cada pessoa')
                                        print(sintomas_retrovirus(pessoas, semana))
                                        print()
                                        print(lista_sintomas(pessoas))
                                        print()
                                        print('Listas de pessoas hospitalizadas com a semana de infeção')
                                        print(hospitalizado_retrovirus(pessoas, semana))
                                        print()
                                        print('Listas de pessoas em quarentena')
                                        print(quarentena_retrovirus(pessoas, semana))
                                        print()
                                        print('Lista de pessoas atualizada')
                                        print(remove_sintomas(pessoas, semana))
                                        print()
                                        opt = menu3()
                                    elif opt == '3':
                                        print('Saiu do menu')
                                        quit()
                                        opio = menux()
                                    else:
                                        print('\033[31mOpção inválida\033[m')
                                        opt = menu3()
                        elif opio == '2':  # OPCAO SAIR                            for i in range (0,12):
                                if i ==2:
                                    print('Saiu do menu')
                                    oput = menu_opcoes()
                                    break
                        else:  # ENCERRA MENUX
                            print('\033[31mOpção inválida\033[m')
                            opio = menux()
                    elif oput == '2':
                        print('Saiu do menu')
                        opv = menuvirus()
                        break
                    else:  # ENCERRA MENU_OPÇOES
                        print('=> Opção inválida')
                        oput = menu_opcoes()
                        break
        elif opv =='4':#sair
            print('Saiu do menu')
            quit()
            break

        else:
            print('\033[31mOpção inválida\033[m')
            opv = menuvirus()

