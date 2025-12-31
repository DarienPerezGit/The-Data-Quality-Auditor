# 🛡️ Data Quality & Automated ETL Auditor

**Herramienta de automatización de limpieza de datos que actúa como barrera de QA antes de la ingestión de datos.**

## 📋 Descripción

Este proyecto resuelve un problema común en operaciones de datos: **la recepción de archivos con errores humanos**. Diseñé un script en Python que actúa como barrera de QA (Quality Assurance), auditando automáticamente datasets antes de su ingestión en sistemas productivos.

## ✨ Key Features

### 🔍 **Automated Validation**
- Detecta emails rotos o mal formateados
- Identifica registros duplicados por ID
- Valida tipos de datos incorrectos (ej: texto en campos numéricos)
- Detecta valores negativos donde no deberían existir
- Identifica campos obligatorios faltantes

### 📊 **QA Reporting**
- Genera un archivo separado (`qa_report_YYYYMMDD.csv`) con todos los registros rechazados
- Incluye columna `error_reason` que detalla exactamente qué regla de negocio falló
- Permite al equipo operativo corregir errores de forma eficiente

### 🚀 **Scalable Logic**
- Utiliza **Pandas** para manejar volúmenes de datos que Excel no soportaría
- Arquitectura modular que permite agregar nuevas reglas de validación fácilmente
- Procesamiento en memoria optimizado para datasets grandes

### 💾 **SQL Integration**
- Incluye queries SQL equivalentes para validación en base de datos
- Demuestra conocimiento de análisis y depuración tanto en archivos como en RDBMS

## 🛠️ Tecnologías Utilizadas

- **Python 3.x** - Lenguaje principal
- **Pandas** - Procesamiento y análisis de datos
- **SQL** - Validación en base de datos
- **CSV** - Formato de entrada/salida

## 📦 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/data-quality-auditor.git
cd data-quality-auditor

# Instalar dependencias
pip install pandas
```

## 🚀 Uso

### Ejecución básica (Consola)

```bash
python auditor.py
```

### 🌟 Ejecución visual (Web Interface)

Para una experiencia interactiva (ideal para demos):

```bash
streamlit run app.py
```

Esto abrirá una interfaz web donde puedes subir tus propios CSVs y ver los gráficos de calidad en tiempo real.

### Salida esperada

```
--- Iniciando Auditoría de Datos ---
Procesamiento finalizado.
Total registros: 7
Registros Aprobados: 2
Registros Rechazados: 5 (Ver qa_report.csv)
```

### Archivos generados

- `clean_data_YYYYMMDD.csv` - Datos validados y listos para ingestión
- `qa_report_YYYYMMDD.csv` - Registros rechazados con razones detalladas

## 📁 Estructura del Proyecto

```
data-quality-auditor/
├── raw_data.csv          # Dataset de ejemplo con errores intencionales
├── auditor.py            # Script principal de auditoría
├── queries.sql           # Validaciones SQL equivalentes
├── README.md             # Documentación
└── requirements.txt      # Dependencias Python
```

## 🧪 Reglas de Validación Implementadas

| Regla | Descripción | Acción |
|-------|-------------|--------|
| **Duplicados** | IDs repetidos en el dataset | Marca como error |
| **Email Inválido** | Falta @ o dominio | Marca como error |
| **Ventas Negativas** | Valores < 0 | Marca como error |
| **Tipo Incorrecto** | Texto en campo numérico | Marca como error |
| **Datos Faltantes** | Nombre vacío/null | Marca como error |

## 🎯 Casos de Uso

### Caso 1: Importación de datos de CRM
Antes de importar datos de clientes desde un Excel manual, el auditor detecta:
- Emails mal escritos que causarían rebotes
- Duplicados que inflarían métricas
- Datos faltantes que romperían reportes

### Caso 2: Validación de datos de ventas
Antes de procesar transacciones, el auditor identifica:
- Montos negativos por errores de captura
- Formatos incorrectos en campos numéricos
- Registros incompletos

### Caso 3: ETL Pipeline
Como primer paso en un pipeline ETL, asegura que solo datos válidos lleguen a la base de datos productiva.

## 🔄 Extensibilidad

Agregar nuevas reglas es simple:

```python
# Ejemplo: Validar que el nombre tenga al menos 2 palabras
def validar_nombre_completo(nombre):
    return isinstance(nombre, str) and len(nombre.split()) >= 2

mask_nombre = ~df['nombre'].apply(validar_nombre_completo)
df.loc[mask_nombre, 'error_reason'] += 'Nombre Incompleto; '
```

## 📈 Métricas de Calidad

En el dataset de ejemplo:
- **Tasa de rechazo**: 71.4% (5 de 7 registros)
- **Errores más comunes**: 
  - IDs duplicados (2 registros)
  - Emails inválidos (1 registro)
  - Ventas inválidas (2 registros)
  - Nombres faltantes (1 registro)

## 🎓 Skills Demostradas

✅ **Data Analysis** - Pandas, limpieza de datos, ETL  
✅ **Quality Assurance** - Validación de reglas de negocio, testing de datos  
✅ **Development** - Python, arquitectura modular, código limpio  
✅ **SQL** - Queries de validación, análisis en base de datos  
✅ **Problem Solving** - Automatización de procesos manuales  

## 🤝 Contribuciones

Este proyecto está abierto a mejoras. Algunas ideas:
- [ ] Agregar validación de fechas
- [ ] Implementar logging más detallado
- [ ] Crear dashboard de métricas de calidad
- [ ] Integración con bases de datos SQL directamente
- [ ] API REST para validación en tiempo real

## 📝 Licencia

MIT License - Siéntete libre de usar este código para tus propios proyectos.

## 👤 Autor

**Tu Nombre**  
*Data Analyst | QA Specialist | Developer*

📧 Email: tu-email@ejemplo.com  
🔗 LinkedIn: [tu-perfil](https://linkedin.com/in/tu-perfil)  
💼 GitHub: [@tu-usuario](https://github.com/tu-usuario)

---

**¿Por qué este proyecto?**

En mi experiencia, los errores de datos son la causa #1 de problemas en producción. Este auditor automatiza la detección temprana, ahorrando horas de debugging y garantizando la integridad de los datos desde el origen.

*"La calidad de tus decisiones nunca puede exceder la calidad de tus datos."* 📊
