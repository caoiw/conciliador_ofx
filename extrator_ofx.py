from ofxparse import OfxParser
import pandas as pd
import os
from categorizador import categorizar


def ler_ofx(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        ofx = OfxParser.parse(arquivo)

    dados = []
    for t in ofx.account.statement.transactions:
        descricao = t.memo
        valor = t.amount
        categoria = categorizar(descricao, valor)

        dados.append({
            'Data': t.date.date(),
            'Descrição': descricao,
            'Valor': valor,
            'Tipo': 'Crédito' if valor > 0 else 'Débito',
            'Categoria': categoria,
            'Arquivo': os.path.basename(caminho_arquivo)
        })

    df = pd.DataFrame(dados)
    return df
