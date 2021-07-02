from Imagem import Imagem


class Filtro:
    def aplicar_efeito(self, matriz_pixels: [int]):
        """
        Define o efeito que será aplicado por cada classe
        :param matriz_pixels:
        :return:
        """
        return matriz_pixels

    def filtro_da_media(self, imagem: Imagem, dim_mascara: (int, int) = (3, 3)):
        """
        Dada uma matriz de pixels de tamanho m por n, calculamos os valores a e b, correspondentes à distância
        do centro da máscara às bordas, sendo: a = (m-1)/2 e b = (n-1)/2. Em seguida, é aplicada a filtragem linear
        para obtenção da imagem g(x,y).
        :param imagem:
        :param dim_mascara:
        :return:
        """
        return imagem.pixels

    def filtro_da_mediana(self, imagem: Imagem, dim_mascara: (int, int) = (3, 3)):
        """
                Dada uma matriz de pixels de tamanho m por n, calculamos os valores a e b, correspondentes à distância
                do centro da máscara às bordas, sendo: a = (m-1)/2 e b = (n-1)/2. Em seguida, é aplicada a filtragem linear
                para obtenção da imagem g(x,y).
                :param imagem:
                :param dim_mascara:
                :return:
                """
        return imagem.pixels


class Identidade(Filtro):
    def aplicar_efeito(self, matriz_pixels: [int]):
        nova_imagem = []
        for pixel in matriz_pixels:
            nova_imagem.append(pixel)

        return '\n'.join(nova_imagem)


class Negativo(Filtro):
    """
    Esta classe implementa um filtro negativo
    """
    def __init__(self, valor_maximo: int):
        self.valor_maximo = int(valor_maximo)

    def aplicar_efeito(self, matriz_pixels: [int]):
        """
        Negativamos a imagem.
        Para cada pixel da imagem, é aplicada a função L - 1 - p
        Em que L é o valor máximo e p é o pixel em questão.

        :param matriz_pixels:
        :return: A matriz de pixels negativados
        """
        negativada = []
        for pixel in matriz_pixels:
            try:
                negativo = self.valor_maximo - 1 - int(pixel)
                if negativo < 0:
                    negativo = 0
                negativada.append(negativo)
            except ValueError:
                pass

        return negativada


class Limiarizacao(Filtro):
    """
    Esta classe implementa o filtro de Limiarização
    """
    def __init__(self, limiar: int, valor_maximo: int):
        self.valor_maximo = valor_maximo
        self.limiar = limiar

    def aplicar_efeito(self, matriz_pixels: [int]):
        """
        Aplica o efeito de limiarização.

        :param matriz_pixels:
        :return:
        """
        limiarizada = []
        for pixel in matriz_pixels:
            try:
                canal = int(pixel)
                if canal >= self.limiar:
                    canal = 255
                else:
                    canal = 0
                limiarizada.append(canal)
            except ValueError:
                pass

        return limiarizada


class Fatiamento(Filtro):
    def __init__(self, limite_inf: int, limite_sup: int):
        if limite_inf < limite_sup:
            self.limite_inf = limite_inf
            self.limite_sup = limite_sup
        elif limite_inf == limite_sup:
            raise ValueError
        else:
            self.limite_inf = limite_sup
            self.limite_sup = limite_inf

    def aplicar_efeito(self, matriz_pixels: [int]):
        """
        Recebe o limite inferior e superior, correspondente a uma faixa de cores.
        As cores nesta faixa serão alteradas para valores maiores, enquanto que
        os valores fora dessa faixa serão mantidos.
        :param matriz_pixels:
        :return:
        """
        contrastante = []

        for pixel in matriz_pixels:
            canal = int(pixel)

            # caso em que o pixel está dentro da faixa de destaque
            if self.limite_inf <= canal < self.limite_sup:
                canal = 230

            contrastante.append(canal)

        return contrastante


class AlargamentoContraste(Filtro):
    def __init__(self):
        pass

    def aplicar_efeito(self, matriz_pixels: [int]):
        """
        O alargamento de contraste recebe dois limites e uma inclinação e mapeia
        os pixels de uma imagem de forma que os valores abaixo do limite inferior
        serão mapeados gradativamente, considerando a inclinação. Os pixels que
        estiverem entre o limite inferior e o superior serão mapeados para valores
        mais altos (maior inclinação da reta nessa faixa) e, por fim, os pixels
        de valor acima do limite superior também serão achatados (inclinação da
        reta igual à do limite inferior e menor que da faixa entre os dois limites.

        :param matriz_pixels:
        :return: Matriz de pixels com o alargamento de contraste aplicado
        """
        img_alargada = []

        return img_alargada


def converter_para_duas_dimensoes(imagem: Imagem):
    import numpy as np

    pixels = imagem.pixels
    dim_y, dim_x = imagem.dimensao.split(' ')
    print('Convertendo para dimensões {}x{}'.format(dim_y, dim_x))
    # outro método pode ser: [pixels[i:i + int(dim_y)] for i in range(0, len(pixels), int(dim_y))]
    return np.reshape(pixels, (int(dim_y), int(dim_x)))


class Suavizacao(Filtro):
    def filtro_da_media(self, imagem: Imagem, dim_mascara: (int, int) = (3, 3)):
        """
        Para a filtragem espacial linear, é considerada uma imagem, chamada de máscara, de
        dimensões n por m, que irá percorrer cada pixel da imagem original e calcular
        a média ponderada dos pixels ao redor. O novo valor do píxel será então essa
        média. Esse filtro acaba por borrar a imagem.

        Este método aplica o filtro da média, desconsiderando os pixels da borda.

        :param imagem: A imagem que será filtrada.
        :param dim_mascara: As dimensões da máscara utilizada.
        :return: A imagem filtrada.
        """
        # m e n são as dimensões da máscara
        m, n = dim_mascara[0], dim_mascara[1]
        # daremos pesos iguais para cada valor do pixel
        # peso = 1 / (m * n)
        peso = 1
        # a e b nos dão, respectivamente, a distância do centro pras bordas verticais e horizontais
        a, b = int(((m - 1) / 2)), int(((n - 1) / 2))
        soma_ponderada = 0
        # objeto que representa a imagem de saída
        imagem_g = Imagem(
            tipo=imagem.tipo,
            dimensao=imagem.dimensao,
            maximo=imagem.maximo,
            pixels=imagem.pixels
        )

        # se a imagem for do tipo P1, ela já foi lida com duas dimensões na abertura
        if not imagem.tipo.__contains__('1'):
            matriz_pixels = converter_para_duas_dimensoes(imagem)
        else:
            matriz_pixels = imagem_g.pixels

        # O for mais externo percorre as linhas da matriz imagem. Ou seja, o eixo x
        for x in range(1, len(matriz_pixels) - 1):
            # Percorre as colunas da matriz imagem. Ou seja, o eixo y
            for y in range(1, len(matriz_pixels) - 1):
                # percorre o eixo x da máscara
                for s in range((-1 * a), a + 1):
                    # percorre o eixo y da máscara
                    for t in range((-1 * b), b + 1):
                        # calculamos a média ponderada de todos os pixels na máscara e alteramos o ponto central
                        # lembrando que (x, y) indicam os pontos que serão alterados e (s, t) os pontos na máscara
                        lin, col = x + s, y + t
                        ponto = int(matriz_pixels[lin][col])
                        soma_ponderada += int((int(peso) * ponto) / 9)
                        print('Soma = {} * {}'.format(int(peso), ponto))
                        print('Soma ponderada: {} ({}, {}) ({}, {}) / 9'.format(soma_ponderada, x, y, s, t))
                print('\nNovo valor: {}\n'.format(soma_ponderada))
                imagem_g.pixels[x][y] = soma_ponderada
                soma_ponderada = 0

        return imagem_g.pixels

    def filtro_da_mediana(self, imagem: Imagem, dim_mascara: (int, int) = (3, 3)):
        # m e n são as dimensões da máscara
        m, n = dim_mascara[0], dim_mascara[1]
        # a e b nos dão, respectivamente, a distância do centro pras bordas verticais e horizontais
        a, b = int(((m - 1) / 2)), int(((n - 1) / 2))
        # objeto que representa a imagem de saída
        imagem_g = Imagem(
            tipo=imagem.tipo,
            dimensao=imagem.dimensao,
            maximo=imagem.maximo,
            pixels=imagem.pixels
        )

        # se a imagem for do tipo P1, ela já foi lida com duas dimensões na abertura
        if not imagem.tipo.__contains__('1'):
            matriz_pixels = converter_para_duas_dimensoes(imagem)
        else:
            matriz_pixels = imagem_g.pixels

        print('A matriz a ser filtrada: {}\n'.format(matriz_pixels))

        # O for mais externo percorre as linhas da matriz imagem. Ou seja, o eixo x
        for x in range(1, len(matriz_pixels) - 1):
            # Percorre as colunas da matriz imagem. Ou seja, o eixo y
            for y in range(1, len(matriz_pixels) - 1):
                valores_vizinhanca = []
                print('\nPonto {} na posição: ({}, {}) sendo analisado'.format(matriz_pixels[x][y], x, y))
                # percorre o eixo x da máscara
                for s in range((-1 * a), a + 1):
                    # percorre o eixo y da máscara
                    for t in range((-1 * b), b + 1):
                        lin, col = x + s, y + t
                        ponto = int(matriz_pixels[lin][col])
                        print('Vizinho {} na posição ({}, {})'.format(ponto, lin, col))
                        valores_vizinhanca.append(ponto)
                valores_vizinhanca.sort()
                print('Valores na vizinhança: ', valores_vizinhanca)
                posicao_meio = round(len(valores_vizinhanca) / 2)
                mediana = valores_vizinhanca[posicao_meio]
                print('A mediana é: ', mediana)
                imagem_g.pixels[x][y] = mediana
                print('O valor do pixel em ({}, {}) agora é: {}'.format(x, y, mediana))

        return imagem_g.pixels


class Morfologia(Filtro):
    def erosao(self, imagem: Imagem, dim_mascara: (int, int) = (3, 3)):
        """
        Recebe uma imagem e uma máscara, aplicando o efeito morfológico de erosão.
        A erosão consiste em criar uma nova imagem com as mesmas dimensões da imagem
        original e preencher os pixels com o valor 1 na nova imagem quando os pixels
        na vizinhança desse possuem todos o valor 1.

        :param imagem: A imagem original que será erodida
        :param dim_mascara: As dimensões da máscara que ira percorrer a imagem
        :return: A imagem erodida
        """
        # m e n são as dimensões da máscara
        m, n = dim_mascara[0], dim_mascara[1]
        # a e b nos dão, respectivamente, a distância do centro pras bordas verticais e horizontais
        a, b = int(((m - 1) / 2)), int(((n - 1) / 2))

        # inicializamos a imagem de saída com todos os pixels em 0
        pixels_g = []

        for linha in imagem.pixels:
            for pixel in linha:
                pixels_g.append(0)

        # objeto que representa a imagem de saída
        imagem_g = Imagem(
            tipo=imagem.tipo,
            dimensao=imagem.dimensao,
            maximo=imagem.maximo,
            pixels=pixels_g
        )

        # se a imagem for do tipo P1, ela já foi lida com duas dimensões na abertura
        if not imagem.tipo.__contains__('1'):
            pixels_original = converter_para_duas_dimensoes(imagem)
        else:
            pixels_original = imagem.pixels

        imagem_g.pixels = converter_para_duas_dimensoes(imagem_g)

        # O for mais externo percorre as linhas da matriz imagem. Ou seja, o eixo x
        for x in range(1, len(pixels_original) - 1):
            # Percorre as colunas da matriz imagem. Ou seja, o eixo y
            for y in range(1, len(pixels_original) - 1):
                valores_vizinhanca = []
                # print('\nPonto {} na posição: ({}, {}) sendo analisado'.format(pixels_original[x][y], x, y))
                # percorre o eixo x da máscara
                for s in range((-1 * b), a + 1):
                    # percorre o eixo y da máscara
                    for t in range((-1 * b), b + 1):
                        # coordenadas do centro da máscara
                        lin, col = x - s, y - t
                        # este é o pixel que está no centro da máscara
                        ponto = int(pixels_original[lin][col])
                        # print('Vizinho {} na posição ({}, {})'.format(ponto, lin, col))
                        valores_vizinhanca.append(ponto)
                # verificamos se a máscara encaixa totalmente nos valores. Ou seja,
                # se todos os valores da vizinhança são 1
                valores = str(valores_vizinhanca)
                # print('Valores na vizinhança: ', valores)
                if not valores.__contains__('0'):
                    # quando todos os valores na máscara são 1,
                    # colocamos o valor 1 na nova imagem, na posição correspondente
                    print('Inserindo valor 1 na posição ({}, {})'.format(x, y))
                    imagem_g.pixels[x][y] = 1

        return imagem_g

    def dilatacao(self, imagem: Imagem, dim_mascara: (int, int) = (3, 3)):
        """

        :param imagem: A imagem original que será dilatada
        :param dim_mascara: As dimensões da máscara que ira percorrer a imagem
        :return: A imagem dilatada
        """
        # m e n são as dimensões da máscara
        m, n = dim_mascara[0], dim_mascara[1]
        # a e b nos dão, respectivamente, a distância do centro pras bordas verticais e horizontais
        a, b = int(((m - 1) / 2)), int(((n - 1) / 2))

        # inicializamos a imagem de saída com todos os pixels em 0
        pixels_g = []

        for linha in imagem.pixels:
            for pixel in linha:
                pixels_g.append(0)

        # objeto que representa a imagem de saída
        imagem_g = Imagem(
            tipo=imagem.tipo,
            dimensao=imagem.dimensao,
            maximo=imagem.maximo,
            pixels=pixels_g
        )

        # se a imagem for do tipo P1, ela já foi lida com duas dimensões na abertura
        if not imagem.tipo.__contains__('1'):
            print('Tipo P1')
            pixels_original = converter_para_duas_dimensoes(imagem)
        else:
            pixels_original = imagem.pixels

        imagem_g.pixels = converter_para_duas_dimensoes(imagem_g)

        # O for mais externo percorre as linhas da matriz imagem. Ou seja, o eixo x
        for x in range(1, len(pixels_original) - 1):
            # Percorre as colunas da matriz imagem. Ou seja, o eixo y
            for y in range(1, len(pixels_original) - 1):
                valores_vizinhanca = []
                # print('\nPonto {} na posição: ({}, {}) sendo analisado'.format(pixels_original[x][y], x, y))
                # percorre o eixo x da máscara
                for s in range((-1 * b), a + 1):
                    # percorre o eixo y da máscara
                    for t in range((-1 * b), b + 1):
                        # coordenadas do centro da máscara
                        lin, col = x - s, y - t
                        # este é o pixel que está no centro da máscara
                        ponto = int(pixels_original[lin][col])
                        # print('Vizinho {} na posição ({}, {})'.format(ponto, lin, col))
                        valores_vizinhanca.append(ponto)
                # verificamos se a máscara encaixa totalmente nos valores. Ou seja,
                # se todos os valores da vizinhança são 1
                valores = str(valores_vizinhanca)
                # print('Valores na vizinhança: ', valores)
                if valores.__contains__('1'):
                    print('Inserindo valor 1 na posição ({}, {})'.format(x, y))
                    imagem_g.pixels[x][y] = 1

        return imagem_g

    def abertura(self, imagem: Imagem):
        morfologia = Morfologia()
        imagem = morfologia.erosao(imagem)
        imagem = morfologia.dilatacao(imagem)

        return imagem

    def fechamento(self, imagem: Imagem):
        morfologia = Morfologia()
        imagem = morfologia.dilatacao(imagem)
        imagem = morfologia.erosao(imagem)

        return imagem