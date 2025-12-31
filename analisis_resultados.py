"""
Análisis Visual de Resultados - Data Quality Auditor
Este script genera estadísticas y visualizaciones de los resultados
"""

import pandas as pd
from datetime import datetime

def analizar_resultados():
    """
    Analiza los resultados del auditor y genera estadísticas
    """
    print("=" * 60)
    print("📊 ANÁLISIS DE RESULTADOS - DATA QUALITY AUDITOR")
    print("=" * 60)
    print()
    
    # Cargar datos originales
    df_raw = pd.read_csv('raw_data.csv')
    
    # Buscar el archivo de reporte más reciente
    import glob
    reportes = glob.glob('qa_report_*.csv')
    if not reportes:
        print("❌ No se encontraron reportes. Ejecuta primero: python auditor.py")
        return
    
    reporte_reciente = max(reportes)
    df_bad = pd.read_csv(reporte_reciente)
    
    # Buscar datos limpios
    limpios = glob.glob('clean_data_*.csv')
    if limpios:
        limpio_reciente = max(limpios)
        df_clean = pd.read_csv(limpio_reciente)
    else:
        df_clean = pd.DataFrame()
    
    # Estadísticas generales
    total = len(df_raw)
    rechazados = len(df_bad)
    aprobados = len(df_clean)
    tasa_rechazo = (rechazados / total) * 100
    
    print(f"📈 MÉTRICAS GENERALES")
    print(f"{'─' * 60}")
    print(f"Total de registros procesados:  {total:>3}")
    print(f"Registros aprobados:             {aprobados:>3} ({100-tasa_rechazo:.1f}%)")
    print(f"Registros rechazados:            {rechazados:>3} ({tasa_rechazo:.1f}%)")
    print()
    
    # Análisis de errores
    print(f"🔍 ANÁLISIS DE ERRORES DETECTADOS")
    print(f"{'─' * 60}")
    
    # Contar cada tipo de error
    errores = {
        'ID Duplicado': 0,
        'Email Inválido': 0,
        'Venta Inválida/Negativa': 0,
        'Nombre Faltante': 0
    }
    
    for _, row in df_bad.iterrows():
        error_reason = str(row['error_reason'])
        for tipo_error in errores.keys():
            if tipo_error in error_reason:
                errores[tipo_error] += 1
    
    # Mostrar distribución de errores
    for tipo, cantidad in sorted(errores.items(), key=lambda x: x[1], reverse=True):
        if cantidad > 0:
            porcentaje = (cantidad / rechazados) * 100
            barra = '█' * int(porcentaje / 5)
            print(f"{tipo:30} {cantidad:>2} {barra} {porcentaje:.1f}%")
    
    print()
    
    # Detalles de registros rechazados
    print(f"📋 DETALLE DE REGISTROS RECHAZADOS")
    print(f"{'─' * 60}")
    print(f"{'ID':<5} {'Nombre':<15} {'Error':<40}")
    print(f"{'─' * 60}")
    
    for _, row in df_bad.iterrows():
        id_val = str(row['id'])
        nombre = str(row['nombre'])[:15] if pd.notna(row['nombre']) else '(vacío)'
        error = str(row['error_reason'])[:40]
        print(f"{id_val:<5} {nombre:<15} {error:<40}")
    
    print()
    
    # Registros aprobados
    if not df_clean.empty:
        print(f"✅ REGISTROS APROBADOS")
        print(f"{'─' * 60}")
        print(f"{'ID':<5} {'Nombre':<20} {'Email':<25} {'Ventas':<10}")
        print(f"{'─' * 60}")
        
        for _, row in df_clean.iterrows():
            print(f"{row['id']:<5} {row['nombre']:<20} {row['email']:<25} ${row['ventas']:<10}")
    
    print()
    
    # Impacto en negocio
    print(f"💰 IMPACTO EN NEGOCIO")
    print(f"{'─' * 60}")
    
    # Calcular ventas totales si todos los datos fueran válidos
    ventas_totales_raw = 0
    for _, row in df_raw.iterrows():
        try:
            ventas_totales_raw += float(row['ventas'])
        except:
            pass
    
    # Calcular ventas reales (solo datos válidos)
    ventas_validas = df_clean['ventas'].sum() if not df_clean.empty else 0
    
    print(f"Ventas reportadas (datos sucios):    ${ventas_totales_raw:,.2f}")
    print(f"Ventas reales (datos limpios):       ${ventas_validas:,.2f}")
    print(f"Diferencia detectada:                ${abs(ventas_totales_raw - ventas_validas):,.2f}")
    print()
    
    if ventas_totales_raw != 0:
        error_porcentual = abs(ventas_totales_raw - ventas_validas) / abs(ventas_totales_raw) * 100
        print(f"⚠️  Error en reportes sin auditoría: {error_porcentual:.1f}%")
    
    print()
    
    # ROI del auditor
    print(f"📊 ROI DEL AUDITOR")
    print(f"{'─' * 60}")
    print(f"Tiempo de desarrollo:                2.5 horas")
    print(f"Tiempo de ejecución:                 < 1 segundo")
    print(f"Errores detectados automáticamente:  {rechazados}")
    print(f"Tiempo ahorrado en debugging:        ~{rechazados * 20} minutos")
    print()
    
    # Proyección a escala
    print(f"🚀 PROYECCIÓN A ESCALA")
    print(f"{'─' * 60}")
    registros_diarios = 10000
    errores_proyectados = int(registros_diarios * (tasa_rechazo / 100))
    tiempo_ahorrado_dia = errores_proyectados * 20 / 60  # en horas
    tiempo_ahorrado_mes = tiempo_ahorrado_dia * 22  # días laborables
    
    print(f"Si procesamos {registros_diarios:,} registros/día:")
    print(f"  → Errores detectados/día:          {errores_proyectados:,}")
    print(f"  → Tiempo ahorrado/día:             {tiempo_ahorrado_dia:.1f} horas")
    print(f"  → Tiempo ahorrado/mes:             {tiempo_ahorrado_mes:.1f} horas")
    print(f"  → Equivalente a:                   {tiempo_ahorrado_mes/8:.1f} días laborables")
    
    print()
    print("=" * 60)
    print(f"✅ Análisis completado - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)


if __name__ == "__main__":
    analizar_resultados()
