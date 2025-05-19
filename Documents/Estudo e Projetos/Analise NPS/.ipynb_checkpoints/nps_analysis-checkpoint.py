import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Exemplo de dados fictícios
data = {
    'Cliente': ['Cliente1', 'Cliente2', 'Cliente3', 'Cliente4', 'Cliente5'],
    'Nota': [10, 9, 6, 4, 7]
}

df = pd.DataFrame(data)

# Classificação NPS
def classificar_nps(nota):
    if nota >= 9:
        return 'Promotor'
    elif nota >= 7:
        return 'Neutro'
    else:
        return 'Detrator'

df['Categoria'] = df['Nota'].apply(classificar_nps)

# Cálculo do NPS
total_respostas = len(df)
promotores = len(df[df['Categoria'] == 'Promotor'])
detratores = len(df[df['Categoria'] == 'Detrator'])

nps = ((promotores - detratores) / total_respostas) * 100

print(f"NPS: {nps:.2f}")

# Visualização
sns.countplot(x='Categoria', data=df, palette='coolwarm')
plt.title('Classificação NPS dos Clientes')
plt.show()
