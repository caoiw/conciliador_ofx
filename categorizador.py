import joblib
import unicodedata
from preprocessador import Preprocessador

_modelo_global = None

# Dicionário de palavras-chave com tipo
PALAVRAS_CHAVE = [
    # (palavra, tipo, categoria)
    ('salario', 'credito', 'Receita'),
    ('bonus', 'credito', 'Receita'),
    ('fatura cartao', 'debito', 'Cartão de Crédito'),
    ('pagamento cartao', 'debito', 'Cartão de Crédito'),
    ('aluguel', 'debito', 'Moradia'),
    ('condominio', 'debito', 'Moradia'),
    ('supermercado', 'debito', 'Alimentação'),
    ('padaria', 'debito', 'Alimentação'),
    ('restaurante', 'debito', 'Alimentação'),
    ('ifood', 'debito', 'Alimentação'),
    ('farmacia', 'debito', 'Saúde'),
    ('consulta', 'debito', 'Saúde'),
    ('hospital', 'debito', 'Saúde'),
    ('imposto', 'debito', 'Impostos'),
    ('pix', None, 'Transferências'),
    ('transferencia', None, 'Transferências'),
    ('combustivel', 'debito', 'Transporte'),
    ('uber', 'debito', 'Transporte'),
    ('99', 'debito', 'Transporte'),
    ('onibus', 'debito', 'Transporte'),
    ('metro', 'debito', 'Transporte'),
    ('cinema', 'debito', 'Lazer'),
    ('show', 'debito', 'Lazer'),
    ('curso', 'debito', 'Educacao'),
    ('faculdade', 'debito', 'Educacao'),
    ('livraria', 'debito', 'Educacao'),
    ('assinatura', 'debito', 'Assinaturas'),
    ('netflix', 'debito', 'Assinaturas'),
    ('spotify', 'debito', 'Assinaturas'),
    ('amazon prime', 'debito', 'Assinaturas'),
    ('disney plus', 'debito', 'Assinaturas'),
    ('hbo max', 'debito', 'Assinaturas'),
    ('apple music', 'debito', 'Assinaturas'),
    ('globo play', 'debito', 'Assinaturas'),
    ('iphone', 'debito', 'Eletrônicos'),
    ('notebook', 'debito', 'Eletrônicos'),
    ('tablet', 'debito', 'Eletrônicos'),
    # Casos de crédito para transferências, reembolsos, etc
    ('devolucao', 'credito', 'Reembolso'),
    ('reembolso', 'credito', 'Reembolso'),
    ('deposito', 'credito', 'Receita'),
    ('freelance', 'credito', 'Receita'),
    ('venda', 'credito', 'Receita'),
]

def carregar_modelo(caminho_modelo='modelo_categorias.joblib'):
    global _modelo_global
    if _modelo_global is None:
        _modelo_global = joblib.load(caminho_modelo)
    return _modelo_global

def preprocessar_texto(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    return texto

def categorizar(descricao, valor, modelo=None):
    desc_proc = preprocessar_texto(descricao)
    tipo = 'credito' if valor > 0 else 'debito'
    # Regras de palavras-chave considerando tipo
    for palavra, tipo_regra, categoria in PALAVRAS_CHAVE:
        if palavra in desc_proc and (tipo_regra is None or tipo == tipo_regra):
            return categoria
    if modelo is None:
        modelo = carregar_modelo()
    entrada = desc_proc + ' ' + tipo
    categoria = modelo.predict([entrada])[0]
    return categoria

# Testes unitários para garantir acertos em descrições críticas
if __name__ == '__main__':
    testes = [
        ("SALARIO MENSAL - EMPRESA XYZ", 5000, "Receita"),
        ("SUPERMERCADO CARREFOUR", -150, "Alimentação"),
        ("PAGAMENTO NETFLIX", -45, "Assinaturas"),
        ("FARMACIA DROGASIL", -89, "Saúde"),
        ("ALUGUEL APARTAMENTO", -1200, "Moradia"),
        ("DEVOLUCAO COMPRA AMAZON", 200, "Reembolso"),
        ("CONTA DE LUZ ENEL", -180, "Moradia"),
        ("TRANSFERENCIA RECEBIDA JOAO SILVA", 2500, "Receita"),
        ("IPHONE LOJA APPLE", -3500, "Eletrônicos"),
        ("IFOOD DELIVERY", -65, "Alimentação"),
        ("PAGAMENTO SALDO CARTAO VISA", -800, "Cartão de Crédito"),
        ("SALDO CARTAO MASTERCARD", 0, "Outros"),
    ]
    modelo = carregar_modelo()
    for desc, valor, esperado in testes:
        cat = categorizar(desc, valor, modelo)
        print(f"{desc} | valor: {valor} | categoria: {cat} | esperado: {esperado} | {'OK' if cat == esperado else 'ERRO'}")
