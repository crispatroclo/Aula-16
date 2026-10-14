import pandas as pd

df = pd.DataFrame({
    'categoria': ['A', 'B', 'A', 'B', 'A'],
    'vendas': [100, 200, 150, 300, 120],
    'quantidade': [1, 2, 1, 3, 2]
})

print(df)
print('\n')

# media de vendas por categoria
#print(df.groupby('categoria')['vendas'].mean())
# solução alternativa 
#categoria_vendas = df.groupby('categoria')['vendas'].mean()
#print(categoria_vendas)
#print('\n')

# soma (de todas as colunas numericas) por categoria
#print(df.groupby('categoria').sum())
#print('\n')

# agrupar por multiplas colunas
#print(df.groupby(['categoria', 'quantidade'])['vendas'].sum()) # sem declarar o as_index como falso
#print(df.groupby(['categoria', 'quantidade'], as_index=False)['vendas'].sum()) # declararando o as_index como falso
#print('\n')

# todas as operaões na coluna vendas agrupadas pela coluna categoria
print(df.groupby('categoria')['vendas'].agg(['sum', 'mean', 'max', 'count']))
print('\n')

# ou com nomes personalizados 
print(df.groupby('categoria').agg(
    total_vendas=('vendas', 'sum'),
    media_vendas=('vendas', 'mean')
))