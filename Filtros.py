class Filtro:
    def aplicar_efeito(self, matriz_pixels: [int]):
        """
        Define o efeito que será aplicado por cada classe
        :param matriz_pixels:
        :return:
        """
        return matriz_pixels

    def filtragem_linear(self, matriz_pixels: [int], prop_mask: (int, int)):
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


class Suavizacao(Filtro):
    def filtragem_linear(self, matriz_pixels: [int], prop_mask: (int, int)):
        m, n = prop_mask[0], prop_mask[1]
        mascara = 1 / (m * n)
        a, b = ((m - 1) / 2), ((n - 1) / 2)
        imagem_g = []

        for x in range(0, len(matriz_pixels) + 1):
            for y in range(0, len(matriz_pixels) + 1):
                for s in range((-1 * b), a + 1):
                    for t in range((-1 * b), b + 1):
                        ponto = mascara[s, t] * matriz_pixels[x + s, y + t]
                        imagem_g.append(ponto)

        return imagem_g
