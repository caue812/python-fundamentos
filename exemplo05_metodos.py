
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



if __name__ == "__main__":
    import os
    os.system("cls")
    somar()
