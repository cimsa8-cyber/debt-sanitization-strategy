# Especificación Técnica - Excel v3.0
## Sistema de Gestión Financiera CIMSA

**Versión:** 3.0
**Fecha:** 12 Noviembre 2025
**Deadline FASE 1 (MVP):** 19 Noviembre 2025 (7 días)
**Deadline FASE 3 (Completo):** 30 Noviembre 2025 (18 días)
**Responsable:** Álvaro Velasco (Owner) + Asistente Administrativa

---

## 📋 ÍNDICE

1. [Contexto y Objetivos](#contexto-y-objetivos)
2. [Arquitectura General](#arquitectura-general)
3. [Estructura de Hojas](#estructura-de-hojas)
4. [Seguridad y Permisos](#seguridad-y-permisos)
5. [Automatización](#automatización)
6. [Plan de Migración](#plan-de-migración)
7. [KPIs y Alertas](#kpis-y-alertas)

---

## 1. CONTEXTO Y OBJETIVOS

### Situación Crítica Actual

**Crisis de Liquidez:**
- Efectivo total: **$3,444.54** (9 cuentas bancarias)
- Gasto mensual promedio: **$8,000**
- **Cobertura: 12.9 DÍAS** (crítico < 30 días)

**Deuda Total: $45,432.58**
| Acreedor | Monto USD | Interés Mensual | Urgencia |
|----------|-----------|-----------------|----------|
| Hacienda (Renta + IVA) | $10,215.83 | 2.0% ($204/mes) | 🔴 BOMBA FISCAL |
| Tarjeta BNCR Visa 3519 | $12,866.76 | 2.1% ($270/mes) | 🔴 ALTA |
| Nissan Qashqai | $18,680.75 | 1.0% ($187/mes) | 🟡 MEDIA |
| Otras TC | $3,669.24 | Variable | 🟡 MEDIA |

**Problemas v2.0:**
- ✅ **$26,000+ en duplicados** detectados (45% ingresos inflados, 300% gastos inflados)
- ✅ Facturación REAL Nov: $9,466.42 (vs $17,188 reportado)
- ✅ Margen REAL: Positivo (vs -11.5% reportado por duplicados)
- ✅ 22 clientes activos (no 3 contratos como se creía)
- ✅ Categorización errónea (Sistema/Banco Promerica como "clientes")

### Objetivos v3.0

1. **Eliminar duplicados:** Sistema robusto de detección automática
2. **Visibilidad real-time:** Dashboard con métricas críticas
3. **Control IVA:** Hoja específica para cumplimiento fiscal
4. **Proyecciones:** Flujo de caja 6 meses adelante
5. **Multi-usuario:** Colaboración sin conflictos (OneDrive)
6. **Automatización:** Reducir trabajo manual de 2h/día a <15min/día

---

## 2. ARQUITECTURA GENERAL

### Archivo Único

**Nombre:** `AlvaroVelasco_Finanzas_v3.0.xlsx`
**Ubicación:** OneDrive (compartido)
**Formato:** .xlsx (Excel 2019+)
**Tamaño estimado:** <10 MB (optimizado)

### Capas de la Aplicación

```
┌─────────────────────────────────────────────┐
│  CAPA 1: ENTRADA DE DATOS                  │
│  - TRANSACCIONES (registro único)          │
│  - Validaciones + Dropdowns                 │
│  - Manual inline (comentarios celdas)      │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│  CAPA 2: PROCESAMIENTO                     │
│  - Fórmulas SUMIFS/COUNTIFS                │
│  - Tablas dinámicas                         │
│  - Detección duplicados                     │
│  - Cálculos IVA                             │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│  CAPA 3: VISUALIZACIÓN                     │
│  - DASHBOARD (KPIs críticos)                │
│  - EFECTIVO (conciliación bancaria)        │
│  - P&L automático                           │
│  - Reportes por cliente                     │
└─────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────┐
│  CAPA 4: AUTOMATIZACIÓN                    │
│  - 5 Macros VBA                             │
│  - 5 Scripts Python externos                │
│  - 4 Reportes PDF automáticos               │
└─────────────────────────────────────────────┘
```

### Organización de Hojas (15 tabs)

**PRIORIDAD 1 - FASE 1 (MVP):**
1. **DASHBOARD** - Vista ejecutiva (KPIs críticos)
2. **TRANSACCIONES** - Registro único de todas las operaciones
3. **EFECTIVO** - Conciliación bancaria (9 cuentas)
4. **CUENTAS_POR_COBRAR** - Aging de facturas pendientes
5. **CUENTAS_POR_PAGAR** - Vencimientos proveedores

**PRIORIDAD 2 - FASE 2:**
6. **IVA_CONTROL** - Cobrado vs Pagado (compliance Hacienda)
7. **PASIVOS** - Tarjetas + Nissan + Hacienda (proyecciones)
8. **UTILIDADES_MENSUALES** - P&L automático mensual

**PRIORIDAD 3 - FASE 3:**
9. **CLIENTES_VIP** - Top 10 clientes + CLV
10. **OPERACIONES** - Detalle por operación (margen individual)
11. **PROYECCIONES** - Flujo de caja 6 meses
12. **PRESUPUESTO** - Budget vs Actual
13. **PERSONAL** - Gastos personales (separados del negocio)

**UTILIDADES:**
14. **CONFIGURACION** - Listas desplegables, tipos de cambio
15. **NOTAS** - Registro de cambios, manual de usuario

---

## 3. ESTRUCTURA DE HOJAS

### 3.1 DASHBOARD (Vista Ejecutiva)

**Objetivo:** Métricas críticas en una sola vista, actualización automática.

**Secciones:**

#### A. Liquidez y Supervivencia
```
┌───────────────────────────────────────────────────────┐
│  💰 LIQUIDEZ - ZONA ROJA                              │
├───────────────────────────────────────────────────────┤
│  Efectivo Total:         $3,444.54                    │
│  Días de Cobertura:      12.9 días  ⚠️ CRÍTICO       │
│  Gasto Diario Prom:      $266.67                      │
│  Fecha Agotamiento:      25 Nov 2025                  │
└───────────────────────────────────────────────────────┘

Fórmulas:
- Efectivo Total: =SUMA(EFECTIVO!C2:C10)
- Gasto Diario: =PROMEDIO(gastos_ultimos_30_dias)/30
- Días Cobertura: =Efectivo_Total/Gasto_Diario
- Fecha Agotamiento: =HOY()+Dias_Cobertura

Formato Condicional:
- Días < 15: ROJO
- Días 15-30: AMARILLO
- Días > 30: VERDE
```

#### B. Deuda y Compromisos
```
┌───────────────────────────────────────────────────────┐
│  💳 DEUDA TOTAL: $45,432.58                           │
├───────────────────────────────────────────────────────┤
│  Hacienda (SIN PLAN):    $10,215.83  🔴              │
│  BNCR Visa 3519:         $12,866.76  🔴              │
│  Nissan Qashqai:         $18,680.75  🟡              │
│  Otras TC:               $3,669.24   🟡              │
│                                                        │
│  Intereses Mensuales:    $625/mes                     │
│  Pagos Actuales:         $556/mes                     │
│  Crecimiento Neto:       +$69/mes ⚠️                 │
└───────────────────────────────────────────────────────┘
```

#### C. Ingresos y Márgenes
```
┌───────────────────────────────────────────────────────┐
│  📊 NOVIEMBRE 2025                                    │
├───────────────────────────────────────────────────────┤
│  Facturación:            $9,466.42                    │
│  Clientes Activos:       22                           │
│  Ticket Promedio:        $430.29                      │
│                                                        │
│  TOP 3 Clientes (40.7%):                              │
│  1. Grupo Acción:        $1,680.00  (17.8%)          │
│  2. VWR:                 $1,400.00  (14.8%)          │
│  3. Mario Mora:          $764.50    (8.1%)           │
└───────────────────────────────────────────────────────┘
```

#### D. IVA y Hacienda
```
┌───────────────────────────────────────────────────────┐
│  🏛️ CUMPLIMIENTO FISCAL                               │
├───────────────────────────────────────────────────────┤
│  IVA Cobrado (Nov):      $1,230.63  (13%)            │
│  IVA Pagado (Nov):       $___.__                      │
│  IVA x Pagar:            $___.__                      │
│  Vencimiento:            15 Dic 2025  📅              │
│                                                        │
│  Deuda Hacienda:         $10,215.83                   │
│  Plan de Pago:           ❌ NO EXISTE                │
│  Crecimiento:            +$204/mes (2%)               │
└───────────────────────────────────────────────────────┘
```

**Color Coding:**
- 🔴 ROJO: Urgente, requiere acción inmediata
- 🟡 AMARILLO: Atención, monitorear de cerca
- 🟢 VERDE: Saludable, bajo control

---

### 3.2 TRANSACCIONES (Registro Único)

**Objetivo:** Punto único de verdad para TODAS las operaciones financieras.

**Columnas (20):**

| # | Columna | Tipo | Ejemplo | Validación | Editable |
|---|---------|------|---------|------------|----------|
| A | **Fecha** | Fecha | 2025-11-05 | FECHA() válida | ✅ AMARILLO |
| B | **Tipo** | Dropdown | Ingreso / Egreso / Transferencia | Lista CONFIGURACION!A2:A4 | ✅ AMARILLO |
| C | **Categoría** | Dropdown | Ingresos Operativos / COGS / Op.Expenses / Personal | Lista dinámica | ✅ AMARILLO |
| D | **Subcategoría** | Dropdown | Facturación / Compras / Sueldos | Depende de Categoría | ✅ AMARILLO |
| E | **Cuenta** | Dropdown | Promerica USD (40000003881774) | Lista EFECTIVO!B2:B10 | ✅ AMARILLO |
| F | **Entidad** | Texto Libre | VWR / Proveedor X / Álvaro Velasco | Autocompletar histórico | ✅ AMARILLO |
| G | **Concepto** | Texto Libre | Factura AR-003 / Compra insumos | Max 200 caracteres | ✅ AMARILLO |
| H | **Referencia** | Texto | AR-003 / Sinpe 12345 / TC#6789 | Única (COUNTIF) | ✅ AMARILLO |
| I | **Monto USD** | Número | 1,400.00 | >0 si USD | ✅ AMARILLO |
| J | **Monto CRC** | Número | 0 | >0 si CRC | ✅ AMARILLO |
| K | **Tipo Cambio** | Número | 517.80 | Auto desde web | 🔒 BLANCO |
| L | **Afecta Efectivo** | Dropdown | Sí / No / Pendiente | Para devengado | ✅ AMARILLO |
| M | **Fecha Efectivo** | Fecha | 2025-11-08 | Si Afecta=Sí | ✅ AMARILLO |
| N | **Estado** | Dropdown | Registrada / Conciliada / Pendiente / Cancelada | Workflow | ✅ AMARILLO |
| O | **ID Operación** | Texto | OP-2025-1145 | Auto-generado | 🔒 BLANCO |
| P | **Método Pago** | Dropdown | Transferencia / Efectivo / TC / Sinpe | Lista | ✅ AMARILLO |
| Q | **Comprobante** | Texto | Link/Path archivo | Ruta OneDrive | ✅ AMARILLO |
| R | **Notas** | Texto Libre | Observaciones internas | Max 500 caracteres | ✅ AMARILLO |
| S | **⚠️ Alerta Duplicado** | Fórmula | ⚠️ DUPLICADO | Auto-detección | 🔒 BLANCO |
| T | **Creado Por** | Fórmula | Álvaro / Asistente / Contador | Auto (usuario Windows) | 🔒 BLANCO |

**Fórmula Anti-Duplicados (Columna S):**
```excel
=SI(
  CONTAR.SI.CONJUNTO(
    $A:$A, A2,       // Misma fecha
    $E:$E, E2,       // Misma cuenta
    $I:$I, I2        // Mismo monto USD
  ) > 1,
  "⚠️ DUPLICADO",
  ""
)
```

**Formato Condicional:**
- ✅ AMARILLO: Celdas editables por usuarios
- 🔒 BLANCO: Celdas protegidas (fórmulas/auto-generadas)
- 🔴 ROJO: Duplicados detectados (fila completa)
- 🟡 NARANJA: Pendientes de conciliar

**Comentarios Inline (Notas de Celdas):**

Cada columna editable tendrá una nota con instrucciones:

```
Columna A - FECHA:
"Fecha de la operación (NO la fecha de registro).
Formato: DD/MM/AAAA
Ejemplo: 05/11/2025"

Columna E - CUENTA:
"Selecciona la cuenta bancaria exacta.
IMPORTANTE: Usa el nombre completo con número para evitar duplicados.
Ejemplo: Promerica USD (40000003881774)
Ver lista completa en hoja EFECTIVO"

Columna H - REFERENCIA:
"Número único de transacción.
- Facturas: AR-001, AR-002...
- Transferencias: Sinpe#12345
- Tarjeta: Comprobante TC#6789
DEBE SER ÚNICA (el sistema alertará duplicados)"
```

**Protección de Hoja:**
- Permitir insertar filas
- Permitir ordenar (solo usuarios autorizados)
- Bloquear eliminación de filas (evitar pérdida de datos)
- Permitir filtros

---

### 3.3 EFECTIVO (Conciliación Bancaria)

**Objetivo:** Saldos reales en tiempo real de las 9 cuentas bancarias.

**Estructura:**

| Cuenta | Saldo Inicial | Entradas | Salidas | Saldo Actual | Última Conciliación |
|--------|---------------|----------|---------|--------------|---------------------|
| Promerica USD (40000003881774) | EDITABLE | FÓRMULA | FÓRMULA | FÓRMULA | EDITABLE |

**Cuentas (9):**

1. Promerica USD (40000003881774) - Principal operativa
2. Promerica CRC (10000003881708) - Respaldo colones
3. BNCR USD #6638 - Cuenta personal/negocio
4. BNCR CRC #3076 - Colones varios
5. BNCR CRC Socios #8307 - Cuenta socios
6. BNCR USD Ahorro #2698 - Ahorro dólares
7. BNCR CRC Ahorro #5491 - Ahorro colones
8. Efectivo Físico USD - Caja chica
9. Efectivo Físico CRC - Caja chica colones

**Fórmulas:**

```excel
// ENTRADAS (columna C)
=SUMAR.SI.CONJUNTO(
  TRANSACCIONES!$I:$I,                    // Monto USD
  TRANSACCIONES!$E:$E, $A2,               // Cuenta = esta fila
  TRANSACCIONES!$B:$B, "Ingreso",         // Tipo = Ingreso
  TRANSACCIONES!$L:$L, "Sí"               // Afecta Efectivo = Sí
)

// SALIDAS (columna D)
=SUMAR.SI.CONJUNTO(
  TRANSACCIONES!$I:$I,
  TRANSACCIONES!$E:$E, $A2,
  TRANSACCIONES!$B:$B, "Egreso",
  TRANSACCIONES!$L:$L, "Sí"
)

// SALDO ACTUAL (columna E)
=B2 + C2 - D2

// DÍAS DE COBERTURA (debajo de la tabla)
=SUMA(E2:E10) / (gasto_diario_promedio)
```

**Validación Bancaria:**
- Columna F: "Saldo según Banco" (EDITABLE - manual mensual)
- Columna G: "Diferencia" = E - F
- Formato condicional: Si diferencia > $10 → ROJO (investigar)

---

### 3.4 CUENTAS_POR_COBRAR (Aging)

**Objetivo:** Tracking de facturas pendientes con antigüedad.

**Columnas:**

| Fecha Emisión | Cliente | Factura | Monto USD | Días Vencido | Aging | Estado | Notas |
|---------------|---------|---------|-----------|--------------|-------|--------|-------|
| 2025-11-01 | VWR | AR-001 | 1,400.00 | 11 | 0-15 | Pendiente | Contactado 10/11 |

**Categorías Aging:**
- **0-15 días:** Verde (normal)
- **16-30 días:** Amarillo (seguimiento)
- **31-60 días:** Naranja (urgente)
- **60+ días:** Rojo (crítico - cobro legal?)

**Fórmulas:**

```excel
// DÍAS VENCIDO (columna E)
=HOY() - A2

// AGING (columna F)
=SI(E2<=15, "0-15 días",
  SI(E2<=30, "16-30 días",
    SI(E2<=60, "31-60 días",
      "60+ días")))

// TOTAL POR AGING (resumen debajo)
=SUMAR.SI(F:F, "0-15 días", D:D)
```

**Dashboard CxC (parte superior):**
```
┌──────────────────────────────────────────┐
│  📋 CUENTAS POR COBRAR                   │
├──────────────────────────────────────────┤
│  Total Pendiente:    $_,___.__           │
│  0-15 días:          $_,___.__ (verde)   │
│  16-30 días:         $_,___.__ (amarillo)│
│  31-60 días:         $_,___.__ (naranja) │
│  60+ días:           $_,___.__ (rojo)    │
│                                           │
│  Promedio Cobro:     __ días             │
│  Cliente + Atrasado: [Nombre] (__días)   │
└──────────────────────────────────────────┘
```

---

### 3.5 IVA_CONTROL (Compliance Fiscal)

**Objetivo:** Evitar delito fiscal, control mensual IVA 13%.

**Estructura:**

| Mes | IVA Cobrado | IVA Pagado | IVA x Pagar | Fecha Límite | Estado | Comprobante |
|-----|-------------|------------|-------------|--------------|--------|-------------|
| Nov 2025 | $1,230.63 | $___.__ | $___.__ | 15 Dic 2025 | Pendiente | - |

**Fórmulas:**

```excel
// IVA COBRADO (columna B)
=SUMAR.SI.CONJUNTO(
  TRANSACCIONES!$I:$I,
  TRANSACCIONES!$B:$B, "Ingreso",
  TRANSACCIONES!$C:$C, "Ingresos Operativos",
  TRANSACCIONES!$A:$A, ">="&FECHA(2025,11,1),
  TRANSACCIONES!$A:$A, "<"&FECHA(2025,12,1)
) * 0.13

// IVA PAGADO (columna C)
=SUMAR.SI.CONJUNTO(
  TRANSACCIONES!$I:$I,
  TRANSACCIONES!$B:$B, "Egreso",
  TRANSACCIONES!$D:$D, "Compras",    // Solo compras con factura
  TRANSACCIONES!$A:$A, ">="&FECHA(2025,11,1),
  TRANSACCIONES!$A:$A, "<"&FECHA(2025,12,1)
) * 0.13

// IVA x PAGAR (columna D)
=B2 - C2

// DÍAS HASTA VENCIMIENTO
=E2 - HOY()
```

**Alertas Automáticas:**
- Si días < 7: ROJO + mensaje "⚠️ VENCE EN X DÍAS"
- Si días < 15: AMARILLO + mensaje "📅 Preparar declaración"
- Si Estado = "Atrasado": ROJO PARPADEANTE

**Sección Resumen:**
```
┌──────────────────────────────────────────┐
│  📊 RESUMEN IVA 2025                     │
├──────────────────────────────────────────┤
│  Total Cobrado:      $_,___.__           │
│  Total Pagado:       $_,___.__           │
│  Total x Pagar:      $_,___.__           │
│                                           │
│  Meses al Día:       __ / 12             │
│  Meses Atrasados:    __ ⚠️              │
│  Próximo Vencimiento: 15 Dic 2025        │
└──────────────────────────────────────────┘
```

---

## 4. SEGURIDAD Y PERMISOS

### 4.1 Compartir en OneDrive (Best Practices 2025)

**Configuración:**
1. Archivo guardado en: `OneDrive/CIMSA/Finanzas/`
2. Compartir usando botón "Share" (NO Legacy Shared Workbook)
3. Permisos por usuario:

| Usuario | Email | Rol | Permisos |
|---------|-------|-----|----------|
| Álvaro Velasco | alvaro@cimsa.com | Owner | Read/Write TODO |
| Asistente Admin | asistente@cimsa.com | Editor | Read/Write (excl. PASIVOS) |
| Contador | contador@cimsa.com | Viewer | Read Only |

**Pasos Compartir:**
```powershell
1. Abrir Excel → Share (esquina superior derecha)
2. Seleccionar "Get a Sharing Link"
3. Crear "Edit Link" para Asistente
4. Crear "View Link" para Contador
5. Enviar links por email seguro
```

### 4.2 Protección de Hojas

**Nivel 1 - Protección de Celdas:**

```vba
' Todas las celdas bloqueadas por defecto
Range("A:Z").Locked = True

' Desbloquear solo celdas AMARILLAS (editables)
Range("A2:A1000").Locked = False  ' Fecha
Range("B2:B1000").Locked = False  ' Tipo
' ... resto de columnas editables

' Celdas con fórmulas SIEMPRE bloqueadas
Range("S2:T1000").Locked = True   ' Duplicados, Creado Por
```

**Nivel 2 - Protección de Hoja:**

```vba
ActiveSheet.Protect Password:="CIMSA2025$", _
    DrawingObjects:=True, _
    Contents:=True, _
    Scenarios:=True, _
    AllowInsertingRows:=True, _      ' Permitir agregar transacciones
    AllowFiltering:=True, _          ' Permitir filtros
    AllowSorting:=False, _           ' SOLO Owner puede ordenar
    AllowDeletingRows:=False         ' Evitar borrado accidental
```

**Nivel 3 - Protección por Usuario (VBA):**

```vba
Sub CheckUserPermissions()
    Dim userName As String
    userName = Environ("USERNAME")

    ' Si NO es Álvaro, proteger hoja PASIVOS
    If userName <> "AlvaroVelasco" Then
        Sheets("PASIVOS").Visible = xlSheetVeryHidden
        Sheets("PERSONAL").Visible = xlSheetVeryHidden
    End If

    ' Si es Contador, bloquear TODO
    If userName = "Contador" Then
        For Each ws In ThisWorkbook.Worksheets
            ws.Protect Password:="CIMSA2025$"
        Next ws
    End If
End Sub
```

### 4.3 Control de Versiones

**Estrategia:**
- Guardar en OneDrive (versionado automático 25 versiones)
- Backup manual semanal: `AlvaroVelasco_Finanzas_v3.0_BACKUP_YYYY-MM-DD.xlsx`
- Git para scripts Python (ya implementado)

**Recuperación de Versión:**
```
1. Click derecho archivo en OneDrive
2. "Version History"
3. Seleccionar fecha/hora
4. "Restore" o "Open"
```

---

## 5. AUTOMATIZACIÓN

### 5.1 Macros VBA (5)

#### Macro #1: BotónConciliarBanco

**Función:** Comparar saldo calculado vs saldo real banco.

```vba
Sub BotónConciliarBanco()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("EFECTIVO")

    Dim cuenta As String
    Dim saldoCalculado As Double
    Dim saldoBanco As Double
    Dim diferencia As Double

    ' Pedir saldo banco al usuario
    cuenta = InputBox("¿Qué cuenta deseas conciliar?", "Conciliación Bancaria")
    saldoBanco = InputBox("Saldo según extracto bancario (USD):", "Saldo Real")

    ' Buscar cuenta en hoja EFECTIVO
    Dim fila As Long
    fila = Application.WorksheetFunction.Match(cuenta, ws.Range("A:A"), 0)

    ' Obtener saldo calculado
    saldoCalculado = ws.Cells(fila, 5).Value  ' Columna E

    ' Calcular diferencia
    diferencia = saldoCalculado - saldoBanco

    ' Registrar en hoja
    ws.Cells(fila, 6).Value = saldoBanco       ' Saldo Banco
    ws.Cells(fila, 7).Value = diferencia       ' Diferencia
    ws.Cells(fila, 8).Value = Date             ' Fecha conciliación

    ' Alertar si diferencia > $10
    If Abs(diferencia) > 10 Then
        MsgBox "⚠️ DIFERENCIA DETECTADA: $" & Format(diferencia, "#,##0.00") & vbCrLf & _
               "Revisar transacciones pendientes o duplicados.", vbExclamation, "Alerta Conciliación"
    Else
        MsgBox "✅ Cuenta conciliada correctamente." & vbCrLf & _
               "Diferencia: $" & Format(diferencia, "#,##0.00"), vbInformation, "Conciliación OK"
    End If
End Sub
```

**Uso:** Ejecutar al recibir extracto bancario (mensual).

---

#### Macro #2: BotónDetectarDuplicados

**Función:** Revisar TODAS las transacciones y marcar duplicados sospechosos.

```vba
Sub BotónDetectarDuplicados()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("TRANSACCIONES")

    Dim lastRow As Long
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row

    Dim duplicados As Long
    duplicados = 0

    Application.ScreenUpdating = False

    ' Recorrer todas las filas
    Dim i As Long
    For i = 2 To lastRow
        ' Si columna S contiene "DUPLICADO"
        If InStr(ws.Cells(i, 19).Value, "DUPLICADO") > 0 Then
            ' Marcar fila en ROJO
            ws.Rows(i).Interior.Color = RGB(255, 200, 200)
            duplicados = duplicados + 1
        End If
    Next i

    Application.ScreenUpdating = True

    ' Reporte final
    If duplicados > 0 Then
        MsgBox "⚠️ DUPLICADOS DETECTADOS: " & duplicados & " transacciones" & vbCrLf & _
               "Revisar filas marcadas en ROJO.", vbExclamation, "Alerta Duplicados"
    Else
        MsgBox "✅ No se detectaron duplicados.", vbInformation, "Sistema Limpio"
    End If
End Sub
```

**Uso:** Ejecutar después de importar datos desde v2.0 o fuentes externas.

---

#### Macro #3: BotónGenerarReportePDF

**Función:** Exportar DASHBOARD a PDF para enviar al contador.

```vba
Sub BotónGenerarReportePDF()
    Dim fileName As String
    Dim filePath As String

    ' Generar nombre archivo
    fileName = "Dashboard_CIMSA_" & Format(Date, "YYYY-MM-DD") & ".pdf"
    filePath = ThisWorkbook.Path & "\Reportes\" & fileName

    ' Exportar hoja DASHBOARD a PDF
    ThisWorkbook.Sheets("DASHBOARD").ExportAsFixedFormat _
        Type:=xlTypePDF, _
        fileName:=filePath, _
        Quality:=xlQualityStandard, _
        IncludeDocProperties:=True, _
        IgnorePrintAreas:=False, _
        OpenAfterPublish:=True

    MsgBox "✅ Reporte PDF generado:" & vbCrLf & filePath, vbInformation, "PDF Creado"
End Sub
```

**Uso:** Semanal (viernes) para revisar con equipo.

---

#### Macro #4: BotónActualizarTodo

**Función:** Recalcular todas las fórmulas + refrescar tablas dinámicas.

```vba
Sub BotónActualizarTodo()
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationAutomatic

    ' Recalcular todo
    Application.CalculateFull

    ' Refrescar tablas dinámicas (si existen)
    Dim pt As PivotTable
    Dim ws As Worksheet

    For Each ws In ThisWorkbook.Worksheets
        For Each pt In ws.PivotTables
            pt.RefreshTable
        Next pt
    Next ws

    Application.ScreenUpdating = True

    MsgBox "✅ Sistema actualizado completamente.", vbInformation, "Actualización OK"
End Sub
```

**Uso:** Al abrir el archivo cada día.

---

#### Macro #5: BotónConciliarIVA

**Función:** Verificar IVA mensual y alertar si faltan días para vencimiento.

```vba
Sub BotónConciliarIVA()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("IVA_CONTROL")

    Dim mesActual As String
    mesActual = Format(Date, "MMM YYYY")

    ' Buscar fila del mes actual
    Dim fila As Long
    On Error Resume Next
    fila = Application.WorksheetFunction.Match(mesActual, ws.Range("A:A"), 0)
    On Error GoTo 0

    If fila = 0 Then
        MsgBox "⚠️ No se encontró registro para " & mesActual, vbExclamation
        Exit Sub
    End If

    Dim ivaCobrado As Double
    Dim ivaPagado As Double
    Dim ivaPorPagar As Double
    Dim fechaLimite As Date
    Dim diasRestantes As Long

    ivaCobrado = ws.Cells(fila, 2).Value
    ivaPagado = ws.Cells(fila, 3).Value
    ivaPorPagar = ws.Cells(fila, 4).Value
    fechaLimite = ws.Cells(fila, 5).Value
    diasRestantes = fechaLimite - Date

    ' Construir mensaje
    Dim msg As String
    msg = "📊 RESUMEN IVA " & mesActual & vbCrLf & vbCrLf
    msg = msg & "IVA Cobrado:   $" & Format(ivaCobrado, "#,##0.00") & vbCrLf
    msg = msg & "IVA Pagado:    $" & Format(ivaPagado, "#,##0.00") & vbCrLf
    msg = msg & "IVA x Pagar:   $" & Format(ivaPorPagar, "#,##0.00") & vbCrLf & vbCrLf
    msg = msg & "Vencimiento:   " & Format(fechaLimite, "DD/MM/YYYY") & vbCrLf
    msg = msg & "Días Restantes: " & diasRestantes & " días"

    ' Alertar según urgencia
    If diasRestantes < 0 Then
        MsgBox msg & vbCrLf & vbCrLf & "🔴 ¡ATRASADO! Delito fiscal.", vbCritical, "IVA VENCIDO"
    ElseIf diasRestantes < 7 Then
        MsgBox msg & vbCrLf & vbCrLf & "⚠️ URGENTE: Pagar esta semana.", vbExclamation, "IVA Próximo a Vencer"
    ElseIf diasRestantes < 15 Then
        MsgBox msg & vbCrLf & vbCrLf & "📅 Preparar declaración.", vbInformation, "IVA Por Vencer"
    Else
        MsgBox msg & vbCrLf & vbCrLf & "✅ Tiempo suficiente.", vbInformation, "IVA OK"
    End If
End Sub
```

**Uso:** Ejecutar cada 1ra semana del mes.

---

### 5.2 Scripts Python (5)

#### Script #1: analizar_v2_y_migrar.py

**Función:** Analizar v2.0, detectar duplicados, migrar datos limpios a v3.0.

```python
import pandas as pd
import openpyxl
from datetime import datetime

# Ya existe: scripts/analizar_v2_metricas_completas.py
# Mejorarlo para incluir detección de duplicados y migración
```

**Mejoras necesarias:**
1. Detectar duplicados por (Fecha, Cuenta, Monto)
2. Reportar duplicados en CSV: `duplicados_v2_YYYY-MM-DD.csv`
3. Crear v3.0 limpio con solo transacciones únicas
4. Mapear categorías v2.0 → v3.0

---

#### Script #2: importar_xml_hacienda.py

**Función:** Leer facturas XML electrónicas Hacienda, extraer datos, agregar a TRANSACCIONES.

```python
import lxml.etree as ET
import openpyxl
from datetime import datetime

def parsear_xml_factura(xml_path):
    """
    Extrae datos de factura electrónica XML de Hacienda
    Retorna: dict con {fecha, cliente, monto, iva, referencia}
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Namespaces Hacienda
    ns = {
        'fe': 'https://cdn.comprobanteselectronicos.go.cr/xml-schemas/v4.3/facturaElectronica'
    }

    # Extraer datos
    fecha = root.find('.//fe:FechaEmision', ns).text
    cliente = root.find('.//fe:Receptor/fe:Nombre', ns).text
    total = float(root.find('.//fe:ResumenFactura/fe:TotalComprobante', ns).text)
    iva = float(root.find('.//fe:ResumenFactura/fe:TotalImpuesto', ns).text)
    clave = root.find('.//fe:Clave', ns).text

    return {
        'fecha': datetime.fromisoformat(fecha),
        'cliente': cliente,
        'monto_usd': total / 1.13,  # Quitar IVA
        'iva': iva,
        'referencia': clave[:20]  # Clave única Hacienda
    }

def agregar_a_transacciones(datos, excel_path):
    """
    Agrega factura a hoja TRANSACCIONES
    """
    wb = openpyxl.load_workbook(excel_path)
    ws = wb['TRANSACCIONES']

    # Buscar última fila
    last_row = ws.max_row + 1

    # Agregar transacción
    ws[f'A{last_row}'] = datos['fecha']
    ws[f'B{last_row}'] = 'Ingreso'
    ws[f'C{last_row}'] = 'Ingresos Operativos'
    ws[f'D{last_row}'] = 'Facturación'
    ws[f'E{last_row}'] = 'Por Definir'  # Usuario debe elegir cuenta
    ws[f'F{last_row}'] = datos['cliente']
    ws[f'G{last_row}'] = f"Factura Electrónica - {datos['referencia']}"
    ws[f'H{last_row}'] = datos['referencia']
    ws[f'I{last_row}'] = datos['monto_usd']
    ws[f'J{last_row}'] = 0
    ws[f'L{last_row}'] = 'Pendiente'  # Usuario debe confirmar cobro
    ws[f'N{last_row}'] = 'Registrada'
    ws[f'P{last_row}'] = 'Factura Electrónica'

    wb.save(excel_path)
    print(f"✅ Factura agregada: {datos['cliente']} - ${datos['monto_usd']:.2f}")

# Uso:
# python scripts/importar_xml_hacienda.py factura.xml
```

---

#### Script #3: proyectar_flujo_caja.py

**Función:** Proyección 6 meses basada en histórico + compromisos.

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def proyectar_flujo_caja(excel_path, meses=6):
    """
    Proyecta flujo de caja próximos N meses

    Entradas:
    - Promedio ingresos últimos 3 meses
    - Promedio egresos últimos 3 meses
    - Compromisos fijos (Nissan, TC, Hacienda)

    Salidas:
    - CSV con proyección mensual
    - Fecha estimada agotamiento efectivo
    """

    # Leer datos
    df_trans = pd.read_excel(excel_path, sheet_name='TRANSACCIONES')
    df_pasivos = pd.read_excel(excel_path, sheet_name='PASIVOS')

    # Calcular promedios (últimos 90 días)
    hoy = datetime.now()
    hace_90 = hoy - timedelta(days=90)

    df_reciente = df_trans[df_trans['Fecha'] >= hace_90]

    ingresos_prom = df_reciente[df_reciente['Tipo'] == 'Ingreso']['Monto USD'].sum() / 3
    egresos_prom = df_reciente[df_reciente['Tipo'] == 'Egreso']['Monto USD'].sum() / 3

    # Agregar compromisos fijos
    nissan = 800  # Mensual
    tc_min = 556  # Pago mínimo TC

    # Proyección
    proyeccion = []
    saldo_inicial = 3444.54  # Efectivo actual

    for mes in range(meses):
        fecha = hoy + timedelta(days=30 * mes)

        # Escenario conservador (90% ingresos, 110% egresos)
        ingresos_mes = ingresos_prom * 0.9
        egresos_mes = egresos_prom * 1.1 + nissan + tc_min

        flujo_neto = ingresos_mes - egresos_mes
        saldo_final = saldo_inicial + flujo_neto

        proyeccion.append({
            'Mes': fecha.strftime('%b %Y'),
            'Ingresos': ingresos_mes,
            'Egresos': egresos_mes,
            'Flujo Neto': flujo_neto,
            'Saldo Inicial': saldo_inicial,
            'Saldo Final': saldo_final,
            'Días Cobertura': (saldo_final / egresos_mes) * 30 if egresos_mes > 0 else 999
        })

        saldo_inicial = saldo_final

        # Alertar si saldo negativo
        if saldo_final < 0:
            print(f"⚠️ ALERTA: Efectivo se agota en {fecha.strftime('%b %Y')}")
            break

    # Guardar CSV
    df_proyeccion = pd.DataFrame(proyeccion)
    output_path = 'reportes/proyeccion_flujo_caja.csv'
    df_proyeccion.to_csv(output_path, index=False)

    print(f"✅ Proyección generada: {output_path}")
    return df_proyeccion

# Uso:
# python scripts/proyectar_flujo_caja.py
```

---

#### Script #4: analizar_margenes.py

**Función:** Calcular margen por cliente, operación, categoría.

*(Pendiente FASE 3)*

---

#### Script #5: reporte_ejecutivo.py

**Función:** Generar PDF ejecutivo con métricas clave.

*(Pendiente FASE 3 - requiere reportlab)*

---

## 6. PLAN DE MIGRACIÓN

### FASE 1: MVP (19 Nov 2025 - 7 días)

**Objetivo:** Sistema funcional básico para operación diaria.

**Entregables:**
1. ✅ Archivo `AlvaroVelasco_Finanzas_v3.0.xlsx` creado
2. ✅ Hojas: DASHBOARD, TRANSACCIONES, EFECTIVO, CxC, CxP
3. ✅ Migración datos Noviembre 2025 desde v2.0
4. ✅ Manual inline (comentarios en celdas)
5. ✅ Compartido en OneDrive con Asistente

**Criterio Éxito:**
- Asistente puede registrar facturas nuevas (<2 min)
- Dashboard muestra días de cobertura correcto (12.9 días)
- Sin duplicados en Noviembre

---

### FASE 2: Operación Crítica (26 Nov 2025 - 14 días)

**Objetivo:** Compliance fiscal + control deuda.

**Entregables:**
1. ✅ Hojas: IVA_CONTROL, PASIVOS, UTILIDADES_MENSUALES
2. ✅ Macro: BotónConciliarBanco
3. ✅ Macro: BotónConciliarIVA
4. ✅ Script: proyectar_flujo_caja.py

**Criterio Éxito:**
- IVA Noviembre calculado correctamente
- Proyección muestra cuándo se agota efectivo
- Conciliación bancaria mensual <30 min

---

### FASE 3: Sistema Completo (30 Nov 2025 - 18 días)

**Objetivo:** Automatización completa + análisis avanzado.

**Entregables:**
1. ✅ Hojas: CLIENTES_VIP, OPERACIONES, PROYECCIONES, PRESUPUESTO, PERSONAL
2. ✅ 5 Macros VBA funcionando
3. ✅ 5 Scripts Python funcionando
4. ✅ Importación XML Hacienda
5. ✅ Reportes PDF automáticos

**Criterio Éxito:**
- Trabajo diario <15 min (vs 2h actual)
- Reportes ejecutivos automáticos
- CLV por cliente calculado

---

### Estrategia Migración Datos

**Desde v2.0 a v3.0:**

1. **Transacciones Noviembre:**
   - Ejecutar: `python scripts/analizar_v2_y_migrar.py`
   - Revisar: `duplicados_v2_2025-11-12.csv`
   - Limpiar manualmente duplicados obvios
   - Importar a v3.0

2. **Saldos Iniciales (1 Nov 2025):**
   - EFECTIVO: Copiar saldos de v2.0 hoja "Bancos" al 31 Oct
   - CxC: Facturas pendientes al 31 Oct
   - CxP: Proveedores pendientes al 31 Oct
   - PASIVOS: Saldos TC + Nissan + Hacienda al 31 Oct

3. **Archivar v2.0:**
   - Renombrar: `AlvaroVelasco_Finanzas_v2.0_ARCHIVO_2025-11-12.xlsx`
   - Mover a: `OneDrive/CIMSA/Finanzas/Archivo/`
   - Marcar como Read-Only
   - Mantener disponible para consulta

---

## 7. KPIS Y ALERTAS

### 7.1 Umbrales Críticos

**Liquidez:**
| Métrica | Verde ✅ | Amarillo 🟡 | Rojo 🔴 |
|---------|----------|-------------|---------|
| Días de Cobertura | > 30 | 15-30 | < 15 |
| Efectivo Total | > $10k | $5k-$10k | < $5k |
| Gasto Diario | < $250 | $250-$350 | > $350 |

**CxC (Cuentas por Cobrar):**
| Métrica | Verde ✅ | Amarillo 🟡 | Rojo 🔴 |
|---------|----------|-------------|---------|
| Promedio Cobro | < 20 días | 20-40 días | > 40 días |
| % 60+ días | < 5% | 5%-15% | > 15% |
| Total CxC | < $8k | $8k-$15k | > $15k |

**IVA:**
| Métrica | Verde ✅ | Amarillo 🟡 | Rojo 🔴 |
|---------|----------|-------------|---------|
| Días para Vencer | > 15 | 7-15 | < 7 |
| Meses Atrasados | 0 | 1 | 2+ |
| IVA x Pagar | < $1,500 | $1,500-$3k | > $3k |

**Deuda:**
| Métrica | Verde ✅ | Amarillo 🟡 | Rojo 🔴 |
|---------|----------|-------------|---------|
| Ratio Deuda/Ingresos | < 3x | 3x-5x | > 5x |
| Crecimiento Deuda | < 0% | 0%-5% | > 5% |
| Pagos vs Intereses | > 150% | 100%-150% | < 100% |

### 7.2 Notificaciones Automáticas

**Diarias:**
- Si Días Cobertura < 15: Email a Álvaro
- Si nueva factura CxC > 30 días: Recordatorio cobro

**Semanales:**
- Resumen Dashboard (PDF) viernes 5pm
- Top 5 clientes semana vs promedio

**Mensuales:**
- IVA recordatorio (1ra semana mes)
- Conciliación bancaria (antes día 10)
- Reporte P&L (antes día 5)

---

## 8. TESTING Y VALIDACIÓN

### Test Cases FASE 1

1. **Registro Transacción:**
   - Usuario: Asistente
   - Acción: Agregar factura AR-023
   - Esperado: Se refleja en DASHBOARD, CxC, EFECTIVO

2. **Detección Duplicado:**
   - Acción: Agregar misma factura 2 veces
   - Esperado: Columna S muestra "⚠️ DUPLICADO", fila en ROJO

3. **Cálculo Días Cobertura:**
   - Efectivo: $3,444.54
   - Gasto diario prom: $266.67
   - Esperado: 12.9 días

4. **Multi-Usuario:**
   - Álvaro y Asistente editan simultáneamente
   - Esperado: Cambios se sincronizan sin conflictos

5. **Protección Hojas:**
   - Asistente intenta editar columna S (Duplicados)
   - Esperado: Error "Celda protegida"

---

## 9. MÉTRICAS DE ÉXITO

**Operacionales:**
- Tiempo diario trabajo: <15 min (vs 2h actual) - **87% reducción**
- Errores duplicados: 0 (vs $26k actual) - **100% eliminación**
- Tiempo conciliación: <30 min (vs 3h actual) - **83% reducción**

**Financieros:**
- Días cobertura: >30 (vs 12.9 actual) - **132% mejora**
- IVA compliance: 100% on-time (vs actual atrasado)
- Cobro CxC promedio: <25 días (medir baseline)

**Estratégicos:**
- Visibilidad real-time: 100% métricas actualizadas
- Confianza datos: 100% (vs 0% con duplicados)
- Decisiones data-driven: Reportes semanales ejecutivos

---

## 10. PRÓXIMOS PASOS (Orden de Ejecución)

### HOY (12 Nov 2025 - 18:00-23:00)

1. ✅ Commit esta especificación técnica
2. ⏳ Crear archivo Excel v3.0 vacío
3. ⏳ Implementar hoja TRANSACCIONES (20 columnas)
4. ⏳ Implementar hoja EFECTIVO (9 cuentas)
5. ⏳ Agregar comentarios inline (manual)

### MAÑANA (13 Nov 2025)

6. ⏳ Implementar hoja DASHBOARD (KPIs)
7. ⏳ Implementar hojas CxC y CxP
8. ⏳ Mejorar script `analizar_v2_y_migrar.py`
9. ⏳ Ejecutar migración Noviembre 2025
10. ⏳ Testing básico con Asistente

### SEMANA 1 (14-19 Nov 2025)

11. ⏳ Compartir en OneDrive + permisos
12. ⏳ Implementar Macros #1 y #2
13. ⏳ Hojas IVA_CONTROL y PASIVOS
14. ⏳ Testing completo FASE 1
15. ⏳ **ENTREGA MVP** (19 Nov)

---

**FIN DE ESPECIFICACIÓN TÉCNICA v3.0**

---

## Apéndice A: Glosario

- **CLV:** Customer Lifetime Value (valor del cliente a lo largo de su vida)
- **COGS:** Cost of Goods Sold (costo de ventas)
- **CxC:** Cuentas por Cobrar
- **CxP:** Cuentas por Pagar
- **P&L:** Profit & Loss (Estado de Resultados)
- **IVA:** Impuesto al Valor Agregado (13% en Costa Rica)

## Apéndice B: Referencias

- Excel OneDrive Multi-User Best Practices 2025
- Financial KPI Dashboard Design Standards
- Costa Rica Hacienda XML Schema v4.3
- VBA Protection Patterns

## Apéndice C: Contactos

- Owner: Álvaro Velasco
- Asistente: [Nombre]
- Contador: [Nombre]
- Soporte Técnico: [Contacto]
