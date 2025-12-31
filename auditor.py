import pandas as pd
import datetime

# 1. Cargar datos
print("--- Iniciando Auditoría de Datos ---")
df = pd.read_csv('raw_data.csv')
total_inicial = len(df)

# 2. Definir reglas de QA (Business Logic)
def validar_email(email):
    return isinstance(email, str) and '@' in email and '.' in email

def validar_ventas(monto):
    try:
        val = float(monto)
        return val >= 0 # No puede haber ventas negativas
    except:
        return False # No es un número

# 3. Detectar errores
# Copia del dataframe para reporte de errores
df['error_reason'] = '' 

# Regla: Duplicados
duplicados = df.duplicated(subset=['id'], keep=False)
df.loc[duplicados, 'error_reason'] += 'ID Duplicado; '

# Regla: Email Inválido
mask_email = ~df['email'].apply(validar_email)
df.loc[mask_email, 'error_reason'] += 'Email Inválido; '

# Regla: Ventas Inválidas
mask_ventas = ~df['ventas'].apply(validar_ventas)
df.loc[mask_ventas, 'error_reason'] += 'Venta Inválida/Negativa; '

# Regla: Datos Faltantes (Nombre)
mask_null = df['nombre'].isna()
df.loc[mask_null, 'error_reason'] += 'Nombre Faltante; '

# 4. Separar Data Limpia vs Data Sucia
df_bad = df[df['error_reason'] != '']
df_clean = df[df['error_reason'] == ''].drop(columns=['error_reason'])

# 5. Exportar Reportes
timestamp = datetime.datetime.now().strftime("%Y%m%d")
df_clean.to_csv(f'clean_data_{timestamp}.csv', index=False)
df_bad.to_csv(f'qa_report_{timestamp}.csv', index=False)

# 6. Log final en consola
print(f"Procesamiento finalizado.")
print(f"Total registros: {total_inicial}")
print(f"Registros Aprobados: {len(df_clean)}")
print(f"Registros Rechazados: {len(df_bad)} (Ver qa_report.csv)")
