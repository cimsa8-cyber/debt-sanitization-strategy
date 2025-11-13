# 📚 SCRIPTS DE AUTOMATIZACIÓN - Excel v3.0

## 🚀 Scripts Disponibles

### 1. `agregar_transaccion.py` - Agregar Transacciones Interactivamente

**Uso:**
```bash
python scripts/agregar_transaccion.py
```

**Qué hace:**
- Pregunta datos de la transacción paso a paso
- Valida duplicados automáticamente
- Sincroniza con IVA_CONTROL si aplica
- Detecta zona franca (VWR, RSHughes)
- Aplica TC default ₡508

**Ejemplo de uso:**
```
Fecha: 13/11/2025
Tipo: 1 (INGRESO)
Descripción: Venta productos HP
Cuenta: BAC USD
Entidad: VWR International
Factura: FAC-123
Moneda: 2 (USD)
Monto: 1500
Método: TRANSFERENCIA
```

---

### 2. `actualizar_dashboard.py` - Dashboard Tiempo Real

**Uso:**
```bash
python scripts/actualizar_dashboard.py
```

**Qué hace:**
- Calcula KPIs automáticamente:
  - Efectivo neto (Bancos - Tarjetas)
  - Flujo del mes (Ingresos - Gastos)
  - CxC total y vencida
  - CxP total y crítica
  - IVA neto (Cobrado - Acreditable)
  - Días de cobertura
- Actualiza hoja DASHBOARD con colores

**Cuándo ejecutar:**
- Después de agregar transacciones
- Antes de tomar decisiones financieras
- Diariamente para monitoreo

---

### 3. `poblar_iva_desde_transacciones.py` - Sincronizar IVA

**Uso:**
```bash
python scripts/poblar_iva_desde_transacciones.py
```

**Qué hace:**
- Extrae INGRESOS → Ventas IVA
- Extrae GASTOS/COMPRAS → Compras IVA
- Calcula IVA 13%, retención 2%
- Detecta zona franca automáticamente

**Nota:** Solo pobla las primeras 15 ventas y 16 compras.

---

### 4. `agregar_iva_control_fase3.py` - Crear Hoja IVA

**Uso:**
```bash
python scripts/agregar_iva_control_fase3.py
```

**Qué hace:**
- Crea hoja IVA_CONTROL desde cero
- 3 secciones: Ventas, Compras, Resumen D-104

**Nota:** Solo ejecutar una vez. Ya está creada en v3.0.

---

### 5. `limpiar_duplicados_cxc_cxp.py` - Mantenimiento

**Uso:**
```bash
python scripts/limpiar_duplicados_cxc_cxp.py
```

**Qué hace:**
- Elimina hojas CxC/CxP duplicadas
- Renombra CxC1/CxP1 → CxC/CxP

---

## 📋 Flujo de Trabajo Diario

1. **Agregar transacciones del día:**
   ```bash
   python scripts/agregar_transaccion.py
   ```

2. **Actualizar dashboard:**
   ```bash
   python scripts/actualizar_dashboard.py
   ```

3. **Revisar Excel:**
   - Abrir `AlvaroVelasco_Finanzas_v3.0.xlsx`
   - Revisar DASHBOARD
   - Verificar IVA_CONTROL
   - Monitorear CxC/CxP

4. **Commit cambios:**
   ```bash
   git add -A
   git commit -m "UPDATE: Transacciones 13/Nov/2025"
   git push
   ```

---

## ⚠️ Notas Importantes

- **SIEMPRE** hacer `git pull` antes de trabajar
- **NUNCA** editar Excel manualmente y con scripts al mismo tiempo
- Scripts detectan duplicados pero **preguntarán** antes de agregar
- IVA_CONTROL tiene **límite** de filas (15 ventas, 16 compras)
- Días de cobertura se calcula: `Efectivo Neto / Gasto Diario Promedio`

---

## 🆘 Solución de Problemas

**Error: "File not found"**
```bash
# Asegurate de estar en la carpeta correcta:
cd C:\Users\Alvaro Velasco\desktop\debt-sanitization-strategy
```

**Error: "openpyxl not found"**
```bash
pip install openpyxl
```

**Hojas duplicadas:**
```bash
python scripts/limpiar_duplicados_cxc_cxp.py
```

---

## 📊 KPIs del Dashboard

| KPI | Descripción | Alerta |
|-----|-------------|--------|
| Efectivo Neto | Bancos - Tarjetas | < $0 (rojo) |
| Flujo Nov | Ingresos - Gastos mes | Negativo (rojo) |
| CxC Vencida | Cuentas con días > 0 | > 30% del total |
| CxP Crítica | Prioridad CRÍTICA | Vence < 7 días |
| IVA Neto | Cobrado - Acreditable | > $0 = a pagar |
| Días Cobertura | Efectivo / Gasto diario | < 15 días (rojo) |

---

**Versión:** 1.0
**Fecha:** 13/Nov/2025
**Autor:** Claude AI + Alvaro Velasco
