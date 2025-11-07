# GUÍA DE IMPLEMENTACIÓN PASO A PASO
## Sistema Financiero Excel - AlvaroVelasco.Net SRL

**Fecha:** 07 de Noviembre 2025
**Tiempo estimado total:** 3-4 horas
**Prerequisitos:** Office 365, archivos CSV en carpeta EXCEL_TEMPLATES/

---

## FASE 0: PREPARACIÓN (15 minutos)

### Paso 1: Verificar archivos necesarios
Asegúrate de tener estos archivos en la carpeta `EXCEL_TEMPLATES/`:

```
✅ EMPRESA_01_Dashboard.csv
✅ EMPRESA_02_Efectivo.csv
✅ EMPRESA_03_Ahorros.csv
✅ EMPRESA_04_CuentasPorCobrar.csv
✅ EMPRESA_05_CuentasPorPagar.csv
✅ EMPRESA_06_TarjetasCredito.csv
✅ EMPRESA_07_GastosFijos.csv
✅ EMPRESA_08_Presupuesto.csv
✅ EMPRESA_10_KPIs.csv
✅ EMPRESA_11_Hacienda.csv
✅ EMPRESA_12_Nissan.csv
✅ EMPRESA_13_AhorroVivienda.csv
✅ FORMULAS_EXCEL_COMPLETAS.md
```

### Paso 2: Crear carpeta de trabajo
```
C:\Finanzas\
  ├─ AlvaroVelascoNet_EMPRESA.xlsx (crearás ahora)
  ├─ Backups\
  └─ Importados\
```

### Paso 3: Abrir Excel
1. Abrir Excel (Office 365)
2. Crear libro nuevo
3. Guardar como: `C:\Finanzas\AlvaroVelascoNet_EMPRESA.xlsx`

---

## FASE 1: CREAR ESTRUCTURA BASE (30 minutos)

### Paso 1: Crear pestañas
Renombrar y crear 15 pestañas en este orden:

1. **Dashboard** (renombrar "Hoja1")
2. **Efectivo** (insertar nueva)
3. **Ahorros** (insertar nueva)
4. **A/R** (insertar nueva)
5. **A/P** (insertar nueva)
6. **TC** (insertar nueva)
7. **GastosFijos** (insertar nueva)
8. **Presupuesto** (insertar nueva)
9. **Proyeccion90** (insertar nueva)
10. **KPIs** (insertar nueva)
11. **Hacienda** (insertar nueva)
12. **Nissan** (insertar nueva)
13. **Vivienda** (insertar nueva)
14. **Analisis** (insertar nueva)
15. **Config** (insertar nueva)

**Cómo crear pestaña:**
- Clic derecho en pestaña → Insertar → Hoja de cálculo
- Doble clic en nombre → Escribir nuevo nombre

**Cómo colorear pestañas (opcional):**
- Clic derecho → Color de pestaña
- Dashboard: Azul oscuro
- Efectivo/Ahorros/A/R: Verde
- A/P/TC: Rojo
- Gastos/Presupuesto: Naranja
- Proyección/KPIs: Morado
- Resto: Gris

### Paso 2: Configurar pestaña Config
Ir a pestaña **Config** y crear:

**Tabla de parámetros:**
```
A1: Parámetro          B1: Valor
A2: TC_USDCRC          B2: 507
A3: Tasa_TC_BNCR       B3: 0.30
A4: Tasa_TC_BNCR_Alta  B4: 0.32
A5: Tasa_TC_BAC        B5: 0.26
A6: Tasa_Nissan        B6: 0.12
A7: Alerta_Efectivo    B7: 1000
A8: Alerta_AR_Dias     B8: 60
```

**Crear nombres de rango:**
1. Seleccionar B2
2. Cuadro de nombres (izquierda arriba) → Escribir: `TC_USDCRC`
3. Enter
4. Repetir para B3-B8

**Agregar instrucciones:**
```
A10: INSTRUCCIONES DE USO
A12: DIARIO (5-10 minutos):
A13: 1. Registrar movimientos efectivo en pestaña Efectivo
A14: 2. Revisar Dashboard - verificar alertas
A15: 3. Si hay cobros: actualizar A/R
A16: 4. Si hay pagos: actualizar A/P
```

(Continúa con instrucciones semanales y mensuales)

---

## FASE 2: IMPORTAR DATOS (45 minutos)

### Método A: Importación CSV (Recomendado)

**Para cada pestaña (Dashboard, Efectivo, Ahorros, etc.):**

1. **Ir a la pestaña correspondiente**
2. **Datos → Obtener datos → Desde archivo → Desde texto/CSV**
3. **Seleccionar archivo CSV** (ej: `EMPRESA_02_Efectivo.csv`)
4. **Vista previa** → Verificar que se vea bien
5. **Cargar datos**
   - Si pregunta delimitador: Coma `,`
   - Si pregunta encoding: UTF-8
6. **Ajustar columnas:**
   - Seleccionar todas (Ctrl+A)
   - Inicio → Formato → Ajustar ancho columna
7. **Repetir** para todas las pestañas

**Orden recomendado:**
1. Config (manual)
2. Dashboard
3. Efectivo
4. Ahorros
5. A/R
6. A/P
7. TC
8. GastosFijos
9. Presupuesto
10. KPIs
11. Hacienda
12. Nissan
13. Vivienda

### Método B: Copy-Paste (Alternativo)

Si CSV no funciona:

1. **Abrir archivo CSV** con Bloc de notas
2. **Copiar todo** (Ctrl+A, Ctrl+C)
3. **En Excel, seleccionar celda A1**
4. **Pegar** (Ctrl+V)
5. **Datos → Texto en columnas**
6. **Delimitado → Coma → Finalizar**

---

## FASE 3: APLICAR FÓRMULAS (60 minutos)

### Paso 1: Abrir guía de fórmulas
Abrir archivo `FORMULAS_EXCEL_COMPLETAS.md` en otra ventana/monitor

### Paso 2: Pestaña EFECTIVO

**Celda H1:** `Balance USD`

**Celda H2:** (si F2 tiene valor de entrada)
```excel
=SI(F2>0, F2, -G2)
```

**Celda H3:**
```excel
=H2 + F3 - G3
```

**Arrastrar H3 hacia abajo:**
- Seleccionar H3
- Clic en esquina inferior derecha (cuadrito)
- Arrastrar hasta fila 100 (o donde terminen tus datos)

**Celda H200 (resumen abajo):**
```excel
=SUMAR.SI(H:H,">0")
```

**Formato:**
- Seleccionar columnas F, G, H
- Inicio → Número → Moneda → $ Inglés (Estados Unidos)
- 2 decimales

### Paso 3: Pestaña AHORROS

**Celda C6 (Total):**
```excel
=SUMA(C2:C5)
```

**Formato:**
- Columna C: Moneda USD, 2 decimales

### Paso 4: Pestaña A/R (Cuentas por Cobrar)

**Celda B28 (Total A/R):**
```excel
=SUMA(B2:B27)
```

**Celda I2 (Alerta por prioridad):**
```excel
=SI(E2="CRÍTICA", "🔴 COBRAR HOY", SI(E2="ALTA", "🟠 Esta semana", ""))
```

**Arrastrar I2 hacia abajo** hasta fila 27

**Formato:**
- Columna B: Moneda USD
- Columna C: Porcentaje 1 decimal

### Paso 5: Pestaña A/P (Cuentas por Pagar)

**Celda F2 (Días para vencer):**
```excel
=SI(E2="", "", E2-HOY())
```

**Celda G2 (Días mora):**
```excel
=SI(E2="", "", SI(E2<HOY(), HOY()-E2, 0))
```

**Celda H2 (Estado automático):**
```excel
=SI(G2>0, "VENCIDO", SI(F2<=15, "PRÓXIMO", "VIGENTE"))
```

**Arrastrar F2:H2** hacia abajo hasta fila 10

**Celda C11 (Total A/P):**
```excel
=SUMA(C2:C10)
```

**Formato:**
- Columna C: Moneda USD
- Columna E: Fecha corta

### Paso 6: Pestaña TC (Tarjetas Crédito)

**Celda F2 (Pago mínimo 6%):**
```excel
=D2*0.06
```

**Celda G2 (Intereses mes):**
```excel
=D2*(E2/12)
```
**IMPORTANTE:** Si columna E está como "32%", cambiar a decimal:
- Seleccionar E2:E6
- Reemplazar "%" por nada
- Dividir entre 100
- O manual: E2 = 0.32

**Celda D7 (Total saldo TC):**
```excel
=SUMA(D2:D6)
```

**Celda D8 (Total vencido):**
```excel
=SUMAR.SI(H:H, "VENCIDA", D:D)
```

**Arrastrar F2:G2** hacia abajo hasta fila 6

**Formato:**
- Columna D, F, G: Moneda USD
- Columna E: Porcentaje 0 decimales

### Paso 7: Pestaña GASTOS FIJOS

**Celda B9 (Total gastos fijos):**
```excel
=SUMA(B2:B8)
```

**Celda E2 (% de cada gasto):**
```excel
=B2/$B$9*100
```

**Arrastrar E2** hacia abajo hasta fila 8

**Formato:**
- Columna B: Moneda USD
- Columna E: Porcentaje 1 decimal

### Paso 8: Pestaña PRESUPUESTO

**Celda D2 (% Usado):**
```excel
=SI(B2=0, 0, C2/B2*100)
```

**Celda E2 (Variación):**
```excel
=C2-B2
```

**Celda G2 (Alerta exceso):**
```excel
=SI(Y(F2="SÍ", C2>B2), "⚠️ EXCEDIDO", "")
```

**Arrastrar D2:G2** hacia abajo hasta filas de datos

**Fórmulas de totales:**
```excel
B7:  =SUMA(B2:B6)          (Total fijos)
B14: =SUMA(B8:B13)         (Total variables)
B15: =B7+B14               (Total gastos)
B19: =B17-B15              (Resultado)
C20: =B19/B17*100          (% Margen)
```

**Formato:**
- Columnas B, C, E: Moneda USD
- Columna D: Porcentaje 1 decimal

### Paso 9: Pestaña KPIs

**Celda B2 (Razón Corriente):**
```excel
=(Efectivo!H200 + Ahorros!C6 + 'A/R'!B28) / (TC!D7 + 'A/P'!C11 + 533.92 + 9265.71 + 19197.69)
```

**Celda B3 (Días Cobertura):**
```excel
=Efectivo!H200 / (GastosFijos!B9 / 30)
```

**Celda B5 (Working Capital):**
```excel
=(Efectivo!H200 + Ahorros!C6 + 'A/R'!B28) - (TC!D7 + 'A/P'!C11)
```

**Celda B6 (% TC Vencidas):**
```excel
=TC!D8 / TC!D7 * 100
```

**Celda B7 (Ratio Deuda/Activos):**
```excel
=(TC!D7 + 'A/P'!C11 + 533.92 + 9265.71 + 19197.69) / (Efectivo!H200 + Ahorros!C6 + 'A/R'!B28)
```

**Celda B8 (% A/R Top 2):**
```excel
=('A/R'!B2 + 'A/R'!B3) / 'A/R'!B28 * 100
```

(Continuar con otros KPIs según FORMULAS_EXCEL_COMPLETAS.md)

**Formato:**
- B2, B5, B7: Número 2 decimales
- B3: Número 1 decimal + " días" (personalizado)
- B6, B8: Porcentaje 1 decimal

### Paso 10: Pestaña HACIENDA

**Celda D3 (Total IVA):**
```excel
=SUMA(D2:D3)
```

**Celda D9 (Total ISR):**
```excel
=SUMA(D5:D9)
```

**Celda D10 (Total Hacienda):**
```excel
=D3 + D9
```

**Celda F2 (Días mora IVA):**
```excel
=HOY() - E2
```

**Formato:**
- Columna D: Moneda USD
- Columna E: Fecha corta
- Columna F: Número 0 decimales

### Paso 11: Pestaña NISSAN

**Escenario 1 (Solo mínimo):**

**Celda C2 (Interés mes 1):**
```excel
=B2 * (0.12 / 12)
```

**Celda D2 (Principal mes 1):**
```excel
=$B$1 - C2
```
Donde B1 = 800 (cuota)

**Celda E2 (Saldo final mes 1):**
```excel
=B2 - D2
```

**Celda B3 (Saldo inicial mes 2):**
```excel
=E2
```

**Arrastrar filas 2-3** hacia abajo 24 meses

**Celda C26 (Total intereses):**
```excel
=SUMA(C2:C25)
```

**Repetir** para Escenario 2 y 3 con cuotas $1000 y $1500

**Formato:**
- Todas columnas moneda USD 2 decimales

### Paso 12: Pestaña VIVIENDA

**Celda D2 (% Progreso actual):**
```excel
=C2 / 45000 * 100
```

**Celda C7 (Balance fin fase 1):**
```excel
=C1 + D7
```
Donde D7 = suma aportes fase 1

**Repetir** lógica para fase 2 y 3

**Celda D26 (% Final):**
```excel
=C26 / 45000 * 100
```

**Formato:**
- Columna C: Moneda USD
- Columna D: Porcentaje 1 decimal

### Paso 13: Guardar progreso
**Ctrl+S** - Guardar archivo

---

## FASE 4: FORMATO CONDICIONAL (30 minutos)

### Paso 1: Efectivo - Alerta bajo

**Seleccionar rango:** H2:H200

**Inicio → Formato condicional → Nueva regla → Usar fórmula:**
```excel
=H2<1000
```

**Formato:**
- Relleno: Rojo claro (#FFC7CE)
- Texto: Rojo oscuro (#9C0006)

**Agregar segunda regla (muy bajo):**
```excel
=H2<500
```
- Relleno: Rojo oscuro (#C00000)
- Texto: Blanco
- Negrita

### Paso 2: A/R - Por prioridad

**Seleccionar:** Filas 2 a 27 completas (clic en número de fila 2, Shift+clic en 27)

**Nueva regla → Usar fórmula:**
```excel
=$E2="CRÍTICA"
```
- Relleno: Rojo muy claro (#FFD1DC)

**Nueva regla:**
```excel
=$E2="ALTA"
```
- Relleno: Naranja claro (#FFE5CC)

### Paso 3: A/P - Estado vencido

**Seleccionar:** Filas 2 a 10 completas

**Nueva regla:**
```excel
=$H2="VENCIDO"
```
- Relleno: Rojo claro (#FFC7CE)
- Texto: Rojo oscuro

**Nueva regla:**
```excel
=$H2="PRÓXIMO"
```
- Relleno: Amarillo claro (#FFEB9C)

### Paso 4: TC - Vencidas

**Seleccionar:** Filas 2 a 6 completas

**Nueva regla:**
```excel
=$H2="VENCIDA"
```
- Relleno: Rojo claro (#FFC7CE)
- Texto: Rojo oscuro

### Paso 5: Presupuesto - Excedido

**Seleccionar:** Filas 2 a 15 completas

**Nueva regla:**
```excel
=Y($F2="SÍ", $C2>$B2)
```
- Relleno: Rojo (#C00000)
- Texto: Blanco
- Negrita

**Nueva regla (Cerca límite 80%):**
```excel
=Y($F2="NO", $D2>0.8)
```
- Relleno: Naranja claro

### Paso 6: KPIs - Valores críticos

**Seleccionar B2 (Razón Corriente):**

**Nueva regla:**
```excel
=B2<1
```
- Relleno: Rojo claro

**Nueva regla:**
```excel
=Y(B2>=1, B2<1.5)
```
- Relleno: Amarillo

**Nueva regla:**
```excel
=B2>=1.5
```
- Relleno: Verde claro

**Repetir** para otros KPIs con umbrales apropiados

### Paso 7: Guardar
**Ctrl+S**

---

## FASE 5: VALIDACIÓN DE DATOS (20 minutos)

### Paso 1: Efectivo - Columna Categoría

**Seleccionar:** E2:E500

**Datos → Validación de datos**
- Permitir: Lista
- Origen: `APERTURA,INGRESO,GASTO,TRANSFER,AJUSTE`
- ✅ Mostrar mensaje de entrada (opcional)
- ✅ Mostrar mensaje de error

**OK**

### Paso 2: Efectivo - Columna Banco

**Seleccionar:** B2:B500

**Validación:**
- Lista: `Promerica,BNCR,BAC,Efectivo,Otro`

### Paso 3: A/R - Columna Prioridad

**Seleccionar:** E2:E100

**Validación:**
- Lista: `CRÍTICA,ALTA,MEDIA,BAJA,NINGUNA`

### Paso 4: A/P - Columna Estado

**Seleccionar:** H2:H100

**Validación:**
- Lista: `VENCIDO,PRÓXIMO,VIGENTE`

### Paso 5: A/P - Columna Prioridad

**Seleccionar:** I2:I100

**Validación:**
- Lista: `CRÍTICA,ALTA,MEDIA,NORMAL`

### Paso 6: TC - Columna Estado

**Seleccionar:** H2:H20

**Validación:**
- Lista: `VENCIDA,ACTIVA,CANCELADA`

### Paso 7: Presupuesto - Límite Rígido

**Seleccionar:** F2:F20

**Validación:**
- Lista: `SÍ,NO`

### Paso 8: Guardar
**Ctrl+S**

---

## FASE 6: CREAR DASHBOARD (40 minutos)

### Paso 1: Ir a pestaña Dashboard

### Paso 2: Vincular datos principales

**Celda B2 (Efectivo HOY):**
```excel
=Efectivo!H200
```

**Celda B3 (Cobertura días):**
```excel
=KPIs!B3
```

**Celda B5 (Recursos totales):**
```excel
=Efectivo!H200 + Ahorros!C6 + 'A/R'!B28
```

**Celda B10 (Deuda total):**
```excel
=TC!D7 + 'A/P'!C11 + Hacienda!D10 + Nissan!B2
```

**Celda B16 (Déficit):**
```excel
=B5 - B10
```

**Celda B17 (Razón Corriente):**
```excel
=KPIs!B2
```

### Paso 3: Vincular alertas

**Celda E2 (Alerta TC vencidas):**
```excel
="🔴 " & CONTAR.SI(TC!H:H, "VENCIDA") & " TC BNCR vencidas: $" & TEXTO(TC!D8, "#,##0.00")
```

**Celda E3 (Alerta IVA):**
```excel
="🔴 IVA vencido: $" & TEXTO(Hacienda!D3, "#,##0.00") & " (" & Hacienda!F2 & " días mora)"
```

**Celda E4 (Alerta A/P):**
```excel
="🔴 A/P vencido: $" & TEXTO(SUMAR.SI('A/P'!H:H, "VENCIDO", 'A/P'!C:C), "#,##0.00")
```

### Paso 4: Top 5 clientes/proveedores

**Celdas D20:E24** - Vincular a pestaña A/R:
```excel
D20: ='A/R'!A2
E20: ='A/R'!B2
F20: ='A/R'!C2
```
Arrastrar hacia abajo 5 filas

**Celdas H20:I22** - Top 3 proveedores A/P (similar)

### Paso 5: Formato Dashboard

**Títulos principales** (A1, A2, D1):
- Fuente: Calibri 18pt negrita
- Color: Azul oscuro

**Secciones** (A3, A6, etc.):
- Fuente: Calibri 14pt negrita
- Fondo: Gris claro

**Valores principales** (B2, B5, B10):
- Fuente: Calibri 16pt negrita
- Formato: Moneda USD

**Alertas** (E2:E5):
- Fuente: Calibri 11pt
- Sin bordes

**Agregar bordes:**
- Seleccionar rangos importantes
- Inicio → Bordes → Todos los bordes

### Paso 6: Crear gráfico Efectivo Trending

**Insertar → Gráficos → Línea**

**Datos:**
- Crear tabla temporal en Analisis con:
  - Columna A: Fechas últimos 12 meses
  - Columna B: Balance efectivo cada mes

**Seleccionar datos → Crear gráfico → Copiar a Dashboard**

**Ajustar:**
- Título: "Evolución Efectivo 12 Meses"
- Eje Y: Formato moneda
- Sin leyenda
- Posición: Lado derecho Dashboard

### Paso 7: Crear gráfico Composición Gastos

**Insertar → Gráficos → Circular**

**Datos:** GastosFijos tabla resumen por categoría

**Copiar a Dashboard**

**Ajustar:**
- Título: "Distribución Gastos Fijos"
- Etiquetas: Porcentaje + Categoría
- Colores diferenciados

### Paso 8: Guardar
**Ctrl+S**

---

## FASE 7: VERIFICACIÓN Y PRUEBAS (30 minutos)

### Checklist de verificación:

#### ✅ Fórmulas funcionando
- [ ] Efectivo: Balance running calculado correctamente
- [ ] A/R: Total suma $10,866.42
- [ ] A/P: Total suma $6,103.66
- [ ] TC: Total suma $16,382.69
- [ ] KPIs: Razón Corriente = 0.451
- [ ] Dashboard: Todos los valores vinculados

#### ✅ Formato condicional
- [ ] Efectivo bajo: Celdas <$1000 en rojo claro
- [ ] A/R CRÍTICA: Filas en rojo claro
- [ ] A/P VENCIDO: Filas en rojo claro
- [ ] TC VENCIDA: Filas en rojo claro

#### ✅ Validación de datos
- [ ] Efectivo categoría: Lista desplegable funciona
- [ ] A/R prioridad: Lista desplegable funciona
- [ ] A/P estado: Lista desplegable funciona

#### ✅ Dashboard
- [ ] Efectivo HOY: $4,302.10
- [ ] Recursos totales: $23,222.49
- [ ] Deuda total: $51,483.67
- [ ] Déficit: -$28,261.18
- [ ] Gráficos visibles y correctos

### Prueba de funcionamiento:

**1. Agregar movimiento efectivo:**
- Ir a Efectivo
- Última fila vacía
- Fecha: HOY()
- Banco: Promerica
- Concepto: "Prueba sistema"
- Categoría: INGRESO
- Entrada: $100
- Balance: Debe calcular automáticamente

**Verificar:**
- Balance actualizado correctamente
- Dashboard refleja nuevo efectivo

**2. Si funciona correctamente:**
- Eliminar fila de prueba
- Guardar

**3. Si NO funciona:**
- Revisar fórmula celda H (debe ser H anterior + entrada - salida)
- Ver FORMULAS_EXCEL_COMPLETAS.md sección Efectivo

---

## FASE 8: BACKUP Y CONFIGURACIÓN FINAL (15 minutos)

### Paso 1: Crear backup inicial

**Archivo → Guardar como:**
```
C:\Finanzas\Backups\AlvaroVelascoNet_EMPRESA_INICIAL_07NOV2025.xlsx
```

### Paso 2: Configurar OneDrive (si Office 365)

1. **Archivo → Compartir → Guardar en la nube**
2. **Seleccionar OneDrive**
3. **Carpeta:** `Finanzas/`
4. **Guardar**

**Configurar sincronización automática:**
- OneDrive → Configuración
- ✅ Sincronizar carpeta Finanzas
- ✅ Activar versionado (mantener 30 versiones)

### Paso 3: Proteger fórmulas

**Para cada pestaña con fórmulas:**

1. **Ctrl+A** (seleccionar todo)
2. **Inicio → Formato → Formato de celdas**
3. **Protección → ☐ Bloqueada** (desmarcar)
4. **OK**

5. **Seleccionar solo celdas con fórmulas:**
   - Ctrl+G
   - Especial → Fórmulas
   - OK

6. **Inicio → Formato → Formato de celdas**
7. **Protección → ☑ Bloqueada** (marcar)
8. **OK**

9. **Revisar → Proteger hoja**
10. **Contraseña:** (dejar vacío o poner simple)
11. **✅ Seleccionar celdas bloqueadas**
12. **✅ Seleccionar celdas desbloqueadas**
13. **OK**

**Resultado:** Puedes editar datos, pero NO borrar/cambiar fórmulas accidentalmente

### Paso 4: Configurar impresión

**Pestaña Dashboard:**

1. **Diseño de página → Orientación → Horizontal**
2. **Diseño de página → Tamaño → Carta**
3. **Diseño de página → Área de impresión → Establecer**
4. **Vista previa de impresión** (Ctrl+P)
5. **Ajustar** para que todo quepa en 1 página

### Paso 5: Crear acceso directo

**Escritorio Windows:**

1. Clic derecho en `AlvaroVelascoNet_EMPRESA.xlsx`
2. Enviar a → Escritorio (crear acceso directo)
3. Renombrar: "💰 Finanzas Empresa"

### Paso 6: Guardar final
**Ctrl+S**

---

## FASE 9: USO DIARIO (Desde mañana)

### RUTINA DIARIA (5-10 minutos)

**1. Abrir archivo**
- Doble clic en acceso directo escritorio
- O abrir desde OneDrive

**2. Ir a Dashboard**
- Verificar alertas críticas
- Ver efectivo actual
- Revisar cobertura días

**3. Registrar movimientos del día**

**Si hubo ingresos:**
- Ir a pestaña Efectivo
- Última fila vacía
- Fecha, Banco, Concepto, Categoría=INGRESO, Entrada=monto
- Balance se calcula automático

**Si hubo gastos:**
- Ir a pestaña Efectivo
- Última fila vacía
- Fecha, Banco, Concepto, Categoría=GASTO, Salida=monto
- Balance se calcula automático

**Si cobraste factura:**
- Ir a pestaña A/R
- Buscar cliente
- Reducir monto o poner $0.00
- Agregar nota en columna Notas: "Cobrado 08/11/2025"
- IR A Efectivo y registrar el ingreso

**Si pagaste proveedor:**
- Ir a pestaña A/P
- Buscar factura
- Reducir monto o poner $0.00
- Agregar nota: "Pagado 08/11/2025"
- IR A Efectivo y registrar el gasto

**4. Guardar**
- Ctrl+S
- OneDrive sincroniza automático

**5. Cerrar**

---

### RUTINA SEMANAL (Lunes, 15 minutos)

**1. Revisar A/R**
- Identificar CRÍTICAS y ALTAS
- Enviar correos recordatorio
- Hacer llamadas de seguimiento
- Actualizar columna "Fecha Contacto"

**2. Revisar A/P**
- Ver próximos vencimientos (15 días)
- Programar pagos
- Si necesario: negociar extensiones

**3. Revisar TC**
- Verificar pagos mínimos realizados
- Ajustar plan sanitización si hubo cambios

**4. Actualizar Proyección 90 días**
- Pestaña Proyeccion90
- Ajustar ingresos esperados
- Revisar escenarios

**5. Guardar**

---

### RUTINA MENSUAL (Día 1 del mes, 30 minutos)

**1. Cerrar mes anterior**

**Presupuesto:**
- Ir a pestaña Presupuesto
- Copiar Real del mes
- Pegar en nueva tabla histórica (columna siguiente)
- Resetear columna Real a $0.00
- Ver variaciones
- Ajustar presupuesto próximo mes si necesario

**2. Actualizar TC**
- Ir a apps bancos
- Verificar saldos reales
- Actualizar columna D (Saldo USD)
- Verificar pagos mínimos

**3. Actualizar Nissan**
- Verificar saldo real
- Actualizar proyección

**4. Actualizar Hacienda**
- Declarar IVA mes anterior
- Pagar IVA
- Actualizar estado arreglo ISR

**5. Actualizar Vivienda**
- Si hubo ahorro, actualizar monto
- Verificar % progreso

**6. Revisar KPIs**
- Dashboard completo
- Comparar con mes anterior
- Identificar mejoras/empeoramientos

**7. Backup mensual**
```
C:\Finanzas\Backups\AlvaroVelascoNet_EMPRESA_MES11_2025.xlsx
```

**8. Guardar**

---

## FASE 10: POWER BI (OPCIONAL - 2 horas)

### Prerequisitos:
- Power BI Desktop instalado (gratis)
- Archivo Excel en OneDrive
- Conocimientos básicos Power BI

### Paso 1: Crear archivo Power BI

1. **Abrir Power BI Desktop**
2. **Archivo → Nuevo**
3. **Guardar como:** `C:\Finanzas\AlvaroVelascoNet_Dashboard.pbix`

### Paso 2: Conectar a Excel

1. **Obtener datos → Excel**
2. **Seleccionar:** `AlvaroVelascoNet_EMPRESA.xlsx` (desde OneDrive)
3. **Seleccionar tablas:**
   - ✅ Dashboard
   - ✅ Efectivo
   - ✅ A/R
   - ✅ A/P
   - ✅ TC
   - ✅ KPIs
4. **Transformar datos**
5. **Aplicar y cerrar**

### Paso 3: Crear medidas DAX

**Medida 1: Total Efectivo**
```dax
Total Efectivo = SUM(Efectivo[Balance USD])
```

**Medida 2: Cobertura Días**
```dax
Cobertura Días = DIVIDE([Total Efectivo], [Gastos Mensuales]/30)
```

**Medida 3: Razón Corriente**
```dax
Razón Corriente = DIVIDE([Total Activos], [Total Pasivos])
```

(Ver archivo `CODIGO_DAX_POWERBI.txt` para medidas completas)

### Paso 4: Crear Dashboard Ejecutivo

**Página 1: Executive Summary**

**Agregar:**
- Tarjeta: Total Efectivo
- Tarjeta: Cobertura Días
- Tarjeta: Razón Corriente
- Gráfico línea: Evolución Efectivo
- Gráfico pie: Composición Gastos
- Tabla: Top 5 A/R
- Tabla: Alertas críticas

**Página 2: Cash Flow**

**Agregar:**
- Gráfico cascada: Ingresos vs Gastos
- Gráfico área: Proyección 90 días
- Tabla: Movimientos últimos 30 días

**Página 3: Debt Sanitization**

**Agregar:**
- Gráfico línea: Proyección pago TC 24 meses
- Gráfico columnas: Comparativa escenarios
- Tarjeta: Ahorro intereses proyectado

**Página 4: Accounts Receivable**

**Agregar:**
- Gráfico embudo: A/R Aging
- Gráfico barras: Top 10 clientes
- Tabla: A/R por prioridad

### Paso 5: Configurar actualización automática

1. **Publicar en Power BI Service:**
   - Archivo → Publicar
   - Seleccionar workspace
   - Iniciar sesión Power BI

2. **Configurar refresh:**
   - Power BI Service → Dataset settings
   - Actualización programada
   - ✅ Activar
   - Frecuencia: Diaria, 7:00 AM
   - ✅ Enviar notificación si falla

3. **Compartir dashboard:**
   - Dashboard → Compartir
   - Agregar correos si necesario

### Paso 6: Ver en mobile

1. **Descargar app Power BI** (iOS/Android)
2. **Iniciar sesión**
3. **Ver dashboard** desde cualquier lugar

---

## TROUBLESHOOTING (Solución problemas comunes)

### Problema 1: Fórmula #REF!

**Causa:** Referencias rotas a otras hojas

**Solución:**
1. Verificar que nombre de pestañas sea exacto
2. Si renombraste pestaña, actualizar fórmulas:
   - Buscar (Ctrl+F) → Reemplazar
   - Buscar: `'NombreViejo'!`
   - Reemplazar: `'NombreNuevo'!`

### Problema 2: #DIV/0!

**Causa:** División entre cero

**Solución:**
1. Identificar fórmula con división
2. Cambiar a: `=SI(B2=0, 0, A2/B2)`

### Problema 3: Balance efectivo incorrecto

**Causa:** Fórmula arrastra incorrecta

**Solución:**
1. Ir a primera celda balance (H3)
2. Verificar fórmula: `=H2+F3-G3`
3. Arrastrar nuevamente hacia abajo
4. Verificar que referencias cambien (H3→H4, F3→F4, etc.)

### Problema 4: CSV no importa correctamente

**Causa:** Encoding o delimitador

**Solución:**
1. Método alternativo: Abrir CSV con Excel directamente
2. Copiar todo (Ctrl+A, Ctrl+C)
3. Pegar en pestaña destino
4. Datos → Texto en columnas → Delimitado → Coma

### Problema 5: OneDrive no sincroniza

**Causa:** Internet o configuración

**Solución:**
1. Verificar conexión internet
2. OneDrive → Configuración → Cuenta → Desvincular
3. Volver a vincular
4. O guardar manualmente: Archivo → Guardar como → OneDrive

### Problema 6: Formato condicional no funciona

**Causa:** Regla mal configurada

**Solución:**
1. Seleccionar rango
2. Formato condicional → Administrar reglas
3. Editar regla
4. Verificar fórmula ($ antes de columna, NO antes de fila)
5. Ejemplo correcto: `=$E2="CRÍTICA"`
6. Ejemplo incorrecto: `=$E$2="CRÍTICA"`

---

## RECURSOS ADICIONALES

### Archivos de referencia:
- `FORMULAS_EXCEL_COMPLETAS.md` - Todas las fórmulas
- `ESTADO_FINANCIERO_ACTUAL.json` - Datos fuente
- `SISTEMA_EXCEL_FINANCIERO_COMPLETO_PLAN_MAESTRO.md` - Plan completo

### Tutoriales recomendados:
- Excel tablas dinámicas: YouTube "Excel pivot tables español"
- Power BI básico: YouTube "Power BI tutorial español"
- Formato condicional avanzado: YouTube "Excel conditional formatting"

### Atajos útiles Excel:
- `Ctrl+S`: Guardar
- `Ctrl+Z`: Deshacer
- `Ctrl+C / Ctrl+V`: Copiar/Pegar
- `Ctrl+Flecha`: Ir a última celda con datos
- `Ctrl+Shift+L`: Activar filtros
- `Alt+=`: Autosuma
- `F2`: Editar celda
- `F4`: Cambiar referencias ($ absoluto/relativo)

---

## SIGUIENTE PASO

**¡SISTEMA LISTO!** ✅

**Mañana 08/11/2025:**
1. Abrir archivo
2. Ir a Dashboard
3. Comenzar registro movimientos diarios

**Prioridades primeros 7 días:**
1. ✅ Pagar IVA $533.92
2. ✅ Cobrar VWR $2,800
3. ✅ Cobrar Grupo Acción $1,689
4. ✅ Pagar Intcomex vencido $410.09
5. ✅ Negociar plan pago 4 TC BNCR
6. ✅ Registrar TODOS los movimientos diarios

**En 30 días tendrás:**
- Control total efectivo
- Visibilidad completa finanzas
- KPIs actualizados
- Proyecciones confiables
- Plan sanitización en marcha

---

**TIEMPO TOTAL IMPLEMENTACIÓN: 3-4 horas**

**RESULTADO: Sistema financiero profesional completo funcionando** 🎉

¿Preguntas? Ver `FORMULAS_EXCEL_COMPLETAS.md` o documentación adicional.
