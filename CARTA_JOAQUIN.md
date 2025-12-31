# 📧 Carta para Joaquín

Hola Joaquín,

Gracias por considerar mi aplicación para la posición de **Data Analyst / QA / Developer**.

He creado este proyecto específicamente para demostrar mis habilidades en los tres frentes que buscan:

## 🎯 Lo que este proyecto demuestra

### 1️⃣ **Data Skills**
- ✅ Análisis y depuración de bases de datos (requisito clave del puesto)
- ✅ Limpieza de datos con Pandas
- ✅ Manejo de datasets con errores reales de negocio
- ✅ Generación de reportes automatizados

### 2️⃣ **QA Skills**
- ✅ Definición de reglas de validación de negocio
- ✅ Detección automática de errores
- ✅ Reportes detallados de QA con razones de rechazo
- ✅ Mindset de calidad: "prevenir antes que corregir"

### 3️⃣ **Dev Skills**
- ✅ Código Python limpio y modular
- ✅ Arquitectura escalable y extensible
- ✅ Queries SQL para validación en base de datos
- ✅ Documentación profesional
- ✅ Control de versiones con Git

## ⚡ Ejecución Rápida (2 minutos)

```bash
# 1. Clonar el repositorio
git clone [URL_DEL_REPO]
cd data-quality-auditor

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar el auditor
python auditor.py
```

**Resultado esperado:**
```
--- Iniciando Auditoría de Datos ---
Procesamiento finalizado.
Total registros: 7
Registros Aprobados: 1
Registros Rechazados: 6 (Ver qa_report.csv)
```

## 📊 Archivos Generados

Después de ejecutar, verás:
- `clean_data_YYYYMMDD.csv` - Solo 1 registro válido (Sofia Diaz)
- `qa_report_YYYYMMDD.csv` - 6 registros rechazados con razones detalladas

## 🔍 Errores Detectados Automáticamente

| ID | Nombre | Error Detectado |
|----|--------|-----------------|
| 101 | Juan Perez | ❌ ID Duplicado |
| 102 | Ana Gomez | ❌ Email sin @ |
| 103 | (vacío) | ❌ Nombre faltante |
| 104 | Maria Lopez | ❌ Venta negativa (-50) |
| 105 | Pedro Ruiz | ❌ Venta no numérica (ABC) |

## 💡 Por qué este proyecto es relevante

En mi investigación sobre la posición, noté que mencionan:
> *"Análisis y depuración de bases de datos"*

Este es exactamente el tipo de problema que resuelvo aquí:
- **Antes**: Datos sucios entran a producción → bugs, reportes incorrectos, pérdida de confianza
- **Después**: Barrera de QA automatizada → solo datos válidos en producción

## 🚀 Escalabilidad

Este script puede:
- Procesar millones de registros (Pandas es muy eficiente)
- Integrarse en pipelines ETL
- Adaptarse a cualquier regla de negocio nueva
- Conectarse directamente a bases de datos SQL

## 📈 Impacto en Negocio

**Caso real**: Si este auditor procesa 10,000 registros diarios y detecta un 5% de errores:
- **500 registros corregidos antes de llegar a producción**
- **Ahorro**: ~2 horas/día de debugging
- **ROI**: Script de 2 horas que ahorra 40+ horas/mes

## 🤝 Próximos Pasos

Estoy disponible para:
1. **Demo en vivo** - Puedo mostrar cómo agregar nuevas reglas de validación
2. **Discutir casos de uso** - Adaptar esto a problemas reales de su empresa
3. **Integración SQL** - Mostrar cómo conectar esto a PostgreSQL/MySQL/SQL Server

## 📞 Contacto

📧 **Email**: [tu-email]  
📱 **Teléfono**: [tu-teléfono]  
💼 **LinkedIn**: [tu-linkedin]  
🔗 **GitHub**: [tu-github]

---

**Tiempo de desarrollo**: 2.5 horas  
**Tecnologías**: Python, Pandas, SQL, Git  
**Líneas de código**: ~100 (calidad > cantidad)

Espero que este proyecto demuestre que tengo las habilidades técnicas y el mindset de calidad que buscan.

¡Quedo atento a tus comentarios!

Saludos,  
[Tu Nombre]

---

*P.D.: Este proyecto está en GitHub con commits limpios y documentación profesional. Listo para ser usado en producción con mínimas adaptaciones.*
