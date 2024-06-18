from main import Carro #importo da main a classe Carro onde estão as instancias do objeto
                       #carro

class Administrador: #crio uma class Admnisitrador
    def __init__(self): #crio uma instancia de classe para receber os "selfs"
        self.carros = [] #crio uma lista, para armazenar os carros

    def cadastrar_carro(self): #crio uma def para cadastrar os carros
        modelo = input("Digite o modelo do Carro: ") #crio as caracteristica
        marca = input("Digite a marca do modelo: ")
        cor = input("Digite a cor do Carro: ")
        potencia = input("Digite a potência do carro: ")

        carro = Carro(modelo, marca, cor, potencia)#crio uma variável carro, onde vai receber
                                        #o objeto carro e cadastrar o modelo marca cor e potencia

        self.carros.append(carro) #adiciono os balores dentro da lista carros
        print("Carro cadastrado com sucesso!") #finalizo com um print avisando que deu certo
