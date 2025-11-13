# PROYECTO: SISTEMA FINANCIERO COMPLETO
## Sistema de Gestión Financiera, Utilidades y Presupuestación

**Fecha Inicio:** 10 de Noviembre 2025
**Estado:** En Desarrollo (Fase 1)
**Prioridad:** Alta

---

## 📋 ÍNDICE
1. [Modelo de Negocio](#modelo-de-negocio)
2. [Objetivos del Proyecto](#objetivos-del-proyecto)
3. [Estructura Técnica](#estructura-técnica)
4. [Roadmap y Fases](#roadmap-y-fases)
5. [Decisiones de Diseño](#decisiones-de-diseño)
6. [Estado Actual](#estado-actual)
7. [Próximos Pasos](#próximos-pasos)

---

## 🏢 MODELO DE NEGOCIO

**Tipo:** Intermediación/Distribución sin inventario físico

**Flujo operativo:**
```
1. Cliente solicita producto (ej: toners HP)
2. Se compra a proveedor (ej: Intcomex)
3. Se vende al cliente inmediatamente
4. Utilidad = Precio Venta - Costo Compra - Gastos
```

**Características clave:**
- ✅ NO se mantiene inventario
- ✅ Compras contra pedido del cliente
- ✅ Ciclo rápido: compra y venta en días
- ✅ Múltiples proveedores (Intcomex, otros)
- ✅ Múltiples clientes (B2B y B2C)

**Implicaciones contables:**
- Las compras a proveedores son **COGS** (Cost of Goods Sold / Costo de Ventas)
- NO son "Gastos Operativos" (esos son luz, renta, etc.)
- NO es "Inventario" (no se almacena)
- Cada compra debe poder vincularse con su venta correspondiente

---

## 🎯 OBJETIVOS DEL PROYECTO

### Objetivos Principales

1. **Sistema de Categorización Correcto**
   - Separar claramente: COGS vs Gastos Operativos vs Ingresos
   - Permitir análisis financiero preciso
   - Vincular compras con ventas

2. **Cálculo Automático de Utilidades Mensuales**
   - Utilidad Bruta = Ingresos - COGS
   - Utilidad Neta = Utilidad Bruta - Gastos Operativos
   - Desglose por categoría y subcategoría
   - Márgenes de utilidad (% sobre ventas)

3. **Sistema de Presupuestación**
   - Presupuesto mensual por categoría
   - Comparación: Presupuesto vs Real
   - % de cumplimiento
   - Alertas de sobre-presupuesto

4. **Análisis de Patrones de Compra**
   - Detectar compras recurrentes
   - Identificar proveedores frecuentes
   - Líneas de producto más vendidas
   - Predecir presupuesto para próximo mes

5. **Dashboard Comparativo Mes a Mes**
   - KPIs: Ingresos, COGS, Gastos, Utilidad
   - Variación % mes a mes
   - Tendencias (crecimiento, caídas)
   - Detección de anomalías

6. **Sistema de Alertas**
   - Operaciones con pérdida (venta < costo)
   - Márgenes muy bajos (<10%)
   - Sobre-presupuesto (>10% del plan)
   - Cuentas por cobrar vencidas

### Beneficios Esperados

- 📊 **Visibilidad total** de rentabilidad por mes
- 💰 **Control de gastos** mediante presupuestos
- 📈 **Proyecciones precisas** basadas en histórico
- ⚠️ **Detección temprana** de problemas financieros
- 🎯 **Decisiones informadas** sobre qué productos/servicios son más rentables

---

## 🏗️ ESTRUCTURA TÉCNICA

### Estructura de Categorías Propuesta

```
📊 TRANSACCIONES (Hoja Existente)
│
├─ INGRESOS
│  ├─ Ventas de Productos
│  ├─ Ventas de Servicios
│  └─ Otros Ingresos
│
├─ COSTO DE VENTAS (COGS)
│  ├─ COGS - Productos (compras a proveedores)
│  ├─ COGS - Flete/Importación
│  └─ COGS - Devoluciones
│
├─ GASTOS OPERATIVOS
│  ├─ Suministros de Oficina (uso propio)
│  ├─ Servicios (luz, internet, teléfono)
│  ├─ Nómina/Salarios
│  ├─ Marketing/Publicidad
│  ├─ Mantenimiento
│  └─ Otros Gastos
│
└─ GASTOS FINANCIEROS
   ├─ Intereses Bancarios
   ├─ Comisiones Bancarias
   └─ Diferencial Cambiario
```

### Nuevas Hojas Excel

#### 1. **UTILIDADES_MENSUALES**
```
Columnas:
- Mes/Año
- Total Ingresos
- Total COGS
- Utilidad Bruta (Ingresos - COGS)
- Margen Bruto % (Utilidad Bruta / Ingresos * 100)
- Total Gastos Operativos
- Total Gastos Financieros
- Utilidad Neta (Utilidad Bruta - Gastos)
- Margen Neto % (Utilidad Neta / Ingresos * 100)
```

#### 2. **PRESUPUESTO_MENSUAL**
```
Columnas:
- Mes/Año
- Categoría
- Subcategoría
- Presupuesto Planeado
- Real Ejecutado
- Diferencia (Real - Presupuesto)
- % Cumplimiento
- Estado (OK / Sobre-presupuesto / Bajo presupuesto)
```

#### 3. **COMPRAS_RECURRENTES**
```
Columnas:
- Proveedor
- Producto/Categoría
- Frecuencia (veces/mes)
- Monto Promedio
- Monto Total (últimos 3 meses)
- Tendencia (↑ ↓ →)
- Presupuesto Sugerido (próximo mes)
```

#### 4. **VINCULOS_COMPRA_VENTA**
```
Columnas:
- ID Operación
- Fecha Compra
- Proveedor
- Monto Compra (COGS)
- Fecha Venta
- Cliente
- Monto Venta (Ingreso)
- Utilidad ($)
- Margen (%)
- Estado (Completado / Pendiente Venta / Pendiente Pago)
```

#### 5. **DASHBOARD_COMPARATIVO**
```
Secciones:
- KPIs Mensuales (últimos 12 meses)
- Gráfica: Ingresos vs Utilidad
- Gráfica: Margen % tendencia
- Top 5 Productos más rentables
- Top 5 Proveedores por volumen
- Alertas activas
```

### Scripts Python

#### 1. **analizar_utilidades_mensuales.py**
```python
"""
Lee TRANSACCIONES y calcula:
- Suma de ingresos por mes
- Suma de COGS por mes
- Suma de gastos por mes
- Utilidad bruta y neta
- Márgenes %
Escribe en hoja UTILIDADES_MENSUALES
"""
```

#### 2. **detectar_compras_recurrentes.py**
```python
"""
Analiza TRANSACCIONES (últimos 3-6 meses):
- Agrupa por proveedor + producto/categoría
- Cuenta frecuencia de compras
- Calcula promedios y totales
- Detecta patrones (cada semana, mensual, etc.)
- Sugiere presupuesto para próximo mes
Escribe en hoja COMPRAS_RECURRENTES
"""
```

#### 3. **vincular_compras_ventas.py**
```python
"""
Intenta vincular cada compra (COGS) con su venta (Ingreso):
- Por referencia común en Concepto/Notas
- Por fechas cercanas (±7 días)
- Por cliente mencionado en notas
- Calcula utilidad por operación
Escribe en hoja VINCULOS_COMPRA_VENTA
"""
```

#### 4. **comparar_presupuesto_vs_real.py**
```python
"""
Lee PRESUPUESTO_MENSUAL y TRANSACCIONES:
- Compara presupuesto vs real por categoría
- Calcula diferencias y % cumplimiento
- Identifica sobre-presupuestos
- Genera alertas
Actualiza hoja PRESUPUESTO_MENSUAL
"""
```

#### 5. **generar_dashboard.py**
```python
"""
Genera dashboard visual en Excel:
- Tablas pivote con KPIs
- Gráficas automáticas
- Secciones de alertas
- Comparativas mes a mes
Actualiza hoja DASHBOARD_COMPARATIVO
"""
```

#### 6. **sistema_alertas.py**
```python
"""
Revisa condiciones y genera alertas:
- Operaciones con pérdida (venta < costo)
- Margen bajo (<10%)
- Sobre-presupuesto (>10%)
- Cuentas por cobrar vencidas (>30 días)
- Cuentas por pagar próximas a vencer (<7 días)
Genera reporte de alertas en terminal y Excel
"""
```

#### 7. **actualizar_categorias.py**
```python
"""
Actualiza categorización masiva:
- Lee reglas de categorización
- Aplica a transacciones sin categoría o mal categorizadas
- Usa alias de proveedores
- Backup antes de modificar
"""
```

---

## 🗺️ ROADMAP Y FASES

### **FASE 1: CORRECCIÓN Y BASES** (Días 1-3)
**Objetivo:** Corregir estructura actual y sentar bases

- [x] Crear documento maestro del proyecto
- [ ] Auditar Excel actual (categorías existentes)
- [ ] Corregir fila 206 (Intcomex: Gastos Operativos → COGS)
- [ ] Definir e implementar estructura completa de categorías
- [ ] Actualizar script `procesar_factura_intcomex.py` con nueva categorización
- [ ] Crear script `actualizar_categorias.py` para corrección masiva
- [ ] Aplicar categorización correcta a transacciones históricas

**Entregables:**
- ✅ Estructura de categorías implementada
- ✅ Transacciones históricas recategorizadas
- ✅ Scripts de procesamiento actualizados

---

### **FASE 2: UTILIDADES Y ANÁLISIS BÁSICO** (Días 4-7)
**Objetivo:** Calcular utilidades mensuales y análisis de rentabilidad

- [ ] Crear hoja UTILIDADES_MENSUALES en Excel
- [ ] Desarrollar script `analizar_utilidades_mensuales.py`
- [ ] Calcular utilidades de todos los meses históricos
- [ ] Crear hoja VINCULOS_COMPRA_VENTA
- [ ] Desarrollar script `vincular_compras_ventas.py`
- [ ] Vincular compras con ventas (cuando sea posible)
- [ ] Calcular márgenes por operación

**Entregables:**
- ✅ Reporte de utilidades mensuales (histórico completo)
- ✅ Análisis de márgenes por operación
- ✅ Identificación de operaciones rentables vs no rentables

---

### **FASE 3: PATRONES Y PRESUPUESTOS** (Días 8-12)
**Objetivo:** Detectar patrones y crear sistema de presupuestación

- [ ] Crear hoja COMPRAS_RECURRENTES
- [ ] Desarrollar script `detectar_compras_recurrentes.py`
- [ ] Analizar histórico (3-6 meses)
- [ ] Identificar compras recurrentes por proveedor/producto
- [ ] Calcular frecuencias y promedios
- [ ] Crear hoja PRESUPUESTO_MENSUAL
- [ ] Desarrollar script `comparar_presupuesto_vs_real.py`
- [ ] Generar presupuesto sugerido para próximo mes basado en histórico

**Entregables:**
- ✅ Análisis de patrones de compra
- ✅ Presupuesto mensual sugerido
- ✅ Sistema de comparación presupuesto vs real

---

### **FASE 4: DASHBOARD Y COMPARATIVAS** (Días 13-17)
**Objetivo:** Visualización y comparativas mes a mes

- [ ] Crear hoja DASHBOARD_COMPARATIVO
- [ ] Desarrollar script `generar_dashboard.py`
- [ ] Implementar gráficas automáticas:
  - Ingresos vs COGS vs Gastos (últimos 12 meses)
  - Evolución de márgenes %
  - Top 5 productos/servicios más rentables
  - Top 5 proveedores por volumen
- [ ] Implementar KPIs:
  - Variación % mes a mes
  - Crecimiento/caída de ingresos
  - Tendencia de márgenes
- [ ] Crear sección de comparativas:
  - Mes actual vs mes anterior
  - Mes actual vs mismo mes año anterior
  - Promedio móvil (3 meses, 6 meses)

**Entregables:**
- ✅ Dashboard visual en Excel
- ✅ Gráficas automáticas
- ✅ Reporte de comparativas mensuales

---

### **FASE 5: ALERTAS Y AUTOMATIZACIÓN** (Días 18-21)
**Objetivo:** Sistema de alertas proactivo

- [ ] Desarrollar script `sistema_alertas.py`
- [ ] Implementar alertas:
  - ⚠️ Operaciones con pérdida
  - ⚠️ Márgenes bajos (<10%)
  - ⚠️ Sobre-presupuesto (>10%)
  - ⚠️ Cuentas por cobrar vencidas
  - ⚠️ Cuentas por pagar próximas a vencer
  - ⚠️ Caída de ingresos mes a mes (>15%)
- [ ] Crear reporte de alertas en terminal
- [ ] Agregar sección de alertas en Dashboard
- [ ] Script de ejecución automática mensual

**Entregables:**
- ✅ Sistema de alertas funcionando
- ✅ Reporte de alertas
- ✅ Automatización de análisis mensual

---

### **FASE 6: OPTIMIZACIÓN Y DOCUMENTACIÓN** (Días 22-25)
**Objetivo:** Pulir, optimizar y documentar

- [ ] Crear guía de uso del sistema completo
- [ ] Documentar procedimientos:
  - Cómo registrar una compra
  - Cómo registrar una venta
  - Cómo vincular compra con venta
  - Cómo establecer presupuestos
  - Cómo interpretar dashboard y alertas
- [ ] Crear script maestro `analisis_mensual.py` que ejecuta todo
- [ ] Optimizar performance de scripts
- [ ] Agregar manejo de errores robusto
- [ ] Testing con diferentes escenarios

**Entregables:**
- ✅ Sistema completo funcionando
- ✅ Documentación completa
- ✅ Guía de usuario
- ✅ Script maestro automatizado

---

## 🧠 DECISIONES DE DISEÑO

### Decisión #1: Categorización de Compras a Proveedores
**Contexto:** Factura Intcomex por toners HP para reventa
**Decisión:** Categorizar como "COGS - Productos" NO como "Gastos Operativos"
**Razón:** Modelo de negocio es intermediación sin inventario. Las compras son costo directo de la venta, no gastos de operación.
**Impacto:** Permite calcular correctamente utilidad bruta y márgenes.
**Fecha:** 10/11/2025

### Decisión #2: Estructura de Categorías de 3 Niveles
**Contexto:** Necesidad de análisis detallado pero agrupación flexible
**Decisión:** Tipo → Categoría → Subcategoría
**Ejemplo:** Egreso → COGS → COGS - Productos
**Razón:** Permite drill-down desde macro (Tipo) a micro (Subcategoría)
**Impacto:** Facilita análisis agregado y detallado según necesidad.
**Fecha:** 10/11/2025

### Decisión #3: Vinculación Compra-Venta por Referencias y Fechas
**Contexto:** Necesidad de calcular margen por operación
**Decisión:** Vincular usando (1) referencia común en notas/concepto, (2) fechas cercanas ±7 días
**Razón:** No hay campo ID operación actualmente, usar heurística inteligente
**Impacto:** Vinculación automática ~70-80%, resto requiere revisión manual.
**Fecha:** 10/11/2025

### Decisión #4: Presupuestos Basados en Histórico
**Contexto:** Usuario no tiene presupuestos establecidos aún
**Decisión:** Generar presupuesto sugerido basado en promedio últimos 3 meses + 10% buffer
**Razón:** Punto de partida realista, ajustable manualmente después
**Impacto:** Usuario puede adoptar o modificar según objetivos de crecimiento.
**Fecha:** 10/11/2025

### Decisión #5: Dashboard en Excel, No App Separada
**Contexto:** Usuario prefiere trabajar en Excel
**Decisión:** Dashboard dentro del mismo archivo Excel, actualizable con scripts
**Razón:** No agregar complejidad de otra herramienta, mantener todo en un lugar
**Impacto:** Scripts Python leen/escriben Excel, usuario solo abre archivo.
**Fecha:** 10/11/2025

---

## 📊 ESTADO ACTUAL

**Fase:** FASE 1 - CORRECCIÓN Y BASES
**Progreso:** 10% (1/10 tareas completadas)

### ✅ Completado
- [x] Documento maestro del proyecto creado
- [x] Script `procesar_factura_intcomex.py` funcional (Windows compatible)
- [x] Factura Intcomex registrada (fila 206) - **Requiere corrección de categoría**

### 🔄 En Proceso
- [ ] Auditoría de Excel actual

### ⏳ Pendiente
- [ ] Corrección de fila 206
- [ ] Definir categorías completas
- [ ] Implementar categorías en Excel
- [ ] Desarrollar scripts de análisis

### 🚨 Issues Conocidos
1. **Fila 206 mal categorizada:** Registrada como "Gastos Operativos", debe ser "COGS - Productos"
2. **Estructura de categorías incompleta:** Necesita expansión para soportar modelo de negocio
3. **Sin vinculación compra-venta:** Imposible calcular márgenes por operación actualmente
4. **Sin análisis de utilidades:** No hay visibilidad de rentabilidad mensual

---

## 🚀 PRÓXIMOS PASOS

### Inmediatos (Esta Sesión)
1. **Auditar Excel actual:** Ver qué categorías existen, cómo están estructuradas
2. **Definir estructura de categorías completa:** Acordar nombres y niveles
3. **Corregir fila 206:** Cambiar Gastos Operativos → COGS - Productos
4. **Actualizar script procesador:** Usar nueva categorización

### Corto Plazo (Próximas 2 Sesiones)
1. **Crear script `actualizar_categorias.py`:** Para corrección masiva
2. **Recategorizar transacciones históricas:** Aplicar estructura correcta
3. **Crear hoja UTILIDADES_MENSUALES**
4. **Desarrollar `analizar_utilidades_mensuales.py`**
5. **Generar primer reporte de utilidades**

### Mediano Plazo (Próximas 5 Sesiones)
1. Completar FASE 2: Utilidades y análisis básico
2. Completar FASE 3: Patrones y presupuestos
3. Comenzar FASE 4: Dashboard

---

## 📝 NOTAS Y OBSERVACIONES

### Modelo de Negocio - Detalles Importantes
- **NO hay inventario físico:** Cada compra está asociada a un cliente específico
- **Ciclo rápido:** Compra y venta en días, no semanas/meses
- **Múltiples proveedores:** Intcomex es uno de varios, necesita flexibilidad
- **Variedad de productos:** No solo toners, cualquier producto tecnológico

### Consideraciones Técnicas
- **Excel es fuente de verdad:** Todos los scripts leen/escriben desde/hacia Excel
- **Backups automáticos:** Antes de cualquier modificación masiva
- **Compatibilidad Windows:** Scripts deben funcionar en Windows (no solo Linux)
- **Formato de fechas:** Usar formato manual (día/mes/año) para compatibilidad cross-platform

### Métricas Clave a Monitorear
- **Margen bruto %:** Utilidad Bruta / Ingresos (objetivo: >20%)
- **Margen neto %:** Utilidad Neta / Ingresos (objetivo: >10%)
- **Rotación:** Días entre compra y venta (objetivo: <7 días)
- **Cumplimiento presupuesto:** % adherencia (objetivo: 90-110%)
- **Crecimiento mensual:** Variación % ingresos mes a mes

---

## 📚 RECURSOS Y REFERENCIAS

### Archivos del Proyecto
- `PROYECTO_SISTEMA_FINANCIERO.md` (este documento)
- `INFORME_EJECUTIVO.md` (estado general del proyecto deuda)
- `GUIA_APRENDIZAJE_CLAUDE_AI.md` (guía de comandos y herramientas)
- `AlvaroVelasco_Finanzas_v2.0.xlsx` (Excel principal - .gitignore)

### Scripts Existentes
- `scripts/procesar_factura_intcomex.py` - Procesador de facturas electrónicas XML
- `scripts/auditoria_con_alias.py` - Auditoría de balances con sistema de alias
- `scripts/alias_cuentas.py` - Sistema de alias para cuentas y conceptos

### Branch de Trabajo
- `claude/continue-project-011CUzXviLotjtyCRLo5QCev`

---

**Última Actualización:** 10 de Noviembre 2025, 23:30
**Actualizado por:** Claude
**Próxima Revisión:** Al completar FASE 1
