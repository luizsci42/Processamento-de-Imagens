from processamento.Filtros import Morfologia


def gradiente_interno():
    """
    Para a extração de bordas, basta a aplicar a erosão em uma imagem e, em seguida, subtrair a imagem original da
    imagem erodida. O resultado será a borda da imagem. Esse é chamado o gradiente interno. A - (A erosão B).
    # TODO
    :return:
    """
    return -1


def gradiente_externo():
    """
    O gradiente externo é feito de forma análoga, mas substituindo a erosão pela dilatação. (A dilatação B) - A.
    # TODO
    :return:
    """
    return -1


def gradiente_morfologico():
    """
    A extração via gradiente morfológico é uma combinação das duas. Dilata e depois erode.
    (A dilatação B) - (A erosão B).
    # TODO
    :return:
    """
    return -1
