# PLANTILLAS EXCEL SISTEMA FINANCIERO
## AlvaroVelasco.Net SRL - Implementación Completa

**Fecha creación:** 07 de Noviembre 2025
**Versión:** 1.0
**Autor:** Claude Code + Álvaro Velasco

---

## 📁 CONTENIDO DE ESTA CARPETA

Este directorio contiene **TODOS** los archivos necesarios para implementar el Sistema Financiero Excel completo para AlvaroVelasco.Net SRL en **3-4 horas**.

### ✅ Archivos CSV - Datos Pre-cargados (12 archivos)

Plantillas CSV con datos reales del 07/11/2025, listas para importar a Excel:

| Archivo | Pestaña Excel | Descripción | Datos |
|---------|---------------|-------------|-------|
| `EMPRESA_01_Dashboard.csv` | Dashboard | Panel ejecutivo con resumen | Métricas principales |
| `EMPRESA_02_Efectivo.csv` | Efectivo | Control diario efectivo | 4 cuentas bancarias |
| `EMPRESA_03_Ahorros.csv` | Ahorros | Cuentas ahorro BNCR | 4 cuentas, $8,054 |
| `EMPRESA_04_CuentasPorCobrar.csv` | A/R | Cuentas por cobrar | 26 clientes, $10,866 |
| `EMPRESA_05_CuentasPorPagar.csv` | A/P | Cuentas por pagar | 9 facturas, $6,104 |
| `EMPRESA_06_TarjetasCredito.csv` | TC | Tarjetas crédito | 5 tarjetas, $16,383 |
| `EMPRESA_07_GastosFijos.csv` | GastosFijos | Gastos fijos mensuales | 7 gastos, $2,809/mes |
| `EMPRESA_08_Presupuesto.csv` | Presupuesto | Presupuesto mensual | Fijos + Variables |
| `EMPRESA_10_KPIs.csv` | KPIs | Indicadores financieros | 15 KPIs |
| `EMPRESA_11_Hacienda.csv` | Hacienda | Impuestos pendientes | IVA + ISR $9,800 |
| `EMPRESA_12_Nissan.csv` | Nissan | Préstamo vehículo | $19,198 + 3 escenarios |
| `EMPRESA_13_AhorroVivienda.csv` | Vivienda | Plan ahorro 24 meses | Meta $45,000 |

### 📖 Archivos Documentación (3 archivos)

| Archivo | Descripción | Tamaño | Uso |
|---------|-------------|--------|-----|
| `FORMULAS_EXCEL_COMPLETAS.md` | **TODAS** las fórmulas Excel listas para copy-paste | ~800 líneas | Referencia durante implementación |
| `GUIA_IMPLEMENTACION_PASO_A_PASO.md` | Guía completa implementación 9 fases | ~1,200 líneas | Seguir paso a paso |
| `CODIGO_DAX_POWERBI.txt` | 50+ medidas DAX para Power BI | ~650 líneas | Opcional - Dashboard avanzado |

### 📄 Este archivo
| Archivo | Descripción |
|---------|-------------|
| `README.md` | Este archivo que estás leyendo |

---

## 🚀 INICIO RÁPIDO (30 segundos)

### ¿Nuevo aquí? Empieza por:

1. **Lee primero:** `GUIA_IMPLEMENTACION_PASO_A_PASO.md` (abre en editor texto)
2. **Importa CSVs:** Los 12 archivos CSV a Excel (sección FASE 2 de la guía)
3. **Copia fórmulas:** De `FORMULAS_EXCEL_COMPLETAS.md` (sección FASE 3)
4. **¡Listo!** En 3-4 horas tendrás sistema completo funcionando

---

## 📋 PREREQUISITOS

### Software necesario:
- ✅ **Microsoft Excel** (Office 365 recomendado, funciona con 2016+)
- ✅ **Windows 10/11** o **macOS** (con Excel instalado)
- ⚠️ **NO funciona con:** Google Sheets, LibreOffice, Numbers (fórmulas incompatibles)

### Conocimientos:
- ✅ Básico Excel (abrir, copiar, pegar, fórmulas simples)
- ✅ Importar CSV a Excel
- ⚠️ **NO requiere:** Programación, macros, VBA, ni conocimiento avanzado

### Tiempo disponible:
- ✅ **Implementación completa:** 3-4 horas
- ✅ **Uso diario:** 5-10 minutos
- ✅ **Revisión semanal:** 15 minutos
- ✅ **Cierre mensual:** 30 minutos

---

## 📚 ORDEN DE IMPLEMENTACIÓN

### Sigue este orden para mejores resultados:

#### PASO 1: Preparación (15 min)
1. Leer `GUIA_IMPLEMENTACION_PASO_A_PASO.md` completa
2. Crear carpeta `C:\Finanzas\`
3. Tener estos archivos accesibles

#### PASO 2: Importar datos (45 min)
1. Crear archivo Excel nuevo: `AlvaroVelascoNet_EMPRESA.xlsx`
2. Crear 15 pestañas (Dashboard, Efectivo, Ahorros, etc.)
3. Importar cada CSV a su pestaña correspondiente
4. Ajustar anchos de columna

#### PASO 3: Aplicar fórmulas (60 min)
1. Abrir `FORMULAS_EXCEL_COMPLETAS.md` en otra ventana
2. Copiar fórmulas pestaña por pestaña
3. Verificar que calculen correctamente
4. Guardar frecuentemente

#### PASO 4: Formato condicional (30 min)
1. Aplicar colores a alertas (rojo = crítico, amarillo = alerta)
2. Resaltar prioridades
3. Facilitar lectura visual

#### PASO 5: Validación datos (20 min)
1. Crear listas desplegables (categorías, estados, prioridades)
2. Prevenir errores de entrada
3. Estandarizar datos

#### PASO 6: Dashboard (40 min)
1. Vincular todas las métricas principales
2. Crear gráficos (efectivo trending, gastos)
3. Configurar alertas automáticas

#### PASO 7: Verificación (30 min)
1. Probar cada pestaña
2. Verificar cálculos
3. Agregar movimiento de prueba

#### PASO 8: Backup y protección (15 min)
1. Guardar en OneDrive
2. Crear backup local
3. Proteger fórmulas
4. Crear acceso directo escritorio

#### PASO 9: Power BI - OPCIONAL (2 horas)
1. Instalar Power BI Desktop (gratis)
2. Conectar a Excel
3. Copiar medidas DAX de `CODIGO_DAX_POWERBI.txt`
4. Crear 4 dashboards interactivos
5. Publicar a Power BI Service
6. Configurar refresh automático

---

## 🎯 CARACTERÍSTICAS DEL SISTEMA

### Lo que obtendrás al implementar:

#### ✅ Control Efectivo
- Registro diario entradas/salidas
- Balance running automático
- Alertas cuando <$1000
- Proyección 90 días

#### ✅ Gestión Cuentas por Cobrar
- 26 clientes con prioridades
- Total: $10,866.42
- Alertas clientes críticos
- Plan cobranza semanal

#### ✅ Gestión Cuentas por Pagar
- 9 proveedores
- Total: $6,103.66
- Alertas vencimientos
- Priorización pagos

#### ✅ Control Tarjetas Crédito
- 5 tarjetas ($16,383 total)
- Plan sanitización 12 meses
- Ahorro proyectado: $18,088 intereses
- Método avalanche (tasa más alta primero)

#### ✅ Presupuesto Inteligente
- Gastos fijos rígidos: $2,809/mes
- Gastos variables flexibles: $2,750/mes
- Alertas excesos
- Comparativa real vs presupuestado

#### ✅ KPIs Profesionales
- 15 indicadores financieros
- Razón Corriente: 0.451
- Días Cobertura: 45.9 días
- DSO, Working Capital, etc.

#### ✅ Plan Ahorro Vivienda
- Meta: $45,000 en 24 meses
- 3 fases (Sanitización → Transición → Aceleración)
- Proyección mes a mes
- % progreso automático

#### ✅ Dashboard Ejecutivo
- Todas las métricas en una vista
- Alertas críticas destacadas
- Gráficos visuales
- Top 5 clientes/proveedores

---

## 📊 DATOS INCLUIDOS

### Estado financiero al 07/11/2025:

| Concepto | Monto USD | Cuentas/Items |
|----------|-----------|---------------|
| **RECURSOS** |||
| Efectivo | $4,302.10 | 4 cuentas |
| Ahorros | $8,053.97 | 4 BNCR |
| A/R | $10,866.42 | 26 clientes |
| **Total Recursos** | **$23,222.49** ||
||||
| **DEUDA** |||
| Tarjetas Crédito | $16,382.69 | 5 TC |
| A/P | $6,103.66 | 9 facturas |
| Hacienda (IVA+ISR) | $9,799.63 | Impuestos |
| Nissan Frontier | $19,197.69 | Préstamo |
| **Total Deuda** | **$51,483.67** ||
||||
| **DÉFICIT** | **-$28,261.18** | **Insolvencia técnica** |
| **Razón Corriente** | **0.451** | Crítico (<1.0) |
| **Días Cobertura** | **45.9 días** | Solo 1.5 meses |

### Top 5 Clientes (41% del total A/R):
1. VWR International: $2,800.00 (25.8%)
2. Grupo Acción: $1,689.04 (15.5%)
3. Alfipac: $761.05 (7.0%)
4. 3-102-887892 SRL: $691.56 (6.4%)
5. Waipio SA: $687.27 (6.3%)

### Gastos Fijos Mensuales: $2,809.38
- Nómina Álvaro: $1,000 (35.6%)
- Vehículo (Nissan + parqueos): $859 (30.6%)
- Servicios (ICE): $380 (13.5%)
- Impuestos (CCSS): $353 (12.6%)
- Software: $217 (7.7%)

---

## 🎨 ESTRUCTURA VISUAL

### Pestañas del archivo Excel (15 total):

```
📊 AlvaroVelascoNet_EMPRESA.xlsx
│
├─ 01_Dashboard         [Azul]    Panel ejecutivo resumen
├─ 02_Efectivo          [Verde]   Control diario cash
├─ 03_Ahorros           [Verde]   4 cuentas BNCR
├─ 04_A/R               [Verde]   26 clientes por cobrar
├─ 05_A/P               [Rojo]    9 facturas por pagar
├─ 06_TC                [Rojo]    5 tarjetas crédito
├─ 07_GastosFijos       [Naranja] 7 gastos recurrentes
├─ 08_Presupuesto       [Naranja] Fijos + Variables
├─ 09_Proyeccion90      [Morado]  3 escenarios flujo caja
├─ 10_KPIs              [Morado]  15 indicadores
├─ 11_Hacienda          [Gris]    IVA + ISR pendiente
├─ 12_Nissan            [Gris]    Préstamo vehículo
├─ 13_Vivienda          [Gris]    Plan ahorro $45k
├─ 14_Analisis          [Gris]    Gráficos y tendencias
└─ 15_Config            [Gris]    Parámetros e instrucciones
```

---

## 🔧 PERSONALIZACIÓN

### Puedes adaptar el sistema a tus necesidades:

#### Agregar más filas:
- A/R: Agregar más clientes (copiar fila, pegar, ajustar referencias)
- A/P: Agregar más proveedores
- Efectivo: Infinitas filas para movimientos

#### Cambiar parámetros:
- Ir a pestaña **Config**
- Modificar:
  - TC_USDCRC (tipo cambio)
  - Tasas interés TC
  - Umbrales alertas

#### Agregar categorías:
- Presupuesto: Nuevas líneas de gastos
- Efectivo: Nuevas categorías (editar lista validación)

#### Crear gráficos adicionales:
- Pestaña **Analisis** tiene espacio
- Insertar → Gráficos → Seleccionar datos

---

## 💾 BACKUPS Y SEGURIDAD

### Sistema incluye 3 niveles de protección:

#### 1. OneDrive (Automático - Recomendado)
```
- Guardar archivo en OneDrive
- Sincronización automática cada cambio
- Versionado: hasta 30 versiones anteriores
- Acceso desde cualquier dispositivo
- Recuperación si borras accidentalmente
```

#### 2. Backup local semanal
```
Ubicación: C:\Finanzas\Backups\
Formato: AlvaroVelascoNet_EMPRESA_YYYY-MM-DD.xlsx
Frecuencia: Cada lunes antes de iniciar trabajo
```

#### 3. Protección fórmulas
```
- Celdas con fórmulas: BLOQUEADAS
- Celdas con datos: DESBLOQUEADAS
- Previene borrado accidental fórmulas
- Sin contraseña (fácil desproteger si necesario)
```

---

## 📱 ACCESO MOBILE (OPCIONAL)

### Con Power BI puedes ver en celular:

1. **Instalar app Power BI** (iOS/Android - gratis)
2. **Publicar dashboard** desde Power BI Desktop
3. **Ver métricas en tiempo real** desde cualquier lugar
4. **Recibir alertas** cuando KPI crítico

**Ejemplo alertas push:**
- 🔴 "Efectivo bajo $1000"
- 🟠 "4 TC vencidas - acción requerida"
- 🟠 "A/P Eurocomp vence en 3 días"

---

## ❓ PREGUNTAS FRECUENTES (FAQ)

### ¿Puedo usar Google Sheets?
**NO.** Las fórmulas están optimizadas para Excel Office 365. Google Sheets tiene sintaxis diferente (ej: `SUMAR.SI` en Excel vs `SUMIF` en Sheets). Necesitas Excel.

### ¿Funciona en Mac?
**SÍ.** Excel para Mac (Office 365) es compatible. Todas las fórmulas funcionan igual.

### ¿Necesito Power BI?
**NO.** Power BI es OPCIONAL para dashboards avanzados. El sistema Excel es 100% funcional sin Power BI.

### ¿Qué pasa si cometo un error?
1. **Ctrl+Z** deshace último cambio
2. **OneDrive** tiene versiones anteriores (clic derecho → Historial de versiones)
3. **Backup local** semanal como último recurso

### ¿Puedo agregar más clientes A/R?
**SÍ.** Copia última fila con datos, pega abajo, edita info. Las fórmulas se ajustan automáticamente.

### ¿Cómo actualizo el tipo de cambio USD/CRC?
Ir a pestaña **Config** → Celda B2 → Cambiar 507 a nuevo valor. Todas las conversiones se actualizan automático.

### ¿Funciona sin internet?
**SÍ.** Excel funciona offline. Solo necesitas internet para:
- Sincronizar OneDrive
- Actualizar Power BI
- Verificar saldos bancarios online

### ¿Cuánto tiempo toma el uso diario?
**5-10 minutos.** Registras movimientos del día, verificas dashboard, guardas. Listo.

### ¿Puedo compartir con mi contador?
**SÍ.** Guarda en OneDrive, clic derecho → Compartir → Enviar link. O exporta pestaña específica a PDF.

---

## 🆘 SOPORTE Y AYUDA

### Si tienes problemas durante implementación:

#### 1. Revisar documentación
- `GUIA_IMPLEMENTACION_PASO_A_PASO.md` tiene troubleshooting al final
- `FORMULAS_EXCEL_COMPLETAS.md` tiene todas las fórmulas corregidas

#### 2. Verificar pasos
- ¿Seguiste el orden correcto?
- ¿Importaste todos los CSVs?
- ¿Nombres de pestañas exactos? (Dashboard, Efectivo, A/R, etc.)

#### 3. Errores comunes
| Error | Causa | Solución |
|-------|-------|----------|
| #REF! | Referencia rota | Verificar nombre pestaña en fórmula |
| #DIV/0! | División por cero | Agregar SI(denominador=0, 0, división) |
| #VALOR! | Tipo dato incorrecto | Verificar formato columna (número vs texto) |
| Fórmula no calcula | Texto en vez de número | Cambiar formato columna a Número |

#### 4. Recursos externos
- **YouTube:** "Excel tutorial español" para conceptos básicos
- **Microsoft Docs:** Para fórmulas específicas
- **Reddit r/excel:** Comunidad muy activa para preguntas

---

## 📈 RESULTADOS ESPERADOS

### Después de implementar este sistema verás:

#### ✅ En 7 días:
- Control total de efectivo diario
- Visibilidad completa de ingresos/gastos
- Identificación de clientes críticos por cobrar
- Priorización de pagos urgentes

#### ✅ En 30 días:
- Historial completo de movimientos
- KPIs actualizados y confiables
- Proyecciones de flujo caja precisas
- Presupuesto funcionando con alertas

#### ✅ En 90 días:
- Tendencias claras de ingresos/gastos
- Comparativas mensuales
- Ajustes presupuesto basados en datos reales
- Hábito diario consolidado

#### ✅ En 12 meses:
- Plan sanitización TC completado (ahorro $18k intereses)
- Todas las tarjetas liquidadas ✅
- Deuda reducida significativamente
- Cash flow positivo sostenible

#### ✅ En 24 meses:
- Ahorro vivienda: $45,000 ✅
- Nissan parcial/totalmente pagado
- Working capital positivo
- Empresa financieramente sana

---

## 🎓 APRENDERÁS

### Al usar este sistema desarrollarás:

- ✅ **Disciplina financiera:** Registro diario 5-10 min
- ✅ **Visión estratégica:** KPIs guían decisiones
- ✅ **Control presupuesto:** Alertas previenen excesos
- ✅ **Proyección:** Anticipas problemas antes que ocurran
- ✅ **Priorización:** Sabes qué pagar primero
- ✅ **Excel avanzado:** Fórmulas, formato condicional, gráficos
- ✅ **Business Intelligence:** Si usas Power BI

---

## 🚀 PRÓXIMOS PASOS

### Después de implementar el sistema Excel:

#### Corto plazo (1-3 meses):
1. **Consolidar hábito diario** - No saltear ningún día
2. **Ajustar presupuesto** - Basado en datos reales
3. **Optimizar categorías** - Agregar/quitar según necesites
4. **Crear reportes mensuales** - Para análisis tendencias

#### Mediano plazo (3-12 meses):
1. **Implementar Power BI** - Dashboards interactivos
2. **Automatizar cobros** - Recordatorios automáticos A/R
3. **Integrar con banco** - Si tu banco tiene API/export
4. **Proyecciones avanzadas** - Scenarios "what-if"

#### Largo plazo (12+ meses):
1. **Migrar a software contable** - Si empresa crece mucho
2. **Contratar contador tiempo completo** - Cuando sea viable
3. **Sistema ERP** - Solo si ventas >$500k/año
4. **Mantener Excel** - Como backup y análisis rápidos

---

## 📜 LICENCIA Y CRÉDITOS

### Licencia
Este sistema es propiedad de **AlvaroVelasco.Net SRL**. Puedes:
- ✅ Usar libremente para tu empresa
- ✅ Modificar y adaptar a tus necesidades
- ✅ Compartir con tu equipo/contador
- ⛔ NO redistribuir comercialmente
- ⛔ NO vender las plantillas

### Créditos
- **Diseño sistema:** Claude Code (Anthropic)
- **Datos financieros:** Álvaro Velasco
- **Requerimientos:** AlvaroVelasco.Net SRL
- **Fecha:** 07 de Noviembre 2025

---

## 📞 INFORMACIÓN CONTACTO

**Empresa:** AlvaroVelasco.Net SRL
**Ubicación:** Costa Rica
**Moneda base:** USD (secundaria: CRC)
**Tipo cambio:** 507 CRC/USD

**Sistema versión:** 1.0
**Última actualización:** 07 de Noviembre 2025
**Próxima revisión:** 07 de Diciembre 2025

---

## ✅ CHECKLIST FINAL

Antes de comenzar, verifica que tienes TODO:

- [ ] Excel Office 365 instalado
- [ ] Los 12 archivos CSV en esta carpeta
- [ ] `GUIA_IMPLEMENTACION_PASO_A_PASO.md` leído
- [ ] `FORMULAS_EXCEL_COMPLETAS.md` abierto en otra ventana
- [ ] 3-4 horas disponibles sin interrupciones
- [ ] Carpeta `C:\Finanzas\` creada
- [ ] OneDrive configurado (opcional pero recomendado)
- [ ] Café/agua/snacks para las 4 horas ☕

**¿TODO LISTO?** → Abre `GUIA_IMPLEMENTACION_PASO_A_PASO.md` y comienza FASE 0 🚀

---

**¡ÉXITO EN TU IMPLEMENTACIÓN!** 🎉

Este sistema cambiará completamente cómo manejas las finanzas de tu empresa.
En 30 días no podrás creer cómo trabajabas antes sin él.

**Pregunta:** ¿Cuánto vale para ti tener control total de tus finanzas?
**Respuesta:** Las 4 horas que invertirás implementando este sistema. 💪

---

_Última actualización: 07 de Noviembre 2025_
_Versión: 1.0_
_Sistema: Excel + Power BI_
