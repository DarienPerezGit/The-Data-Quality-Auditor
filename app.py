import streamlit as st
import pandas as pd
import plotly.express as px
import io
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Data Quality Auditor",
    page_icon="🛡️",
    layout="wide"
)

# Título y Descripción
st.title("🛡️ Data Quality Auditor")
st.markdown("""
Esta herramienta automatiza la **auditoría y limpieza de datos**.  
Sube un archivo CSV sucio y obtén instantáneamente un reporte de calidad y los datos limpios.
""")

# --- LÓGICA DE NEGOCIO (El mismo motor que auditor.py) ---
def validar_email(email):
    return isinstance(email, str) and '@' in email and '.' in email

def validar_ventas(monto):
    try:
        val = float(monto)
        return val >= 0 
    except:
        return False

def procesar_datos(df):
    df_audit = df.copy()
    df_audit['error_reason'] = ''

    # 1. Duplicados
    duplicados = df_audit.duplicated(subset=['id'], keep=False)
    df_audit.loc[duplicados, 'error_reason'] += 'ID Duplicado; '

    # 2. Email
    mask_email = ~df_audit['email'].apply(validar_email)
    df_audit.loc[mask_email, 'error_reason'] += 'Email Inválido; '

    # 3. Ventas
    mask_ventas = ~df_audit['ventas'].apply(validar_ventas)
    df_audit.loc[mask_ventas, 'error_reason'] += 'Venta Inválida/Negativa; '

    # 4. Datos faltantes
    mask_null = df_audit['nombre'].isna()
    df_audit.loc[mask_null, 'error_reason'] += 'Nombre Faltante; '

    # Separar
    df_bad = df_audit[df_audit['error_reason'] != '']
    df_clean = df_audit[df_audit['error_reason'] == ''].drop(columns=['error_reason'])
    
    return df_clean, df_bad

# --- INTERFAZ ---

# Sidebar para cargas
with st.sidebar:
    st.header("📂 Carga de Datos")
    uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])
    
    st.info("¿No tienes archivo? Se usará el dataset de prueba.")

# Cargar datos (subidos o default)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("Archivo cargado exitosamente")
else:
    try:
        df = pd.read_csv('raw_data.csv')
    except:
        st.error("No se encontró raw_data.csv. Sube un archivo.")
        st.stop()

# Mostrar datos originales (Preview)
with st.expander("👀 Ver Datos Originales (Raw Data)", expanded=False):
    st.dataframe(df)

# Botón de acción
if st.button("🚀 Ejecutar Auditoría de Calidad", type="primary"):
    
    with st.spinner('Auditando reglas de negocio...'):
        df_clean, df_bad = procesar_datos(df)
        
        # --- MÉTRICAS ---
        col1, col2, col3, col4 = st.columns(4)
        total = len(df)
        rejections = len(df_bad)
        acceptance_rate = (len(df_clean) / total) * 100
        
        col1.metric("Total Registros", total)
        col2.metric("Registros Aprobados", len(df_clean), delta_color="normal")
        col3.metric("Registros Rechazados", rejections, delta_color="inverse")
        col4.metric("Tasa de Calidad", f"{acceptance_rate:.1f}%")
        
        st.divider()
        
        # --- VISUALIZACIÓN ---
        col_viz1, col_viz2 = st.columns(2)
        
        with col_viz1:
            st.subheader("📊 Distribución de Errores")
            if not df_bad.empty:
                # Procesar errores para el gráfico
                all_errors = []
                for err in df_bad['error_reason']:
                    all_errors.extend([e.strip() for e in err.split(';') if e.strip()])
                
                error_counts = pd.Series(all_errors).value_counts().reset_index()
                error_counts.columns = ['Tipo de Error', 'Cantidad']
                
                fig = px.bar(error_counts, x='Cantidad', y='Tipo de Error', orientation='h', 
                             color='Cantidad', color_continuous_scale='Reds')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.success("¡Datos perfectos! No se encontraron errores.")

        with col_viz2:
            st.subheader("📉 Impacto en Datos")
            fig_pie = px.pie(names=['Aprobados', 'Rechazados'], 
                             values=[len(df_clean), len(df_bad)],
                             color=['Aprobados', 'Rechazados'],
                             color_discrete_map={'Aprobados':'#00CC96', 'Rechazados':'#EF553B'})
            st.plotly_chart(fig_pie, use_container_width=True)

        # --- DETALLE DE ERRORES ---
        if not df_bad.empty:
            st.subheader("🔍 Detalle de Rechazos (QA Report)")
            st.dataframe(df_bad.style.applymap(lambda x: 'background-color: #ffcccc', subset=['error_reason']))
        
        # --- DESCARGAS ---
        st.subheader("💾 Descargar Resultados")
        c1, c2 = st.columns(2)
        
        csv_clean = df_clean.to_csv(index=False).encode('utf-8')
        csv_report = df_bad.to_csv(index=False).encode('utf-8')
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        
        c1.download_button(
            label="✅ Descargar Datos Limpios",
            data=csv_clean,
            file_name=f'clean_data_{timestamp}.csv',
            mime='text/csv',
        )
        
        c2.download_button(
            label="❌ Descargar Reporte de QA",
            data=csv_report,
            file_name=f'qa_report_{timestamp}.csv',
            mime='text/csv',
        )
