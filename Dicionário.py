
import random
import uuid

# Função para escrever o dicionário na consola
def print_loja():
    print("-------------------------------------------------")
    for (chave, valor) in loja.items():
        print(chave, valor)

# Construção do dicionário
loja = {
    uuid.uuid4(): {"nome": "Caderno", "preço": 1.0, "quantidade": random.randint(1, 1500)},
    uuid.uuid4(): {"nome": "Caneta", "preço": 0.50, "quantidade": random.randint(1, 1500)},
    uuid.uuid4(): {"nome": "Borracha", "preço": 2.0, "quantidade": random.randint(1, 1500)},
    uuid.uuid4(): {"nome": "Lápis", "preço": 1.0, "quantidade": random.randint(1, 1500)}
}

# Função principal para o menu
def menu():
    while True:
        print("-------------------------------------------------")
        print("Comandos:")
        print("Exibir loja")
        print("Adicionar produto")
        print("Adicionar produto com lista")
        print("Atualizar produto")
        print("Remover produto")
        print("Contar a quantidade de produtos")
        print("Contar o número de produtos")
        print("Calcular o preço total em loja")
        print("Sair")
        print("-------------------------------------------------")
        menu = input("O que queres fazer?\n")

        if menu == "Exibir loja":
            print_loja()
        elif menu == "Adicionar produto":
            cod_produto = uuid.uuid4()
            nome = input("Escreve o nome do produto: ")
            while True:
                try:
                    preço = float(input("Escreve o preço do produto: "))
                    break
                except ValueError:
                    print("Erro! Introduz um preço válido.")
            while True:
                try:
                    quantidade = int(input("Escreva a quantidade do produto: "))
                    break
                except ValueError:
                    print("Erro! Introduz uma quantidade válida.")
            add_produto(cod_produto, nome, preço, quantidade)
            print(f"{nome} adicionado com sucesso.")
        elif menu == "Adicionar produto com lista":
            cod_produto = uuid.uuid4()
            while True:
                try:
                    nomes = input("Escreve os nomes dos produtos: ").split(',')
                    preços = list(map(float, input("Escreve os preços dos produtos: ").split(',')))
                    quantidades = list(map(int, input("Escreve as quantidades dos produtos: ").split(',')))
                    break
                except ValueError:
                    print("Erro! Introduz valores válidos e tenta novamente.")
            add_produto_com_lista(cod_produto, nomes, preços, quantidades)
            print(f"{nomes} adicionados com sucesso.")
        elif menu == "Atualizar produto":
            nome_produto = input("Escreve o nome do produto a atualizar: ")
            cod_produto = nome_codigo(nome_produto)
            if cod_produto:
                while True:
                    try:
                        preço = float(input("Escreve o novo preço do produto: "))
                        break
                    except ValueError:
                        print("Erro! Introduz um preço válido.")
                while True:
                    try:
                        quantidade = int(input("Escreve a nova quantidade do produto: "))
                        break
                    except ValueError:
                        print("Erro! Introduz uma quantidade válida.")
                update_produto(cod_produto, preço, quantidade)
                print(f"{nome_produto} atualizado com sucesso.")
            else:
                print(f"{nome_produto} não encontrado na loja! Tenta novamente.")
        elif menu == "Remover produto":
            nome_produto = input("Escreve o nome do produto a remover: ")
            cod_produto = nome_codigo(nome_produto)
            if cod_produto:
                remover_produto(cod_produto)
            else:
                print(f"{nome_produto} não encontrado na loja! Tenta novamente.")
        elif menu == "Contar a quantidade de produtos":
            # Contar a quantidade de produtos no dicionário
            quantidade = contar_quantidade()
            print("-------------------------------------------------")
            print(f"A quantidade de produtos em loja é: {quantidade}")
        elif menu == "Contar o número de produtos":
            # Contar o número de produtos existentes no dicionário
            numero_de_produtos = contar_produtos()
            print("-------------------------------------------------")
            print(f"O número de produtos em loja é: {numero_de_produtos}")
        elif menu== "Calcular o preço total em loja":
            # Calcular o preço total na loja
            preço_total = contar_preço()
            print("-------------------------------------------------")
            print(f"O preço total em loja é: {preço_total:.2f} euros")
        elif menu == "Sair":
            print("A sair...")
            break
        else:
            print("Opção inválida! Tenta novamente.")

# Função para atualizar produtos
def update_produto(cod_produto, preço, quantidade):
    if cod_produto in loja:
        loja[cod_produto]["preço"] = preço
        loja[cod_produto]["quantidade"] = quantidade
    else:
        nome = loja[cod_produto]["nome"]
        print(f"{nome} não encontrado na loja")

# Função para adicionar produtos
def add_produto(cod_produto, nome, preço, quantidade):
    novo_produto = {"nome": nome, "preço": preço ,"quantidade": quantidade}
    loja[cod_produto] = novo_produto

# Função para remover produtos
def remover_produto(cod_produto):
    if cod_produto in loja:
        nome = loja[cod_produto]["nome"]
        del loja[cod_produto]
        print(f"{nome} removido.")
    else:
        nome = loja[cod_produto]["nome"]
        print(f"{nome} não encontrado.")

# Função para adicionar produtos com listas no dicionário
def add_produto_com_lista(cod_produto, nomes, preços, quantidades):
    novo_produto = {"nomes": nomes, "preços": preços, "quantidades": quantidades}
    loja[cod_produto] = novo_produto

# Função para contar a quantidade de produtos no dicionário
def contar_quantidade():
    total=0
    for produtos in loja.values():
        if "quantidade" in produtos:
            total += produtos["quantidade"]
        elif "quantidades" in produtos:
            total += sum(produtos["quantidades"])
        else:
            print(f"Produto {produtos} não tem chave 'quantidade' ou 'quantidades'")
    return total

# Função para contar o número de produtos existentes no dicionário
def contar_produtos():
    return len(loja)

# Função para contar o preço total em loja
def contar_preço():
    total_preço = 0
    for produto in loja.values():
        if "preço" in produto and "quantidade" in produto:
            total_preço += produto["preço"] * produto["quantidade"]
        elif "preços" in produto and "quantidades" in produto:
            total_preço += sum(p * q for p, q in zip(produto["preços"], produto["quantidades"]))
    return total_preço

# Função para encontrar o código do produto através do nome
def nome_codigo(nome_produto):
    for código, detalhes in loja.items():
        if detalhes["nome"] == nome_produto:
            return código
    return None

# Executar o menu
menu()
