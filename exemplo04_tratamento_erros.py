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


if __name__ == "__main__":
    import os
    os.system("cls")
    nome_curso_super_dev()
