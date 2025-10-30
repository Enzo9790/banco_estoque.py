estoque = {}


def adicionar_produto():
    nome = input("Informe o nome do produto: ")
    try:
        quantidade = int(input("Informe a quantidade: "))
        preco = float(input("Informe o preço unitário: "))
        
        if quantidade <= 0 or preco <= 0:
            print("Quantidade ou preço inválido! Tente novamente.")
            return
        
        
        if nome in estoque:
            estoque[nome]['quantidade'] += quantidade
            print(f"Produto {nome} atualizado no estoque! Novo estoque: {estoque[nome]['quantidade']} unidades.")
        else:
            
            estoque[nome] = {'quantidade': quantidade, 'preco': preco}
            print(f"Produto {nome} adicionado ao estoque!")
    except ValueError:
        print("Valor inválido! Quantidade deve ser um número inteiro e preço deve ser um número decimal.")


def vender_produto():
    nome = input("Informe o nome do produto a ser vendido: ")
    
    if nome not in estoque:
        print(f"O produto {nome} não está disponível no estoque.")
        return
    
    try:
        quantidade_venda = int(input("Informe a quantidade a ser vendida: "))
        
        if quantidade_venda <= 0:
            print("A quantidade a ser vendida deve ser positiva.")
            return
        
        
        if estoque[nome]['quantidade'] >= quantidade_venda:
            estoque[nome]['quantidade'] -= quantidade_venda
            print(f"Venda realizada! Quantidade de {nome} em estoque: {estoque[nome]['quantidade']} unidades.")
        else:
            print(f"Estoque insuficiente para realizar a venda. Estoque atual de {nome}: {estoque[nome]['quantidade']} unidades.")
    except ValueError:
        print("Quantidade inválida! Informe um número inteiro.")


def ver_estoque():
    if not estoque:
        print("O estoque está vazio.")
        return
    
    print("\nEstoque atual:")
    for nome, dados in estoque.items():
        print(f"- {nome}: {dados['quantidade']} unidades, R${dados['preco']:.2f} cada")


def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar produto")
        print("2. Vender produto")
        print("3. Ver estoque")
        print("4. Sair")
        
        opcao = input("Digite o número da operação desejada: ")
        
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            vender_produto()
        elif opcao == '3':
            ver_estoque()
        elif opcao == '4':
            print("Obrigado por usar o sistema de controle de estoque. Até logo!")
            break  
        else:
            print("Opção inválida! Tente novamente.")


menu()