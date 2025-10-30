# SISTEMA DE BANCO

# Inicializando variáveis
contas = {
    "1234": {"saldo": 1000.0, "extrato": []},
    "5678": {"saldo": 500.0, "extrato": []}
}

def acessar_conta():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        return numero_conta
    else:
        print("Conta não encontrada.")
        return None

def menu():
    print("\nMENU")
    print("1. Ver extrato")
    print("2. Fazer um depósito")
    print("3. Fazer um saque")
    print("4. Sair do sistema")

def main():
    conta = acessar_conta()
    if conta is None:
        return

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"\nSaldo: R${contas[conta]['saldo']:.2f}")
            print("Extrato:")
            for operacao in contas[conta]['extrato']:
                print(operacao)
        elif opcao == "2":
            deposito = float(input("Digite o valor do depósito: R$"))
            contas[conta]['saldo'] += deposito
            contas[conta]['extrato'].append(f"Depósito: R${deposito:.2f}")
            print(f"Depósito realizado com sucesso. Saldo atual: R${contas[conta]['saldo']:.2f}")
        elif opcao == "3":
            saque = float(input("Digite o valor do saque: R$"))
            if saque <= contas[conta]['saldo']:
                contas[conta]['saldo'] -= saque
                contas[conta]['extrato'].append(f"Saque: R${saque:.2f}")
                print(f"Saque realizado com sucesso. Saldo atual: R${contas[conta]['saldo']:.2f}")
            else:
                print("Saldo insuficiente.")
        elif opcao == "4":
            print("Obrigado por usar o sistema de banco!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()