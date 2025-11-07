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

