class Filtro:
    def aplicar_efeito(self, matriz_pixels: [int]):
        """
        Define o efeito que será aplicado por cada classe
        :param matriz_pixels:
        :return:
        """
        return matriz_pixels

    def filtro_da_media(self, matriz_pixels: [int], prop_mask: (int, int)):
        """
        Dada uma matriz de pixels de tamanho m por n, calculamos os valores a e b, correspondentes à distância
        do centro da máscara às bordas, sendo: a = (m-1)/2 e b = (n-1)/2. Em seguida, é aplicada a filtragem linear
        para obtenção da imagem g(x,y).
        :param matriz_pixels:
        :param prop_mask:
        :return:
        """
        return matriz_pixels

    def filtro_da_mediana(self, matriz_pixels: [int], prop_mask: (int, int) = (3, 3)):
        """
                Dada uma matriz de pixels de tamanho m por n, calculamos os valores a e b, correspondentes à distância
                do centro da máscara às bordas, sendo: a = (m-1)/2 e b = (n-1)/2. Em seguida, é aplicada a filtragem linear
                para obtenção da imagem g(x,y).
                :param matriz_pixels:
                :param prop_mask:
                :return:
                """
        return matriz_pixels


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
        alargada = []

        return alargada


def converter_para_duas_dimensoes(pixels: [int]):
    dimensao_y = 512
    contador = 0
    nova_matriz = []

    for pixel in pixels:
        vetor_dim_y = []
        while contador <= dimensao_y:
            vetor_dim_y.append(pixel)
            contador += 1
        nova_matriz.append(vetor_dim_y)
        contador = 0

    return nova_matriz


class Suavizacao(Filtro):
    def filtragem_linear(self, matriz_pixels: [int], dim_mascara: (int, int)):
        """
        Para a filtragem espacial linear, é considerada uma imagem, chamada de máscara, de
        dimensões n por m, que irá percorrer cada pixel da imagem original e calcular
        a média ponderada dos pixels ao redor. O novo valor do píxel será então essa
        média. Esse filtro acaba por borrar a imagem.

        Este método aplica o filtro da média, desconsiderando os pixels da borda.

        :param matriz_pixels: A matriz formada com os pixels da imagem.
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
        imagem_g = []
        cont = 0

        matriz_pixels = converter_para_duas_dimensoes(matriz_pixels)

        # O for mais externo percorre as linhas da matriz imagem. Ou seja, o eixo x
        for x in range(1, len(matriz_pixels)):
            # Percorre as colunas da matriz imagem. Ou seja, o eixo y
            for y in range(1, len(matriz_pixels)):
                imagem_g.append(soma_ponderada)
                soma_ponderada = 0
                # percorre o eixo x da máscara
                for s in range((-1 * b), a + 1):
                    # percorre o eixo y da máscara
                    for t in range((-1 * b), b + 1):
                        print('({}, {}) ({}, {})'.format(x, y, s, t))
                        # calculamos a média ponderada de todos os pixels na máscara e alteramos o ponto central
                        # lembrando que (x, y) indicam os pontos que serão alterados e (s, t) os pontos na máscara
                        ponto = int(matriz_pixels[s][t])
                        soma_ponderada += int((int(peso) * ponto) / 9)

        return matriz_pixels
