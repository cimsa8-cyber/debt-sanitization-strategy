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
- ✅ **Bloque #2 (T1-T5):** COMPLETADO - Pagos tarjetas, uso empresa/personal, 22 clientes facturados, alias, canjes
- ✅ **Bloque #3 (B1-B5):** COMPLETADO - 9 cuentas bancarias, $3.4k efectivo (12.9 días cobertura), CIMSA=cliente
- ✅ **Bloque #4 (H1-H5):** COMPLETADO - $10k deuda Hacienda, 2% mensual, $45k deuda total, sin arreglo de pago
- ✅ **Bloque #5 (E1-E5):** COMPLETADO - 1 archivo único, multi-usuario OneDrive, automatización avanzada, actualización diaria
- ⏳ **Bloque #6 (M1-M5):** PRÓXIMO - Plan de migración desde v2.0
- 📋 **Bloques #7-8:** PLANIFICADOS - Categorización, dashboards

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

## ✅ BLOQUE #2 - TARJETAS, CLIENTES TOP, ALIAS
**Estado:** COMPLETADO
**Fecha:** 12 Nov 2025

### T1. Montos de Pago Mensual de Tarjetas

**Pregunta:** ¿Cuánto pagas mensualmente a cada una de las 5 tarjetas?

**Respuesta:** ✅ **Estrategia de Pago Mínimo + 50%**

**Detalle:**
- **VISA 3519 (Personal):** Se trata de pagar TOTAL cada mes
- **VISA 9837, 6386, MC 8759, BAC 9550:** Pago típico = Mínimo × 1.5
- **Tarjeta Simán:** EXTINGUIDA el mes pasado (debería estar en $0 + intereses residuales)

**Análisis Crítico:**
- 🚨 **ALERTA:** Pagar solo 1.5x el mínimo genera deuda rotativa crónica
- Con $14,867 de deuda y pago mínimo típico ~2.5%, pagas ~$371/mes
- A 1.5x mínimo = ~$556/mes en 4 tarjetas
- Tasas BNCR/BAC: ~45-52% anual → ~$625/mes SOLO EN INTERESES
- **Conclusión:** Estás pagando $556/mes pero generando $625/mes en intereses = DEUDA CRECIENTE

**Para v3.0:**
- Dashboard con proyección de deuda a 6/12 meses
- Alerta si Pago Mensual < Intereses Generados
- Tracking de "Deuda Neta" (balance actual - pagos + cargos)

---

### T2. Uso Empresarial vs Personal por Tarjeta

**Pregunta:** ¿Qué porcentaje de cada tarjeta es uso empresarial vs personal?

**Respuesta:** ✅ **Clara Separación - 1 Personal, 4 Empresa**

**Desglose:**
1. **VISA 3519:** 0% Empresa / **100% Personal** ✅ Se declara personal
2. **VISA 9837:** **100% Empresa** / 0% Personal
3. **VISA 6386 (Alejandra):** **100% Empresa** / 0% Personal
4. **MC 8759:** **100% Empresa** / 0% Personal
5. **BAC 9550:** **100% Empresa** / 0% Personal

**Análisis Crítico:**
- ✅ **Excelente separación** - Simplifica enormemente la contabilidad
- VISA 3519 ($3,864.90): 100% deducible como préstamo/retiro personal
- Otras 4 tarjetas ($10,671.83): 100% deducible como gasto/inversión empresarial
- **IMPLICACIÓN FISCAL:** Intereses de las 4 tarjetas empresa son gasto deducible

**Para v3.0:**
- Campo "Tipo Entidad" = "Personal" para VISA 3519
- Todas las demás transacciones TC = "Empresa"
- Separar reportes: "Gastos Empresa" vs "Retiros Personales"

---

### T3. TOP 5 Clientes por Ingresos Mensuales

**Pregunta:** ¿Cuáles son los 5 clientes que más ingresos generan mensualmente?

**Respuesta:** ✅ **FACTURACIÓN REAL NOVIEMBRE 2025 (22 clientes)**

#### 🏆 TOP 5 CLIENTES - NOVIEMBRE 2025:

1. **GRUPO ACCION COMERCIAL S.A.** - $1,689.04 (17.8% del total) 👑
2. **VWR INTERNATIONAL LTDA** - $1,400.00 (14.8%)
3. **ALFIPAC (Almacén Fiscal del Pacífico)** - $761.05 (8.0%)
4. **3-102-887892 SRL** - $691.56 (7.3%)
5. **WAIPIO S.A.** - $687.27 (7.3%)

**Subtotal TOP 5:** $5,228.92 (55.2% de ingresos totales)

#### 📊 FACTURACIÓN COMPLETA - 22 CLIENTES:

| # | Cliente | Factura | Fecha | Monto USD | % Total |
|---|---------|---------|-------|-----------|---------|
| 1 | Grupo Acción Comercial S.A. | AR-002 | 01/11/25 | $1,689.04 | 17.8% |
| 2 | VWR International Ltda | AR-001 | 01/11/25 | $1,400.00 | 14.8% |
| 3 | Alfipac (Almacén Fiscal Pacífico) | AR-003 | 01/11/25 | $761.05 | 8.0% |
| 4 | 3-102-887892 SRL | AR-004 | 01/11/25 | $691.56 | 7.3% |
| 5 | Waipio S.A. | AR-005 | 01/11/25 | $687.27 | 7.3% |
| 6 | Centro Integral Oncología CIO SRL | AR-006 | 01/11/25 | $687.05 | 7.3% |
| 7 | Ortodoncia de la Cruz | AR-007 | 01/11/25 | $494.50 | 5.2% |
| 8 | Global Automotriz GACR S.A. | AR-008 | 01/11/25 | $439.61 | 4.6% |
| 9 | Solusa Consolidators | AR-009 | 01/11/25 | $378.35 | 4.0% |
| 10 | Cemso | AR-010 | 01/11/25 | $333.92 | 3.5% |
| 11 | Acacia (Asoc. CR Agencias Carga) | AR-011 | 01/11/25 | $333.35 | 3.5% |
| 12 | Rodriguez Rojas Carlos Humberto | AR-012 | 01/11/25 | $282.50 | 3.0% |
| 13 | Supply Net C.R.W.H S.A. | AR-013 | 01/11/25 | $276.85 | 2.9% |
| 14 | Operation Managment Tierra Magnifica | AR-014 | 01/11/25 | $209.06 | 2.2% |
| 15 | Gentra de Costa Rica S.A. | AR-015 | 01/11/25 | $183.63 | 1.9% |
| 16 | Sevilla Navarro Edgar | AR-016 | 01/11/25 | $169.50 | 1.8% |
| 17 | Gomez Ajoy Edgar Luis | AR-017 | 01/11/25 | $113.00 | 1.2% |
| 18 | Melendez Morales Monica | AR-018 | 01/11/25 | $113.00 | 1.2% |
| 19 | Bandogo Soluciones Tecnológicas S.A. | AR-019 | 01/11/25 | $67.80 | 0.7% |
| 20 | CPF Servicios Radiológicos S.A. | AR-020 | 01/11/25 | $56.50 | 0.6% |
| 21 | Ortodec S.A. | AR-021 | 01/11/25 | $56.50 | 0.6% |
| 22 | Perez Morales Francisco | AR-022 | 01/11/25 | $42.38 | 0.4% |

**TOTAL FACTURACIÓN NOVIEMBRE 2025:** $9,466.42

---

## 🚨 ANÁLISIS CRÍTICO EXPLOSIVO - T3

### 💣 DISCREPANCIA MASIVA CON V2.0:

**v2.0 reportó:** $17,188 ingresos en Noviembre
**FACTURACIÓN REAL:** $9,466.42
**DIFERENCIA:** -$7,721.58 (45% DE INFLACIÓN!!!)

**CONFIRMACIÓN DEFINITIVA:** El Excel v2.0 tiene duplicados MASIVOS no solo en gastos sino también en INGRESOS.

### 📈 Métricas Reales:

- **Promedio por cliente:** $430.29
- **Concentración TOP 3:** 40.7% (Grupo Acción + VWR + Alfipac)
- **Concentración TOP 5:** 55.2%
- **Diversificación:** ✅ Excelente (22 clientes activos)

### 🔄 Cambio de Liderazgo:

**ANTES pensábamos:**
- VWR = Cliente #1 con 51% concentración (RIESGO CRÍTICO)

**REALIDAD:**
- **Grupo Acción = Cliente #1** con $1,689.04 (17.8%) 👑
- VWR = Cliente #2 con $1,400.00 (14.8%)
- **Concentración distribuida:** TOP 3 = 40.7% (SALUDABLE)

### 💡 Insights Clave:

1. **Grupo Acción facturó $1,689.04** (contrato $678 + licencias $258 = $936) → ¿Diferencia de $753? Probablemente servicios adicionales/productos
2. **VWR facturó exactamente $1,400** (su contrato mensual) → Sin adicionales este mes
3. **Global Automotriz ($439.61)** está en la lista → Confirmando que SÍ se facturan los canjes
4. **Gentra solo $183.63** este mes vs contrato de $678/mes → Posible pago atrasado o parcial
5. **22 clientes facturaron** → Modelo de negocio saludablemente diversificado

### ⚠️ Alertas para V3.0:

- **Gentra subperformance:** ¿Por qué solo $183 vs $678 esperado?
- **Facturación variable:** Algunos meses pueden tener diferencias significativas
- Necesitamos tracking de "Facturación Esperada vs Real" por cliente

### 🎯 Para v3.0:

- Hoja CLIENTES_VIP con:
  - Facturación mensual esperada (contratos + licencias)
  - Facturación real mensual
  - Variación % mes a mes
  - Customer Lifetime Value (CLV)
  - Días promedio de pago por cliente
- Dashboard de concentración de riesgo (actualización automática)
- Alertas: "Cliente X no facturó este mes" o "Facturación < 50% de esperado"

---

### T4. Lista Normalizada de Alias de Clientes

**Pregunta:** ¿Cuáles son todas las variaciones de nombres que usas para cada cliente?

**Respuesta:** ✅ **Usar Sistema de Alias Existente + Expandir a Clientes**

**Referencia:** Ya existe archivo `/home/user/debt-sanitization-strategy/SISTEMA_ALIAS_CUENTAS.md`

**Sistema Actual:**
- Documenta normalización de cuentas BANCARIAS (Promerica, BNCR, tarjetas)
- Scripts disponibles:
  - `crear_hoja_alias_cuentas.py`
  - `normalizar_cuentas_universal.py`

**Alias Ya Identificados:**
- Futuropa → Proimagen (o viceversa)
- Real Clean → JDSRealClean, RealCleanJDS
- Tecnoambientes → Ambientes con Tecnología
- Start Sistemas → Sistema, SWS-Software

**Análisis Crítico:**
- ✅ Sistema robusto ya implementado para cuentas bancarias
- 🔧 Necesita EXPANSIÓN para incluir:
  - **Clientes** (22+ nombres oficiales con variaciones)
  - **Proveedores** (Intcomex, Eurocomp, TD Synex, etc.)
  - **Categorías** (normalizaciones de subcategorías)

**Para v3.0:**
- Expandir hoja **CUENTAS_ALIAS** a **ENTIDADES_ALIAS**
- Agregar columna "Tipo" (Cliente/Proveedor/Banco/Interno)
- Normalizar nombres de facturas AR-001 a AR-022 con variaciones futuras
- Script único: `normalizar_entidades_universal.py`

**Acción Pendiente:**
- Crear tabla maestra de alias de los 22 clientes
- Mapear variaciones comunes (ej: "GRUPO ACCION" vs "Grupo Acción Comercial S.A.")
- Integrar con sistema existente

---

### T5. Manejo de Transacciones de Canje/Intercambio

**Pregunta:** ¿Cómo quieres registrar las transacciones de canje con Global Automotriz, Miguel Solano y Start Sistemas?

**Respuesta:** ✅ **Sistema Mixto - Según Tipo de Relación**

**Criterio: Relación 1-a-1 con Facturación vs Palabra:**

#### ✅ REGISTRAR CON FACTURACIÓN (Opción B):
**Global Automotriz:**
- **Método:** Doble registro (Ingreso + Egreso)
- **Razón:** Relación 1-a-1, se emiten facturas formales
- **Ejemplo:**
  - Ingreso: "Servicio Mantenimiento a Global Automotriz" +$439.61 (Factura AR-008)
  - Egreso: "Canje - Servicio mecánico recibido de Global" -$439.61 (COGS)
  - **Net:** $0 (no afecta utilidad neta)
  - **Beneficio:** Refleja volumen real de operaciones, cumple obligaciones fiscales (factura legal)

#### ❌ NO REGISTRAR (Opción A):
**Miguel Solano y Start Sistemas (SWS-Software):**
- **Método:** No registrar movimientos contables
- **Razón:** Relación de palabra, sin facturación formal
- **Implementación:** Solo notas en hoja CLIENTES_VIP o sección MEMO

**Análisis Crítico:**

**Ventajas del Sistema Mixto:**
1. ✅ **Cumplimiento Fiscal:** Global Automotriz genera factura legal → debe registrarse
2. ✅ **Volumen Real:** Refleja $9,466 de facturación (no $9,026 excluyendo Global)
3. ✅ **Trazabilidad:** Auditoría puede verificar factura AR-008
4. ✅ **Simplicidad:** Miguel Solano y SWS sin factura = sin registro (menos trabajo)

**Implicaciones:**
- Global Automotriz facturó $439.61 en Nov → Genera IVA cobrado (13% = $57.15)
- Debes pagar ese IVA a Hacienda aunque no recibiste efectivo
- **IMPORTANTE:** Verificar si el "servicio recibido" de Global también tiene IVA (deducible)

**Para v3.0:**
- Campo "Es Canje" (SI/NO) para marcar transacciones de intercambio
- Filtro en reportes: "Ingresos Efectivo Real" (excluye canjes)
- Dashboard separado: "Ingresos Totales" vs "Ingresos en Efectivo"
- Alerta: "IVA por pagar en canjes: $X.XX"

**Confirmación Datos:**
- Global Automotriz AR-008: $439.61 (01/11/2025) → ✅ Registrado en facturación
- Esta transacción ya está en tu sistema de facturación
- Solo falta registrar el EGRESO correspondiente (servicio recibido)

---

## ✅ BLOQUE #3 - CUENTAS BANCARIAS Y NORMALIZACIÓN
**Estado:** COMPLETADO
**Fecha:** 12 Nov 2025

### B1. Lista Completa de Cuentas Bancarias

**Respuesta:** ✅ **9 CUENTAS BANCARIAS (5 BNCR + 4 Promerica)**

#### BNCR (5 cuentas):
1. **100-01-000-188618-3** (Colones) - ₡211.24 - NEGOCIO
2. **100-02-087-601066-4** (Dólares) - $1,087.37 - NEGOCIO
3. **200-01-087-042186-9** (Colones) - ₡28,950.50 - NEGOCIO/RESERVAS
4. **200-02-087-009589-4** (Dólares) - $0.43 - PERSONAL
5. **200-02-087-011112-1** (Dólares) - $21.84 - PERSONAL

#### PROMERICA (4 cuentas - A nombre de "ALVARO VELASCONET SOCIEDAD DE RESPONSABILIDAD LIMITADA"):
6. **10000003881708** (SINPE Colones) - ₡1,090.00 - NEGOCIO
7. **20000003881691** (Ahorros Dólares) - $0.00 - NEGOCIO
8. **30000003904229** (CC Corporativa Colones) - ₡0.00 - NEGOCIO
9. **40000003881774** (CC Corporativa Dólares) - $2,276.44 - NEGOCIO 👑

---

### B2 & B3. Saldos y Uso (12 Nov 2025 16:04)

**Respuesta:** ✅ **Incluidos en B1**

**RESUMEN:**
- **7 cuentas NEGOCIO** (77.8%)
- **2 cuentas PERSONAL** (22.2%)
- **1 cuenta RESERVAS** (cuenta compartida negocio/reservas)
- **3 cuentas en $0:** Promerica Ahorros USD, Promerica CC CRC, BNCR Personal USD 9589

---

### B4. ¿Qué es CIMSA?

**Pregunta:** ¿CIMSA es tu empresa o un intermediario separado?

**Respuesta:** ✅ **OPCIÓN B - CIMSA es un distribuidor/cliente (intermediario separado)**

"CIMSA es un distribuidor nuestro, se le factura como a cualquier otro cliente."

**Análisis Crítico:**
- Tu razón social real: **"ALVARO VELASCONET SOCIEDAD DE RESPONSABILIDAD LIMITADA"** (revelado en cuentas Promerica)
- CIMSA = Cliente externo, no tu empresa
- Se factura como cliente normal (posiblemente mayorista/distribuidor)

**Para v3.0:**
- Agregar CIMSA a la lista de clientes
- Categorizar como "Distribuidor" o "Cliente Mayorista" si hay precios especiales

---

### B5. Variaciones de Nombres en v2.0

**Pregunta:** ¿Cuáles son las variaciones con las que aparecen tus cuentas en v2.0?

**Respuesta:** ✅ **Confirmado para Promerica USD (40000003881774)**

**Variaciones Identificadas:**
- Promerica USD
- Promerica USD (40000003881774)
- Promerica USD 1774
- Promerica USD (*1774)
- Promerica 1774

**Análisis Crítico:**
- ✅ Sistema de alias existente puede manejar estas variaciones
- Necesita expansión para las 9 cuentas (especialmente las 5 de BNCR)
- Patrón común: Banco + Moneda + últimos 4 dígitos con diferentes formatos

**Para v3.0:**
- Nombre estándar BNCR: "BNCR [Moneda] (***[últimos4])" (ej: "BNCR CRC (***8618)")
- Nombre estándar Promerica: "Promerica [Moneda] (***[últimos4])" (ej: "Promerica USD (***1774)")
- Script de normalización: Expandir para cubrir las 9 cuentas

---

## 🚨 ANÁLISIS CRÍTICO EXPLOSIVO - BLOQUE #3

### 💣 CRISIS DE LIQUIDEZ DETECTADA:

**EFECTIVO TOTAL DISPONIBLE:** $3,444.54
```
BNCR:
  Colones: ₡29,161.74 (~$56.35)
  Dólares: $1,109.64
  Subtotal: $1,165.99

PROMERICA:
  Colones: ₡1,090.00 (~$2.11)
  Dólares: $2,276.44
  Subtotal: $2,278.55

TOTAL: $3,444.54
```

### 🚨 ALERTA CRÍTICA DE SUPERVIVENCIA:

```
Break-even mensual:     $8,000
Efectivo disponible:    $3,444
COBERTURA:              12.9 DÍAS (1.8 semanas)
DÉFICIT:                -$4,556
```

**¡SITUACIÓN CRÍTICA!** Tienes efectivo para menos de 2 semanas de operación.

### 📊 Concentración de Efectivo:

- **Cuenta principal:** Promerica USD 1774 = $2,276.44 (66% del total)
- **Cuenta reservas:** BNCR CRC 2186 = ₡28,950 (~$56) - NO es reserva real
- **Cuentas personales:** $22.27 (0.6%)
- **3 cuentas en $0:** Promerica Ahorros, Promerica CC CRC, BNCR 9589

### 💡 Contexto vs Cuentas por Cobrar:

```
Cuentas por Cobrar estimadas:  $9,200 - $10,866
Efectivo en banco:             $3,444
RATIO COBRO/EFECTIVO:          2.7x - 3.2x
```

**BUENA NOTICIA:** Si cobras solo 32-38% de CxC pendientes, duplicas tu efectivo disponible.

**MALA NOTICIA:** Dependes críticamente de cobros para operar día a día.

### ⚠️ Riesgos Identificados:

1. **CRÍTICO - Liquidez Ultra Baja:** 12.9 días de cobertura
2. **Alta Dependencia de CxC:** $9k+ por cobrar vs $3.4k en banco
3. **Cuenta "Reservas" Inútil:** Solo ₡28,950 (~$56) en colones
4. **Fragmentación Excesiva:** 9 cuentas para operar (complejidad innecesaria)
5. **3 Cuentas Inactivas:** $0 saldo (mantenerlas cuesta)

### 🎯 Para v3.0:

- **URGENTE:** Dashboard de liquidez con alerta si efectivo < 20 días de operación
- Proyección de flujo de caja semanal (no mensual)
- Tracking de antigüedad de CxC (0-15, 16-30, 31-60, 60+ días)
- Alertas: "Efectivo crítico: < 15 días de cobertura"
- Consolidación de cuentas: ¿Realmente necesitas 9 cuentas?

---

## 📋 BLOQUES PLANIFICADOS

## ✅ BLOQUE #4 - DEUDA HACIENDA (BOMBA FISCAL)
**Estado:** COMPLETADO
**Fecha:** 12 Nov 2025

### H1. Monto Total Adeudado a Hacienda

**Respuesta:** ✅ **₡5,286,694 (~$10,215.83 USD)**

---

### H2. Desglose por Tipo de Impuesto

**Respuesta:** ✅ **4 años de Renta + 3 meses de IVA**

**IMPUESTO DE RENTA (4 años sin pagar):**
- 2020: ₡947,987 (~$1,831.86)
- 2021: ₡1,389,119 (~$2,684.29)
- 2022: ₡1,391,192 (~$2,688.29) 👈 Año más alto
- 2023: ₡789,497 (~$1,525.60)
- **SUBTOTAL RENTA:** ₡4,517,795 (~$8,730.04)

**IVA (3 meses sin pagar):**
- Septiembre 2025: ₡478,806 (~$925.23)
- Octubre 2025: ₡244,129 (~$471.75)
- Noviembre 2025: ₡45,964 (~$88.82)
- **SUBTOTAL IVA:** ₡768,899 (~$1,485.80)

**TOTAL DEUDA HACIENDA:** ₡5,286,694 ($10,215.83)

**Análisis Crítico:**
- IVA bajó 90% de Sep a Nov (₡478k → ₡45k)
- Posible: Facturación de Nov menor, o facturas exentas de IVA
- IVA Nov esperado (13% de $9,466): ~$1,231 vs real $89 → DISCREPANCIA $1,142
- Probable: Muchas facturas exentas (licencias Microsoft, servicios) o régimen de caja

---

### H3. Cuotas Pendientes de Cada Tipo

**Respuesta:** ✅ **Documentado en H2**

- **Renta:** 4 períodos anuales completos (2020, 2021, 2022, 2023)
- **IVA:** 3 períodos mensuales (Sep, Oct, Nov 2025)

**Análisis Crítico:**
- Renta 2021 y 2022 son casi idénticas (~₡1.39M cada una)
- Renta 2023 es 43% menor que 2021/2022
- Sugiere: Negocio tuvo mejores años 2021-2022, bajó en 2023

---

### H4. Pago Mensual Acordado

**Pregunta:** ¿Tienes arreglo de pago con Hacienda?

**Respuesta:** ✅ **NO - Sin arreglo formal**

**Proceso Actual:**
- **IVA:** Contador prepara fórmula mensual (13% de facturas) → Envía al banco → **NO SE ESTÁ PAGANDO**
- **Renta:** Contador analiza ventas/gastos anuales → Crea fórmula → **NO SE ESTÁ PAGANDO**

**Análisis Crítico:**
- 🚨 **CRÍTICO:** NO hay plan de pago activo
- El "$544/mes" mencionado antes NO se está pagando realmente
- La deuda está **ACUMULÁNDOSE sin control**
- Contador prepara fórmulas pero **NO se ejecutan los pagos**
- **RIESGO:** Hacienda puede embargar cuentas, cerrar negocio, inhabilitar para licitaciones

---

### H5. Recargos e Intereses

**Pregunta:** ¿Hacienda cobra recargos/intereses?

**Respuesta:** ✅ **SÍ - 2% mensual (26.8% anual efectivo)**

**Detalle:**
- **A. SÍ:** 2% mensual de recargo
- **B. SÍ:** Se agregan automáticamente al saldo
- **C. NO:** Aún sin resolver por parte de Hacienda (interpretación: NO hay acuerdo formal)

**Cálculo de Intereses:**
```
Capital actual: ₡5,286,694 ($10,215.83)
Interés mensual (2%): ₡105,734 (~$204.32/mes)
Interés anual (26.8%): ₡1,268,807 (~$2,451.80/año)
```

**Proyección sin pagos:**
```
Hoy (12 Nov 2025):      $10,215.83
6 meses (May 2026):     $11,479.77 (+$1,264)
12 meses (Nov 2026):    $12,951.85 (+$2,736)
24 meses (Nov 2027):    $16,380.67 (+$6,165)
```

**Análisis Crítico:**
- 🔥 **INTERÉS USURARIO:** 26.8% anual efectivo
- En 1 año la deuda crece $2,736 SOLO en intereses
- Si no pagas, en 24 meses deberás $16,380 (60% más)
- **URGENCIA MÁXIMA:** Necesitas arreglo de pago YA

---

## 🚨 ANÁLISIS CRÍTICO DEVASTADOR - BLOQUE #4

### 💣 BOMBA DE TIEMPO FISCAL:

**DEUDA TOTAL CONSOLIDADA:**
```
Tarjetas Crédito:    $16,536.00
Nissan Frontier:     $18,680.75
Hacienda:            $10,215.83 👈 NUEVA BOMBA
────────────────────────────────
TOTAL DEUDA:         $45,432.58
```

**Contexto Brutal:**
- Efectivo disponible: $3,444.54
- Deuda total: $45,432.58
- **RATIO: 13.2x** (debes 13 veces lo que tienes en banco)

### 💰 PAGOS MENSUALES OBLIGATORIOS MÍNIMOS:

```
TC (1.5x mínimo):              $556.00
Nissan Frontier:               $800.00
Hacienda (solo intereses):     $204.32 👈 NUEVO
────────────────────────────────────────
TOTAL MÍNIMO MENSUAL:          $1,560.32
```

**Análisis:**
- Break-even: $8,000/mes
- Pagos deuda: $1,560/mes (19.5% del break-even)
- **MARGEN OPERATIVO DISPONIBLE:** $6,440/mes
- Facturación Nov: $9,466 → Margen real: ~$7,906/mes
- **CONCLUSIÓN:** Técnicamente manejable SI cobras y mantienes facturación

### ⚠️ ALERTA ROJA MÁXIMA - IVA NO PAGADO:

**IVA es dinero que YA COBRASTE a clientes:**
```
Sep: ₡478,806 (~$925) 👈 Cobraste en facturas
Oct: ₡244,129 (~$472) 👈 Cobraste en facturas
Nov: ₡45,964  (~$89)  👈 Cobraste en facturas
TOTAL: ₡768,899 (~$1,486) NO pagado a Hacienda
```

**Esto es GRAVÍSIMO porque:**
1. No es "tu" dinero, es del gobierno temporal en tu poder
2. Hacienda puede EMBARGAR cuentas bancarias sin aviso
3. Puede INHABILITAR para participar en licitaciones/contratos
4. Puede CERRAR el negocio administrativamente
5. Delito fiscal si se prueba intencionalidad

### 🔍 DISCREPANCIA IVA NOVIEMBRE:

```
Facturación Nov 2025:    $9,466.42
IVA 13% esperado:        $1,230.63
IVA reportado Nov:       $88.82
DIFERENCIA:              -$1,141.81 (93% faltante!)
```

**Posibles explicaciones:**
1. Muchas facturas exentas de IVA (Microsoft 365, servicios)
2. Régimen de caja: Solo se declara IVA de facturas COBRADAS
3. Facturas de Nov aún pendientes de cobro
4. Error en cálculo del contador

**Acción requerida:** Verificar con contador qué % de facturación está exenta de IVA

### 🎯 PRIORIDAD ABSOLUTA PARA V3.0:

**1. Dashboard IVA:**
- IVA Cobrado este mes
- IVA Pagado a Hacienda
- IVA Pendiente de pago (acumulado)
- Alerta roja: "IVA vencido: $X"

**2. Proyección Deuda Hacienda:**
- Gráfico crecimiento exponencial (2% mensual)
- Simulador de pagos: "¿Cuánto debo pagar mensualmente?"
- Escenarios: Pagar solo intereses vs amortizar capital

**3. Tracking de Impuestos:**
- Renta: Provisión mensual (1/12 de estimado anual)
- IVA: Separación automática del 13% en cada factura
- Alerta: "Provisión insuficiente para pagar Renta 2025"

---

## ✅ BLOQUE #5 - ESTRUCTURA EXCEL V3.0
**Estado:** COMPLETADO
**Fecha:** 12 Nov 2025

### E1. Archivo Único o Múltiples Workbooks

**Pregunta:** ¿Prefieres 1 archivo único o múltiples archivos separados?

**Respuesta:** ✅ **OPCIÓN A - 1 ARCHIVO ÚNICO con múltiples pestañas**

**Especificaciones:**
- Archivo único: `AlvaroVelasco_Finanzas_v3.0.xlsx`
- Múltiples pestañas de trabajo
- ✅ Todo en un lugar
- ✅ Fácil de respaldar
- **IMPORTANTE:** Incluir 1 o varias pestañas para uso PERSONAL (separación empresa/personal)

**Análisis Crítico:**
- ✅ Decisión correcta para tu caso: Facilita respaldos y sincronización OneDrive
- Con 15+ hojas planificadas, el archivo será ~5-10 MB (manejable)
- Separación personal = clave para contabilidad limpia
- Sugerencia: Agrupar pestañas por color (Operativas=azul, Pasivos=rojo, Dashboards=verde, Personal=gris)

**Para v3.0:**
- Estructura de pestañas con índice de navegación
- Hipervínculos entre hojas relacionadas
- Pestaña PERSONAL separada con estructura simplificada
- Protección de hojas: Solo campos editables desbloqueados

---

### E2. Hojas Más Críticas

**Pregunta:** ¿Cuáles son las hojas MÁS CRÍTICAS (TOP 5)?

**Respuesta:** ✅ **Priorización Clara + Inclusión Total**

**TOP 5 por prioridad:**
1. **TRANSACCIONES** (fuente de verdad)
2. **EFECTIVO** (saldos bancarios)
3. **CUENTAS_POR_COBRAR** (antigüedad CxC)
4. **CUENTAS_POR_PAGAR** (proveedores)
5. **DASHBOARD** (resumen ejecutivo)

**IMPORTANTE:** Usuario indica "todas las demás también son importantes, no me gustaría que quedaran fuera"

**Análisis Crítico:**
- Priorización alineada con operación diaria: Transacciones → Efectivo → Cobros → Pagos → Dashboard
- IVA_CONTROL no está en TOP 5 pero es CRÍTICA por situación fiscal
- Orden de implementación sugerido:
  1. **FASE 1 (MVP):** TRANSACCIONES + EFECTIVO + DASHBOARD
  2. **FASE 2 (Operación):** CUENTAS_POR_COBRAR + CUENTAS_POR_PAGAR + IVA_CONTROL
  3. **FASE 3 (Gestión):** PASIVOS + UTILIDADES_MENSUALES + CLIENTES_VIP
  4. **FASE 4 (Estrategia):** OPERACIONES + PROYECCIONES + PRESUPUESTO + PERSONAL

**Para v3.0:**
- Implementar TODAS las 15+ hojas
- Priorizar desarrollo según TOP 5
- IVA_CONTROL como hoja crítica (dado contexto fiscal)
- PERSONAL como hoja independiente

---

### E3. Nivel de Automatización

**Pregunta:** ¿Cuánta automatización quieres?

**Respuesta:** ✅ **OPCIÓN C - AVANZADO**

**Funcionalidades requeridas:**
- ✅ Macros/VBA para procesos repetitivos
- ✅ Scripts Python para análisis profundo
- ✅ Importación automática de datos
- ✅ Reportes PDF automatizados

**Análisis Crítico:**
- 🎯 **Nivel correcto** para frecuencia diaria de actualización
- VBA necesario para: Botones de conciliación, importación datos, limpieza duplicados
- Python para: Análisis v2.0, detección duplicados, reportes avanzados, proyecciones
- Importación automática: Extractos bancarios (CSV), facturas (XML Hacienda)
- Reportes PDF: Dashboard semanal, P&L mensual, IVA mensual para contador

**Implementaciones específicas:**

**VBA Macros necesarios:**
1. **BotónConciliarBanco:** Importa CSV de banco → Compara con TRANSACCIONES → Marca conciliadas
2. **BotónDetectarDuplicados:** Escanea TRANSACCIONES → Resalta duplicados potenciales
3. **BotónGenerarReportePDF:** Captura DASHBOARD → Exporta PDF con fecha
4. **BotónActualizarTodo:** Refresca todas las tablas dinámicas y cálculos
5. **BotónConciliarIVA:** Calcula IVA cobrado vs pagado → Genera reporte mensual

**Python Scripts necesarios:**
1. **analizar_v2_y_migrar.py:** Limpia duplicados de v2.0 → Importa a v3.0
2. **importar_xml_hacienda.py:** Lee facturas XML → Extrae datos → Agrega a TRANSACCIONES
3. **proyectar_flujo_caja.py:** Analiza histórico → Proyecta 6 meses → Grafica
4. **analizar_margenes.py:** Calcula margen por operación, cliente, producto
5. **reporte_ejecutivo.py:** Genera PDF con métricas clave

**Formato de reportes PDF:**
- Dashboard semanal (lunes, resumen última semana)
- P&L mensual (día 5 de cada mes)
- IVA mensual (día 10, antes de vencimiento 15)
- Proyecciones trimestrales

**Para v3.0:**
- Botones visibles en hoja DASHBOARD
- Scripts Python en carpeta `/scripts/`
- Manual de uso de cada macro en pestaña AYUDA
- Logs de ejecución de macros

---

### E4. Frecuencia de Actualización

**Pregunta:** ¿Con qué frecuencia actualizarás el Excel?

**Respuesta:** ✅ **OPCIÓN A - DIARIA + Conciliación SEMANAL**

**Detalle:**
- **Registro de transacciones:** DIARIO (cada día)
- **Conciliación bancaria:** SEMANAL (con extractos)

**Análisis Crítico:**
- 🚨 **Actualización diaria = Diseño EFICIENTE crítico**
- Tiempo estimado actualización diaria: 10-15 minutos máximo
- Conciliación semanal: 30-45 minutos (viernes o lunes)
- Necesita formularios de entrada rápida
- Validaciones automáticas para evitar errores

**Flujo de trabajo diario:**
```
9:00 AM - Abrir Excel v3.0
         ↓
9:02 AM - Ir a hoja TRANSACCIONES
         ↓
9:03 AM - Agregar transacciones del día anterior (3-5 transacciones típicas)
         ↓
9:05 AM - Verificar alertas en DASHBOARD
         ↓
9:08 AM - Revisar CUENTAS_POR_COBRAR (¿qué cobrar hoy?)
         ↓
9:10 AM - Revisar CUENTAS_POR_PAGAR (¿qué pagar hoy?)
         ↓
9:12 AM - Cerrar y sincronizar OneDrive
```

**Flujo de conciliación semanal:**
```
Viernes 4:00 PM - Descargar extractos bancarios (9 cuentas)
                 ↓
4:05 PM - Ejecutar macro "BotónConciliarBanco"
         ↓
4:10 PM - Revisar transacciones no conciliadas (investigar)
         ↓
4:20 PM - Ajustar/corregir transacciones
         ↓
4:30 PM - Verificar saldos EFECTIVO vs extractos
         ↓
4:40 PM - Generar reporte semanal PDF
         ↓
4:45 PM - Enviar PDF a contador (si es fin de mes)
```

**Para v3.0:**
- Formulario de entrada rápida (UserForm VBA)
- Atajos de teclado para acciones comunes
- Validación en tiempo real (dropdowns, alertas)
- Botón "Conciliación Semanal" con wizard paso a paso
- Timer: "Última actualización hace X días" (alerta si >3 días)

---

### E5. Versión Móvil / Acceso Compartido

**Pregunta:** ¿Necesitas acceso móvil o compartir con otros?

**Respuesta:** ✅ **Excel en PC + Compartir OneDrive (Multi-usuario)**

**Usuarios y permisos:**

**1. ÁLVARO (Propietario):**
- Acceso: TOTAL (lectura + escritura + configuración)
- Dispositivo: PC (Excel Desktop)
- Actualización: Diaria
- Responsabilidad: Ingresar transacciones, tomar decisiones

**2. CONTADOR (Solo lectura):**
- Acceso: LECTURA únicamente
- Compartir: OneDrive
- Frecuencia: Mensual (al cierre)
- Responsabilidad: Revisar P&L, IVA, Renta para declaraciones

**3. ASISTENTE (Lectura + Escritura):**
- Acceso: LECTURA + ESCRITURA (hojas específicas)
- Compartir: OneDrive
- Frecuencia: Diaria (apoyo en registro)
- Responsabilidad: Registrar transacciones, conciliar bancos, actualizar CxC/CxP

**CRÍTICO - MANUAL DE USO:**
- ✅ Celdas con NOTAS adjuntas
- ✅ Explicación de qué hace cada celda
- ✅ Instrucciones de qué debe hacer el usuario
- ✅ Formato: Comentarios de Excel (botón derecho → Insertar comentario)

**Análisis Crítico:**
- 🚨 **Multi-usuario = Riesgo de conflictos** (2 personas editando simultáneamente)
- OneDrive tiene sincronización automática pero puede causar duplicados
- Necesita PROTECCIÓN DE HOJAS con contraseña
- Solo celdas de entrada desbloqueadas (coloreadas en amarillo)
- Fórmulas y tablas dinámicas bloqueadas

**Estrategia de protección:**

**Hojas 100% protegidas (solo lectura para asistente/contador):**
- DASHBOARD
- UTILIDADES_MENSUALES
- PROYECCIONES
- PRESUPUESTO

**Hojas parcialmente protegidas (campos editables para asistente):**
- TRANSACCIONES: Campos A-T desbloqueados, columnas de fórmulas bloqueadas
- EFECTIVO: Solo "Saldo Inicial" editable
- CUENTAS_POR_COBRAR: Campo "Fecha Cobrado" editable
- CUENTAS_POR_PAGAR: Campo "Fecha Pagado" editable
- IVA_CONTROL: Solo "IVA Pagado" editable

**Hojas personales (100% bloqueadas para todos excepto propietario):**
- PERSONAL
- PASIVOS (contiene info sensible de deudas)

**Sistema de notas/manual:**
```
Ejemplo de nota en celda B2 (TRANSACCIONES - Tipo):
┌─────────────────────────────────────────┐
│ TIPO DE TRANSACCIÓN                     │
│                                         │
│ Selecciona del dropdown:                │
│ • Ingreso: Dinero que ENTRA             │
│ • Egreso: Dinero que SALE               │
│ • Transferencia: Entre cuentas propias  │
│ • Apertura: Saldo inicial               │
│                                         │
│ ⚠️ Transferencias NO afectan P&L        │
└─────────────────────────────────────────┘
```

**Para v3.0:**
- Pestaña "AYUDA" con manual completo
- Comentarios en TODAS las celdas editables
- Color amarillo = editable, blanco = solo lectura
- Botón "Modo Asistente" que oculta hojas sensibles
- Registro de cambios: Quién editó qué y cuándo (VBA log)
- Validación: Si Asistente intenta editar celda bloqueada → Mensaje explicativo

---

## 🚨 ANÁLISIS CRÍTICO - BLOQUE #5

### 📋 ESPECIFICACIONES FINALES V3.0:

**ARQUITECTURA:**
- ✅ 1 archivo único: `AlvaroVelasco_Finanzas_v3.0.xlsx`
- ✅ 15+ pestañas (incluye PERSONAL separada)
- ✅ Tamaño estimado: 5-10 MB
- ✅ Almacenamiento: OneDrive (sincronización automática)

**USUARIOS:**
- 👤 Álvaro (Propietario): Control total
- 👤 Asistente: Lectura + Escritura en hojas operativas
- 👤 Contador: Solo lectura (mensual)

**AUTOMATIZACIÓN:**
- 🤖 VBA: 5 macros principales (conciliación, duplicados, reportes, actualización, IVA)
- 🐍 Python: 5 scripts (migración, XML, proyecciones, márgenes, reportes)
- 📄 PDF: 4 tipos de reportes automatizados

**FRECUENCIA:**
- 📅 Actualización: DIARIA (10-15 min)
- 🏦 Conciliación: SEMANAL (30-45 min)
- 📊 Reportes: Automáticos según calendario

**USABILIDAD:**
- 📝 Manual inline con notas en celdas
- 🎨 Códigos de color (amarillo=editable, blanco=protegido)
- 🔒 Protección de hojas con permisos granulares
- 📚 Pestaña AYUDA con documentación completa

### 🎯 PRIORIDADES DE IMPLEMENTACIÓN:

**FASE 1 - MVP (Mínimo Viable):**
1. TRANSACCIONES (con formulario de entrada)
2. EFECTIVO (con 9 cuentas bancarias)
3. DASHBOARD (métricas básicas)
4. Manual de uso en celdas

**FASE 2 - Operación Crítica:**
5. CUENTAS_POR_COBRAR (con antigüedad)
6. CUENTAS_POR_PAGAR (con vencimientos)
7. IVA_CONTROL (urgente por situación fiscal)
8. Macro de conciliación bancaria

**FASE 3 - Gestión de Deuda:**
9. PASIVOS (TC, Nissan, Hacienda con proyecciones)
10. UTILIDADES_MENSUALES (P&L automático)
11. CLIENTES_VIP (CLV, contratos)
12. Script Python migración v2.0

**FASE 4 - Estrategia y Análisis:**
13. OPERACIONES (margen por venta)
14. PROYECCIONES (flujo de caja 6 meses)
15. PRESUPUESTO (vs real)
16. PERSONAL (gastos personales)
17. Reportes PDF automatizados

### ⚠️ RIESGOS Y MITIGACIONES:

**RIESGO 1: Conflictos multi-usuario**
- Mitigación: OneDrive sincroniza cambios, pero entrenar a asistente en "Guardar cada 5 min"
- Plan B: Si hay conflictos frecuentes, considerar Excel Online en lugar de Desktop

**RIESGO 2: Actualización diaria no sostenible**
- Mitigación: Formulario de entrada ULTRA rápido (<2 min por transacción)
- Plan B: Si fallas >3 días, macro detecta y alerta

**RIESGO 3: Complejidad abruma a asistente**
- Mitigación: Manual detallado + sesión de capacitación 2 horas
- Plan B: "Modo Simple" con solo hojas esenciales visibles

**RIESGO 4: Archivo corrupto/perdido**
- Mitigación: OneDrive mantiene versiones (recuperación hasta 30 días)
- Plan B: Backup semanal manual a carpeta local (macro automático viernes)

---

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

### 💣 DESCUBRIMIENTO EXPLOSIVO - BLOQUE #2:

**DUPLICADOS MASIVOS EN INGRESOS:**
- v2.0 reportó: $17,188 ingresos en Noviembre
- **FACTURACIÓN REAL:** $9,466.42
- **DIFERENCIA:** -$7,721.58 (45% DE INFLACIÓN!!!)
- **Conclusión:** v2.0 duplica TANTO ingresos como gastos

**RECÁLCULO DE SITUACIÓN REAL NOVIEMBRE:**
- Ingresos reales: $9,466.42 (no $17,188)
- Gastos reales estimados: ~$6,000-$8,000 (no $24,422)
- **Utilidad real estimada:** +$1,500 a +$3,500 (NO -$7,234 como mostraba v2.0)
- **CONFIRMADO:** El negocio SÍ es rentable

### Datos Financieros Confirmados:

**Deuda Total:** $45,432.58
- Tarjetas Crédito: $16,536 USD equivalente
  - VISA 3519 (Personal): $3,864.90 → Pago TOTAL mensual
  - VISA 9837 (Empresa): $3,299.01 → Pago 1.5x mínimo (~$123/mes)
  - VISA 6386 (Empresa): $5,195.07 → Pago 1.5x mínimo (~$195/mes)
  - MC 8759 (Empresa): ₡863,830 → Pago 1.5x mínimo (~₡32k/mes)
  - BAC 9550 (Empresa): $2,508.75 → Pago 1.5x mínimo (~$94/mes)
  - Tarjeta Simán: EXTINGUIDA (nov 2025)
- 🚨 **ALERTA TC:** Pagos 1.5x mínimo (~$556/mes) < Intereses (~$625/mes) = DEUDA CRECIENTE
- Nissan Frontier: $18,680.75 saldo, $800/mes
- Hacienda: $10,215.83 (₡5,286,694)
  - Renta 2020-2023: $8,730.04 (4 años sin pagar)
  - IVA Sep-Nov 2025: $1,485.80 (3 meses sin pagar)
  - Intereses: 2% mensual (26.8% anual) = $204.32/mes
  - 🔥 **SIN ARREGLO DE PAGO:** Deuda creciendo sin control

**Facturación Real - Noviembre 2025:**
- **22 clientes activos** facturaron $9,466.42
- **Cliente #1:** Grupo Acción ($1,689.04 = 17.8%) 👑
- **Cliente #2:** VWR ($1,400.00 = 14.8%)
- Concentración TOP 3: 40.7% (saludable, no 51% crítico)
- Concentración TOP 5: 55.2%
- Promedio por cliente: $430.29

**Flujo Operativo:**
- Ingresos reales: ~$9,466/mes (Noviembre)
- Break-even: ~$8k/mes
- 85% ventas a crédito (15-30 días)
- Paga proveedores en 30 días
- Ciclo de conversión: -15 días (favorable)

**Efectivo en Bancos (12 Nov 2025):**
- 9 cuentas totales (5 BNCR + 4 Promerica)
- Total efectivo: $3,444.54 USD equivalente
- Razón social: "Alvaro Velasconet SRL"
- 🚨 CRÍTICO: Solo 12.9 días de cobertura operativa

**Cuentas por Cobrar:**
- Estimado: $9,200-$10,866
- Ratio CxC/Efectivo: 2.7x - 3.2x (alta dependencia de cobros)

**Proveedores Principales:**
- Intcomex: $5k crédito
- Eurocomp: $4k
- CompuEconómicos: $5k
- TD Synex, ICD Soft

**Modelo de Negocio:**
- Intermediación SIN inventario
- 22+ clientes activos (diversificado)
- 45% Contratos Mantenimiento
- 20% Licencias Microsoft
- 15% Productos
- 15% Servicios
- 5% Cloud Services

**Canjes:**
- Global Automotriz: Registrar (factura AR-008: $439.61)
- Miguel Solano: NO registrar (palabra)
- Start Sistemas (SWS): NO registrar (palabra)

### Problemas Confirmados de v2.0:

1. **Duplicados MASIVOS:**
   - Ingresos inflados +81% ($7,721 duplicados)
   - Gastos inflados +300% ($18,310 duplicados)
   - Totales: ~$26,000+ en duplicados
2. **Categorizaciones Incorrectas:**
   - Transferencias internas como ingresos
   - Pagos completos TC como "intereses"
   - Sistema de facturación como cliente
3. **Mezcla Personal/Empresarial:** Sin separación clara (ahora: 1 tarjeta personal, 4 empresa)
4. **Fragmentación de Nombres:** Múltiples alias sin normalizar
5. **Sin Tracking de Márgenes:** Por operación/producto

### Riesgos Identificados:

1. **🔴 CRÍTICO - Bomba Fiscal Hacienda:** $10k deuda, 2% mensual, sin arreglo de pago, riesgo de embargo
2. **🔴 CRÍTICO - Crisis de Liquidez:** Solo 12.9 días de efectivo (meta: 30+ días)
3. **🔴 CRÍTICO - Deuda TC Creciente:** Pagos ($556/mes) < Intereses ($625/mes)
4. **🔴 CRÍTICO - IVA No Pagado:** $1,486 cobrado a clientes pero no pagado a Hacienda (delito fiscal)
5. **🟠 ALTO - Dependencia CxC:** $9k+ por cobrar vs $3.4k efectivo (ratio 2.7x-3.2x)
6. **🟠 ALTO - Ratio Deuda/Efectivo:** 13.2x (debes 13 veces lo que tienes)
7. **🟡 MEDIO - Concentración Cliente:** TOP 2 = 32.6% (mejorado vs 51%)
8. **🟡 MEDIO - Volatilidad Ingresos:** Verificar con más meses limpios
9. **🟢 BAJO - Fondo Emergencia:** Meta $10k (actual: $3.4k = 34%)

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
