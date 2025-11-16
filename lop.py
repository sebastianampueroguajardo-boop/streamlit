import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("database_titanic.csv")

st.write("""
# Mi primera aplicación interactiva
## Gráficos usando la base de datos del Titanic
""")


with st.sidebar:
    st.write("# Opciones")
    div = st.slider("Número de bins (histograma):", 1, 20, 5)
    st.write("Bins seleccionados:", div)


fig, ax = plt.subplots(1, 2, figsize=(10, 3))


ax[0].hist(df["Age"].dropna(), bins=div)
ax[0].set_xlabel("Edad")
ax[0].set_ylabel("Frecuencia")
ax[0].set_title("Histograma de edades")


df_male = df[df["Sex"] == "male"]
cant_male = len(df_male)
df_female = df[df["Sex"] == "female"]
cant_female = len(df_female)


ax[1].bar(["masculino","femenino"], [cant_male, cant_female], color = "red")
ax[1].set_xlabel("Sexo")
ax[1].set_ylabel("Cantidad")
ax[1].set_title("Distribucion de hombres y mujeres")

st.pyplot(fig)

st.write("## Número de sobrevivientes agrupados por sexo")

survivors_by_sex = df.groupby("Sex")["Survived"].sum()

fig2, ax2 = plt.subplots(figsize=(5, 3))
ax2.bar(["Femenino", "Masculino"], [survivors_by_sex["female"], survivors_by_sex["male"]])
ax2.set_xlabel("Sexo")
ax2.set_ylabel("Sobrevivientes")
ax2.set_title("Sobrevivientes por sexo")

st.pyplot(fig2)

st.write("## Muestra de datos cargados")
st.table(df.head())
    