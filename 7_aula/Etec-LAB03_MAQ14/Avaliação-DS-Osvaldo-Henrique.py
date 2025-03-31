
class Carro:
    def __init__(self, marca, modelo, ano):
        
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0 

    def acelerar(self, valor):
        
        self.velocidade += valor

    def frear(self, valor):
        
        self.velocidade = max(0, self.velocidade - valor)

    def mostrar_info(self):
        
        print(f'Marca do Carro: {self.marca}')
        print(f'Modelo do Carro: {self.modelo}')
        print(f'Ano do Carro: {self.ano}')
        print(f'Velocidade atual: {self.velocidade} km/h')



marca = input("Digite qual é a marca do carro: ")
modelo = input("Digite qual o modelo do carro: ")
ano = int(input("Digite qual o ano do carro: "))


carro = Carro(marca, modelo, ano)


carro.mostrar_info()


while True:
    acao = input("você deseja acelerar ou frear o carro? (Digite 'acelerar', 'frear' ou 'sair' para encerrar): ").lower()

    if acao == 'acelerar':
        valor = int(input("quanto deseja acelerar? "))
        carro.acelerar(valor)
        carro.mostrar_info()
    elif acao == 'frear':
        valor = int(input("quanto deseja frear? "))
        carro.frear(valor)
        carro.mostrar_info()
    elif acao == 'sair':
        print("*******Saindo do programa*******")
        break
    else:
        print("Comando inválido!!!. Tente novamente.")