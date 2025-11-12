# CUESTIONARIO FUNDACIONAL - EXCEL V3.0
**Sistema Financiero Completo - Álvaro Velasco**
**Fecha Inicio:** 12 Noviembre 2025
**Branch:** `claude/continue-project-011CUzXviLotjtyCRLo5QCev`

---

## 🎯 OBJETIVO

Establecer bases sólidas para el diseño del Excel v3.0 mediante cuestionario estructurado en bloques de 5 preguntas. Este documento es la **fuente de verdad** de todas las respuestas y decisiones fundacionales.

---

## 📊 PROGRESO GENERAL

- ✅ **Bloque #1 (C1-C5):** COMPLETADO - Tarjetas, Gastos Noviembre, Márgenes, Contratos, Categorizaciones
- ⏳ **Bloque #2 (T1-T5):** ENVIADO - Esperando respuestas sobre pagos, uso, top clientes, alias
- 📋 **Bloques #3-8:** PLANIFICADOS - Cuentas bancarias, Hacienda, estructura, migración, dashboards

---

## ✅ BLOQUE #1 - ANÁLISIS CRÍTICO DE V2.0
**Estado:** COMPLETADO
**Fecha:** 12 Nov 2025

### C1. Categoría "Intereses Tarjetas Crédito" ($17,197 en 2 meses)

**Pregunta:** ¿Qué representa realmente esta categoría?

**Respuesta:** ✅ **Categoría B - Pagos Completos (principal + interés)**

**Detalle de las 5 Tarjetas:**

#### TARJETAS BNCR (4 tarjetas):

1. **VISA 3519 (Alvaro)**
   - Balance USD: $3,864.90
   - Balance CRC: ₡0

2. **VISA 9837 (Alvaro)**
   - Balance USD: $3,299.01
   - Balance CRC: ₡0

3. **VISA 6386 (Alejandra)**
   - Balance USD: $5,195.07
   - Balance CRC: ₡0

4. **MasterCard 8759 (Alvaro)**
   - Balance USD: $0
   - Balance CRC: ₡863,830

#### TARJETA BAC (1 tarjeta):

5. **VISA 9550 (Alvaro)**
   - Balance USD: $2,508.75
   - Balance CRC: ₡0

**TOTAL DEUDA REAL:**
- **USD:** $14,867.73
- **CRC:** ₡863,830 (~$1,669 al TC 517.5)
- **TOTAL EQUIVALENTE USD:** ~$16,536

**Análisis Crítico:**
- v2.0 mostraba $16,380 → Diferencia de ~$156 USD (dentro del margen de pagos/cargos del período)
- El 56% de gastos en esta categoría se explica: son PAGOS COMPLETOS, no solo intereses
- Para v3.0: Separar en subcategorías "Pago Principal TC" y "Intereses TC"

---

### C2. Gastos Catastróficos Noviembre ($24,422 vs $6,112 en Octubre)

**Pregunta:** ¿Por qué noviembre tuvo 4x los gastos de octubre?

**Respuesta:** ✅ **DUPLICADOS en v2.0**

**Confirmación:** El usuario confirmó que los gastos inflados artificialmente son por transacciones duplicadas en el Excel v2.0.

**Análisis Crítico:**
- Octubre: $6,112 gastos (realista)
- Noviembre: $24,422 gastos (inflado por duplicados)
- Diferencia: ~$18,310 en duplicados estimados
- Script `eliminar_duplicados.py` disponible pero aún no ejecutado

**Para v3.0:**
- Implementar detección automática de duplicados (Columna S: Alerta Duplicado)
- Fórmula: `=IF(COUNTIFS($A:$A, A2, $E:$E, E2, $I:$I, I2) > 1, "⚠️ DUPLICADO", "")`
- Formato condicional rojo para alertas visuales

---

### C3. Margen Negativo (-11.5%)

**Pregunta:** ¿El negocio realmente está perdiendo dinero?

**Respuesta:** ✅ **NO - Error de datos**

**Causas Confirmadas:**
1. Duplicados (C2) inflan gastos artificialmente
2. Categorizaciones incorrectas (transferencias internas como ingresos)
3. Mezcla de gastos personales/empresariales sin separación
4. Pagos completos de TC en categoría "Intereses" (C1)

**Realidad del Negocio:**
- Usuario confirmó: "el negocio SÍ es rentable"
- Break-even: ~$8,000/mes
- Ingresos variables: $8k-$17k/mes
- Margen real positivo (por calcular con datos limpios)

**Para v3.0:**
- Separación clara COGS vs Gastos Operativos
- Tracking de márgenes por operación (ID Operación)
- Dashboard con márgenes: Bruto, Operativo, Neto

---

### C4. Contratos Mensuales

**Pregunta Inicial:** ¿Son correctos los montos de los 3 contratos (VWR, Grupo Acción, Gentra)?

**Respuesta:** ✅ **Corrección de montos + REVELACIÓN CRÍTICA**

**Corrección de Montos:**
- VWR: $1,400/mes (no $1,200)
- Grupo Acción: $678/mes + $258 licencias = $936/mes
- Gentra: $452/mes + $226 licencias = $678/mes
- **Subtotal 3 contratos:** $3,014/mes (no $2,330)

**REVELACIÓN CRÍTICA:** No son 3 contratos, son **22+ CLIENTES ACTIVOS**

#### LISTA COMPLETA DE 22 CLIENTES:

**Contratos de Mantenimiento (7 clientes):**
1. VWR - $1,400/mes
2. Grupo Acción - $678/mes
3. Gentra - $452/mes
4. Proimagen (Futuropa) - Contrato
5. CCSS - Contrato
6. J.P. Agentes Duales - Contrato
7. Genfar - Contrato

**Microsoft 365 Licencias (~200 licencias totales):**
8. Grupo Acción - $258/mes
9. Gentra - $226/mes
10. Proimagen (Futuropa) - Licencias
11. JDSRealClean (Real Clean, RealCleanJDS) - Licencias
12. Tecnoambientes (Ambientes con Tecnología) - Licencias
13. Multiplica - Licencias
14. Eurocomp - Licencias

**Servicios Ocasionales:**
15. Diesco
16. Fertica
17. Tecnoambientes
18. María Gabriela
19. Eurocomp

**Canjes/Intercambio (sin flujo directo de efectivo):**
20. Global Automotriz
21. Miguel Solano
22. Start Sistemas (Sistema/SWS-Software)

**Análisis Crítico:**
- Ingresos por contratos: $3,014+ mensual (solo 3 principales)
- 200+ licencias Microsoft 365: ~$1,600-$2,000/mes adicional
- Concentración de riesgo: VWR = 51% de ingresos por contratos ($1,400/$2,730)
- Modelo: 45% Contratos, 20% Licencias, 15% Productos, 15% Servicios, 5% Cloud

**Para v3.0:**
- Hoja CLIENTES_VIP con Customer Lifetime Value (CLV)
- Tracking de concentración de riesgo por cliente
- Análisis de márgenes por tipo de cliente

---

### C5. "Sistema" y "Banco Promerica" como Clientes

**Pregunta:** ¿Por qué aparecen como clientes top en el análisis?

**Respuesta:** ✅ **CATEGORIZACIONES INCORRECTAS en v2.0**

**"Sistema" = Start Sistemas (SWS-Software):**
- Es su sistema de facturación
- Transacciones son probablemente licencias/servicios DEL sistema
- NO debería aparecer como ingreso en muchos casos
- Relación de CANJE (ver cliente #22)

**"Banco Promerica":**
- Son transferencias internas entre cuentas propias
- Incorrectamente categorizadas como INGRESOS
- Deben ser tipo "Transferencia" (no afecta P&L)

**Para v3.0:**
- Tipo de transacción "Transferencia" excluido de P&L
- Validación de datos: Dropdown para "Tipo Entidad" (Cliente/Proveedor/Banco/Interno)
- Normalización de nombres de entidades

---

## ⏳ BLOQUE #2 - TARJETAS, CLIENTES TOP, ALIAS
**Estado:** ENVIADO - Esperando Respuestas
**Fecha Envío:** 12 Nov 2025

### T1. Montos de Pago Mensual de Tarjetas

**Pregunta:** ¿Cuánto pagas mensualmente a cada una de las 5 tarjetas?

**Formato solicitado:**
```
1. VISA 3519: $___/mes
2. VISA 9837: $___/mes
3. VISA 6386 (Alejandra): $___/mes
4. MC 8759: ₡___/mes
5. BAC 9550: $___/mes
```

**⏳ PENDIENTE DE RESPUESTA**

---

### T2. Uso Empresarial vs Personal por Tarjeta

**Pregunta:** ¿Qué porcentaje de cada tarjeta es uso empresarial vs personal?

**Formato solicitado:**
```
1. VISA 3519: ___% Empresa / ___% Personal
2. VISA 9837: ___% Empresa / ___% Personal
3. VISA 6386: ___% Empresa / ___% Personal
4. MC 8759: ___% Empresa / ___% Personal
5. BAC 9550: ___% Empresa / ___% Personal
```

**⏳ PENDIENTE DE RESPUESTA**

---

### T3. TOP 5 Clientes por Ingresos Mensuales

**Pregunta:** ¿Cuáles son los 5 clientes que más ingresos generan mensualmente (contratos + licencias + ocasional)?

**Formato solicitado:**
```
1. [Cliente]: $___/mes (Contratos: $___ + Licencias: $___ + Ocasional: $___)
2. [Cliente]: $___/mes (breakdown)
3. [Cliente]: $___/mes (breakdown)
4. [Cliente]: $___/mes (breakdown)
5. [Cliente]: $___/mes (breakdown)
```

**⏳ PENDIENTE DE RESPUESTA**

---

### T4. Lista Normalizada de Alias de Clientes

**Pregunta:** ¿Cuáles son todas las variaciones de nombres que usas para cada cliente?

**Ya Identificados:**
- Futuropa → Proimagen (o viceversa)
- Real Clean → JDSRealClean, RealCleanJDS
- Tecnoambientes → Ambientes con Tecnología
- Start Sistemas → Sistema, SWS-Software

**Formato solicitado:**
```
Nombre Oficial → alias1, alias2, alias3

Ejemplo:
VWR Costa Rica → VWR, VWR CR
[Continúa con los 22 clientes...]
```

**⏳ PENDIENTE DE RESPUESTA**

---

### T5. Manejo de Transacciones de Canje/Intercambio

**Pregunta:** ¿Cómo quieres registrar las transacciones de canje con Global Automotriz, Miguel Solano y Start Sistemas?

**Opciones:**

**A. No Registrar ($0):**
- No aparece en TRANSACCIONES
- Solo nota en hoja CLIENTES_VIP

**B. Doble Registro (Ingreso + Egreso):**
- Ingreso: "Servicio a Global Automotriz" +$500
- Egreso: "Canje - Servicio recibido" -$500
- Net: $0, pero refleja volumen de operaciones

**C. Memo/Nota Únicamente:**
- Registro con Monto = $0
- Campo Notas: "Canje: Valor estimado $500"
- No afecta P&L ni métricas

**⏳ PENDIENTE DE RESPUESTA**

---

## 📋 BLOQUES PLANIFICADOS

### Bloque #3 - Cuentas Bancarias
- B1: Lista completa de cuentas (normalización de nombres)
- B2: Saldos actuales de cada cuenta
- B3: Uso principal de cada cuenta (operativa, nómina, ahorro)
- B4: ¿CIMSA es tu empresa o intermediario separado?
- B5: Preferencia de nombres normalizados

### Bloque #4 - Deuda Hacienda
- H1: Monto total adeudado a Hacienda
- H2: Desglose por tipo (Renta, IVA)
- H3: Cuotas pendientes de cada tipo
- H4: Pago mensual acordado
- H5: ¿Hay recargos/intereses?

### Bloque #5 - Estructura Excel v3.0
- E1: ¿Prefieres 1 archivo o múltiples workbooks?
- E2: ¿Qué hojas consideras más críticas?
- E3: ¿Nivel de automatización deseado?
- E4: ¿Frecuencia de actualización (diaria/semanal)?
- E5: ¿Necesitas versión móvil/Google Sheets?

### Bloque #6 - Plan de Migración
- M1: ¿Partir de cero o migrar transacciones v2.0?
- M2: Si migrar, ¿desde qué fecha?
- M3: ¿Mantener v2.0 como referencia histórica?
- M4: ¿Quién alimentará v3.0 (solo tú, equipo)?
- M5: ¿Deadline para tener v3.0 operativo?

### Bloque #7 - Categorización y Nomenclatura
- N1: Aprobación de categorías principales propuestas
- N2: Subcategorías adicionales necesarias
- N3: Nomenclatura de cuentas (español/inglés)
- N4: ¿Códigos numéricos para categorías?
- N5: ¿Campos personalizados adicionales?

### Bloque #8 - Dashboards y Reportes
- D1: Métricas más importantes para ti
- D2: Frecuencia de revisión de cada métrica
- D3: ¿Comparativas año anterior?
- D4: ¿Alertas automáticas (bajo cash, vencimientos)?
- D5: ¿Exportar reportes PDF/automatizar envíos?

---

## 🔍 HALLAZGOS CRÍTICOS ACUMULADOS

### Datos Financieros Confirmados:

**Deuda Total:**
- Tarjetas Crédito: ~$16,536 USD equivalente (5 tarjetas)
- Nissan Frontier: $18,680.75 saldo, $800/mes
- Hacienda: $544/mes (Renta + IVA atrasados)

**Flujo Operativo:**
- Ingresos variables: $8k-$17k/mes
- Break-even: ~$8k/mes
- 85% ventas a crédito (15-30 días)
- Paga proveedores en 30 días
- Ciclo de conversión: -15 días (favorable)

**Cuentas por Cobrar:**
- Estimado: $9,200-$10,866

**Proveedores Principales:**
- Intcomex: $5k crédito
- Eurocomp: $4k
- CompuEconómicos: $5k
- TD Synex, ICD Soft

**Modelo de Negocio:**
- Intermediación SIN inventario
- 45% Contratos Mantenimiento
- 20% Licencias Microsoft
- 15% Productos
- 15% Servicios
- 5% Cloud Services

### Problemas Confirmados de v2.0:

1. **Duplicados:** ~$3,000+ (explica noviembre catastrófico)
2. **Categorizaciones Incorrectas:**
   - Transferencias internas como ingresos
   - Pagos completos TC como "intereses"
   - Sistema de facturación como cliente
3. **Mezcla Personal/Empresarial:** Sin separación clara
4. **Fragmentación de Nombres:** Múltiples alias sin normalizar
5. **Sin Tracking de Márgenes:** Por operación/producto

### Riesgos Identificados:

1. **Concentración Cliente:** VWR = 51% ingresos por contratos
2. **Volatilidad Ingresos:** $8k-$17k (variación 112%)
3. **Fondo Emergencia:** ~$0 (meta: $10k)
4. **Cuentas por Cobrar:** Alto volumen sin tracking claro

---

## 📈 MÉTRICAS OBJETIVO PARA V3.0

### Dashboard Principal:
- **Ciclo Conversión Efectivo:** Días CxC - Días CxP (actual: -15 días)
- **Ratio Liquidez:** Efectivo / Gastos Fijos Mensuales
- **Punto Equilibrio:** ~$8k/mes (verificar con datos limpios)
- **Concentración Cliente:** % de ingresos por cliente top 5
- **Márgenes:** Bruto, Operativo, Neto por línea de producto

### KPIs Operativos:
- Días promedio de cobro
- Días promedio de pago
- Rotación de cuentas por cobrar
- Crecimiento mensual vs año anterior
- Estacionalidad (meses altos/bajos)

---

## 🎯 PRÓXIMOS PASOS

1. ✅ **Documentar Bloque #1** (Este archivo - COMPLETADO)
2. ⏳ **Recibir respuestas Bloque #2** (T1-T5)
3. 📊 **Analizar y dar feedback Bloque #2**
4. 📋 **Enviar Bloque #3** (Cuentas Bancarias)
5. 🔄 **Repetir proceso hasta Bloque #8**
6. 🏗️ **Diseñar estructura final Excel v3.0**
7. 🚀 **Implementar y migrar datos**

---

**Última Actualización:** 12 Nov 2025 - Bloque #1 Documentado
**Siguiente Acción:** Esperar respuestas T1-T5 del usuario
