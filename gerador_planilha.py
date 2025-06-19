import pandas as pd
import os


def salvar_em_excel(df, nome_arquivo='output/relatorio.xlsx'):
    os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)

    with pd.ExcelWriter(nome_arquivo) as writer:
        df.to_excel(writer, sheet_name='Transacoes', index=False)

        resumo = df.groupby('Tipo')['Valor'].sum().reset_index()
        resumo.to_excel(writer, sheet_name='Resumo', index=False)

    print(f"Planilha salva em: {nome_arquivo}")
