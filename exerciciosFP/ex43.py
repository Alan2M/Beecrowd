import os
os.system('cls')

import csv
import random
from datetime import datetime

# Funções auxiliares
def carregar_dados(arquivo):
    """Carrega os dados de um arquivo CSV."""
    try:
        with open(arquivo, mode='r') as f:
            leitor = csv.DictReader(f)
            return list(leitor)
    except FileNotFoundError:
        return []

def salvar_dados(arquivo, dados, cabecalho):
    """Salva os dados em um arquivo CSV."""
    with open(arquivo, mode='w', newline='') as f:
        escritor = csv.DictWriter(f, fieldnames=cabecalho)
        escritor.writeheader()
        escritor.writerows(dados)

def gerar_id(dados):
    """Gera um novo ID único."""
    if not dados:
        return 1
    return max(int(dado['id']) for dado in dados) + 1

# Função de CRUD
def adicionar_treino(arquivo):
    """Adiciona um novo treino ou competição."""
    dados = carregar_dados(arquivo)
    
    novo_id = gerar_id(dados)
    data = input("Digite a data (dd/mm/yyyy): ")
    distancia = float(input("Digite a distância percorrida (km): "))
    tempo = input("Digite o tempo (hh:mm:ss): ")
    local = input("Digite a localização: ")
    condicoes_climaticas = input("Digite as condições climáticas: ")
    
    dados.append({
        'id': novo_id,
        'data': data,
        'distancia': distancia,
        'tempo': tempo,
        'local': local,
        'condicoes_climaticas': condicoes_climaticas
    })
    
    salvar_dados(arquivo, dados, ['id', 'data', 'distancia', 'tempo', 'local', 'condicoes_climaticas'])
    print("Treino/competição adicionado com sucesso!")

def visualizar_treinos(arquivo):
    """Exibe todos os treinos e competições."""
    dados = carregar_dados(arquivo)
    if dados:
        for dado in dados:
            print(f"ID: {dado['id']}, Data: {dado['data']}, Distância: {dado['distancia']} km, Tempo: {dado['tempo']}, Local: {dado['local']}, Condições: {dado['condicoes_climaticas']}")
    else:
        print("Nenhum treino encontrado.")

def atualizar_treino(arquivo):
    """Atualiza um treino ou competição existente."""
    dados = carregar_dados(arquivo)
    visualizar_treinos(arquivo)
    treino_id = int(input("Digite o ID do treino/competição que deseja atualizar: "))
    
    for dado in dados:
        if int(dado['id']) == treino_id:
            dado['data'] = input(f"Data atual ({dado['data']}): ") or dado['data']
            dado['distancia'] = input(f"Distância atual ({dado['distancia']} km): ") or dado['distancia']
            dado['tempo'] = input(f"Tempo atual ({dado['tempo']}): ") or dado['tempo']
            dado['local'] = input(f"Local atual ({dado['local']}): ") or dado['local']
            dado['condicoes_climaticas'] = input(f"Condições climáticas atuais ({dado['condicoes_climaticas']}): ") or dado['condicoes_climaticas']
            salvar_dados(arquivo, dados, ['id', 'data', 'distancia', 'tempo', 'local', 'condicoes_climaticas'])
            print("Treino atualizado com sucesso!")
            return
    print("Treino não encontrado.")

def excluir_treino(arquivo):
    """Exclui um treino ou competição."""
    dados = carregar_dados(arquivo)
    visualizar_treinos(arquivo)
    treino_id = int(input("Digite o ID do treino/competição que deseja excluir: "))
    
    novos_dados = [dado for dado in dados if int(dado['id']) != treino_id]
    if len(novos_dados) != len(dados):
        salvar_dados(arquivo, novos_dados, ['id', 'data', 'distancia', 'tempo', 'local', 'condicoes_climaticas'])
        print("Treino/competição excluído com sucesso!")
    else:
        print("Treino não encontrado.")

# Filtragem
def filtrar_treinos_por_distancia(arquivo):
    """Filtra treinos por distância."""
    dados = carregar_dados(arquivo)
    distancia_min = float(input("Digite a distância mínima (km): "))
    distancia_max = float(input("Digite a distância máxima (km): "))
    
    filtrados = [dado for dado in dados if distancia_min <= float(dado['distancia']) <= distancia_max]
    if filtrados:
        for dado in filtrados:
            print(f"ID: {dado['id']}, Data: {dado['data']}, Distância: {dado['distancia']} km, Tempo: {dado['tempo']}, Local: {dado['local']}, Condições: {dado['condicoes_climaticas']}")
    else:
        print("Nenhum treino encontrado para essa distância.")

def filtrar_treinos_por_tempo(arquivo):
    """Filtra treinos por tempo."""
    dados = carregar_dados(arquivo)
    tempo_min = input("Digite o tempo mínimo (hh:mm:ss): ")
    tempo_max = input("Digite o tempo máximo (hh:mm:ss): ")
    
    filtrados = [dado for dado in dados if tempo_min <= dado['tempo'] <= tempo_max]
    if filtrados:
        for dado in filtrados:
            print(f"ID: {dado['id']}, Data: {dado['data']}, Distância: {dado['distancia']} km, Tempo: {dado['tempo']}, Local: {dado['local']}, Condições: {dado['condicoes_climaticas']}")
    else:
        print("Nenhum treino encontrado para esse intervalo de tempo.")

# Metas e Desafios
def definir_metas(arquivo):
    """Permite definir uma meta de corrida e verifica o progresso."""
    meta_distancia = float(input("Digite a meta de distância para o mês (km): "))
    dados = carregar_dados(arquivo)
    distancia_total = sum(float(dado['distancia']) for dado in dados)
    
    print(f"Distância total percorrida até agora: {distancia_total} km")
    if distancia_total >= meta_distancia:
        print("Parabéns! Você atingiu sua meta.")
    else:
        print(f"Faltam {meta_distancia - distancia_total} km para atingir sua meta.")

# Sugestão de Treino Aleatório
def sugerir_treino_aleatorio(arquivo):
    """Sugere um treino aleatório baseado no histórico."""
    dados = carregar_dados(arquivo)
    if dados:
        sugestao = random.choice(dados)
        print(f"Sugestão de treino: {sugestao['distancia']} km no local {sugestao['local']} com condições {sugestao['condicoes_climaticas']}")
    else:
        print("Nenhum treino disponível para sugerir.")

# Funcionalidade Extra: Relatório de desempenho
def gerar_relatorio(arquivo):
    """Gera um relatório de desempenho."""
    dados = carregar_dados(arquivo)
    total_treinos = len(dados)
    distancia_total = sum(float(dado['distancia']) for dado in dados)
    
    print(f"Total de treinos: {total_treinos}")
    print(f"Distância total percorrida: {distancia_total} km")

# Menu interativo
def menu():
    arquivo = "treinos.csv"
    while True:
        print("\n--- Menu Principal ---")
        print("1. Adicionar Treino/Competição")
        print("2. Visualizar Treinos/Competições")
        print("3. Atualizar Treino/Competição")
        print("4. Excluir Treino/Competição")
        print("5. Filtrar Treinos por Distância")
        print("6. Filtrar Treinos por Tempo")
        print("7. Definir Metas e Desafios")
        print("8. Sugerir Treino Aleatório")
        print("9. Gerar Relatório de Desempenho")
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_treino(arquivo)
        elif escolha == '2':
            visualizar_treinos(arquivo)
        elif escolha == '3':
            atualizar_treino(arquivo)
        elif escolha == '4':
            excluir_treino(arquivo)
        elif escolha == '5':
            filtrar_treinos_por_distancia(arquivo)
        elif escolha == '6':
            filtrar_treinos_por_tempo(arquivo)
        elif escolha == '7':
            definir_metas(arquivo)
        
        