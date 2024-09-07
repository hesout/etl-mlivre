# import modules
import pandas as pd
import sqlite3
from datetime import datetime

# define dataframe w/ JSONL file path
df = pd.read_json('../data/data-mlivre.jsonl', lines=True, dtype=False)

# add column _source w/ fixed value
df['_source'] = "https://lista.mercadolivre.com.br/tenis-masculino"

# add column _date w/ date and time of colection
df['_date'] = datetime.now()

## Data Cleaning
# removing '.' for prices > 1000
df['old_price_real'] = df['old_price_real'].str.replace('[\.]', '', regex=True)
df['new_price_real'] = df['new_price_real'].str.replace('[\.]', '', regex=True)


# removing 'review_amount' parentesis
df['review_amount'] = df['review_amount'].str.replace('[\(\)]', '', regex=True)

# treat null values and numerical data
df['old_price_real']  = df['old_price_real'].fillna(0).astype(float)
df['old_price_cent']  = df['old_price_cent'].fillna(0).astype(float)
df['new_price_real']  = df['new_price_real'].fillna(0).astype(float)
df['new_price_cent']  = df['new_price_cent'].fillna(0).astype(float)
df['review_score']  = df['review_score'].fillna(0).astype(float)
df['review_amount'] = df['review_amount'].fillna(0).astype(int)

# Calculate total price values
df['old_price'] = df['old_price_real'] + df['old_price_cent']/100
df['new_price'] = df['new_price_real'] + df['new_price_cent']/100

# Remove old columns
df.drop(columns=['old_price_real', 'old_price_cent', 'new_price_real', 'new_price_cent'], inplace=True)

# Rearrange columns
df = df[['brand','name','old_price','new_price', 'review_score','review_amount','_source','_date']]


## SQLite Database
# Connect to db
conn = sqlite3.connect('../data/quotes.db')

# Save dataframe to db
df.to_sql('mercadolivre_itens', conn, if_exists='replace', index=False)

# Close db connection
conn.close()

