#Identar código é uma forma de manter o código fonte mais
#legível e manutenível. Mas em Python ela exerce um segundo
#papel, através da indentação o interpretador consegue
#determinar onde um bloco de comando inicia e onde ele
#termina

def sacar(valor):
    saldo = 200

    if saldo >= valor:
        print("valor sacado!")
        print("Retire seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")
    

def depositar(valor):
    saldo = 500
    saldo+= valor

sacar(1000)


