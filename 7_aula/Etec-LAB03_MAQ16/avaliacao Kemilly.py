class Carro:
    
    placa = "00000"

    ano =  0.0

    velocidade = 2

    modelo = "Volkswagen"

    def __init__(self):
        print("")
#Fim da classe Conta


c1 = Carro()

c2 = Carro()

c3 = Carro()


print(f"Placa: {p2.placa} \Do ano de: {p2.ano} \no modelo do carro é {p2.modelo}!")
print("**********************")

c1.placa = "F02597"
c1.ano = "1960"
c1.modelo = "Fiat"


print(f"Placa: {m6.placa} \Do ano de: {m6.ano} \no modelo do carro é {m6.modelo}!")
print("**********************")

c2.placa = "J318DB"
c2.ano = "2020"
c2.modelo = "Peugeot"

print(f"Placa: {b1.placa} \Do ano de: {b1.ano} \no modelo do carro é {b1.modelo}!")
print("**********************")

def ligar(self):
    print(f"Carro {self.modelo} ligado")

carro1 = Carro()

carro1.modelo = "Fiat"
carro1.placa = "F260KB"
carro1.ano = "2000"

def buzina():
    print("Biiiip! Biiiip!")

res = input("Deseja que o carro buzine?? \n: ")
res = res.upper()

if res == "SIM":
    buzina()
    






