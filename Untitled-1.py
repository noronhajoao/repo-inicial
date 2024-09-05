
menu =   """

---------------------------------
         MENU PRINCIPAL
---------------------------------

[1] Depósitar
[2] Sacar
[3] Extrato
[4] Sair

=>  """

saldo = 10000
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3


while True:

    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Quanto você deseja depositar?: "))
        
        if valor > 0: 
          saldo += valor
          extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Algo deu errado! Por favor, tente novamente.")  

    
    
    elif opcao == "2":
        valor = float(input("Quanto você deseja sacar?: "))

        excedeu_saldo  = valor > saldo

        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print ("Operação falhou! saldo insuficiente. ")

        elif excedeu_limite:
            print ("Operção falhou! Você excedeu o limite. ") 

        elif excedeu_saques:
            print ("Operação falhou! Número máximo de saques excedido. ") 

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n" 
            numero_saque += 1

        else:
            print("Algo deu errado! Por favor, tente novamente.\n")    
    
    elif opcao == "3":
        print("\n================= EXTRATO ==================")
        print("Não foram realizadas nenhuma movimentações." if not extrato else extrato )
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")

    
    elif opcao "4": 
        break

   else: 
      print("Ops! algo deu errado, por favor, tente novamente.") 


