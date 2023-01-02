# Operadores de associação são utilizados para verificar se um objeto está presente em uma sequência.
# Podendo ser utiliados em um banco de dados exemplo a gente recupera uma lista de produtos e verificar se alguma coisa está nessa lista
# podemos utilizar o in, (claro que respeitando as boas práticas de consultas de consição de sistemas para escalar) 

curso = "Curso Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

print("Python" in curso)

print("melão" in frutas)

print("120" not in saques)

saldo = 500
saldo += 300
print(saldo)

x = (22 - 10) *3
print(x)