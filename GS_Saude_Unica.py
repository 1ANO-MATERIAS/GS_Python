# import json

# with open('especialidades.json', 'r', encoding='utf-8') as file:
#     especialidades = json.load(file)

# print(especialidades)


import json
import sys
from datetime import datetime
import os

usuarios = {}
agendamentos = []

def carregar_especialidades():
    with open("especialidades.json", "r") as file:
        return json.load(file)

def escolher_especialidade():
    especialidades = carregar_especialidades()

    print("Especialidades Disponíveis:")
    for idx, especialidade in enumerate(especialidades, start=1):
        print(f"{idx}. {especialidade}")

    escolha_especialidade = int(input("\nEscolha a especialidade: "))
    especialidade_selecionada = list(especialidades.keys())[escolha_especialidade - 1]
    locais = especialidades[especialidade_selecionada]

    locais = sorted(locais, key=lambda x: x['Tempo Estimado'])

    print("\nLocais disponíveis para a especialidade escolhida:")
    for idx, local in enumerate(locais, start=1):
        print(f"{idx}. {local['Nome']} - Tempo estimado: {local['Tempo Estimado']} minutos - Distância: {local['Distancia']} km")


    escolha_local = int(input("\nEscolha o local desejado: "))
    local_selecionado = locais[escolha_local - 1]

    cpf = input("Digite o CPF: ")
    if cpf not in usuarios:
        nome = input("Digite o Nome: ")
        rg = input("Digite o RG: ")
        email = input("Digite o Email: ")
        data_nascimento = input("Digite a Data de Nascimento (DD/MM/AAAA): ")
        convenio = input("Digite o Convênio (opcional): ")
        usuarios[cpf] = {"Nome": nome, "RG": rg, "Email": email, "Data de Nascimento": data_nascimento, "Convênio": convenio}

    agendamento = {"CPF": cpf, "Especialidade": especialidade_selecionada, "Local": local_selecionado['Nome'], "Tempo Estimado": local_selecionado['Tempo Estimado'], "Distância": local_selecionado['Distância']}
    agendamentos.append(agendamento)
    print("Agendamento realizado com sucesso!")

def acompanhar_jornadas():
    cpf = input("Digite o CPF: ")
    if cpf in usuarios:
        print("Seus agendamentos:")
        for agendamento in agendamentos:
            if agendamento["CPF"] == cpf:
                print(f"Especialidade: {agendamento['Especialidade']}, Local: {agendamento['Local']}, Tempo Estimado: {agendamento['Tempo Estimado']} minutos, Distância: {agendamento['Distância']} km")

def exibir_relatorios():
    with open("relatorio.txt", "w") as file:
        file.write("Relatório de Cadastros:\n")
        for cpf, usuario in usuarios.items():
            file.write(f"CPF: {cpf}, Nome: {usuario['Nome']}, Email: {usuario['Email']}, Convênio: {usuario['Convênio'] if 'Convênio' in usuario else 'N/A'}\n")

        file.write("\nRelatório de Agendamentos:\n")
        for agendamento in agendamentos:
            file.write(f"CPF: {agendamento['CPF']}, Especialidade: {agendamento['Especialidade']}, Local: {agendamento['Local']}, Tempo Estimado: {agendamento['Tempo Estimado']} minutos, Distância: {agendamento['Distância']} km\n")
    print("Relatórios exportados para relatorio.txt")

def dados_usuario():
    cpf = input("Digite o CPF: ")
    if cpf in usuarios:
        print("Dados do Usuário:")
        for key, value in usuarios[cpf].items():
            print(f"{key}: {value}")
    else:
        print("Cadastro não encontrado. Por favor, preencha seus dados.")
        nome = input("Digite o Nome: ")
        rg = input("Digite o RG: ")
        email = input("Digite o Email: ")
        data_nascimento = input("Digite a Data de Nascimento (DD/MM/AAAA): ")
        convenio = input("Digite o Convênio (opcional): ")
        usuarios[cpf] = {"Nome": nome, "RG": rg, "Email": email, "Data de Nascimento": data_nascimento, "Convênio": convenio}
        print("Cadastro realizado com sucesso!")

def sair_do_sistema():
    exibir_relatorios()
    print("Sistema encerrado")

# Menu principal
while True:
    print("\n----- Menu Principal -----")
    print("1. Escolher Especialidade")
    print("2. Acompanhar Jornadas de Saúde")
    print("3. Exibir Relatórios")
    print("4. Dados do Usuário")
    print("5. Sair do Sistema")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        escolher_especialidade()
    elif opcao == 2:
        acompanhar_jornadas()
    elif opcao == 3:
        exibir_relatorios()
    elif opcao == 4:
        dados_usuario()
    elif opcao == 5:
        sair_do_sistema()
        break
    else:
        print("Opção inválida. Escolha novamente.")
