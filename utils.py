import os


def listar_ofx(pasta='arquivos'):
    arquivos = []
    for arquivo in os.listdir(pasta):
        if arquivo.lower().endswith('.ofx'):
            arquivos.append(os.path.join(pasta, arquivo))
    return arquivos
