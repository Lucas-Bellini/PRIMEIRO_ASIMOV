import streamlit as st
import pandas as pd 
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# df_reviews
# aqui exibe o conteudo da tabela reviews

# df_reviews.index isso mostra os indices
# df_reviews["book name"] vai mostrar todos os nomes de livro
# df_top100_books[df_top100_books["book price"] < 10] aqui ele vai mostrar
# apenas os livros abaixo dos dez dolares

price_max = df_top100_books["book price"].max()
# esse metodo vai procurar pelo valor maximo dessa coluna
price_min = df_top100_books["book price"].min()

max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books

