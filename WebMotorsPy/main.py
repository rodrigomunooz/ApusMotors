class Carro: #aqui eu criei a class carro, nela eu vou colocar todas as caracteristicas
             # que o objeto carro possui
    def __init__(self, modelo, marca, cor, potencia): #criei uma instancia da classe
                                                    #que é onde vou colocar os dados
        self.modelo = modelo                        #por exemplo, a cor até potencia  
        self.marca = marca                          #o self é basicamente o "proprio" objt
        self.cor = cor                              # para cada item criado e escolhido ele vai "mudar" la na outra parte do código                                 
        self.potencia = potencia            #ou seja se o usuario escolher ver preto, 200cv, etc, ele vai puxar todos que tem essas expecificações

    def exibir_informacoes(self): #criei uma def para mostrar as informações do carro, quando for chamado
        print(f"Modelo: {self.modelo}, Marca: {self.marca}, Cor: {self.cor}, Potência: {self.potencia}")


def main():# fora da class, aqui crio a def main, ela é o programa principal basicamente
    from adm.index import Administrador #aqui vou importar o arquivo index, da pasta adm
                                        #e também vou importar a class Administrador
    from usuario.index import Usuario  #aqui faço o mesmo processo, porém da pasta usuario
                                       #e chamo a class Usuario

    print("RodrigoMotors app") # inicio de boas vindas
    print("-------------")

    administrador = Administrador() #crio uma variavel para receber a função administrador

    while True: #enquanto for verdadeiro( enquanto não escolher a opção de sair)
        print("\n1. Cadastrar carro") # coloco as opções
        print("2. Consultar carros por característica")
        print("3. Sair")
        escolha = input("Escolha uma opção: ") # um input para o usuario ou adm escolher

        if escolha == '1':
            administrador.cadastrar_carro() #se a escolha for 1, abrir o modo adm e chamo
                                            #a função para cadastrar um carro
        elif escolha == '2':                        
            usuario = Usuario(administrador.carros)#se for 2, abrir no modo usuario e chamo
            usuario.consultar_por_caracteristica()#a função para consultar caracteristicas
        elif escolha == '3':
            break #fechar se a opção for 3
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
