import pandas as pd

df = pd.read_csv(r"C:\Users\cristiane.patroclo\Downloads\funcionarios.csv")
#print(df)

#df['liquido'] = df['lucro'] - df['salario']
#print('df com coluna criada: liquido')
#print(df)

#df['nome'] = df['nome'].str.upper()
#print('df com coluna nome com valores em letra maisucula')
#print(df)

#df['lucro positivo'] = df['liquido'].apply(lambda x: 'lucro positivo' if x > 0 else 'lucro negativo')
#print('df com nova coluna, lucro positivo, construida a partir de um função')
#print(df)

#df = df.rename(columns={'liquido': 'lucro liquido', 'lucro positivo':'lucro final'})
#print('df com alteração de nome das colunas')
#print(df)

# criar coluna chamada 'salario_maior_5000' que terá os valores possui e 'não possui', a partir da coluan 'salario'
# renomear a coluna 'ativo' para 'empregado'

#df['salario_maior_5000'] = df['salario'].apply(lambda x: 'possui' if x > 5000 else 'não possui')
#df = df.rename(columns={'ativo': 'empregado'})
#print('df com a nova coluna, salario_maior_5000, e com coluna ativo renomeada como empregado')
#print(df)     

# faça a criação da coluna 'salario_maior_5000' novamente, mas somente com os funcionarios ativos
#df = df[df['ativo'] == True] 
#df['salario_maior_5000'] = df['salario'].apply(lambda x: 'possui' if x > 5000 else 'não possui')
#print(df)

