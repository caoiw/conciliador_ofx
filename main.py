from extrator_ofx import ler_ofx
from gerador_planilha import salvar_em_excel
from utils import listar_ofx
import pandas as pd


def main():
    arquivos = listar_ofx()

    if not arquivos:
        print("Nenhum arquivo OFX encontrado na pasta 'arquivos'.")
        return

    lista_df = []

    for arquivo in arquivos:
        print(f"Lendo arquivo: {arquivo}")
        df = ler_ofx(arquivo)
        lista_df.append(df)

    df_final = pd.concat(lista_df, ignore_index=True)

    salvar_em_excel(df_final)
    print("Processo concluído com sucesso.")


if __name__ == '__main__':
    main()
