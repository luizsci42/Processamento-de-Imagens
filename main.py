from Imagem import Imagem, TuplaCores
import Filtros as ft

"""
Vamos ler algumas imagens, aplicar efeitos e salvá-las em arquivo
"""


def ler_imagem(caminho: str):
    img = open(caminho, encoding='utf-8')
    linhas = []

    for linha in img:
        if not linha.startswith('#'):
            linhas.append(linha)

    # TODO: fazer com que na leitura, seja criado  objeto tupla, que especifica o número de canais de um pixel.
    # em seguida, o objeto pixel deve tomar a tupla como base para formar a matriz que sera iterada nos efeitos.
    # tipo_img = TuplaCores(linhas[0])
    tipo_img = linhas[0]
    dim_matriz = linhas[1]
    valor_max = int(linhas[2])

    return tipo_img, dim_matriz, valor_max, linhas[3:]


def realizar_operacoes_na_imagem(imagem: Imagem, efeito: ft.Filtro, saida: str):
    # nova_imagem = imagem
    nova_imagem = Imagem(imagem.tipo, imagem.dimensao, imagem.maximo, imagem.pixels)

    pixels_com_efeito = efeito.aplicar_efeito(imagem.pixels)
    nova_imagem.pixels = pixels_com_efeito
    nova_imagem.gerar_histograma(normalizar=True)
    print(nova_imagem.histograma)
    nova_imagem.salvar(saida)


path_entrada = 'img/lago_escuro.pgm'

tipo, dim, maxi, pixels = ler_imagem(path_entrada)
img_original = Imagem(tipo=str(tipo), dimensao=dim, maximo=maxi, pixels=pixels)
# img_original.mostrar_propriedades()

efeito_negativo = ft.Negativo(valor_maximo=img_original.maximo)
saida_negativo = 'img/saida_negativa.ppm'

efeito_limiarizacao = ft.Limiarizacao(valor_maximo=img_original.maximo, limiar=127)
saida_limiarizacao = 'img/saida_limiarizada.ppm'

efeito_fatiamento = ft.Fatiamento(100, 150)
saida_fatiamento = 'img/saida_fatiada.ppm'

realizar_operacoes_na_imagem(imagem=img_original, efeito=efeito_negativo, saida=saida_negativo)
realizar_operacoes_na_imagem(imagem=img_original, efeito=efeito_limiarizacao, saida=saida_limiarizacao)
realizar_operacoes_na_imagem(imagem=img_original, efeito=efeito_fatiamento, saida=saida_fatiamento)
