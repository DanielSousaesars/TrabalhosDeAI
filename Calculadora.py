
# Lista para adicionar histórico
histórico = []

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

# Função para o histórico para adicionar e manter a lista com as últimas 5 operações
def add_histórico(operação, num1, num2, result):
    histórico.append(f"{operação}: {num1} e {num2} = {result}")
    if len(histórico) > 5:
        histórico.pop(0)  # Remover o primeiro elemento da lista

# Função principal
def calculadora():
    while True:
        operação = input ("Escolha a operação: ")
        if operação in ["subtração", "soma", "multiplicação", "divisão"]:
            while True:
                try:
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    break
                except ValueError:
                    print("Valores Inválidos!")
            if operação == "subtração":
                result = subtração(num1, num2)
                print("Resultado da subtração: " + str(result))
            elif operação == "soma":
                result =  soma(num1, num2)
                print("Resultado da soma: " + str(result))
            elif operação == "multiplicação":
                result = multiplicação(num1, num2)
                print("Resultado da multiplicação: " + str(result))
            elif operação == "divisão":
                result = divisão(num1, num2)
                print("Resultado da divisão: " + str(result))
            add_histórico(operação, num1, num2, result)
        elif operação == "sair":
            print("A sair da calculadora...")
            break # Sair do loop e fechar o programa
        elif operação == "histórico":
            print("Histórico de operações:")
            for item in histórico:
                print(item)
        elif operação not in ["soma", "subtração", "divisão", "multiplicação"]:
            print("Operação inválida!")

# Executar a calculadora
calculadora()
