# Função para exibir o menu de opções
def exibir_menu():
    menu = """
    [u] Criar usuário
    [c] Criar conta
    [lu] Listar usuários
    [lc] Listar contas
    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair

    => """
    return input(menu)

# Função para criar um novo usuário
def criar_usuario(usuarios):
    # Solicitar as informações do usuário
    cpf = input("Digite o CPF: ")
    # Remover pontos e hífen do CPF
    cpf_numerico = cpf.replace(".", "").replace("-", "")
    # Verificar se já existe um usuário com o mesmo CPF
    for usuario in usuarios:
        if usuario["cpf"] == cpf_numerico:
            print(f"Erro: Usuário com CPF {cpf_numerico} já está cadastrado.")
            return
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento (formato DD/MM/AAAA): ")
    endereco = input("Digite o endereço (formato 'Logradouro, número - bairro - cidade/sigla do estado'): ")

    # Se o CPF não estiver cadastrado, adicionar o novo usuário
    usuario = {
        "cpf": cpf_numerico,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} armazenado com sucesso!")

# Função para verificar se o usuário existe com base no CPF
def buscar_usuario_por_cpf(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def listar_usuarios(usuarios):
    print("\n================ Usuários ================")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"CPF: {usuario['cpf']}")
            print(f"Nome: {usuario['nome']}")
            print(f"Data de Nascimento: {usuario['data_nascimento']}")
            print(f"Endereço: {usuario['endereco']}")
            print("-------------------------------------------")
    print("==========================================")


# Função para adicionar uma nova conta
def criar_conta(usuarios, contas, num_conta):
    cpf = input("Digite o CPF do usuário: ")
    cpf_numerico = cpf.replace(".", "").replace("-", "")
    
    usuario = buscar_usuario_por_cpf(cpf_numerico, usuarios)
    
    if usuario:
        num_conta += 1
        conta = {
            "agencia": "0001",
            "num_conta": num_conta,
            "usuario": usuario
        }
        contas.append(conta)
        print(f"Conta {num_conta} criada para o usuário {usuario['nome']}")
    else:
        print("Usuário não encontrado. Por favor, cadastre o usuário primeiro.")
    
    return num_conta

def listar_contas(contas):
    print("\n================ Contas ================")
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            usuario = conta["usuario"]
            print(f"Conta: {conta['num_conta']}")
            print(f"Agência: {conta['agencia']}")
            print(f"Nome do Usuário: {usuario['nome']}")
            print("-------------------------------------------")
    print("==========================================")


# Função para realizar depósito
def deposito(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função para realizar saque
def saque(saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

# Função para exibir o extrato
def extrato(saldo, /, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    usuarios = []
    contas = []
    num_conta = 0
    saldo = 0
    limite = 500
    extrato_str = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = exibir_menu()

        if opcao == "u":
            criar_usuario(usuarios)
        elif opcao == "c":
            num_conta = criar_conta(usuarios, contas, num_conta)
        elif opcao == "lu":
            listar_usuarios(usuarios)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "d":
            saldo, extrato_str = deposito(saldo, extrato_str)
        elif opcao == "s":
            saldo, extrato_str, numero_saques = saque(saldo, limite, extrato_str, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            extrato(saldo, extrato_str)
        elif opcao == "q":
            print("Obrigado por usar o sistema bancário. Até logo!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
