class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0 

    def acelerar(self, quantidade):
        self.velocidade += quantidade

    def frear(self, quantidade):
        self.velocidade = max(0, self.velocidade - quantidade)

    def mostrar_info(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'Velocidade atual: {self.velocidade} km/h')


marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
ano = int(input("Digite o ano de fabricação do carro: "))

carro = Carro(marca, modelo, ano)

carro.mostrar_info()

while True:
    acao = input("Deseja acelerar ou frear o carro? (Digite 'aumentar', 'diminuir' ou 'fechar' para fechar o programa): ").lower()

    if acao == 'aumentar':
        quantidade = int(input("Quanto deseja aumentar? "))
        carro.acelerar(quantidade)
        carro.mostrar_info()
    elif acao == 'diminuir':
        quantidade = int(input("Quanto deseja diminuir? "))
        carro.frear(quantidade)
        carro.mostrar_info()
    elif acao == 'fechar':
        print("fechando.")
        break
    else:
        print("Comando inválido. Tente novamente.")