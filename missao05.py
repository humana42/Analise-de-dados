# Este programa analisa um arquivo JSON de site de compras, com os seguintes criterios:

# ** Contagem de Compradores **
# Número total de compradores

# ** Análise Geral de Compras **
# Número de itens exclusivos
# Preço médio de compra
# Número total de compras
# Rendimento total

# ** Informações Demográficas Por Gênero **
# Porcentagem e contagem de compradores masculinos
# Porcentagem e contagem de compradores do sexo feminino
# Porcentagem e contagem de outros / não divulgados

# ** Análise de Compras Por Gênero **
# Número de compras
# Preço médio de compra
# Valor Total de Compra
# Compras for faixa etária

# ** Identifique os 5 principais compradores pelo valor total de compra e, em seguida, liste (em uma tabela): **
# Login
# Número de compras
# Preço médio de compra
# Valor Total de Compra
# Itens mais populares

# ** Identifique os 5 itens mais populares por contagem de compras e, em seguida, liste (em uma tabela): **
# ID do item
# Nome do item
# Número de compras
# Preço do item
# Valor Total de Compra
# Itens mais lucrativos

# ** Identifique os 5 itens mais lucrativos pelo valor total de compra e, em seguida, liste (em uma tabela): **
# ID do item
# Nome do item
# Número de compras
# Preço do item
# Valor Total de Compra

import json
import pandas as pd
# abrir o arquivo
arquivo = pd.read_json('dados_compras.JSON')
#print(arquivo.head())

#informações sobre os compradores:
info = arquivo.loc[: ,['Login', 'Idade', 'Sexo']]
#print(info.head())

#Quantidade de Compradores
info = info.drop_duplicates()
qtd = info.count()
#print(pd.DataFrame({'TOTAL DE COMPRADORES': [qtd]}))


#Analise geral de comprar
unico = len(arquivo['Item ID'].unique())
qtd_compras = arquivo['Valor'].count()
total = arquivo['Valor'].sum()
media = arquivo['Valor'].mean()

analise_geral = pd.DataFrame({'Numero de itens unico': unico,
                    'Qtd de Compras': qtd_compras,
                    'Total de Vendas (R$)': total,
                    'Preço medio (R$)': [media]})
analise_geral = analise_geral.round(2)
#print(analise_geral)

#Informações Demograficas
qtd_sexo = arquivo['Sexo'].value_counts()
percent_sexo = (qtd_sexo/qtd)*100

info_demografica = pd.DataFrame({'Qtd': qtd_sexo,
                                 '%': percent_sexo})
info_demografica = info_demografica.round(2)
#print(info_demografica)

#Analise por Genero
qtd_com_genero = arquivo.groupby(['Sexo']).count()['Valor'].rename('Numero Compras')
media_preco_genero = arquivo.groupby(['Sexo']).mean()['Valor'].rename('Media Preço')
total_preco_genero = arquivo.groupby(['Sexo']).sum()['Valor'].rename('Total Preço')
faixa_etaria = total_preco_genero/qtd_sexo

analise_genero = pd.DataFrame({'Numero de compras': qtd_com_genero,
                               'Media de Preço': media_preco_genero,
                               'Total Preço': total_preco_genero,
                               'Faixa etaria': faixa_etaria})
analise_genero = analise_genero.round(2)
#print(analise_genero)

# Top 5 compradores
valor_total = arquivo.groupby(['Login']).sum()['Valor'].rename('Valor Total de Compras')
valor_medio = arquivo.groupby(['Login']).mean()['Valor'].rename('Valor medio de compras')
numero_compra = arquivo.groupby(['Login']).count()['Valor'].rename('Numero de compras')

compradores = pd.DataFrame({'Valor total de compras': valor_total,
                            'Valor medio de compras': valor_medio,
                            'Numero de Compras': numero_compra})

compradores = compradores.round(2)
#print(compradores.sort_values('Valor total de compras', ascending=False).head(5))

# Top 5 itens mais comprados
item_total = arquivo.groupby(['Nome do Item']).sum()['Valor'].rename('Preço dos itens')
item_media = arquivo.groupby(['Nome do Item']).mean()['Valor'].rename('Media dos itens')
itens_num = arquivo.groupby(['Nome do Item']).count()['Valor'].rename('Numeros de itens')

itens = pd.DataFrame({'Preço de itens': item_total,
                      'Media dos itens': item_media,
                      'Numero de itens': itens_num})
itens = itens.round(2)
#print(itens.sort_values('Numero de itens', ascending=False).head(5))

# Top 5 itens mais caros
print(itens.sort_values('Preço de itens', ascending=False).head(5))