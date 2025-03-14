def tratar_erro_conversao_string_nao_inteira():
    # Tentar executar um trecho de código que sabemos que poderá acontecer algum erro
    try: # tente
        # convertendo o que o usuário digitou de str para int e sabemos que pode acontecer algum erro
        numero = int(input("Digite o número: "))
    except Exception as erro: # quando ocorrer algum erro executa o código daqui de dentro do except
        print("Deu erro na conversão do número")
        # Caso desejar apresentar a mensagem do erro
        print("Mensagem do erro: ", erro)

    # Apresentar essa mensagem dando erro ou não
    print("Programa finalizado com sucesso")

def tratar_divisao_com_multiplos_except():
    try:
        numero1 = int(input("Digite o número 1: "))
        numero2 = int(input("Digite o número 2: "))
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    except ZeroDivisionError as erro: # cai aqui quando ocorrer erro na divisão
        print("Não é possível realizar a divisão por 0")
    except ValueError as erro: # cai aqui quando ocorrer erro na conversão
        print("Não foi possível converter o número para inteiro")
    except Exception as erro: # cai aqui com qualquer tipo de erro, caso n tiver sido tratado nos excepts anteriores
        print("Ocorreu um erro inesperado")

    print("Encerrou a aplicação com sucesso")


# ✔ Solicitar até que o usuário digite sair
# ✔ Solicitar os seguintes dados:
#   ✔ - nome do curso: str
#   ✔   Validar min: 8
#   ✔   Validar max: 20
#   ✔ - quantidade_alunos: int
#   ✔   Validar erro de conversão (try except)
#   ✔   Validar min: 5
#   ✔   Validar max: 20
def exemplo_curso():
    opcao: str = ""
    while opcao.strip().upper() != "SAIR":
        # Solicitar os dados do nome do curso
        nome: str = input("Digite o nome do curso: ").strip()
        while len(nome) < 8 or len(nome) > 20:
            print("Nome deve conter no mínimo 8 e no máximo 20 caracteres")
            nome = input("Digite o nome do curso: ").strip()

        quantidade_alunos: int = 0
        quantidade_valida = False
        while quantidade_valida == False:
            try:
                quantidade_alunos: int = int(input("Digite a quantidade de alunos: "))
                # if quantidade_alunos <5 or quantidade_alunos > 20:
                #    print("A quantidade mínima de alunos é 5 e a máxima é 20")
                #    continue

                if quantidade_alunos < 5:
                    print("A quantidade mínima de alunos para turma é 5")
                    continue

                if quantidade_alunos > 20:
                    print("A quantidade máxima de alunos para uma turma é 20")
                    continue

                quantidade_valida = True
            except Exception as erro:
                print("A quantidade de alunos deve ser um número inteiro")

        opcao = input("Presione enter para continuar ou digete 'sair' para encerrar.... ")

# Ex. 1: Solicitar um número inteiro e apresentar se ele é menor que 15 ou maior que 15

def numero_inteiro():
    numero = int(input("Digite um número inteiro: "))
    
    if numero < 15:
        print("Número é menor que 15")

    else:
        print("Número é maior que 15")


# Ex. 2: Solicitar o nome de um animal e apresentar a quantidade de caracteres

def nome_animal():
   nome_animal = input("Digite o nome de um animal: ")
   quantidade_caracteres = len(nome_animal)
   
   print(f"O nome do animal tem {quantidade_caracteres} caracteres. ")


# Ex. 3: Solicitar um texto, remover espaços do começo transformando em minúsculo

def solicitar_texto():
    texto = input("Digite o seu texto: ")
    texto_processado =  texto.strip().lower()
    print("Texto começo:", texto_processado)

# Ex. 4: Solicitar o nome de uma empresa e remover o texto 'LTDA', assim como, 'SA'.

def nome_empresa():
    nome_empresa = input("Digite o nome da empresa: ")

    nome_empresa_processado = nome_empresa.replace("LTDA", "").replace("SA", "")

    print("Nome da empresa sem 'LTDA' e 'SA':", nome_empresa_processado)

# Ex. 5: Solicitar o nome do curso e apresentar se o curso começa com SuperDev, caso contrário apresentar que não começa com SuperDev
def nome_curso_super_dev():
# Solicitar o nome do curso
    nome_curso_super_dev = input("Digite o nome do curso: ")
# Verificar se o nome do curso começa com "SuperDev"
    if nome_curso_super_dev.startswith("SuperDev"):
        print("O curso começa com 'SuperDev'.")
    else:
     print("O curso NÃO começa com 'SuperDev'.")

# Ex. 6: Solicitar uma idade e apresentar se é:
#   - Adulto
#   - Criança
#   - Adolescente
#   - Idoso
# Solicita a idade ao usuário
def solicitar_idade():

    idade = int(input("Digite a sua idade: "))

    # Condicionais para determinar a faixa etária
    if   idade <= 12:
        print("Criança")
    elif 13 <= idade <= 17:
        print("Adolescente")
    elif 18 <= idade <= 59:
        print("Adulto")
    else:
        print("Idoso")

#  UTILIZAR WHILE para estes exercícios abaixo:

# Ex. 7: Solicitar o nome da empresa e verificar se termina com LTDA, apresentar que é uma empresa 
# 'Sociedade de responsabilidade limitada', caso terminar com SA apresentar que é uma empresa 'Sociedade Anônima
# Solicita o nome da empresa
# Solicita o nome da empresa até que o nome seja válido
def solicitar_nome_empresa():
    while True:
        nome_empresa = input("Digite o nome da empresa: ")
        if nome_empresa.endswith("LTDA"):
            print("A empresa é uma Sociedade de responsabilidade limitada.")
            break
        elif nome_empresa.endswith("SA"):
            print("A empresa é uma Sociedade Anônima.")
            break
        else:
            print("A empresa não é reconhecida como LTDA ou SA. Tente novamente.")

# Ex. 8: Solicitar 5 vezes o nome do dia da semana
# Inicializa um contador para garantir que o loop aconteça 5 vezes
def solicitar_nome_dia_semana():
    contador = 0
    while contador < 5:
        dia = input(f"Digite o nome do dia da semana {contador + 1}: ")
        print(f"Você digitou: {dia}")
        contador += 1

# Ex. 9: Solicitar o nome da cidade e a quantidade de habitantes para quatro cidades.
# Inicializa o contador para 4 cidades
def solicitar_nome_cidade():
    contador = 0
    while contador < 4:
        cidade = input(f"Digite o nome da cidade {contador + 1}: ")
        habitantes = input(f"Digite a quantidade de habitantes de {cidade}: ")
        print(f"Cidade: {cidade}, Habitantes: {habitantes}")
        contador += 1

# Ex. 10: Solicitar o nome e altura de 6 alunos, descobrir  qual a maior altura e apresentar
# Inicializa as variáveis para armazenar a maior altura e o nome do aluno
def solicitar_nome_altura_alunos():
    maior_altura = 0
    nome_maior_altura = ""
    contador = 0
    while contador < 6:
        nome = input(f"Digite o nome do aluno {contador + 1}: ")
        altura = float(input(f"Digite a altura de {nome}: "))
        if altura > maior_altura:
            maior_altura = altura
            nome_maior_altura = nome
        contador += 1

    print(f"A maior altura é de {nome_maior_altura} com {maior_altura}m.")

# Ex. 11: Solicitar nome e preço de 5 notebooks, descobrir qual o nome e o valor do notebook que tem o menor preço
# Inicializa as variáveis para armazenar o nome e preço do notebook com o menor preço
def solicitar_nome_preco():
    menor_preco = float('inf')
    nome_menor_preco = ""
    contador = 0
    while contador < 5:
        nome_notebook = input(f"Digite o nome do notebook {contador + 1}: ")
        preco = float(input(f"Digite o preço de {nome_notebook}: "))
        if preco < menor_preco:
            menor_preco = preco
            nome_menor_preco = nome_notebook
        contador += 1

    print(f"O notebook mais barato é {nome_menor_preco} com o preço de R${menor_preco:.2f}.")

# Ex. 12: Solicitar o preço do petróleo e tratar o erro (neste não precisa de while, somente try/except)
# Solicita o preço do petróleo e trata possíveis erros
# Ex. 12: Solicitar o peso da carne e tratar o erro (neste precisa de while e try/except)
# Solicita o peso da carne e trata o erro com try/except
def solicitar_preco_petroleo():
    try:
        preco_petroleo = float(input("Digite o preço do petróleo: "))
        print(f"O preço do petróleo é R${preco_petroleo:.2f}.")
    except ValueError:
        print("Erro: valor inválido. Por favor, digite um número válido.")
while True:
    try:
        peso_carne = float(input("Digite o peso da carne (kg): "))
        if peso_carne <= 0:
            print("O peso não pode ser zero ou negativo. Tente novamente.")
        else:
            print(f"O peso da carne é {peso_carne}kg.")
            break
    except ValueError:
        print("Erro: valor inválido. Por favor, digite um número válido.")



# Ex. 13: Solicitar o salário do pedreiro (neste precisa de while e try/catch), passos para resolver:
#         Solicitar o salário
#         Adicionar o try/except
#         Fazer com que repita com while
#         Validar que o salário mínimo é de R$ 4000,00
#         Validar que o salário máximo é R$ 15000,00
# Solicita o salário do pedreiro e valida se está dentro do intervalo correto
def solicitar_salario_pedreiro():
    while True:
        try:
            salario = float(input("Digite o salário do pedreiro: R$ "))
            if salario < 4000 or salario > 15000:
                print("O salário deve estar entre R$ 4000,00 e R$ 15000,00. Tente novamente.")
            else:
                print(f"Salário do pedreiro: R${salario:.2f}.")
                break
        except ValueError:
            print("Erro: valor inválido. Por favor, digite um número válido.")

# Ex. 13: Solicitar nome do projeto, categoria e seu custo, apresentar conforme abaixo:
#           - Quantidade de projetos da categoria 'Cross Fit'
#           - Quantidade de projetos da categoria 'Pilates'
#           - Quantidade de projetos da categoria 'Fisioculturismo'
# Inicializa as contagens das categorias
def solicitar_nome_projeto():
    count_crossfit = 0
    count_pilates = 0
    count_fisioculturismo = 0

    while True:
        nome_projeto = input("Digite o nome do projeto (ou 'fim' para encerrar): ")
        if nome_projeto.lower() == 'fim':
            break
        categoria = input(f"Digite a categoria do projeto '{nome_projeto}': ")
        custo = float(input(f"Digite o custo do projeto '{nome_projeto}': R$ "))

        # Conta os projetos por categoria
        if categoria.lower() == "cross fit":
            count_crossfit += 1
        elif categoria.lower() == "pilates":
            count_pilates += 1
        elif categoria.lower() == "fisioculturismo":
            count_fisioculturismo += 1

    print(f"Quantidade de projetos 'Cross Fit': {count_crossfit}")
    print(f"Quantidade de projetos 'Pilates': {count_pilates}")
    print(f"Quantidade de projetos 'Fisioculturismo': {count_fisioculturismo}")

# Ex. 14: Solicitar nome, nota 1, nota 2 e nota 3 até que o usuário digite 'fim'.
# Ex. 14: (continuação) Calcular a média das notas e apresentar.
# Ex. 14: (continuação) Descobrir qual o status da média e apresentar
#        Critérios de média:
#        Até 4.99 reprovado
#        Até 6.99 em exame
#        Até 10 aprovado
# Ex. 14: (continuação) Descobrir e apresentar qual é a menor nota 1
# Ex. 14: (continuação) Descobrir e apresentar qual é a maior nota 2
# Ex. 14: (continuação) Descobrir e apresentar qual é a maior média e o nome do aluno
# Ex. 14: (continuação) Descobrir e apresentar qual é a menor média e o nome do aluno
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que tem "Enzo" em seu nome
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o nome começa com "Valentina"
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o status é reprovado
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o status é aprovado
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o status é em exame
# Inicializa variáveis para cálculos
def solicitar_nome_calcular_notas_apresentar():
    menor_nota1 = float('inf')
    maior_nota2 = -float('inf')
    maior_media = -float('inf')
    menor_media = float('inf')
    aluno_maior_media = ""
    aluno_menor_media = ""
    count_reprovado = 0
    count_aprovado = 0
    count_exame = 0
    count_enzo = 0
    count_valentina = 0

    while True:
        nome_aluno = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
        if nome_aluno.lower() == 'fim':
            break
        nota1 = float(input("Digite a nota 1: "))
        nota2 = float(input("Digite a nota 2: "))
        nota3 = float(input("Digite a nota 3: "))
        
        media = (nota1 + nota2 + nota3) / 3
        if nome_aluno.lower().find("enzo") != -1:
            count_enzo += 1
        if nome_aluno.lower().startswith("valentina"):
            count_valentina += 1
        
        if media < 5:
            status = "Reprovado"
            count_reprovado += 1
        elif media < 7:
            status = "Em exame"
            count_exame += 1
        else:
            status = "Aprovado"
            count_aprovado += 1

        # Atualiza as variáveis de maior e menor nota/media
        if nota1 < menor_nota1:
            menor_nota1 = nota1
        if nota2 > maior_nota2:
            maior_nota2 = nota2
        if media > maior_media:
            maior_media = media
            aluno_maior_media = nome_aluno
        if media < menor_media:
            menor_media = media
            aluno_menor_media = nome_aluno

        print(f"Aluno: {nome_aluno}, Média: {media}, Status: {status}")

    # Resultados finais
    print(f"Menor Nota 1: {menor_nota1}")
    print(f"Maior Nota 2: {maior_nota2}")
    print(f"Maior Média: {maior_media} (Aluno: {aluno_maior_media})")
    print(f"Menor Média: {menor_media} (Aluno: {aluno_menor_media})")
    print(f"Quantidade de alunos com 'Enzo' no nome: {count_enzo}")
    print(f"Quantidade de alunos cujo nome começa com 'Valentina': {count_valentina}")
    print(f"Quantidade de alunos reprovados: {count_reprovado}")
    print(f"Quantidade de alunos aprovados: {count_aprovado}")
    print(f"Quantidade de alunos em exame: {count_exame}")


if __name__ == "__main__":
    import os
    os.system("cls")
    solicitar_preco_petroleo()
