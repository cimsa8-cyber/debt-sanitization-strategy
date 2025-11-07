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

---

### **PESTAÑA 10: 📈 KPIs & MÉTRICAS**

**Propósito:** Indicadores clave salud financiera

**KPIs Principales:**
```
┌──────────────────────────────────────────────────────────┐
│ INDICADORES CLAVE - Actualización Automática            │
├──────────────────────────────────────────────────────────┤
│                                                          │
│ LIQUIDEZ:                                                │
│ • Razón Corriente:        0.45  🔴 (Meta: >1.5)         │
│   Activos/Pasivos                                        │
│                                                          │
│ • Días Cobertura Efectivo: 45  🔴 (Meta: >90)           │
│   Efectivo/(Gastos/30)                                   │
│                                                          │
│ • Working Capital:      -$28,261  🔴 (Meta: >$10k)      │
│   Activos - Pasivos                                      │
│                                                          │
│ COBRANZA:                                                │
│ • DSO (Days Sales Out):   45 días  ⚠️ (Meta: <30)       │
│   (A/R / Ventas) * 30                                    │
│                                                          │
│ • % A/R >30 días:        67.3%  🔴 (Meta: <20%)         │
│                                                          │
│ • Concentración Top 2:   41.3%  ⚠️ (Meta: <30%)         │
│   Top 2 clientes / Total A/R                             │
│                                                          │
│ DEUDA:                                                   │
│ • Ratio Deuda/Activos:   2.22  🔴 (Meta: <1.0)          │
│                                                          │
│ • Cobertura Intereses:   0x  🔴 (Meta: >2x)             │
│   EBITDA / Intereses                                     │
│                                                          │
│ • % TC vencidas:         81.1%  🔴 (Meta: 0%)           │
│                                                          │
│ OPERATIVO:                                               │
│ • Margen Bruto:          N/A  ⚠️ (Falta data ventas)    │
│                                                          │
│ • Gastos Fijos/Ingresos: 47%  🔴 (Meta: <35%)           │
│                                                          │
│ • Burn Rate:           $2,809/mes  ⚠️                    │
│   Gastos mensuales sin ingresos                          │
│                                                          │
│ AHORRO:                                                  │
│ • Meta Vivienda:         0%  🔴 (Meta: 100% en 24m)     │
│   Ahorrado / $45,000                                     │
│                                                          │
│ • Tasa Ahorro Mensual:   0%  🔴 (Meta: 30%)             │
│   Ahorro / Ingresos                                      │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

**Fórmulas Excel:**
```excel
Razón Corriente = (Efectivo+Ahorros+AR)/(TC+AP+IVA+Hacienda+Nissan)
Días Cobertura = Efectivo/(GastosFijos!Total/30)
Working Capital = TotalActivos - TotalPasivos
DSO = (AR!Total / (Ingresos!Promedio3Meses)) * 30
% AR >30 días = SUMAR.SI(AR!DíasMora,">30",AR!Monto) / AR!Total
```

**Dashboard visual:**
```
[Gauge circular - Razón Corriente]
   0.45 / 1.5 meta
   Rojo <1, Amarillo 1-1.5, Verde >1.5

[Termómetro - Días Cobertura]
   45 días actual
   Zona crítica <60, Precaución 60-90, Seguro >90

[Barra progreso - Meta Vivienda]
   $0 / $45,000
   0% completado
```

**Tendencias (gráficos línea):**
- Efectivo últimos 6 meses
- A/R últimos 6 meses
- Deuda total últimos 6 meses
- Gastos vs Ingresos comparativo mensual

---

### **PESTAÑA 11: 🏛️ HACIENDA (Impuestos)**

**Propósito:** Control deuda fiscal + plan arreglo

**IVA Vencido:**
```
| Período | Mes          | Monto CRC | Monto USD | Vence      | Días Mora | Multa Est | Total+Multa |
|---------|--------------|-----------|-----------|------------|-----------|-----------|-------------|
| 202508  | Agosto 2025  | 244129    | 481.44    | 16/09/2025 | 52        | 48.14     | 529.58      |
| 202509  | Sept 2025    | 26608     | 52.48     | 24/10/2025 | 14        | 2.62      | 55.10       |
|---------|--------------|-----------|-----------|------------|-----------|-----------|-------------|
| TOTAL   |              | 270737    | 533.92    |            |           | 50.76     | 584.68      |
```

**ISR Pendiente:**
```
| Año | Período | Monto CRC | Monto USD | Estado           | Incluido Arreglo |
|-----|---------|-----------|-----------|------------------|------------------|
| 2020| 202001  | 981664    | 1936.30   | Vencido          | ✅ Sí            |
| 2021| 202101  | 1442277   | 2844.62   | Vencido          | ✅ Sí            |
| 2022| 202201  | 1448546   | 2856.99   | Vencido          | ✅ Sí            |
| 2023| 202301  | 825297    | 1627.80   | Vencido          | ✅ Sí            |
| 2024| 202401  | ?         | ?         | Por confirmar    | ⚠️ Verificar     |
|-----|---------|-----------|-----------|------------------|------------------|
| TOTAL (2020-2023) | 4697784 | 9265.71 | En arreglo       | DGV-523678-M6W1  |
```

**Solicitud Arreglo Pago:**
```
Número: DGV-523678-M6W1
Fecha solicitud: 19/08/2025 (estimado)
Estado: EN TRÁMITE - Esperando resolución
Monto solicitado: ₡4,697,784 ($9,265.71) ISR 2020-2023

Acción requerida:
☐ Llamar 800-TRIBUT para seguimiento
☐ Entrar ATV Hacienda verificar estado
☐ Confirmar si incluye IVA vencido o solo ISR
☐ Preparar estados financieros actualizados si solicitan
```

**Plan propuesto (pendiente aprobación):**
```
Opción A: Quita + Cuotas
   - Quita: 30% ($2,780)
   - Saldo: $6,486
   - Cuotas: 24 meses de $270/mes
   - Total pagar: $6,486

Opción B: Solo Cuotas
   - Saldo completo: $9,266
   - Cuotas: 36 meses de $257/mes
   - Total pagar: $9,266

Preferencia: OPCIÓN A
```

**Calendario pagos (si aprueban):**
```
| Mes    | IVA Vencido | ISR Arreglo | Total Hacienda | Acumulado |
|--------|-------------|-------------|----------------|-----------|
| Nov 25 | 585         | -           | 585            | 585       |
| Dic 25 | -           | 270         | 270            | 855       |
| Ene 26 | -           | 270         | 270            | 1,125     |
| ... 24 meses hasta liquidar
```

**Alerta crítica:**
```
🔴 IVA vencido creciendo multas e intereses diariamente
🔴 Llamar Hacienda URGENTE para:
   1. Verificar estado arreglo DGV-523678-M6W1
   2. Informar pago IVA vencido esta semana
   3. Solicitar suspensión multas mientras se resuelve
```

---

### **PESTAÑA 12: 🚗 NISSAN FRONTIER (Préstamo)**

**Propósito:** Control préstamo vehículo + proyección liquidación

**Datos préstamo:**
```
Vehículo: Nissan Frontier UD202840
Saldo actual: $19,197.69 (confirmado 07/11/2025)
Cuota mensual: $800.00
Tasa interés: PENDIENTE CONFIRMAR
Plazo restante: PENDIENTE CONFIRMAR
Fecha vencimiento cuota: Día 10 cada mes
Cuenta pago: BNCR 601066-4 USD
```

**Tabla amortización (estimada - pendiente confirmar):**
```
| Mes    | Cuota   | Capital | Interés | Saldo Rest | % Pagado |
|--------|---------|---------|---------|------------|----------|
| Nov 25 | 800.00  | 700.00  | 100.00  | 18,497.69  | 3.6%     |
| Dic 25 | 800.00  | 703.00  | 97.00   | 17,794.69  | 7.3%     |
| Ene 26 | 800.00  | 706.03  | 93.97   | 17,088.66  | 11.0%    |
| ... proyección hasta liquidar
```

**Escenarios liquidación:**

**ESCENARIO 1: Solo cuota mínima ($800/mes)**
```
Tiempo: 24 meses
Interés total: $3,802 (estimado)
Total pagar: $23,000
Fecha liquidación: Nov 2027
```

**ESCENARIO 2: Cuota + extra $200/mes ($1,000/mes)**
```
Tiempo: 19 meses
Interés total: $2,450
Total pagar: $21,647
AHORRO: $1,353
Fecha liquidación: Jun 2027
```

**ESCENARIO 3: Pago agresivo $1,500/mes**
```
Tiempo: 13 meses
Interés total: $1,200
Total pagar: $20,397
AHORRO: $2,603
Fecha liquidación: Dic 2026
```

**RECOMENDACIÓN:**
```
MES 1-12: Pagar solo mínimo ($800) mientras se liquidan TC
MES 13-24: Aumentar a $1,500/mes después de TC liquidadas
Balance: Entre sanitizar TC primero (mayor interés) vs aliviar flujo mensual

Acción inmediata:
☐ Solicitar banco estado de cuenta detallado
☐ Confirmar tasa interés exacta
☐ Confirmar plazo restante
☐ Evaluar refinanciamiento si tasa >12%
```

**Gráfico progreso:**
```
[Barra horizontal - Progreso liquidación]
$0 ────────────────────────────────── $19,197.69
Pagado: 0% | Restante: 100%

[Proyección 3 escenarios - línea]
Eje X: Meses
Eje Y: Saldo
3 líneas: Mínimo, +$200, +$700
```

---

### **PESTAÑA 13: 💾 AHORRO VIVIENDA 2 AÑOS**

**Propósito:** Plan ahorro $45,000 en 24 meses

**META VIVIENDA:**
```
┌────────────────────────────────────────────────┐
│ 🏠 META: CUOTA INICIAL VIVIENDA                │
├────────────────────────────────────────────────┤
│ Monto objetivo:           $45,000              │
│ Plazo:                    24 meses             │
│ Fecha meta:               Noviembre 2027       │
│ Ahorro mensual requerido: $1,875/mes           │
│ Ahorro actual:            $8,054 (ahorros)     │
│ Por ahorrar:              $36,946              │
│ Avance:                   17.9%                │
│ Estado:                   🟡 INICIANDO         │
└────────────────────────────────────────────────┘
```

**ESTRATEGIA AHORRO (fases):**

**FASE 1: SANITIZACIÓN (Meses 1-6)**
```
Objetivo: Liquidar deuda urgente primero

Prioridad:
1. IVA vencido $585 ✅ Mes 1
2. A/P vencido $454 ✅ Mes 1
3. TC BNCR inicio pago plan
4. Buffer emergencia $5,000

Ahorro vivienda: $0/mes (PAUSA)
Razón: Pagar deuda alta tasa > ahorrar tasa 0%
```

**FASE 2: TRANSICIÓN (Meses 7-12)**
```
Objetivo: Balance entre liquidar TC y empezar ahorro

TC restante: ~$8,000
Plan pago TC: $1,000/mes
Ahorro vivienda: $500/mes (INICIO)

Total necesario: $1,500/mes
```

**FASE 3: ACELERACIÓN (Meses 13-24)**
```
Objetivo: TC liquidadas, ahorro agresivo

TC: ✅ Liquidadas
Ahorro vivienda: $2,500/mes (MÁXIMO)
Nissan extra: $500/mes

En 12 meses: $2,500 x 12 = $30,000
```

**PROYECCIÓN 24 MESES:**
```
| Mes | TC Pago | Ahorro Viv | Nissan Extra | Acumulado Viv | % Meta |
|-----|---------|------------|--------------|---------------|--------|
| 1   | 1445    | 0          | 0            | 8,054         | 17.9%  |
| 2   | 1445    | 0          | 0            | 8,054         | 17.9%  |
| 3   | 1445    | 0          | 0            | 8,054         | 17.9%  |
| 4   | 1445    | 0          | 0            | 8,054         | 17.9%  |
| 5   | 1433    | 0          | 0            | 8,054         | 17.9%  |
| 6   | 1433    | 0          | 0            | 8,054         | 17.9%  |
| 7   | 1000    | 500        | 0            | 8,554         | 19.0%  |
| 8   | 1000    | 500        | 0            | 9,054         | 20.1%  |
| 9   | 1000    | 500        | 0            | 9,554         | 21.2%  |
| 10  | 1000    | 500        | 0            | 10,054        | 22.3%  |
| 11  | 592     | 1000       | 0            | 11,054        | 24.6%  |
| 12  | 592     | 1000       | 0            | 12,054        | 26.8%  |
| 13  | 0       | 2500       | 500          | 14,554        | 32.3%  |
| 14  | 0       | 2500       | 500          | 17,054        | 37.9%  |
| ... hasta mes 24
| 24  | 0       | 2500       | 500          | 45,054        | 100.1% |
```

**AJUSTES DINÁMICOS:**
```
SI(EfectivoDisponible > $10,000):
   Aumentar ahorro a $3,000/mes

SI(A/R cobrado > proyectado):
   Bonus 50% extra → Ahorro vivienda

SI(Gasto inesperado >$2,000):
   Reducir ahorro mes siguiente (mantener liquidez)
```

**Cuentas sugeridas ahorro:**
```
Primaria: BNCR 17000002201 (Vehículo Nuevo)
   Actual: $4,559
   Depositar: Mensual automático

Secundaria: Nueva cuenta vivienda específica
   Recomendación: Abrir cuenta ahorro plazo
   Tasa: Buscar mejor tasa mercado (3-5%)
```

**Gráfico progreso:**
```
[Barra acumulativa 24 meses]
Meta: $45,000
Línea proyectada vs línea real
Hitos: $10k, $20k, $30k, $40k, $45k
```

---

### **PESTAÑA 14: 🔍 ANÁLISIS & GRÁFICOS**

**Propósito:** Visualizaciones comportamiento financiero

**GRÁFICO 1: Evolución Efectivo (12 meses)**
```
[Gráfico línea]
Eje X: Nov 2024 → Nov 2025
Eje Y: Efectivo USD
Línea azul: Balance mensual
Puntos críticos: <$2,000 marcados rojos
Promedio: Línea punteada
```

**GRÁFICO 2: Composición Gastos (Pie)**
```
[Gráfico circular]
Nómina: 35.6%
Vehículo: 30.6%
Servicios: 13.5%
Impuestos: 12.6%
Software: 7.7%
```

**GRÁFICO 3: A/R Aging (Columnas apiladas)**
```
[Gráfico columnas]
Eje X: Noviembre
Eje Y: Monto USD
Segmentos:
- 0-30 días (verde)
- 31-60 días (amarillo)
- 61-90 días (naranja)
- >90 días (rojo)
```

**GRÁFICO 4: Deuda Total Trending**
```
[Gráfico área]
Eje X: Mes
Eje Y: Deuda USD
Áreas apiladas:
- TC (rojo oscuro)
- A/P (naranja)
- Hacienda (amarillo)
- Nissan (gris)
```

**GRÁFICO 5: Ingresos vs Gastos**
```
[Gráfico barras agrupadas]
Eje X: Meses
Eje Y: Monto USD
Barras verdes: Ingresos
Barras rojas: Gastos
Línea: Diferencia (profit/loss)
```

**GRÁFICO 6: Proyección Sanitización Deuda**
```
[Gráfico línea proyección]
Eje X: Mes 1-24
Eje Y: Deuda total USD
Línea descendente: De $51,484 → $19,198 (Nissan)
Hitos marcados: TC liquidadas (mes 12)
```

**TABLA RESUMEN MENSUAL:**
```
| Mes    | Ingresos | Gastos | Resultado | TC Pagadas | Ahorro Viv | Efectivo Fin |
|--------|----------|--------|-----------|------------|------------|--------------|
| Nov 25 | 10,750   | 9,658  | +1,092    | 0          | 0          | 5,394        |
| Dic 25 | 6,500    | 8,590  | -2,090    | 1,445      | 0          | 3,304        |
| Ene 26 | 5,000    | 4,254  | +746      | 1,445      | 0          | 4,050        |
| ... proyección 24 meses
```

---

### **PESTAÑA 15: ⚙️ CONFIGURACIÓN & HELP**

**Propósito:** Parámetros sistema + ayuda usuario

**PARÁMETROS GLOBALES:**
```
┌─────────────────────────────────────────────┐
│ CONFIGURACIÓN SISTEMA                       │
├─────────────────────────────────────────────┤
│ Tipo Cambio USD/CRC:        507             │
│ Última actualización TC:    07/11/2025      │
│ Actualizar automático:      [ ] Sí [X] No   │
│                                             │
│ Tasa interés estimada:                      │
│ - TC BNCR:                  30%             │
│ - TC BAC:                   26%             │
│ - Préstamo Nissan:          12% (estim)     │
│                                             │
│ Alertas activadas:                          │
│ [X] Efectivo < $2,000                       │
│ [X] Factura vence 7 días                    │
│ [X] Cliente >45 días mora                   │
│ [X] Presupuesto excedido >10%               │
│                                             │
│ Backup automático OneDrive:  [X] Activado   │
│ Frecuencia backup:           Diario 23:00   │
└─────────────────────────────────────────────┘
```

**CATEGORÍAS (Listas desplegables):**
```
Categorías Gastos:
- Nómina
- Impuestos
- Servicios
- Software
- Vehículo
- Proveedores
- Marketing
- Capacitación
- Mantenimiento
- Imprevistos
- Otros

Categorías Ingresos:
- Facturación Clientes
- Servicios Profesionales
- Productos
- Otros Ingresos
```

**INSTRUCCIONES USO DIARIO:**
```
📝 RUTINA DIARIA (5-10 minutos):

1. Abrir pestaña EFECTIVO
2. Registrar transacciones del día:
   - Fecha (HOY)
   - Banco correspondiente
   - Concepto breve
   - Categoría (lista desplegable)
   - Monto en Entrada o Salida
3. Verificar balance actualizado automáticamente
4. Revisar DASHBOARD alertas críticas
5. Guardar archivo (Ctrl+S)

✅ Listo - Sistema actualizado
```

**INSTRUCCIONES SEMANAL:**
```
📊 REVISIÓN SEMANAL (15 minutos):

Lunes:
1. Revisar pestaña A/R
   - Identificar clientes próximos a vencer
   - Hacer llamadas cobranza
   - Actualizar "Última Gestión"

2. Revisar pestaña A/P
   - Verificar facturas próxima semana
   - Planificar pagos según proyección

3. Revisar PROYECCIÓN 90 DÍAS
   - Ajustar si hubo cambios grandes
   - Verificar puntos críticos

4. Backup manual adicional
```

**INSTRUCCIONES MENSUAL:**
```
📈 CIERRE MENSUAL (30 minutos):

Día 1 mes siguiente:
1. Pestaña PRESUPUESTO
   - Copiar columna "Real" mes anterior
   - Comparar vs presupuesto
   - Analizar variaciones >10%
   - Ajustar presupuesto mes siguiente si necesario

2. Pestaña KPIs
   - Revisar todos los indicadores
   - Tomar screenshot para histórico
   - Identificar tendencias preocupantes

3. Pestaña AHORRO VIVIENDA
   - Registrar depósito mensual
   - Actualizar % progreso
   - Ajustar proyección si necesario

4. Crear archivo mensual:
   - Guardar copia: "AlvaroVelascoNet_Nov2025.xlsx"
   - Mantener archivo activo para mes nuevo
```

**FÓRMULAS CLAVE USADAS:**
```excel
Efectivo Total:
=SUMA(Efectivo!B:B) - SUMA(Efectivo!C:C)

Meses Cobertura:
=Efectivo!Total / (GastosFijos!Total/30)

% Presupuesto:
=Real/Presupuesto

Días Mora A/R:
=SI(HOY()>VenceFact, HOY()-VenceFact, 0)

Proyección Balance:
=BalanceAnterior + Entradas - Salidas
```

**TROUBLESHOOTING:**
```
Problema: Balance no cuadra
Solución:
1. Verificar no hay celdas vacías en columnas clave
2. Revisar fórmulas balance = anterior + entrada - salida
3. Usar Ctrl+` para ver fórmulas

Problema: Gráfico no actualiza
Solución:
1. Click derecho gráfico → Seleccionar datos
2. Verificar rango correcto
3. F9 para recalcular todo

Problema: Categorías no aparecen
Solución:
1. Pestaña Configuración → verificar listas
2. Asegurar validación datos activa
3. Re-crear lista si necesario
```

**CONTACTO SOPORTE:**
```
Creador sistema: Claude AI
Versión: 1.0
Fecha: 07/11/2025
Usuario: Álvaro Velasco (AlvaroVelasco.Net SRL)

Para modificaciones:
- Documentar cambios en CHANGELOG
- Backup antes de editar fórmulas complejas
- Probar en copia antes de producción
```

---

## 📁 ARCHIVO PERSONAL: ESTRUCTURA

### **ARCHIVO: AlvaroVelasco_PERSONAL.xlsx**

**Propósito:** Control finanzas personales Álvaro separado de empresa

**8 PESTAÑAS:**

1. **Dashboard Personal** - Vista rápida efectivo, gastos, ahorro
2. **Efectivo Personal** - 3 cuentas BNCR personal
3. **Ingresos Personal** - Salario empresa + otros ingresos
4. **Gastos Personal** - Categorización gastos personales/familia
5. **Presupuesto Personal** - $1,000/mes salario → distribución
6. **Ahorro Personal** - Metas personales (emergencia, educación, etc)
7. **Proyección Personal** - 90 días flujo caja personal
8. **Config Personal** - Categorías gastos personales

**Estructura más simple que empresa:**
- Control básico entrada/salida
- Presupuesto mensual $1,000
- Identificar si salario suficiente
- Alertas sobregasto categorías
- Separación TOTAL empresa/personal

**Conexión con empresa:**
- Recibe salario 2 tractos quincenales
- NO mezclar gastos
- Transfer empresa → personal registrados ambos lados

