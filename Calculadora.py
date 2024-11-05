
# Função para soma
def soma(x, y):
    return x + y


# Função para subtração
def subtração(x, y):
    return x - y


# Função para multiplicação
def multiplicação(x, y):
    return x * y


# Função para divisão
def divisão(x, y):
    if y == 0:
        return ("Erro!")
    return x / y

# Função principal
def calculadora():
    operação = input("Escolha a operação: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if operação == "subtração":
        result = subtração(num1, num2)
        print("Resultado da subtração: " + str(result))
    elif operação == "soma":
        result = soma(num1, num2)
        print("Resultado da soma: " + str(result))
    elif operação == "multiplicação":
        result = multiplicação(num1, num2)
        print("Resultado da multiplicação: " + str(result))
    elif operação == "divisão":
        result = divisão(num1, num2)
        print("Resultado da divisão: " + str(result))

# Executar a calculadora
calculadora()
