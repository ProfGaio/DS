class Carro:
    def __init__(self, marca, modelo, ano):
       
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0  

    def acelerar(self, valor):
        
        self.velocidade += valor
        print(f'O carro acelerou para {self.velocidade} km/h.')

    def frear(self, valor):
        
        self.velocidade = max(0, self.velocidade - valor)
        print(f'O carro reduziu a velocidade para {self.velocidade} km/h.')

    def mostrar_info(self):
        
        print(f'Carro: {self.marca} {self.modelo} ({self.ano})')
        print(f'Velocidade atual: {self.velocidade} km/h')

    def buzinar(self):
        
        print("Biiip! Biiip!")



marca = input("Informe a marca do carro: ")
modelo = input("Informe o modelo do carro: ")
ano = int(input("Informe o ano de fabricação do carro: "))

meu_carro = Carro(marca, modelo, ano)


meu_carro.acelerar(50)
meu_carro.frear(20)
meu_carro.mostrar_info()
meu_carro.buzinar()

carros = [
    Carro("Ford", "Fiesta", 2020),
    Carro("Chevrolet", "Onix", 2023),
    Carro("Honda", "Civic", 2021)
]

for carro in carros:
    carro.mostrar_info()
    carro.buzinar()
