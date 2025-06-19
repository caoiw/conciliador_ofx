from ofxparse import OfxParser
import pandas as pd
import os


def ler_ofx(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        ofx = OfxParser.parse(arquivo)

    dados = []
    for t in ofx.account.statement.transactions:
        dados.append({
            'Data': t.date.date(),
            'Descrição': t.memo,
            'Valor': t.amount,
            'Tipo': 'Crédito' if t.amount > 0 else 'Débito',
            'Arquivo': os.path.basename(caminho_arquivo)
        })

    df = pd.DataFrame(dados)
    return df
