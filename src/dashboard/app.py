import sqlite3
import pandas as pd
import streamlit as st

## SQLite Database
# Connect to db
conn = sqlite3.connect('../data/quotes.db')

# Load dataframe from db
df = pd.read_sql_query('SELECT * FROM mercadolivre_itens', conn)

# Close db connection 
conn.close()

## Streamlit
# Title
st.title('Pesquisa de Mercado - Tênis Masculinos no Mercado Livre')

## KPIs
# Improve layout with KPI columns
st.subheader('KPIs principais do sistema')
col1, col2, col3 = st.columns(3)

# KPI 1 total items
total_items = df.shape[0]
col1.metric(label='Número Total de Itens', value=total_items)

# KPI 2 unique brands
unique_brands = df['brand'].nunique()
col2.metric(label='Número de Marcas Únicas', value=unique_brands)

# KPI 3 average price
average_new_price = df['new_price'].mean()
col3.metric(label='Preço Médio (R$)', value=f'{average_new_price: .2f}')

##  Brands
# Most found brands until page 10
st.subheader('Marcas mais encontradas até a página 10')
col1, col2 = st.columns([4, 2])
top_10_pages_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)

# Brands average price
st.subheader('Preço Médio por Marca')
col1, col2 = st.columns([4, 2])
avg_price_by_brand = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(avg_price_by_brand)
col2.write(avg_price_by_brand)

# Brands satisfaction
st.subheader('Satisfação por Marca')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[ df['review_score'] > 0 ]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['review_score'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)