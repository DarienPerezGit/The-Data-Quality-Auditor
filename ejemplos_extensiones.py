"""
Ejemplos de Extensiones para el Data Quality Auditor
Este archivo muestra cómo agregar nuevas reglas de validación
"""

import pandas as pd
import re
from datetime import datetime

# ============================================
# EJEMPLO 1: Validación de Fechas
# ============================================

def validar_fecha(fecha_str):
    """
    Valida que la fecha esté en formato correcto y no sea futura
    """
    try:
        fecha = pd.to_datetime(fecha_str)
        hoy = datetime.now()
        return fecha <= hoy  # No puede ser fecha futura
    except:
        return False

# Uso en el auditor:
# mask_fecha = ~df['fecha'].apply(validar_fecha)
# df.loc[mask_fecha, 'error_reason'] += 'Fecha Inválida/Futura; '


# ============================================
# EJEMPLO 2: Validación de Teléfonos
# ============================================

def validar_telefono(telefono):
    """
    Valida formato de teléfono (ejemplo: +54 9 11 1234-5678)
    """
    if not isinstance(telefono, str):
        return False
    
    # Eliminar espacios y guiones para validar
    tel_limpio = telefono.replace(' ', '').replace('-', '')
    
    # Debe tener entre 10 y 15 dígitos
    return tel_limpio.isdigit() and 10 <= len(tel_limpio) <= 15


# ============================================
# EJEMPLO 3: Validación de DNI/CUIT
# ============================================

def validar_dni(dni):
    """
    Valida que el DNI sea un número de 7-8 dígitos
    """
    try:
        dni_int = int(dni)
        return 1000000 <= dni_int <= 99999999
    except:
        return False


# ============================================
# EJEMPLO 4: Validación de Rangos de Negocio
# ============================================

def validar_descuento(descuento):
    """
    Valida que el descuento esté entre 0% y 100%
    """
    try:
        desc = float(descuento)
        return 0 <= desc <= 100
    except:
        return False


# ============================================
# EJEMPLO 5: Validación de Códigos Postales
# ============================================

def validar_codigo_postal_argentina(cp):
    """
    Valida formato de código postal argentino (ej: C1234ABC o 1234)
    """
    if not isinstance(cp, str):
        return False
    
    # Formato nuevo: C1234ABC
    patron_nuevo = r'^[A-Z]\d{4}[A-Z]{3}$'
    # Formato viejo: 1234
    patron_viejo = r'^\d{4}$'
    
    return bool(re.match(patron_nuevo, cp) or re.match(patron_viejo, cp))


# ============================================
# EJEMPLO 6: Validación de Nombres Completos
# ============================================

def validar_nombre_completo(nombre):
    """
    Valida que el nombre tenga al menos nombre y apellido
    """
    if not isinstance(nombre, str):
        return False
    
    palabras = nombre.strip().split()
    return len(palabras) >= 2 and all(len(p) >= 2 for p in palabras)


# ============================================
# EJEMPLO 7: Validación de URLs
# ============================================

def validar_url(url):
    """
    Valida formato básico de URL
    """
    if not isinstance(url, str):
        return False
    
    patron = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(patron, url))


# ============================================
# EJEMPLO 8: Validación de Montos Monetarios
# ============================================

def validar_monto_razonable(monto, min_val=0, max_val=1000000):
    """
    Valida que el monto esté en un rango razonable de negocio
    """
    try:
        val = float(monto)
        return min_val <= val <= max_val
    except:
        return False


# ============================================
# EJEMPLO 9: Validación de Categorías
# ============================================

def validar_categoria(categoria, categorias_validas):
    """
    Valida que la categoría esté en la lista permitida
    """
    return categoria in categorias_validas

# Uso:
# categorias_permitidas = ['Electrónica', 'Ropa', 'Alimentos', 'Hogar']
# mask_cat = ~df['categoria'].apply(lambda x: validar_categoria(x, categorias_permitidas))
# df.loc[mask_cat, 'error_reason'] += 'Categoría No Válida; '


# ============================================
# EJEMPLO 10: Validación Cruzada (Cross-Field)
# ============================================

def validar_coherencia_fechas(df):
    """
    Valida que fecha_fin > fecha_inicio
    """
    try:
        inicio = pd.to_datetime(df['fecha_inicio'])
        fin = pd.to_datetime(df['fecha_fin'])
        return fin > inicio
    except:
        return False

# Uso:
# mask_fechas = ~df.apply(validar_coherencia_fechas, axis=1)
# df.loc[mask_fechas, 'error_reason'] += 'Fechas Incoherentes; '


# ============================================
# EJEMPLO 11: Detección de Outliers
# ============================================

def detectar_outlier_iqr(serie):
    """
    Detecta outliers usando el método IQR (Interquartile Range)
    """
    Q1 = serie.quantile(0.25)
    Q3 = serie.quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    return (serie < limite_inferior) | (serie > limite_superior)

# Uso:
# outliers = detectar_outlier_iqr(df['ventas'])
# df.loc[outliers, 'error_reason'] += 'Outlier Estadístico; '


# ============================================
# EJEMPLO 12: Validación de Formato de Texto
# ============================================

def validar_solo_letras(texto):
    """
    Valida que el texto solo contenga letras y espacios
    """
    if not isinstance(texto, str):
        return False
    
    return bool(re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', texto))


# ============================================
# EJEMPLO COMPLETO: Auditor Extendido
# ============================================

def auditor_extendido(df):
    """
    Ejemplo de cómo usar múltiples validaciones
    """
    df['error_reason'] = ''
    
    # Validación 1: Duplicados
    duplicados = df.duplicated(subset=['id'], keep=False)
    df.loc[duplicados, 'error_reason'] += 'ID Duplicado; '
    
    # Validación 2: Email
    mask_email = ~df['email'].apply(lambda x: isinstance(x, str) and '@' in x)
    df.loc[mask_email, 'error_reason'] += 'Email Inválido; '
    
    # Validación 3: Nombre completo
    mask_nombre = ~df['nombre'].apply(validar_nombre_completo)
    df.loc[mask_nombre, 'error_reason'] += 'Nombre Incompleto; '
    
    # Validación 4: Ventas en rango razonable
    mask_ventas = ~df['ventas'].apply(lambda x: validar_monto_razonable(x, 0, 100000))
    df.loc[mask_ventas, 'error_reason'] += 'Venta Fuera de Rango; '
    
    # Validación 5: Fecha válida
    mask_fecha = ~df['fecha'].apply(validar_fecha)
    df.loc[mask_fecha, 'error_reason'] += 'Fecha Inválida; '
    
    return df


# ============================================
# TIPS PARA PRODUCCIÓN
# ============================================

"""
1. LOGGING: Agregar logs detallados
   import logging
   logging.info(f"Procesados {len(df)} registros")

2. CONFIGURACIÓN: Usar archivo de config
   import yaml
   config = yaml.safe_load(open('config.yml'))

3. MÉTRICAS: Trackear performance
   import time
   start = time.time()
   # ... proceso ...
   print(f"Tiempo: {time.time() - start:.2f}s")

4. ALERTAS: Notificar si hay muchos errores
   if len(df_bad) / len(df) > 0.5:
       send_alert("Más del 50% de registros rechazados!")

5. VERSIONADO: Guardar versión del auditor
   VERSION = "1.0.0"
   df_clean['auditor_version'] = VERSION

6. TESTING: Crear tests unitarios
   import pytest
   def test_validar_email():
       assert validar_email("test@test.com") == True
       assert validar_email("invalid") == False
"""
