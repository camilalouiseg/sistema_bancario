saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def depositar():
    global saldo,extrato
    valor = float(input("Digite o valor que deseja depositar "))
    if valor > 0:
        saldo += valor
        print(f"Você depositou R${valor} e o seu saldo é R${saldo}")
        extrato += f"Depósito de R${valor:.2f}\n"

    else:
        print("Não é possível depositar este valor")

def sacar():
    global saldo, numero_saques, extrato
    valor = float(input("Digite o valor que deseja sacar "))
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo

    if excedeu_saldo:
        print("Você não tem saldo suficiente")

    elif excedeu_limite:
        print("O valor ultrapassa o limite")

    elif excedeu_saques:
        print("Você já excedeu o número de saques")
        
    elif valor > 0:
        saldo -= valor
        print(f"Você sacou R${valor} e o seu saldo é {saldo}")
        extrato += f"Saque de R${valor:.2f}\n"
        numero_saques +=1
    else:
        print('Operação falhou!')

def ver_extrato():
    global extrato
    print("=========   EXTRATO   =========")
    print(f"\n{extrato}\n")
    print(f"Saldo: R${saldo:.2f}")
    print("===============================")
       
        
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

while True :
    opcao = input(menu)

    if opcao == "d":
        depositar()

    elif opcao == "s":
        sacar()
    
    elif opcao == "e":
        ver_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida")