# 🏦 SISTEMA EXCEL FINANCIERO COMPLETO - PLAN MAESTRO
**AlvaroVelasco.Net SRL - Gestión Financiera Inteligente**

**Fecha creación:** 07/11/2025 09:00
**Versión:** 1.0
**Objetivo:** Control total finanzas empresa/personal + Sanitización deuda + Ahorro vivienda 2 años

---

## 🎯 OBJETIVOS DEL SISTEMA

### **MISIÓN PRINCIPAL:**
Transformar crisis financiera actual en estabilidad sostenible mediante control diario, presupuestos estrictos, sanitización de deuda y ahorro estratégico.

### **OBJETIVOS ESPECÍFICOS:**

**1. CONTROL OPERATIVO (Inmediato)**
- ✅ Ver efectivo disponible HOY en 5 segundos
- ✅ Proyectar si puedo pagar gastos del mes
- ✅ Identificar clientes morosos urgentes
- ✅ Evitar sobregiros y cheques rechazados
- ✅ Separación clara empresa/personal

**2. PRESUPUESTOS (Crítico)**
- ✅ Presupuesto empresa por categoría
- ✅ Presupuesto personal Álvaro
- ✅ Alertas automáticas al exceder
- ✅ Comparación real vs presupuesto mensual
- ✅ Límites estrictos por categoría

**3. SANITIZACIÓN DEUDA (Estratégico)**
- ✅ Plan pago tarjetas crédito 4 BNCR vencidas ($13,295)
- ✅ Plan pago A/P vencido ($454)
- ✅ Regularización IVA vencido ($534)
- ✅ Negociación Hacienda ISR ($9,266)
- ✅ Estrategia pago Nissan ($19,198)

**4. AHORRO VIVIENDA (2 años)**
- ✅ Meta: $40,000 - $50,000 en 24 meses
- ✅ Ahorro mensual requerido: $1,667 - $2,083
- ✅ Tracking mensual progreso
- ✅ Ajustes dinámicos según flujo caja

**5. ANÁLISIS INTELIGENTE**
- ✅ Gráficos comportamiento histórico
- ✅ Flujo de caja proyectado 90 días
- ✅ KPIs críticos (ratios, tendencias)
- ✅ Análisis categorías gasto
- ✅ Dashboard Power BI ejecutivo

---

## 🏗️ ARQUITECTURA DEL SISTEMA

### **COMPONENTE 1: ARCHIVOS EXCEL MAESTROS**

**A) AlvaroVelascoNet_EMPRESA.xlsx** (Archivo principal empresa)
- 15 pestañas especializadas
- Fórmulas Office 365 avanzadas
- Conexión Power Query bancos
- Sincronización OneDrive automática

**B) AlvaroVelasco_PERSONAL.xlsx** (Archivo personal)
- 8 pestañas esenciales
- Control salario y gastos personales
- Separación estricta empresa/personal

### **COMPONENTE 2: POWER BI DASHBOARDS**

**Dashboard 1: Executive Summary**
- KPIs tiempo real
- Alertas críticas
- Tendencias principales

**Dashboard 2: Cash Flow**
- Proyección 90 días
- Entradas vs salidas
- Puntos críticos

**Dashboard 3: Debt Sanitization**
- Progreso pago deuda
- Timeline visual
- Savings goals

### **COMPONENTE 3: POWER AUTOMATE (Opcional)**

**Automatizaciones:**
- Alertas email cuando efectivo < $2,000
- Recordatorios pago facturas vencimiento
- Backup automático archivos Excel
- Sincronización con apps bancarias (futuro)

---

## 📁 ARCHIVO EMPRESA: ESTRUCTURA DETALLADA

### **ARCHIVO: AlvaroVelascoNet_EMPRESA.xlsx**

---

### **PESTAÑA 1: 📊 DASHBOARD EJECUTIVO**

**Propósito:** Vista general 360° en una pantalla

**Diseño visual:**
```
┌─────────────────────────────────────────────────────────────┐
│  ALVAROVELASCO.NET SRL - Financial Command Center           │
│  Actualizado: 07/11/2025 09:00                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  💰 EFECTIVO HOY                                            │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐  │
│  │ $4,302.10     │  │ Ahorros       │  │ Total Liquid  │  │
│  │ Operativo     │  │ $8,053.97     │  │ $12,356.07    │  │
│  └───────────────┘  └───────────────┘  └───────────────┘  │
│                                                             │
│  📈 RECURSOS vs DEUDA                                       │
│  [████████░░░░░░░░░░] 45.1%                                │
│  Recursos: $23,222  |  Deuda: $51,484  |  Gap: -$28,261   │
│                                                             │
│  ⚠️ ALERTAS CRÍTICAS                                        │
│  🔴 Efectivo solo cubre 1.5 meses gastos (45 días)         │
│  🔴 4 TC BNCR vencidas: $13,295 - NEGOCIAR URGENTE          │
│  🔴 IVA vencido $534 - Multas creciendo                     │
│  🟡 A/R Top 2: $4,489 (41%) - Cobrar en 48h                │
│                                                             │
│  💳 TARJETAS CRÉDITO                                        │
│  Total: $16,383  |  Vencido: $13,295 (81%)                 │
│  [Gráfico circular por tarjeta]                            │
│                                                             │
│  📅 PRÓXIMOS 7 DÍAS                                         │
│  08/11  Cobrar VWR $2,800        ┃ Proyectado              │
│  10/11  Pagar IVA $534           ┃ Compromiso              │
│  10/11  Pagar Intcomex $410      ┃ Vencido                 │
│  10/11  Nissan $800              ┃ Mensual                 │
│  15/11  Salario quincenal $500   ┃ Nómina                  │
│                                                             │
│  📊 GRÁFICOS RÁPIDOS                                        │
│  [Efectivo últimos 30 días - línea]                        │
│  [Gastos por categoría - barras]                           │
│  [A/R aging - embudo]                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Celdas clave:**
- `B2` = Efectivo total HOY (=SUMA(Efectivo!Total))
- `B3` = Ahorros total (=SUMA(Ahorros!Total))
- `B5` = Recursos total (=B2+B3+AR!Total)
- `B6` = Deuda total (=TC!Total+AP!Total+IVA!Total+...)
- `B7` = Déficit (=B5-B6)
- `B9` = Meses cobertura (=B2/GastosFijos!TotalMensual)
- `B10` = Alerta efectivo (=SI(B9<2,"🔴 CRÍTICO","✅ OK"))

**Formato condicional:**
- Efectivo < $3,000 → Rojo
- Efectivo $3,000-$5,000 → Amarillo
- Efectivo > $5,000 → Verde
- Meses cobertura < 1.5 → Rojo crítico

---

### **PESTAÑA 2: 💵 EFECTIVO (Control diario)**

**Propósito:** Registro transacciones diarias + saldos actuales

**Estructura tabla:**
```
| Fecha      | Banco          | Cuenta    | Concepto      | Cat    | Entrada | Salida | Balance | Notas |
|------------|----------------|-----------|---------------|--------|---------|--------|---------|-------|
| 07/11/2025 | Promerica USD  | 3881774   | Saldo Inicial | -      | -       | -      | 2999.24 | Real  |
| 07/11/2025 | BNCR USD       | 601066-4  | Saldo Inicial | -      | -       | -      | 1240.87 | Real  |
| 07/11/2025 | BNCR CRC       | 188618-3  | Saldo Inicial | -      | -       | -      | 59.84   | Real  |
| 07/11/2025 | Promerica CRC  | 3881708   | Saldo Inicial | -      | -       | -      | 2.15    | Real  |
| 07/11/2025 | BNCR CRC       | 188618-3  | Transfer PQ   | Veh    | -       | 59.17  | 0.67    | ₡30k  |
| 07/11/2025 | Promerica USD  | 3881774   | Apple One     | Soft   | -       | 16.85  | 2982.39 | Mens  |
| 08/11/2025 | [Nueva fila]   |           |               |        |         |        |         |       |
```

**Fórmulas clave:**
- Balance = Fila anterior + Entrada - Salida
- Total Efectivo = SUMA(Últimas filas cada banco)
- Conversión CRC: `=Monto_CRC/507` (celda TC actualizable)

**Validación datos:**
- Banco: Lista desplegable (Promerica USD, BNCR USD, BNCR CRC, Promerica CRC)
- Categoría: Lista desplegable (Nómina, CCSS, ICE, Soft, Veh, Proveedores, Clientes, Otros)

**Tabla resumen (lado derecho):**
```
RESUMEN EFECTIVO HOY:
Promerica USD:    $2,982.39
BNCR USD:         $1,240.87
BNCR CRC:         $0.67
Promerica CRC:    $2.15
──────────────────────────
TOTAL USD:        $4,226.08
```

---

### **PESTAÑA 3: 💰 AHORROS**

**Propósito:** Control 4 cuentas ahorro BNCR empresa

**Estructura:**
```
| Cuenta      | Descripción          | Saldo Inicial | Depósitos | Retiros | Saldo Actual | Meta      | % Meta |
|-------------|----------------------|---------------|-----------|---------|--------------|-----------|--------|
| 1002335826  | Matrimonio           | 1006.06       | 0.00      | 0.00    | 1006.06      | 2000.00   | 50%    |
| 1002273441  | Impuestos Municip    | 2263.15       | 0.00      | 0.00    | 2263.15      | 3000.00   | 75%    |
| 1002388223  | Black Friday         | 225.43        | 0.00      | 0.00    | 225.43       | 1000.00   | 23%    |
| 17000002201 | Vehículo Nuevo       | 4559.33       | 0.00      | 0.00    | 4559.33      | 10000.00  | 46%    |
|-------------|----------------------|---------------|-----------|---------|--------------|-----------|--------|
| TOTAL       |                      | 8053.97       | 0.00      | 0.00    | 8053.97      | 16000.00  | 50%    |
```

**Columnas adicionales:**
- Fecha último movimiento
- Tipo movimiento (Depósito/Retiro/Transfer)
- Propósito específico
- Disponible emergencia (Sí/No)

**Gráfico:**
- Barra apilada: Progreso hacia metas individuales
- Pie: Distribución ahorros por propósito

**Alertas:**
- Si Saldo < Meta y hace +60 días sin depósito → ⚠️ Reactivar ahorro
- Disponible emergencia: Sumar solo cuentas marcadas "Sí"

---

### **PESTAÑA 4: 🏦 A/R (Cuentas por Cobrar)**

**Propósito:** Gestión cobranza 26 clientes

**Tabla principal:**
```
| Cliente                  | Monto    | Fecha Fact | Días Venc | Días Mora | Prior  | Última Gestión | Próx Acción | Estado   |
|--------------------------|----------|------------|-----------|-----------|--------|----------------|-------------|----------|
| VWR INTERNATIONAL        | 2800.00  | 09/10/2025 | 30        | 30        | CRIT   | 05/11 Email    | 08/11 Call  | VENCIDO  |
| GRUPO ACCION COMERCIAL   | 1689.04  | 11/10/2025 | 30        | 28        | CRIT   | 06/11 Email    | 08/11 Call  | VENCIDO  |
| ALFIPAC                  | 761.05   | 16/10/2025 | 30        | 23        | ALTA   | Pendiente      | 09/11 Email | MORA     |
| 3-102-887892 SRL         | 691.56   | 18/10/2025 | 30        | 21        | ALTA   | Pendiente      | 10/11 Email | MORA     |
| ... (22 clientes más)    |          |            |           |           |        |                |             |          |
|--------------------------|----------|------------|-----------|-----------|--------|----------------|-------------|----------|
| TOTAL A/R                | 10866.42 |            |           |           |        |                |             |          |
```

**Columnas calculadas:**
- Días Vencimiento = Fecha Fact + 30
- Días Mora = HOY - Fecha Vencimiento (si >0)
- Estado = SI(Días Mora > 30, "VENCIDO", SI(Días Mora > 0, "MORA", "VIGENTE"))
- Prioridad = Basado en monto + días mora

**Resumen por prioridad:**
```
CRÍTICA (0-48h):   $4,489.04  (41.3%)  - 2 clientes
ALTA (1 semana):   $2,826.93  (26.0%)  - 4 clientes
MEDIA (2 semanas): $2,358.13  (21.7%)  - 6 clientes
BAJA (30+ días):   $1,192.32  (11.0%)  - 10 clientes
CERO (al día):     $0.00      (0.0%)   - 4 clientes
```

**Plan cobranza (tabla aparte):**
```
SEMANA 1 (07-14 Nov):
☐ VWR $2,800 - Llamada gerente + email formal
☐ Grupo Acción $1,689 - Visita presencial si posible
Meta semana: $4,489

SEMANA 2 (15-21 Nov):
☐ Alfipac $761
☐ 3-102-887892 $692
☐ Waipio $687
☐ CIO $687
Meta semana: $2,827

Objetivo 2 semanas: $7,316 (67% del total)
```

**Gráfico embudo:**
- CRÍTICA → ALTA → MEDIA → BAJA → CERO
- Muestra visualmente dónde está concentrado el dinero

**Alertas:**
- Cliente >45 días mora → 🔴 Escalar a legal
- Cliente >60 días → 🔴 Provisión incobrable
- Top 2 clientes > 40% total → ⚠️ Riesgo concentración

---

### **PESTAÑA 5: 📋 A/P (Cuentas por Pagar)**

**Propósito:** Control proveedores + estrategia pago

**Tabla principal:**
```
| Proveedor      | Factura | Monto USD | Monto CRC | Fecha Fact | Vence     | Días | Estado   | Prior | Notas               |
|----------------|---------|-----------|-----------|------------|-----------|------|----------|-------|---------------------|
| Intcomex       | 2502060 | 410.09    | -         | 04/09/2025 | 04/10/2025| 34   | VENCIDO  | CRIT  | Proveedor principal |
| SEA Global     | Varias  | 44.07     | -         | 10/09/2025 | 10/10/2025| 28   | VENCIDO  | ALTA  | Facturas antiguas   |
| Eurocomp       | 203637  | 2007.68   | -         | 17/10/2025 | 16/11/2025| -9   | PRÓXIMO  | ALTA  | Negociar extensión  |
| Eurocomp       | 203831  | 16.92     | -         | 20/10/2025 | 19/11/2025| -12  | VIGENTE  | MEDIA | Pequeña             |
| Compueconomicos| 012616  | 284.91    | -         | 24/10/2025 | 23/11/2025| -16  | VIGENTE  | MEDIA | Normal              |
| Intcomex       | Cloud   | 2317.09   | -         | 03/11/2025 | 03/12/2025| -26  | VIGENTE  | NORM  | Servicios cloud     |
| Intcomex       | Lenovo  | 679.12    | -         | 04/11/2025 | 04/12/2025| -27  | VIGENTE  | NORM  | Equipo              |
| SEA Global     | Nueva   | 58.76     | -         | 06/11/2025 | 06/12/2025| -29  | VIGENTE  | NORM  | Factura nueva       |
| IBASA          | -       | -         | 144516    | 05/11/2025 | 05/12/2025| -28  | VIGENTE  | NORM  | ₡144,516            |
|----------------|---------|-----------|-----------|------------|-----------|------|----------|-------|---------------------|
| TOTAL          |         | 5818.64   | 144516    |            |           |      |          |       | $6,103.66 total USD |
```

**Resumen por estado:**
```
VENCIDO (Pagar HOY):        $454.16   (7.4%)   - 2 facturas  🔴
PRÓXIMOS 15 DÍAS:           $2,309.51 (37.9%)  - 3 facturas  🟡
VIGENTE (30+ días):         $3,339.99 (54.7%)  - 4 facturas  ✅
──────────────────────────────────────────────────────────────
TOTAL A/P:                  $6,103.66 (100%)   - 9 facturas
```

**Plan de pago:**
```
SEMANA 1 (07-13 Nov):
☐ Intcomex 2502060  $410.09  - URGENTE proveedor estratégico
☐ SEA Global        $44.07   - Completar vencidos
Total semana: $454.16

SEMANA 2 (14-20 Nov):
☐ Eurocomp 203637   $2,007.68 - NEGOCIAR extensión 15 días si necesario
☐ Eurocomp 203831   $16.92
Total semana: $2,024.60

SEMANA 3 (21-27 Nov):
☐ Compueconomicos   $284.91
Total semana: $284.91

DICIEMBRE (mes completo):
☐ Intcomex Cloud    $2,317.09
☐ Intcomex Lenovo   $679.12
☐ SEA Global        $58.76
☐ IBASA CRC         $285.02 (₡144,516)
Total mes: $3,339.99
```

**Fórmulas clave:**
- Días = Vence - HOY() (negativo = aún no vence)
- Estado = SI(Días>0, "VENCIDO", SI(Días>-15, "PRÓXIMO", "VIGENTE"))
- Prioridad = Basado en días + importancia proveedor

**Alertas:**
- Factura vencida + proveedor estratégico → 🔴 PAGAR HOY
- Factura grande (>$2,000) próxima → 🟡 Negociar si cash flow ajustado
- Concentración >50% en un proveedor → ⚠️ Diversificar

---

### **PESTAÑA 6: 💳 TARJETAS CRÉDITO**

**Propósito:** Control 5 TC + plan pago agresivo sanitización

**Tabla principal:**
```
| TC   | Banco | Titular      | Saldo USD | Límite  | Uso% | Vence      | Días  | Estado  | Tasa | Interés/Mes | Min Pago |
|------|-------|--------------|-----------|---------|------|------------|-------|---------|------|-------------|----------|
| 3519 | BNCR  | Álvaro       | 1192.44   | 3000    | 40%  | 06/11/2025 | 1     | VENCIDA | 28%  | 27.82       | 23.85    |
| 9837 | BNCR  | Álvaro       | 5779.40   | 10000   | 58%  | 03/11/2025 | 4     | VENCIDA | 32%  | 154.12      | 115.59   |
| 6386 | BNCR  | Alej (adic)  | 591.70    | 3000    | 20%  | 03/11/2025 | 4     | VENCIDA | 32%  | 15.78       | 11.83    |
| 8759 | BNCR  | Álvaro       | 5731.48   | 10000   | 57%  | 03/11/2025 | 4     | VENCIDA | 30%  | 143.29      | 114.63   |
| BAC  | BAC   | Álvaro       | 3087.67   | 8000    | 39%  | 25/11/2025 | -18   | ACTIVA  | 26%  | 66.90       | 61.75    |
|------|-------|--------------|-----------|---------|------|------------|-------|---------|------|-------------|----------|
| TOTAL|       |              | 16382.69  | 34000   | 48%  |            |       |         |      | 407.91      | 327.65   |
```

**CRÍTICO: 4 BNCR Vencidas = $13,295.02**

**Resumen por estado:**
```
🔴 VENCIDAS (4 BNCR):       $13,295.02  (81.1%)  - Intereses moratorios
✅ ACTIVA (1 BAC):          $3,087.67   (18.9%)  - Al día

Interés mensual total:      $407.91/mes
Pago mínimo total:          $327.65/mes
```

**PLAN SANITIZACIÓN TARJETAS (12 meses):**

**FASE 1: NEGOCIACIÓN (Semana 1-2)**
```
Objetivo: Negociar plan pago BNCR 4 TC vencidas

Estrategia:
1. Llamar BNCR gerente cuentas
2. Solicitar:
   - Congelamiento intereses moratorios
   - Plan pago 12 cuotas sin interés adicional
   - No reportar central riesgos si cumplimos

Oferta propuesta:
   - Pago inicial: $1,500 (buena fe)
   - 12 cuotas de: $982.50/mes
   - Total: $13,295.02

Alternativa:
   - Si no aceptan: Pagar mínimos + extra $500/mes a saldo más alto
```

**FASE 2: EJECUCIÓN PAGO (12 meses)**
```
Prioridad pago (método avalancha - mayor interés primero):

MES 1-4: TC 9837 (32% - $5,779.40)
   Pago: $1,445/mes x 4 = Liquidada

MES 5-8: TC 8759 (30% - $5,731.48)
   Pago: $1,433/mes x 4 = Liquidada

MES 9-10: TC 3519 (28% - $1,192.44)
   Pago: $596/mes x 2 = Liquidada

MES 11: TC 6386 (32% - $591.70)
   Pago: $592/mes x 1 = Liquidada

MES 12: BAC (26% - $3,087.67)
   Mantener activa, pagar completo mensual
```

**Proyección ahorro intereses:**
```
Escenario actual (solo pago mínimo):
   Tiempo pagar: 8.5 años
   Interés pagado: $17,450
   Total pagado: $33,833

Escenario plan 12 meses:
   Tiempo pagar: 12 meses
   Interés pagado: $2,450 (si negocian congelamiento: $0)
   Total pagado: $15,745

AHORRO: $18,088 en intereses ✅
```

**Tabla tracking mensual:**
```
| Mes    | TC 9837 | TC 8759 | TC 3519 | TC 6386 | BAC    | Total Pagado | Saldo Rest |
|--------|---------|---------|---------|---------|--------|--------------|------------|
| Nov 25 | 5779    | 5731    | 1192    | 592     | 3088   | 0            | 16,383     |
| Dic 25 | 4334    | 5731    | 1192    | 592     | 3088   | 1,445        | 14,938     |
| Ene 26 | 2889    | 5731    | 1192    | 592     | 3088   | 2,890        | 13,493     |
| Feb 26 | 1444    | 5731    | 1192    | 592     | 3088   | 4,335        | 12,048     |
| Mar 26 | 0       | 5731    | 1192    | 592     | 3088   | 5,780        | 10,603     |
| ... hasta liquidar todas
```

**Fórmulas Excel:**
- Uso% = Saldo/Límite
- Interés/Mes = Saldo * (Tasa/12)
- Color: Vencida=Rojo, Uso>80%=Naranja, Uso<50%=Verde

**Alertas:**
- TC vencida >30 días → 🔴 URGENTE negociar
- Uso >80% límite → ⚠️ Riesgo bloqueo
- Interés mensual >$400 → 💰 Priorizar liquidación

---

### **PESTAÑA 7: 💵 GASTOS FIJOS MENSUALES**

**Propósito:** Control gastos recurrentes empresa

**Tabla principal:**
```
| Concepto          | Categoría | Monto USD | Monto CRC | Equiv USD | Frecuencia | Vence Día | Cuenta Pago      | Criticidad |
|-------------------|-----------|-----------|-----------|-----------|------------|-----------|------------------|------------|
| Salario Álvaro    | Nómina    | 1000.00   | -         | 1000.00   | Quincenal  | 15/30     | Personal 042186-9| CRÍTICA    |
| CCSS              | Impuestos | -         | 179000    | 353.26    | Mensual    | 30        | Promerica SINPE  | CRÍTICA    |
| ICE               | Servicios | -         | 192804    | 380.24    | Mensual    | 15        | BNCR CRC         | CRÍTICA    |
| TeamViewer        | Software  | 200.00    | -         | 200.00    | Mensual    | 5         | TC BAC           | CRÍTICA    |
| Apple One         | Software  | 16.85     | -         | 16.85     | Mensual    | 1         | TC BAC           | MEDIA      |
| Nissan Frontier   | Vehículo  | 800.00    | -         | 800.00    | Mensual    | 10        | BNCR USD         | ALTA       |
| Parqueos/QuickPass| Vehículo  | -         | 30000     | 59.17     | Mensual    | 7         | BNCR CRC         | MEDIA      |
|-------------------|-----------|-----------|-----------|-----------|------------|-----------|------------------|------------|
| TOTAL MENSUAL     |           | 2016.85   | 401804    | 2809.38   |            |           |                  |            |
```

**Resumen por categoría:**
```
Nómina:         $1,000.00  (35.6%)  ████████████
Vehículo:       $859.17    (30.6%)  ██████████
Servicios:      $380.24    (13.5%)  █████
Impuestos:      $353.26    (12.6%)  ████
Software:       $216.85    (7.7%)   ███
─────────────────────────────────────────
TOTAL:          $2,809.38  (100%)
```

**Calendario pagos mes:**
```
Día 1:  Apple One           $16.85
Día 5:  TeamViewer          $200.00
Día 7:  Parqueos            $59.17
Día 10: Nissan              $800.00
Día 15: ICE                 $380.24
Día 15: Salario (1a quincena) $500.00
Día 30: CCSS                $353.26
Día 30: Salario (2a quincena) $500.00
───────────────────────────────────
TOTAL:                      $2,809.52
```

**Análisis cobertura:**
```
Efectivo actual:            $4,302.10
Gastos fijos mes:           $2,809.38
─────────────────────────────────────
Cobertura:                  1.53 meses (45 días)
Estado:                     🔴 CRÍTICO

Necesidad mensual:          $2,809.38
Ingresos necesarios:        $2,810/mes (break-even)
Buffer ideal (3 meses):     $8,428.14
Gap a buffer:               -$4,126.04
```

**Proyección 12 meses:**
```
| Mes    | Gastos Fijos | Variables Est | Total Est | Ingreso Req | Gap     |
|--------|--------------|---------------|-----------|-------------|---------|
| Nov 25 | 2,809        | 800           | 3,609     | 4,000       | +391    |
| Dic 25 | 2,809        | 1,200         | 4,009     | 5,000       | +991    |
| Ene 26 | 2,809        | 600           | 3,409     | 3,500       | +91     |
| ... proyección 12 meses
```

**Alertas:**
- Cobertura <1.5 meses → 🔴 CRÍTICO cobrar A/R urgente
- Gasto >105% presupuesto → ⚠️ Revisar justificación
- Nuevo gasto recurrente → ⚠️ Evaluar impacto anual

---

### **PESTAÑA 8: 📊 PRESUPUESTO EMPRESA**

**Propósito:** Presupuesto mensual por categoría + control real vs plan

**Estructura:**
```
PRESUPUESTO MENSUAL EMPRESA - 2025

| Categoría        | Presup/Mes | Nov Real | Nov % | Dic Proy | Promedio | Variación | Límite Rígido |
|------------------|------------|----------|-------|----------|----------|-----------|---------------|
| GASTOS FIJOS     |            |          |       |          |          |           |               |
| Nómina           | 1000.00    | 1000.00  | 100%  | 1000.00  | 1000.00  | 0.00      | SÍ            |
| Impuestos        | 353.26     | 353.26   | 100%  | 353.26   | 353.26   | 0.00      | SÍ            |
| Servicios (ICE)  | 380.24     | 380.24   | 100%  | 380.24   | 380.24   | 0.00      | SÍ            |
| Software         | 216.85     | 216.85   | 100%  | 216.85   | 216.85   | 0.00      | SÍ            |
| Vehículo         | 859.17     | 859.17   | 100%  | 859.17   | 859.17   | 0.00      | SÍ            |
| Subtotal Fijos   | 2809.38    | 2809.38  | 100%  | 2809.38  | 2809.38  | 0.00      | SÍ            |
|                  |            |          |       |          |          |           |               |
| GASTOS VARIABLES |            |          |       |          |          |           |               |
| Proveedores      | 2000.00    | 454.16   | 23%   | 2300.00  | 1377.08  | -1622.84  | NO            |
| Marketing        | 300.00     | 0.00     | 0%    | 200.00   | 100.00   | -300.00   | NO            |
| Capacitación     | 100.00     | 0.00     | 0%    | 0.00     | 0.00     | -100.00   | NO            |
| Mantenimiento    | 150.00     | 0.00     | 0%    | 100.00   | 50.00    | -150.00   | NO            |
| Imprevistos      | 200.00     | 0.00     | 0%    | 150.00   | 75.00    | -200.00   | NO            |
| Subtotal Variabl | 2750.00    | 454.16   | 17%   | 2750.00  | 1602.08  | -2295.84  | NO            |
|                  |            |          |       |          |          |           |               |
| TOTAL GASTOS     | 5559.38    | 3263.54  | 59%   | 5559.38  | 4411.46  | -2295.84  |               |
|                  |            |          |       |          |          |           |               |
| INGRESOS         | 6000.00    | 0.00     | 0%    | 6500.00  | 3250.00  | -6000.00  |               |
|                  |            |          |       |          |          |           |               |
| RESULTADO        | +440.62    | -3263.54 | -741% | +940.62  | -1161.46 | -3704.16  |               |
```

**Formato condicional:**
- Real >110% presupuesto → Rojo
- Real 90-110% → Amarillo
- Real <90% → Verde
- Límite rígido excedido → 🔴 CRÍTICO

**Gráfico comparativo:**
```
[Gráfico barras agrupadas]
Eje X: Categorías
Eje Y: Monto USD
Barras: Presupuesto (azul) vs Real (naranja)
```

**Alertas automáticas:**
```
🔴 CRÍTICO:
   - Gastos fijos >100% presupuesto (NUNCA debe pasar)
   - Resultado mensual negativo >2 meses seguidos
   - Gastos variables >120% sin justificación

🟡 PRECAUCIÓN:
   - Categoría >110% presupuesto
   - Tendencia creciente gastos variables
   - Ingresos <90% presupuesto

✅ BIEN:
   - Todas categorías dentro 90-110%
   - Resultado positivo
   - Buffer creciendo
```

**Ajuste presupuesto:**
```
Revisión: Mensual
Método: Real últimos 3 meses + 10% buffer
Aprobación: Álvaro (owner)
```

---

### **PESTAÑA 9: 🔮 PROYECCIÓN 90 DÍAS**

**Propósito:** Flujo caja proyectado 3 meses adelante

**Tabla principal:**
```
| Fecha      | Concepto              | Categoría  | Entrada | Salida  | Balance | Estado | Notas             |
|------------|-----------------------|------------|---------|---------|---------|--------|-------------------|
| 07/11/2025 | Balance Inicial       | -          | -       | -       | 4302.10 | ✅     | Real              |
|            |                       |            |         |         |         |        |                   |
| 08/11/2025 | Cobro VWR (proyec)    | A/R        | 2800.00 | -       | 7102.10 | 🟡     | 80% probabilidad  |
| 08/11/2025 | Cobro Grupo Acción    | A/R        | 1689.04 | -       | 8791.14 | 🟡     | 70% probabilidad  |
|            |                       |            |         |         |         |        |                   |
| 10/11/2025 | Pago IVA vencido      | Hacienda   | -       | 533.92  | 8257.22 | 🔴     | OBLIGATORIO       |
| 10/11/2025 | Pago Intcomex         | A/P        | -       | 410.09  | 7847.13 | 🔴     | Vencido           |
| 10/11/2025 | Nissan Frontier       | Vehículo   | -       | 800.00  | 7047.13 | 🔴     | Mensual           |
|            |                       |            |         |         |         |        |                   |
| 15/11/2025 | Salario quincenal     | Nómina     | -       | 500.00  | 6547.13 | 🔴     | 1a quincena       |
| 15/11/2025 | ICE                   | Servicios  | -       | 380.24  | 6166.89 | 🔴     | Mensual           |
| 15/11/2025 | Cobro Alfipac (proy)  | A/R        | 761.05  | -       | 6927.94 | 🟡     | 60% probabilidad  |
|            |                       |            |         |         |         |        |                   |
| 16/11/2025 | Eurocomp 203637       | A/P        | -       | 2007.68 | 4920.26 | ⚠️     | Negociar extensión|
|            |                       |            |         |         |         |        |                   |
| 23/11/2025 | Compueconomicos       | A/P        | -       | 284.91  | 4635.35 | ✅     | Vigente           |
| 25/11/2025 | Pago TC BAC           | TC         | -       | 3087.67 | 1547.68 | 🟡     | Pagar completo    |
|            |                       |            |         |         |         |        |                   |
| 30/11/2025 | Salario quincenal     | Nómina     | -       | 500.00  | 1047.68 | 🔴     | 2a quincena       |
| 30/11/2025 | CCSS                  | Impuestos  | -       | 353.26  | 694.42  | 🔴     | Mensual           |
| 30/11/2025 | Facturación mensual   | Ingresos   | 5500.00 | -       | 6194.42 | 🟡     | Proyectado        |
|            |                       |            |         |         |         |        |                   |
| ... continúa hasta 90 días
```

**Resumen por mes:**
```
NOVIEMBRE 2025:
   Entradas:       $10,750.09  (Cobros A/R proyectados)
   Salidas:        $9,657.77   (Gastos críticos)
   Resultado:      +$1,092.32
   Balance final:  $5,394.42
   Estado:         🟡 AJUSTADO (depende cobros)

DICIEMBRE 2025:
   Entradas:       $6,500.00   (Facturación + cobros)
   Salidas:        $8,589.99   (A/P + gastos + TC)
   Resultado:      -$2,089.99
   Balance final:  $3,304.43
   Estado:         ⚠️ DÉFICIT (revisar)

ENERO 2026:
   Entradas:       $5,000.00   (Facturación normal)
   Salidas:        $4,254.38   (Solo fijos + TC)
   Resultado:      +$745.62
   Balance final:  $4,050.05
   Estado:         ✅ POSITIVO
```

**Indicadores críticos:**
```
Punto más bajo 90 días:     $694.42 (30/11 antes facturación)
Días con balance <$2,000:   5 días (17%)
Riesgo sobregiro:           MEDIO
Acción requerida:           Cobrar A/R top 2 en semana 1
```

**Escenarios:**
```
OPTIMISTA (100% cobros A/R):
   Balance 90 días: $8,500

REALISTA (70% cobros A/R):
   Balance 90 días: $4,050

PESIMISTA (50% cobros A/R):
   Balance 90 días: $1,200
   🔴 Usar ahorros emergencia
```

**Gráfico línea:**
- Eje X: Días (07/11 → 07/02)
- Eje Y: Balance USD
- Línea azul: Proyección
- Zona roja: <$2,000 (crítico)
- Zona amarilla: $2,000-$4,000 (precaución)
- Zona verde: >$4,000 (seguro)

