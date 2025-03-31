class Carro:
    
    placa = "00000"

    ano =  0.0

    modelo = "Volkswagen"

    def __init__(self):
        print("")
#Fim da classe Conta


c1 = Carro()

c2 = Carro()

c3 = Carro()


print(f"Placa: {c1.placa} \nDo ano de: {c1.ano} \nO modelo do carro é {c1.modelo}!")
print("**********************")

c1.placa = "F02498"
c1.ano = "1948"
c1.modelo = "Fiat"


print(f"Placa: {c1.placa} \n Do ano de: {c1.ano} \nO modelo do carro é {c1.modelo}!")
print("**********************")

c2.placa = "J342VG"
c2.ano = "2012"
c2.modelo = "Peugeot"

print(f"Placa: {c2.placa} \nDo ano de: {c2.ano} \nO modelo do carro é {c2.modelo}!")
print("**********************")

def ligar(self):
    print(f"Carro {self.modelo} ligado")

carro1 = Carro()

carro1.modelo = "Fiat"
carro1.placa = "FB437C"
carro1.ano = "1998"

def buzina():
    print("Biiiip! Biiiip!")

res = input("Deseja que o carro buzine?? \n: ")
res = res.upper()

if res == "SIM":
    buzina()
    






