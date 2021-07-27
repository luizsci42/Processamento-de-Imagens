class Pixel:
    """
    O objeto Pixel é composto por tuplas de cores. Seu atributo numero_fontes deve
    ser substituído por um objeto TuplaCores.
    """

    def __init__(self, n_fontes: str):
        # self.tupla = TuplaCores(int(n_fontes[1]))
        self.numero_fontes = n_fontes


class TuplaCores:
    """
    Classe correspondente à tupla de cores que compõe o Pixel. Quando é do tipo P2, os
    pixels são monocromáticos, enquanto que o tipo P3 indica que os pixels são compostos de valores RGB.
    """

    def __init__(self, tipo_tupla: str):
        self.tipo_tupla = tipo_tupla[1]


class Imagem:
    """
    Esta classe define uma imagem em formato .ppm
    Nesse formato, são especificados se cada pixel usa 2 ou 3 fontes de cor, sendo assim,
    monocromática ou colorida; a dimensão da array de pixels, ou seja, a resolução; o valor
    máximo para cada fonte que compõe o pixel e, por fim, a matriz de pixels. Ou seja, a
    imagem propriamente dita.

    O atributo pixels deve ser substituido por um objeto Pixel e o atributo tipo deve ser removido.
    """

    def __init__(self, tipo: str, dimensao: str, maximo: int, pixels: [int]):
        # self.tipo = Pixel(tipo)
        self.tipo = tipo
        self.dimensao = dimensao
        self.maximo = maximo
        self.pixels = pixels
        self.histograma = []

    def salvar(self, nome: str):
        with open(nome, mode='w') as saida:
            saida.write(str(self.tipo))
            saida.write(str(self.dimensao))
            if not str(self.tipo).__contains__('1'):
                saida.write(str(self.maximo))
            saida.write('\n')
            for pixel in self.pixels:
                for valor in pixel:
                    saida.write(str(valor) + '\n')

    def mostrar_propriedades(self):
        print('Tipo: {}\nDimensões: {}\nValor máximo: {}'.format(
            self.tipo,
            self.dimensao,
            self.maximo
            ))

    def gerar_histograma(self, normalizar: bool = False, salvar: bool = False):
        """
        O histograma de uma imagem é definido como uma função discreta
        h(rk) = nk, em que rk é o k-ésimo nível de cinza e nk é o número
        de pixels na imagem contendo o nível de cinza rk.

        Quando o parâmetro normalizar está definido como True, o histograma
        é dado por p(rk) = nk/n para k [0, L-1], em que L é o valor máximo
        dos pixels. A função p(r) nos dá a probabilidade de ocorrência de
        dado nível de cinza rk. Assim, o formato do histograma não muda,
        mas os valores vão ficar entre 0 e 1.

        :param normalizar:
        :param salvar:
        :return: void
        """
        histograma = []
        nks = []
        pixels = self.pixels
        niveis_cinza = list(set(pixels))

        for nivel in niveis_cinza:
            if normalizar:
                nk = pixels.count(nivel) / len(pixels)
            else:
                nk = pixels.count(nivel)
            nks.append(nk)
            histograma.append([nivel, nk])

        self.histograma = histograma

        if salvar:
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots(figsize=(23, 8))
            ax.bar(niveis_cinza, nks)
            ax.set_title('Histograma da imagem')
            ax.set_xlabel('Níveis de cores')
            ax.set_ylabel('nk')

            if normalizar:
                fig.savefig('img/histograma_norm.png')
            else:
                fig.savefig('img/histograma.png')

    def equalizar(self, salvar: bool = False, verboso: bool = False):
        """
        Esse é doideira pra explicar

        :return:
        """
        novo_histograma = []
        pixels_img = self.pixels
        niveis_cinza = list(set(pixels_img))
        soma = 0

        if verboso:
            print('Numero de níveis de cinza: {}'.format(len(niveis_cinza)))
            hist_norm = []
            hist_cum = []

            # o histograma normalizado me diz a probabilidade de cada nível de cinza aparecer em um pixel
            for nivel in niveis_cinza:
                # a normalização diz a probabilidade de cada nível de cinza aparecer em um pixel arbitrário
                nk = pixels_img.count(nivel) / len(pixels_img)
                hist_norm.append(nk)

            print('Histograma normalizado:\n{}'.format(hist_norm))

            for i in range(0, len(hist_norm)):
                # fazemos a soma cumulativa dessas probabilidades
                soma += hist_norm[i]
                hist_cum.append(soma)

            print('Histograma cumulativo:\n{}'.format(hist_cum))

            for i in range(0, len(hist_cum)):
                # retiramos os valores de sua representação probabilistica
                valor_final = round(hist_cum[i] * self.maximo)
                novo_histograma.append(valor_final)

            print('Histograma final:\n{}'.format(novo_histograma, len(novo_histograma)))

        # se a opção verbosa estiver desabilitada
        else:
            # o histograma normalizado me diz a probabilidade de cada nível de cinza aparecer em um pixel
            for nivel in niveis_cinza:
                # a normalização diz a probabilidade de cada nível de cinza aparecer em um pixel arbitrário
                nk = pixels_img.count(nivel) / len(pixels_img)
                # fazemos a soma cumulativa dessas probabilidades
                soma += nk
                # retiramos os valores de sua representação probabilistica
                valor_final = round(soma * self.maximo)
                novo_histograma.append(valor_final)

        print('Fim da operação, alterando pixels da imagem')
        self.pixels = novo_histograma

        if salvar:
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots(figsize=(23, 8))
            ax.bar(niveis_cinza, novo_histograma)
            ax.set_title('Histograma equalizado da imagem original')
            ax.set_xlabel('Níveis de cores')
            ax.set_ylabel('Valor normalizado')

            fig.savefig('img/histograma_equalizado.png')
