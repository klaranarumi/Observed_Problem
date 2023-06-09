# Dataset
data = pd.read_csv('dataset.csv')

# Informações dos Bancos
## Pedaço do banco de dados
data.head()
## Informações gerais do banco de dados
data.info()
## Verificar quantos tipos tem em cada coluna
data.nunique()

# Ordenar os dados da coluna
data.sort_values(by='Col', ascending=False).head(10)

# Valores Nulos
## Verificar os valores nulos
data.isnull().sum()
## Excluir os valores nulos
data = data.dropna(axis=0)

# Valores Drops
## Verificar os valores duplicados
data[data.duplicated()]
## Excluir os valores duplicados
data = data.drop_duplicates()

# Remover linhas de acordo com Filtro
data_remove = data.loc[(data['Col'] > 100)]
data = data.drop(data_remove.index)

# Mudar o Tipo de coluna
data['Col'] = (data['Col']).astype('int')

# Mudar o Tipo da Data
data['Col_data'] = pd.to_datetime(data['Col_data'])
## Pegar os Dados do Mês da data
data['Col_data'].dt.month 
