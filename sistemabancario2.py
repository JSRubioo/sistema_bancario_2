def menu():
    menu = """\n
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """
    return input(menu)



def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito R$: {valor:.2f}\n"
        print("Valor depositado com sucesso.") 
    else:
        print("Valor invalido")
    
    return saldo, extrato

def exibir_extrato(saldo , /, *, extrato):
    
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:\t\tR$ {saldo:.2f}")
        print("==================")


def sacar(*,saldo, valor, extrato, limite, LIMITE_SAQUES):
    excedeu_limite = valor > limite
    excedeu_limite_saques = LIMITE_SAQUES <= 0
    falta_dinheiro = saldo <= 0

    if excedeu_limite:
        print("Valor acima do limite.")

    elif excedeu_limite_saques:
        print("Numero de saques diarios excedidos")

    elif falta_dinheiro:
        print("Saldo insuficiente.")

    elif valor >0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n" 
        print("Saque efetuado com sucesso.")
        LIMITE_SAQUES -= 1
       
        print(LIMITE_SAQUES)
    else:
        print("Valor invalido.")
    return(saldo, extrato, LIMITE_SAQUES)

def novo_usuario(usuarios):
    cpf = input("Digite o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print("CPF já cadastrado") 
        return
    nome = input("Digite seu nome completo => ")
    data_nascimento = input("Digite a data de nascimento => ")
    endereco = input("Digite seu logadouro, nº, bairro,cidade/sigla do estado => ")
    usuarios.append({"nome":nome, "data de nascimento":data_nascimento, "CPF":cpf,"logadouro":endereco})
    print("Cadastro realizado coom sucesso.")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return{"agencia": agencia, "numero_conta":numero_conta, "usuario":usuario}
    print("Usuario nao encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia: {conta["agencia"]}
            C/C: {conta["numero_conta"]}
            Titular: {conta["usuario"]["nome"]}
        """
        print("="*50)
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    extrato = ""
    limite = 500

    contas=[]
    usuarios=[]
    

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Informe o valor => "))
           
            saldo, extrato = depositar(  saldo, valor,extrato )
            
        elif opcao =="e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao =="s":
            valor = float(input("Insira o valor => "))
           
            saldo, extrato, LIMITE_SAQUES = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                LIMITE_SAQUES=LIMITE_SAQUES,
                
            )

        elif opcao == "nu":
            novo_usuario(usuarios)


        elif opcao == "nc":
            numero_conta = len(contas)+ 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)


        elif opcao == "lc":
            listar_contas(contas)




        elif opcao =="q":
            break
        else:
            print("Opção invalida")
main()