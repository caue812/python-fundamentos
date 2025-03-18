# Encapsulamento: é a forma que termos para proteger métodos, variáveis...........
# Método privados: Método que será utolizado somente no arquivo atual,
#                 tem como prefuxo '__calcular()', '_calcular()'
# Métodos públicos: Método que será utilizado em qualquer outro arquivo
def __solicitar_numero1() -> int:
    numero1 = int(input("Digite o número 1: "))
    return numero1

def __solicitar_numero02() -> int:
    numero02 = int(input("Digite o número 2: "))
    return numero02

# Método com retorno do tipo inteiro que recebe dois parâmetros:
# O primeiro chama-se numero1 que é do tipo inteiro
# O segundo chama-se numero2 que é do tipo inteiro
# Como chamar(executar) métodos que tem parâmetros? somar(20, 2)
def __somar(numero1: int, numero2: int) -> int:
    soma = numero1 + numero2
    return soma

def __solicitar_nome_colaborador() -> str:
    nome_colaborador = input("Digite o nome do colaborador: ")
    return nome_colaborador

def __solicitar_horas_trabalhadas() -> int:
    horas_trabalhadas = 0 
    while horas_trabalhadas <= 0:
        try:
            horas_trabalhadas = int(
                input("Digite a quantidade de horas trabalhadas: ").strip()
            )
        except ValueError as error:
            print("A quantidade de horas deve ser um número inteiro")
        
    return horas_trabalhadas

def __solicitar_cargo() -> str:
    cargos_disponiveis = ["Junior", "Pleno", "Senior"]

    cargo = ""
    while cargo not in cargos_disponiveis:
        cargo = input("Digite o cargo: ")
        if cargo not in cargos_disponiveis:
            print("CArgo inválido, cargo disponiveis:", cargos_disponiveis)
    return cargo

    



# Método de entrada para calcular a folha de pagamento do usuário
def caalcular_folha_pagamento():





def calculadora():
    numero1 = __solicitar_numero1()
    numero2 = __solicitar_numero02()

    soma = __somar(numero1, numero2)

    print("Número 1:", numero1)
    print("Número 2:", numero2)
    print("Soma:", soma)

