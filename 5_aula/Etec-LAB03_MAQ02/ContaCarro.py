class Carro:
modelo =""
marca = ""
ano =0
km =0
cor =""

def __init__(self):
    print ("objeto carro criado! ")

 def   ligar (self):
      print(f"Carro {self. modelo} ligado") 

carro1 = Carro()
carro1.modelo = "Creta"
carro1.marca = "Hunday"
carro1.ano = 2021
carro1.cor ="branca" 
 carro1 ligar()