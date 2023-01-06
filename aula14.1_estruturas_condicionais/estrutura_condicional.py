#A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressõeslógicas são atendidas

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12


idade = int(input("Informe sua idade:  "))

if idade >=18:
    print("Maior de idade pode tirar a CNH. " )

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH. " )

if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar a CNH. " )
else:
    print("Ainda não pode tirar a CNH. " )



if idade >= MAIOR_IDADE:
        print("Maior de idade pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
     print("Pode fazer as aulas teóricas, mas ainda não pode fazer as praticas")
else:
    print("Ainda não pode tirar a CNH. " )






