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
            saida.write(str(self.maximo))
            saida.writelines(str(self.pixels))

    def mostrar_propriedades(self):
        print('Tipo: {}\nDimensões: {}\nValor máximo: {}'.format(
            self.tipo,
            self.dimensao,
            self.maximo
            ))

    def gerar_histograma(self, normalizar: bool = False):
        """
        O histograma de uma imagem é definido como uma função discreta
        h(rk) = nk, em que rk é o k-ésimo nível de cinza e nk é o número
        de pixels na imagem contendo o nível de cinza rk.

        Quando o parâmetro normalizar está definido como True, o histograma
        é dado por p(rk) = nk/n para k [0, L-1], em que L é o valor máximo
        dos pixels. A função p(r) nos dá a probabilidade de ocorrência de
        dado nível de cinza rk.

        :param normalizar:
        :return:
        """
        histograma = []
        pixels = self.pixels
        niveis_cinza = set(pixels)

        if normalizar:
            for nivel in niveis_cinza:
                nk = pixels.count(nivel) / len(niveis_cinza)
                histograma.append([nivel, nk])
        else:
            for nivel in niveis_cinza:
                nk = pixels.count(nivel)
                histograma.append([nivel, nk])

        self.histograma = histograma
