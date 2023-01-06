conta_normal = False
conta_universitária = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
     print("Saque realizado com uso do cheque especial!")
    else:
     print("Não foi possivel realizar o saque, saldo insuficiente!")
elif conta_universitária:
    
    if saldo >= saque:
     print("Saque realizado com sucesso!")
    else:
     print("Saldo insuficiente!")
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com seu Gerente por favor !")


