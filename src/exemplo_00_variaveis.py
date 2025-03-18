# Entre funções colocar duas linhas 
# Nome de função (def) deve ser no padrão snake_case
def exemplo_tipos_primitivos():
    # Nome de variáveis deve ser no padrão snake_case (nome_completo_funcionario)
    # Nome de variáveis não pode começar com números, n pode conter caracteres especiais (~,´,´.....)
    nome: str = "PS5 Pro" # str é string (texto)
    preco: float = 7000.99 # float número real
    quantidade: int = 2 # int é inteiro
    compra_realizada: bool = True # bool é operador lógico (True: verdadeiro, False: falso)

    # calcular o total da compra
    total_compra: float = preco * quantidade

    print("Nome:", nome)
    print("Preço:", preco)
    print("Quantidade:", quantidade)
    print("Compra realizada:", compra_realizada)
    print("Total da compra:", total_compra)

def exemplo_entrada_dados():
    # input é utilizado para questionar para o usuàrio uma entrada de dados, tudo o
    # que o usuário digitar virá com string
    nome: str = input("Digite o nome: ")
    sobrenome: str = input("Digite o sobrenome: ")
    # Convertendo o que o usuário digitou para inteiro
    idade: int = int(input("Digite a idade: "))

    # + neste cenário está concatenando o nome, espaço e o sobrenome
    nome_completo: str = nome + " " + sobrenome
    # str(idade) => convertendo de int para string
    texto: str = "Nome completo: " + nome_completo + "tem " + str(idade) + " anos"
    print(texto)


def exercicio_paciente():
    nome: str = input("Digite seu nome: ")
    peso: float  = float(input("Digite seu peso: "))
    altura: float = float(input("Digite sua altura: "))
    email: str = input("Digite o e-mail")
    imc: float = peso / (altura * altura)

    texto: str = "Seu IMC é: "  + str(imc) 
    print(texto)


def exercicio_carro():
    modelo_carro: str = input("Digite o modelo do carro: ")
    quantidade_parcelas: int = int(input("Digite a quantidade de parcelas: "))
    valor_parcela: float = float(input("Qual o valor da parcela? "))
    valor_fipe: float = float(input("Qual o valor da fipe? "))
    total_pago: float = quantidade_parcelas * valor_parcela
    total_com_juros: float = total_pago - valor_fipe

    texto: str = " o modelo do carro é: " + modelo_carro + " a quantidade de parcela é de: " + str(quantidade_parcelas) + " o valor total do carro é de: " + str(total_pago) + " a quantidade de juros é de: " + str(total_com_juros) 
    print(texto)
    
    
    
    # esse trecho é chamado quando o arquivo é executado, main é 
    # o ponto de entrada(execução) de uma aplicação
if __name__ == "__main__":
        # executa a função abaixo, ou seja, executará o codigo que está dentro da função
        exercicio_carro()

        # Como executar:
        # Abrir o terminal (Ctrl + J)
        # Executar o contato 'py exemplo_00_variaveis.py'