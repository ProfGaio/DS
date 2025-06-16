class Conta:
    def __init__(self, titular, saldo):
        # Duplo underline
        self.__titular = titular
        self.__saldo = saldo
       

    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo

    @titular.setter
    def titular(self,nome):
        self.__titular = nome
    
   
