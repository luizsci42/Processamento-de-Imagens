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


def realizar_operacoes_na_imagem(imagem: Imagem, efeito: ft.Filtro):
    # nova_imagem = imagem
    nova_imagem = Imagem(imagem.tipo, imagem.dimensao, imagem.maximo, imagem.pixels)

    pixels_com_efeito = efeito.aplicar_efeito(imagem.pixels)
    nova_imagem.pixels = pixels_com_efeito
    nova_imagem.gerar_histograma(normalizar=True, salvar=True)

    return nova_imagem


def aplicar_todos_efeitos(img_original: Imagem):
    efeito_negativo = ft.Negativo(valor_maximo=img_original.maximo)
    efeito_limiarizacao = ft.Limiarizacao(valor_maximo=img_original.maximo, limiar=100)
    efeito_fatiamento = ft.Fatiamento(100, 150)

    img_negativa = realizar_operacoes_na_imagem(imagem=img_original, efeito=efeito_negativo)
    img_limiarizada = realizar_operacoes_na_imagem(imagem=img_original, efeito=efeito_limiarizacao)
    img_fatiada = realizar_operacoes_na_imagem(imagem=img_original, efeito=efeito_fatiamento)

    img_negativa.salvar('img/saida_negativo.ppm')
    img_limiarizada.salvar('img/saida_limiarizacao.ppm')
    img_fatiada.salvar('img/saida_fatiamento.ppm')

    # print('Histograma da imagem negativada:\n{}'.format(img_negativa.histograma))
    # print('Histograma da imagem limiarizada:\n{}'.format(img_limiarizada.histograma))
    # print('Histograma da imagem fatiada:\n{}'.format(img_fatiada.histograma))

    # img_negativa.equalizar()
    # img_limiarizada.equalizar()
    # img_fatiada.equalizar()


def main():
    path_entrada = 'img/teste.ppm'

    tipo, dim, max, pixels = ler_imagem(path_entrada)
    img_original = Imagem(tipo=str(tipo), dimensao=dim, maximo=max, pixels=pixels)

    # objeto que representa a imagem de saída
    nova_imagem = Imagem(
        tipo=img_original.tipo,
        dimensao=img_original.dimensao,
        maximo=img_original.maximo,
        pixels=img_original.pixels
    )

    # objeto que representa o filtro de suavização
    suavizacao = ft.Suavizacao()
    # aplicamos o filtro da mediana na imagem original e colocamos a saída na nova imagem
    nova_imagem.pixels = suavizacao.filtro_da_mediana(img_original)

    # salvamos a imagem filtrada
    arquivo = 'img/saida_teste.pgm'
    nova_imagem.salvar(arquivo)
    print('Imagem salva como: {}'.format(arquivo))


if __name__ == '__main__':
    main()
