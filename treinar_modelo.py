import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import classification_report, confusion_matrix
import joblib
from preprocessador import Preprocessador
import sys

def treinar_modelo(csv_path: str = 'cv_correto.csv', modelo_path: str = 'modelo_categorias.joblib', relatorio_path: str = 'relatorio_treinamento.txt'):
    df = pd.read_csv(csv_path)
    df['Descricao'] = df['Descricao'].astype(str)
    df['Tipo'] = df['Tipo'].astype(str)
    df['texto_completo'] = df['Descricao'] + ' ' + df['Tipo']
    X = df['texto_completo']
    y = df['Categoria']
    modelo = Pipeline([
        ('pre', Preprocessador()),
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42))
    ])
    # Cross-validation
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(modelo, X, y, cv=skf, scoring='accuracy')
    modelo.fit(X, y)
    joblib.dump(modelo, modelo_path)
    # Relatório detalhado
    y_pred = modelo.predict(X)
    report = classification_report(y, y_pred)
    matrix = confusion_matrix(y, y_pred)
    with open(relatorio_path, 'w') as f:
        f.write(f'Acurácia média (cross-val): {scores.mean():.4f}\n')
        f.write('Relatório de classificação (treino):\n')
        f.write(report + '\n')
        f.write('Matriz de confusão (treino):\n')
        f.write(str(matrix) + '\n')
    print(f"Modelo treinado e salvo como '{modelo_path}'")
    print(f"Acurácia média (cross-val): {scores.mean():.4f}")
    print(f"Relatório salvo em '{relatorio_path}'")

def treinar():
    """Treina o modelo de categorização com validação cruzada e relatório."""
    treinar_modelo()

if __name__ == '__main__':
    treinar()
