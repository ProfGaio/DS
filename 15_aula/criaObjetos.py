# Importa a classe Conta do arquivo contaBancaria
from contaBancaria import Conta

c1 = Conta("Antônio",100.00)
c2 = Conta("Maria",500.00)

print(f" Criada a conta para o cliente:{c1.titular}. Saldo Inicial:{c1.saldo}")

print(f" Criada a conta para o cliente:{c2.titular}. Saldo Inicial:{c2.saldo}")

c1.titular = input("Alterar o nome do titular da conta c1")

print(f"Titular atualizado: {c1.titular}")