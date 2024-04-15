import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


st.markdown('# Olá, seja bem vindo ao meu primeiro projeto de Data Science!')

st.markdown('## Estamos aprendendo o basico da ferramenta Streamlit')

df_idhm = pd.read_csv('IDHM_ESP.csv')

tabela_descritiva = df_idhm.describe().T

st.dataframe(df_idhm)
st.table(tabela_descritiva)

plot = sns.boxplot(data=df_idhm , y= df_idhm["idhm_renda"])

hist = sns.histplot(data=df_idhm , x= df_idhm["idhm_renda"])

st.pyplot(plot.get_figure())
st.pyplot(hist.get_figure())
