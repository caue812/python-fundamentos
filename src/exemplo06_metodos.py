
# método com retorno do tipo int
def somar() -> int:
    numero1 = 10
    numero2 = 20
    soma = numero1 + numero2
    return soma

# método sem retorno
def calculadora():
    resultado = somar() 
    print("Soma:", resultado) 


# método sem retorno
# Responsabilidade do método: solicitar o nome garantindo no mínimo 3 carac
def solicitar_nome() -> str:
    nome_solicitado = input("Digite o nome: ").strip()
    while len(nome_solicitado) < 3:
        print("Nome inválidado, deve conter no mínimo de 3 caracteres")
        nome_solicitado = input("Digite o nome: ").strip()
    return nome_solicitado


# Método com retorno do tipo string
# Responsabilidade do método: solicitar o sobrenome garantindo no mínimo 3 máximo 100
def solicitar_sobrenome() -> str:
    sobrenome_solicitado = input("Digite o sobrenome: ").strip()
    while len(sobrenome_solicitado) < 3 or len(sobrenome_solicitado) > 100:
        print("Sobrenome inválido, deve conter no mínimo 3 caracteres e no máximo 100")
        sobrenome_solicitado - input("Digite o sobrenome: ").strip()
    return sobrenome_solicitado

# Método sem retorno 
def apresentar_nome_completo():
    # Executando o método solicitar_nome() e armazenando seu retorno na variável nome
    nome = solicitar_nome()
    # Executando o método solicitar_sobrenome() e armazenando seu retorno na variável sobrenome
    sobrenome = solicitar_sobrenome()

    nome_completo = nome + " " + sobrenome
    print("Nome completo: ", nome_completo)

# Exercício:
# Criar uma função solicitar_modelo min: 4
# Criar uma função solicitar_quantidade min: 1 max: 5
# Criar uma função solicitar_preco min: 100, max: 500, tratar erros com try/except
# Na função solicitar_calcular_produto, chamar as funções e armazenar em variáveis
# Apresentar o total e as variáveis

def solicitar_modelo():
    modelo = input("Digite o modelo pelo menos 4 caracteres: ")
    while len(modelo) < 4:
        print("O modelo deve ter pelo menos 4 caracteres: ")
        modelo = input("Digite o modelo: ")
    return modelo 

def solicitar_quantidade():

    print("Função para solicitar a quantidade, garantindo que seja entre 1 e 5.")
    
    while True:
        try:
            quantidade = int(input("Digite a quantidade (1 a 5): "))
            if 1 <= quantidade <= 5:
                return quantidade  
            else:
                print("A quantidade deve ser entre 1 e 5.")
        except ValueError:
            print("Erro: Por favor, insira um número inteiro válido.")




def solicitar_preco():

    print("Função para solicitar o preço, garantindo que seja entre 100 e 500, com tratamento de erros.")
    while True:
        try:
            preco = float(input("Digite o preço (entre 100 e 500): "))
            if 100 <= preco <= 500:
                return preco
            else:
                print("O preço deve estar entre 100 e 500.")
        except ValueError:
            print("Erro: Por favor, insira um valor numérico válido para o preço.")


def solicitar_calcular_produto():

    print("Função para chamar as funções de solicitação, calcular o total e apresentar os resultados.")
    modelo = solicitar_modelo()  # Solicita o modelo
    quantidade = solicitar_quantidade()  # Solicita a quantidade
    preco = solicitar_preco()  # Solicita o preço

    # Calcula o total
    total = quantidade * preco

    # Exibe os resultados
    print("\nResumo da compra:")
    print(f"Modelo: {modelo}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço unitário: R${preco:.2f}")
    print(f"Total: R${total:.2f}")


if __name__ == "__main__":
    import os
    os.system("cls")
    solicitar_calcular_produto()
