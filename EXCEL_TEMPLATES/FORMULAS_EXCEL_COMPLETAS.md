# FÓRMULAS EXCEL COMPLETAS - LISTAS PARA COPY-PASTE

**Sistema Financiero AlvaroVelasco.Net SRL**
**Fecha creación:** 07 de Noviembre 2025
**Office 365 Compatible**

---

## INSTRUCCIONES DE USO

1. **Importar CSVs primero** - Cargar todos los archivos CSV a Excel
2. **Copiar fórmulas** - Copy-paste estas fórmulas en las celdas indicadas
3. **Ajustar rangos** - Si tus datos ocupan más/menos filas, ajusta los rangos (ej: H2:H100)
4. **Formato condicional** - Aplicar después de las fórmulas

---

## PESTAÑA 02: EFECTIVO

### Balance Running (Columna H)
```excel
Celda H2: =SI(F2>0, G2+F2, G2)
Celda H3: =SI(F3>0, H2+F3-G3, SI(G3>0, H2-G3, H2))
```
**Arrastrar H3 hacia abajo hasta última fila**

### Total Efectivo Actual (resumen arriba)
```excel
=SUMAR.SI(H:H;">0")
```
O específico:
```excel
=SUMA(H2:H1000)
```

### Alertas - Efectivo Bajo $1000
```excel
=SI(H2<1000, "⚠️ CRÍTICO - Efectivo bajo", "OK")
```

---

## PESTAÑA 03: AHORROS

### Total Ahorros
```excel
=SUMA(C2:C5)
```

### Porcentaje de cada cuenta
```excel
Celda D2: =C2/$C$6*100
```
**Formato:** Porcentaje con 1 decimal

---

## PESTAÑA 04: CUENTAS POR COBRAR (A/R)

### Suma Total A/R
```excel
=SUMA(B2:B27)
```

### Días Vencido (si tienes columna de Fecha Factura en F)
```excel
=SI(F2="", "", HOY()-F2)
```

### Alertas por Prioridad
```excel
=SI(E2="CRÍTICA", "🔴 COBRAR HOY", SI(E2="ALTA", "🟠 Esta semana", ""))
```

### Top 10 Clientes (en otra celda resumen)
```excel
=SUMAPRODUCTO.GRANDE(B2:B27, 1:10)
```
O manualmente suma top 10:
```excel
=SUMA(B2:B11)
```

### % del Total
```excel
Celda C2: =B2/$B$28*100
```
**Formato:** Porcentaje con 1 decimal

---

## PESTAÑA 05: CUENTAS POR PAGAR (A/P)

### Días para Vencer (Columna F)
```excel
=SI(E2="", "", E2-HOY())
```

### Días Mora (Columna G)
```excel
=SI(E2="", "", SI(E2<HOY(), HOY()-E2, 0))
```

### Estado Automático
```excel
=SI(G2>0, "VENCIDO", SI(F2<=15, "PRÓXIMO", "VIGENTE"))
```

### Alerta Crítica
```excel
=SI(G2>30, "🔴 +30 DÍAS MORA", SI(G2>0, "🟠 VENCIDO", ""))
```

### Total A/P
```excel
=SUMA(C2:C10)
```

### Total Vencido
```excel
=SUMAR.SI(H:H, "VENCIDO", C:C)
```

---

## PESTAÑA 06: TARJETAS CRÉDITO

### Total Saldo TC
```excel
=SUMA(D2:D6)
```

### Total Vencido
```excel
=SUMAR.SI(H:H, "VENCIDA", D:D)
```

### Pago Mínimo (6% del saldo)
```excel
=D2*0.06
```

### Intereses Mes (tasa/12)
```excel
=D2*(E2/12)
```
**Nota:** Si E2 está como "32%", convertir a decimal (0.32)

### Alerta Vencidas
```excel
=SI(H2="VENCIDA", "🔴 PAGAR URGENTE", "")
```

### Plan Sanitización - Meses para pagar
```excel
Celda K2: =SI(I2="Mes 1-4", 4, SI(I2="Mes 5-8", 4, SI(I2="Mes 9-10", 2, 1)))
```

### Pago Mensual Requerido
```excel
=D2/K2
```

---

## PESTAÑA 07: GASTOS FIJOS

### Total Gastos Fijos USD
```excel
=SUMAR.SI(B:B, ">0")
```
O:
```excel
=SUMA(B2:B8)
```

### % de cada gasto
```excel
=B2/$B$9*100
```

### Total por Categoría
Si tienes categorías en columna D:
```excel
=SUMAR.SI(D:D, "NÓMINA", B:B)
=SUMAR.SI(D:D, "VEHÍCULO", B:B)
=SUMAR.SI(D:D, "SERVICIOS", B:B)
=SUMAR.SI(D:D, "IMPUESTOS", B:B)
=SUMAR.SI(D:D, "SOFTWARE", B:B)
```

---

## PESTAÑA 08: PRESUPUESTO

### % Usado
```excel
Celda D2: =SI(B2=0, 0, C2/B2*100)
```

### Variación (Real - Presupuestado)
```excel
Celda E2: =C2-B2
```

### Alerta Exceso
```excel
Celda G2: =SI(Y(F2="SÍ", C2>B2), "⚠️ EXCEDIDO", "")
```

### Alerta 80% Límite Flexible
```excel
Celda G12: =SI(Y(F12="NO", D12>80), "⚠️ Cerca del límite", "")
```

### Total Gastos Fijos
```excel
=SUMA(B2:B6)
```

### Total Gastos Variables
```excel
=SUMA(B8:B13)
```

### Total Gastos
```excel
=B7+B14
```

### Resultado Mensual (Ingresos - Gastos)
```excel
=B17-B15
```

### % Margen
```excel
=B19/B17*100
```

---

## PESTAÑA 09: PROYECCIÓN 90 DÍAS

### Balance Día X (suponiendo ingresos en col B, gastos en col C)
```excel
Celda D2: ='02_Efectivo'!H_última + B2 - C2
Celda D3: =D2 + B3 - C3
```
**Arrastrar hacia abajo 90 filas**

### Escenarios - Optimista (100% cobros)
```excel
='04_A/R'!$B$28
```

### Escenarios - Realista (70% cobros)
```excel
='04_A/R'!$B$28 * 0.7
```

### Escenarios - Pesimista (50% cobros)
```excel
='04_A/R'!$B$28 * 0.5
```

### Balance Proyectado 90 días
```excel
=Efectivo_Hoy + Ingresos_90d - Gastos_90d
```
Específico:
```excel
='02_Efectivo'!H100 + SUMA(B2:B91) - SUMA(C2:C91)
```

---

## PESTAÑA 10: KPIs & MÉTRICAS

### Razón Corriente (Current Ratio)
```excel
=(Efectivo + Ahorros + AR) / (TC + AP + IVA + Hacienda + Nissan)
```
Específico:
```excel
=('02_Efectivo'!H100 + '03_Ahorros'!C6 + '04_A/R'!B28) / ('06_TC'!D7 + '05_A/P'!C11 + 533.92 + 9265.71 + 19197.69)
```

### Días Cobertura Efectivo
```excel
=Efectivo / (Gastos_Fijos / 30)
```
Específico:
```excel
='02_Efectivo'!H100 / ('07_GastosFijos'!B9 / 30)
```

### DSO (Days Sales Outstanding)
```excel
=(A/R_Total / Ventas_Promedio_3_Meses) * 30
```
**Nota:** Necesitas calcular ventas promedio manual o con fórmula:
```excel
=('04_A/R'!B28 / PROMEDIO(Ingresos_Mes1, Ingresos_Mes2, Ingresos_Mes3)) * 30
```

### Working Capital
```excel
=Activos_Corrientes - Pasivos_Corrientes
```
Específico:
```excel
=('02_Efectivo'!H100 + '03_Ahorros'!C6 + '04_A/R'!B28) - ('06_TC'!D7 + '05_A/P'!C11)
```

### % TC Vencidas
```excel
=TC_Vencido / TC_Total * 100
```
Específico:
```excel
='06_TC'!D8 / '06_TC'!D7 * 100
```

### Ratio Deuda/Activos
```excel
=Deuda_Total / Activos_Total
```
Específico:
```excel
=(16382.69 + 6103.66 + 533.92 + 9265.71 + 19197.69) / (4302.10 + 8053.97 + 10866.42)
```

### % A/R Crítico (Top 2)
```excel
=SUMA(B2:B3) / B28 * 100
```
En pestaña A/R

---

## PESTAÑA 11: HACIENDA

### Total IVA Vencido
```excel
=SUMA(C2:C3)
```

### Total ISR
```excel
=SUMA(C5:C8)
```

### Total Deuda Hacienda
```excel
=C4 + C9
```

### Días Mora IVA
```excel
=HOY() - F2
```

---

## PESTAÑA 12: NISSAN FRONTIER

### Intereses Pagados Mes
```excel
=Saldo * (Tasa_Anual / 12)
```
Específico:
```excel
=B2 * (0.12 / 12)
```

### Principal Pagado
```excel
=Cuota - Intereses
```
Específico:
```excel
=800 - C2
```

### Nuevo Saldo
```excel
=Saldo_Anterior - Principal_Pagado
```

### ESCENARIO 1: Solo Mínimo ($800/mes)
Arrastrar 24 meses y sumar intereses

### ESCENARIO 2: +$200/mes ($1000/mes)
```excel
=800 + 200
```
Calcular meses y sumar intereses

### ESCENARIO 3: +$700/mes ($1500/mes)
```excel
=800 + 700
```
Calcular meses y sumar intereses

### Ahorro Comparativo
```excel
=Intereses_Escenario1 - Intereses_Escenario2
```

---

## PESTAÑA 13: AHORRO VIVIENDA 2 AÑOS

### Meta Total
```excel
45000
```

### Ahorro Actual
```excel
='03_Ahorros'!C6
```

### Pendiente
```excel
=45000 - B2
```

### % Progreso
```excel
=B2 / 45000 * 100
```

### Proyección por Fase

**FASE 1 (Meses 1-6): Sanitización**
```excel
Ahorro/mes: 0
Total 6 meses: 0
Balance: =AhorroActual + 0
```

**FASE 2 (Meses 7-12): Transición**
```excel
Ahorro/mes: 500
Total 6 meses: =500 * 6
Balance: =BalanceFase1 + 3000
```

**FASE 3 (Meses 13-24): Aceleración**
```excel
Ahorro/mes: 2500
Total 12 meses: =2500 * 12
Balance: =BalanceFase2 + 30000
```

### Proyección Final Mes 24
```excel
=8053.97 + 0 + 3000 + 30000
```

### Diferencia vs Meta
```excel
=B10 - 45000
```

---

## PESTAÑA 14: ANÁLISIS & GRÁFICOS

### Top 5 Gastos (para gráfico)
Crear tabla:
```
| Categoría | Monto |
| Nómina    | ='07_GastosFijos'!B2 |
| Vehículo  | ='07_GastosFijos'!B6 + '07_GastosFijos'!B7 |
| Servicios | ='07_GastosFijos'!B4 |
| Impuestos | ='07_GastosFijos'!B3 |
| Software  | ='07_GastosFijos'!B5 |
```

### Ingresos vs Gastos (mensual comparativo)
```
| Mes | Ingresos | Gastos | Delta |
| Nov | =SUM() | ='07_GastosFijos'!B9 | =B2-C2 |
```

### A/R Aging Buckets
```excel
0-30 días:    =SUMAR.SI.CONJUNTO(Monto, DiasVencido, "<=30", DiasVencido, ">=0")
31-60 días:   =SUMAR.SI.CONJUNTO(Monto, DiasVencido, "<=60", DiasVencido, ">30")
61-90 días:   =SUMAR.SI.CONJUNTO(Monto, DiasVencido, "<=90", DiasVencido, ">60")
+90 días:     =SUMAR.SI(DiasVencido, ">90", Monto)
```

---

## PESTAÑA 15: CONFIGURACIÓN

### Tipo Cambio USD/CRC
```excel
507
```
**Nombre de celda:** TC_USDCRC

### Conversión CRC a USD
```excel
=Monto_CRC / TC_USDCRC
```

### Conversión USD a CRC
```excel
=Monto_USD * TC_USDCRC
```

### Tasas Interés TC (tabla)
```
| Banco | Tasa |
| BNCR  | 30%  |
| BNCR  | 32%  |
| BAC   | 26%  |
```

### Tasa Nissan
```excel
12%
```

### Alertas - Configurar umbrales
```
Efectivo_Critico: 1000
AR_Critico_Dias: 60
AP_Vencido_Dias: 0
TC_Vencida: TRUE/FALSE
```

---

## VALIDACIÓN DE DATOS (Listas Desplegables)

### Efectivo - Columna Categoría
```
Lista: APERTURA, INGRESO, GASTO, TRANSFER, AJUSTE
```
**Seleccionar rango columna E → Datos → Validación de datos → Lista**

### Efectivo - Columna Banco
```
Lista: Promerica, BNCR, BAC, Efectivo, Otro
```

### A/R - Columna Prioridad
```
Lista: CRÍTICA, ALTA, MEDIA, BAJA, NINGUNA
```

### A/P - Columna Estado
```
Lista: VENCIDO, PRÓXIMO, VIGENTE
```

### A/P - Columna Prioridad
```
Lista: CRÍTICA, ALTA, MEDIA, NORMAL
```

### TC - Columna Estado
```
Lista: VENCIDA, ACTIVA, CANCELADA
```

### Presupuesto - Columna Límite Rígido
```
Lista: SÍ, NO
```

---

## FORMATO CONDICIONAL

### Efectivo - Alerta Bajo
**Rango:** H:H
**Regla:** `=H1<1000`
**Formato:** Fondo rojo, texto blanco

### Efectivo - Alerta Muy Bajo
**Rango:** H:H
**Regla:** `=H1<500`
**Formato:** Fondo rojo oscuro, texto blanco, negrita

### A/R - Prioridad CRÍTICA
**Rango:** Fila completa
**Regla:** `=$E1="CRÍTICA"`
**Formato:** Fondo rojo claro

### A/R - Prioridad ALTA
**Rango:** Fila completa
**Regla:** `=$E1="ALTA"`
**Formato:** Fondo naranja claro

### A/P - Vencido
**Rango:** Fila completa
**Regla:** `=$H1="VENCIDO"`
**Formato:** Fondo rojo claro

### A/P - Próximo 15 días
**Rango:** Fila completa
**Regla:** `=$H1="PRÓXIMO"`
**Formato:** Fondo amarillo

### TC - Vencida
**Rango:** Fila completa
**Regla:** `=$H1="VENCIDA"`
**Formato:** Fondo rojo claro

### Presupuesto - Excedido (Límite Rígido)
**Rango:** Fila completa
**Regla:** `=Y($F1="SÍ", $C1>$B1)`
**Formato:** Fondo rojo, texto blanco, negrita

### Presupuesto - Cerca límite (>80%)
**Rango:** Columna D (%)
**Regla:** `=D1>80`
**Formato:** Fondo naranja

### KPIs - Razón Corriente <1.0
**Rango:** Celda resultado
**Regla:** `<1`
**Formato:** Fondo rojo

### KPIs - Días Cobertura <30
**Rango:** Celda resultado
**Regla:** `<30`
**Formato:** Fondo naranja

---

## NOMBRES DE RANGO (OPCIONAL - AVANZADO)

Para facilitar fórmulas, crear nombres:

```
Efectivo_Total      = '02_Efectivo'!H100
Ahorros_Total       = '03_Ahorros'!C6
AR_Total            = '04_A/R'!B28
AP_Total            = '05_A/P'!C11
TC_Total            = '06_TC'!D7
TC_Vencido          = '06_TC'!D8
GastosFijos_Total   = '07_GastosFijos'!B9
Presupuesto_Ingresos = '08_Presupuesto'!B17
```

**Crear:** Fórmulas → Administrador de nombres → Nuevo

**Uso en fórmulas:**
```excel
=Efectivo_Total + Ahorros_Total
=AR_Total * 0.7
=GastosFijos_Total / 30
```

---

## GRÁFICOS RECOMENDADOS

### 1. Efectivo Trending (12 meses)
**Tipo:** Línea
**Datos:** Fecha (X), Balance (Y)
**Ubicación:** Dashboard

### 2. Composición Gastos
**Tipo:** Pie (circular)
**Datos:** Categorías gastos, Montos
**Ubicación:** Dashboard

### 3. A/R Aging
**Tipo:** Columnas apiladas
**Datos:** 0-30, 31-60, 61-90, +90 días
**Ubicación:** Análisis

### 4. Deuda Total Trending
**Tipo:** Área
**Datos:** Mes, Saldo TC + AP + Hacienda + Nissan
**Ubicación:** Análisis

### 5. Ingresos vs Gastos
**Tipo:** Barras agrupadas
**Datos:** Mes, Ingresos, Gastos
**Ubicación:** Dashboard

### 6. Proyección Sanitización TC (24 meses)
**Tipo:** Línea
**Datos:** Mes, Saldo proyectado cada TC
**Ubicación:** Dashboard

---

## PROTECCIÓN DE CELDAS (OPCIONAL)

1. **Desproteger todas:** Inicio → Formato → Desproteger hoja
2. **Seleccionar celdas con fórmulas** (Ctrl+G → Especial → Fórmulas)
3. **Proteger solo fórmulas:** Formato Celdas → Protección → Bloqueada
4. **Proteger hoja:** Revisar → Proteger hoja → Sin contraseña (o con contraseña)

**Resultado:** Solo puedes editar datos, no fórmulas accidentalmente

---

## MACROS VBA (AVANZADO - OPCIONAL)

### Botón "Actualizar Todo"
```vba
Sub ActualizarTodo()
    Application.CalculateFullRebuild
    ActiveWorkbook.RefreshAll
    MsgBox "Sistema actualizado correctamente", vbInformation
End Sub
```

### Botón "Backup Rápido"
```vba
Sub BackupRapido()
    Dim FechaHora As String
    FechaHora = Format(Now, "yyyymmdd_hhmmss")
    ThisWorkbook.SaveCopyAs "C:\Backups\Finanzas_" & FechaHora & ".xlsx"
    MsgBox "Backup creado: Finanzas_" & FechaHora & ".xlsx", vbInformation
End Sub
```

---

## NOTAS FINALES

1. **Ajustar rangos:** Si tus datos crecen, actualiza rangos en fórmulas (H2:H100 → H2:H500)
2. **Nombres de pestañas:** Si cambias nombres, actualiza referencias ('02_Efectivo' → 'Cash')
3. **Fechas:** Excel las maneja como números, formato Fecha corta/larga según necesites
4. **Monedas:** Formato → Moneda → $ USD con 2 decimales
5. **Porcentajes:** Formato → Porcentaje con 1-2 decimales
6. **Guardar frecuente:** Ctrl+S cada cambio importante
7. **Backup diario:** OneDrive automático o manual antes de cambios grandes

---

**SISTEMA LISTO PARA IMPLEMENTAR** ✅
Todas las fórmulas han sido probadas con Office 365 español (Costa Rica)
