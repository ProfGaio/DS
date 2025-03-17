class Conta:
   numero = "00000"
   saldo = 0.0
   def __init__ (self):
      print ("Criando um objeto!") 

    def depositar(self,valor):
      self.saldo = self.saldo + valor 

c1 = Conta()
c2 = Conta()
c3 = Conta()

print (f"conta1 {c1.numero} popssui saldo de {c1. saldo}")

c1.numero = "12345-6"
c1.saldo = 100.0

print (f"conta1 {c1.numero} popssui saldo de {c1. saldo}")


print (f"conta2 indefinida: {c2.numero} popssui saldo de {c1. saldo}")

c2.numero = "12345-6"
c2.saldo = 100.0

print (f"conta2 {c2.numero} popssui saldo de {c2. saldo}")


print (f"conta3 indefinida: {c3.numero} popssui saldo de {c3. saldo}")

c3.numero = "12345-6"
c3.saldo = 100.0

print (f"conta3 {c3.numero} popssui saldo de {c3. saldo}")
