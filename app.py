#Estudiantes: Kevin Arrieta, Juan Niño, Anderson Ortega, , Ricardo Henriquez
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Cargar datos
df = pd.read_csv("university_student_data_clean.csv")

# Título del Dashboard
st.title("🎓 University Student Analytics Dashboard")

# Filtros laterales
st.sidebar.header("Filtros")
selected_year = st.sidebar.selectbox("Selecciona un año:", sorted(df['year'].unique()))
selected_term = st.sidebar.selectbox("Selecciona un periodo:", sorted(df['term'].unique()))

# Filtrar datos
filtered = df[(df['year'] == selected_year) & (df['term'] == selected_term)]

# Métricas principales
st.subheader(f"Resumen {selected_year} - {selected_term}")
col1, col2, col3 = st.columns(3)
col1.metric("Retención (%)", round(filtered['retention_rate'].mean(), 2))
col2.metric("Satisfacción (%)", round(filtered['satisfaction'].mean(), 2))
col3.metric("Inscritos", int(filtered['enrolled'].sum()))

# Gráfica 1: Retención a lo largo de los años
st.subheader("Tendencia de la Retención")
fig1, ax1 = plt.subplots()
sns.lineplot(data=df, x='year', y='retention_rate', marker='o', ax=ax1)
st.pyplot(fig1)

# Gráfica 2: Satisfacción por año
st.subheader("Satisfacción promedio por año")
fig2, ax2 = plt.subplots()
sns.barplot(data=df, x='year', y='satisfaction', ax=ax2, color='orange')
st.pyplot(fig2)

# Gráfica 3: Comparación entre semestres
st.subheader("Comparación de Satisfacción entre Periodos")
fig3, ax3 = plt.subplots()
sns.boxplot(data=df, x='term', y='satisfaction', palette='Set2', ax=ax3)
st.pyplot(fig3)

# Mostrar datos filtrados
st.subheader("Datos filtrados")
st.dataframe(filtered)
