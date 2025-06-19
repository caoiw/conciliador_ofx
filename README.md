# 🏦 Conciliador OFX

## Descrição
Este programa lê arquivos OFX (extratos bancários) da pasta `arquivos/` e gera uma planilha Excel consolidando todas as transações.

## Instalação
1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/conciliador_ofx.git

    Instale as dependências:

pip install -r requirements.txt

Como usar

    Coloque seus arquivos .ofx na pasta arquivos/.

    Execute o programa:

python main.py

    O arquivo relatorio.xlsx será gerado na pasta output/.

Estrutura da Planilha

    Aba Transacoes: Todas as transações consolidadas.

    Aba Resumo: Total de créditos e débitos.

Melhorias futuras

    Categorização de despesas.

    Interface gráfica (Streamlit).

    Dashboard com gráficos.