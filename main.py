from processamento.Imagem import Imagem
from processamento import Filtros as ft

"""
Vamos ler algumas imagens, aplicar efeitos e salvá-las em arquivo
"""


def ler_imagem(caminho: str):
    img = open(caminho, encoding='utf-8')
    linhas = []

    for linha in img:
        if not linha.startswith('#') and linha != '\n':
            linhas.append(linha)

    # TODO: fazer com que na leitura, seja criado  objeto tupla, que especifica o número de canais de um pixel.
    # em seguida, o objeto pixel deve tomar a tupla como base para formar a matriz que sera iterada nos efeitos.
    # tipo_img = TuplaCores(linhas[0])
    tipo_img = linhas[0]
    dim_matriz = linhas[1]
    pixels = []

    if tipo_img.__contains__('P1'):
        valor_max = '1'
        for linha in linhas[2:]:
            linha = linha.replace(' ', '')
            linha = linha.replace('\n', '')
            for pixel in linha:
                pixels.append(pixel)
    else:
        valor_max = int(linhas[2])
        pixels = [int(valor) for valor in linhas[3:]]

    return tipo_img, dim_matriz, valor_max, pixels


def realizar_operacoes_na_imagem(imagem: Imagem, efeito: ft.Filtro):
    # nova_imagem = imagem
    nova_imagem = Imagem(imagem.tipo, imagem.dimensao, imagem.maximo, imagem.pixels)

    pixels_com_efeito = efeito.aplicar_efeito(imagem.pixels)
    nova_imagem.pixels = pixels_com_efeito
    nova_imagem.gerar_histograma(normalizar=True, salvar=True)

    return nova_imagem


def aplicar_todos_efeitos(img_original: Imagem):
    efeito_negativo = ft.Negativo()
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
    path_entrada = 'img/ankh_negativo.pbm'
    tipo, dim, maxi, pixels = ler_imagem(path_entrada)
    img_original = Imagem(tipo=str(tipo), dimensao=dim, maximo=maxi, pixels=pixels)
    morfologia = ft.Morfologia()
    suavizacao = ft.Suavizacao()

    img_suavizada = suavizacao.filtro_da_mediana(img_original)
    nome_saida = 'out/ankh_negativo_suavizado.pbm'
    img_suavizada.salvar(nome_saida)
    print('Imagem salva como: ', nome_saida)

    img_erodida = morfologia.erosao(img_original)
    nome_saida = 'out/ankh_negativo_erodido.pbm'
    img_erodida.salvar(nome_saida)
    print('Imagem salva como: ', nome_saida)

    img_dilatado = morfologia.dilatacao(img_original)
    nome_saida = 'out/ankh_negativo_dilatado.pbm'
    img_dilatado.salvar(nome_saida)
    print('Imagem salva como: ', nome_saida)

    img_aberta = morfologia.abertura(img_original)
    nome_saida = 'out/ankh_negativo_aberto.pbm'
    img_aberta.salvar(nome_saida)
    print('Imagem salva como: ', nome_saida)

    img_fechada = morfologia.fechamento(img_original)
    nome_saida = 'out/ankh_negativo_fechado.pbm'
    img_fechada.salvar(nome_saida)
    print('Imagem salva como: ', nome_saida)


if __name__ == '__main__':
    main()
