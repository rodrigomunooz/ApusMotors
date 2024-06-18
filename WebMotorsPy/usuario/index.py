class Usuario:
    def __init__(self, carros):
        self.carros = carros

    def consultar_por_caracteristica(self):
        caracteristica = input("Qual característica você deseja analisar? (modelo | marca | cor | potencia): ").lower()
        escolha = input(f"Digite o {caracteristica} desejado: ")

        resultados = [carro for carro in self.carros if getattr(carro, caracteristica) == escolha]

        if resultados:
            for carro in resultados:
                carro.exibir_informacoes()
        else:
            print("Nenhum carro encontrado com essa característica.")
