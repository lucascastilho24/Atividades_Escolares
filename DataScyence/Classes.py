class Carro:
    def __init__(self,motor,combustivel,cor):
        self.motor = motor
        self.combustivel = combustivel
        self.cor = cor

    def ligar(self):
        print("Dando partida!")
    
    def acelerar(self):
        print("Acelerando!")
    
    def parar(self):
        print("Acionando freio!")

carro1 = Carro("V6","Gasolina","Preto")
carro2 = Carro("V8","Etanol","Vermelho")
print(carro1.motor,carro1.combustivel,carro1.cor)
print(carro2.motor,carro2.combustivel,carro2.cor)
carro1.ligar()
carro2.acelerar()