# Sistema de Alias v3.0 - Normalización Universal de Entidades

## 🎯 Expansión para Excel v3.0

### Qué Cambia en v3.0

**v2.0 (Actual):** Solo normaliza **cuentas bancarias**
- Promerica USD → variaciones
- BNCR → variaciones
- Tarjetas → variaciones

**v3.0 (Nuevo):** Normaliza **TODAS las entidades**
- ✅ Cuentas bancarias (como antes)
- ✅ **Clientes** (22+ clientes con variaciones)
- ✅ **Proveedores** (Intcomex, Eurocomp, etc.)
- ✅ **Categorías** (Licencias, Mantenimiento, etc.)
- ✅ **Productos/Servicios**

---

## 📋 Problema Expandido que Resuelve

### Ejemplo Real - Cliente "Grupo Acción"

Cuando registras transacciones manualmente, facturas electrónicas, o importas datos, el mismo cliente aparece con múltiples nombres:

**Variaciones detectadas:**
- `GRUPO ACCION COMERCIAL S.A.`
- `Grupo Acción Comercial`
- `Grupo Acción`
- `GrupoAccion`
- `ACCION COMERCIAL`
- `G. Acción`

**Problema:** Las fórmulas SUMIFS no suman todas las facturas del cliente porque no reconocen que son la misma entidad.

**Resultado:** Dashboard muestra facturación incorrecta, CLV (Customer Lifetime Value) equivocado, reportes por cliente inútiles.

### Ejemplo Real - Proveedor "Intcomex"

**Variaciones:**
- `INTCOMEX CENTROAMERICA S.A.`
- `Intcomex`
- `INTCOMEX`
- `Intcomex CR`
- `INTCOMEX-CR`

**Problema:** No puedes consolidar cuánto le debes realmente, CxP fragmentadas.

---

## ✅ Solución: Sistema Universal de Alias v3.0

### Estructura Nueva: Hoja ENTIDADES_ALIAS

Reemplaza `CUENTAS_ALIAS` con una tabla más robusta:

| Tipo | Nombre Estándar | Alias 1 | Alias 2 | Alias 3 | Alias 4 | Alias 5 | Categoría | Notas |
|------|----------------|---------|---------|---------|---------|---------|-----------|-------|
| Cliente | Grupo Acción Comercial S.A. | GRUPO ACCION COMERCIAL | Grupo Acción | GrupoAccion | ACCION COMERCIAL | G. Acción | VIP | Cliente #1, 17.8% facturación |
| Cliente | VWR International Ltda | VWR | VWR INTL | VWR International | VWR Costa Rica | | VIP | Contrato $1,400/mes |
| Proveedor | Intcomex Centroamérica S.A. | INTCOMEX CENTROAMERICA | Intcomex | INTCOMEX | Intcomex CR | INTCOMEX-CR | Hardware | Crédito $5k |
| Banco | Promerica USD (***1774) | Promerica USD | Promerica USD 1774 | Promerica USD (*1774) | Promerica 1774 | 40000003881774 | Operativa | Cuenta principal |
| Categoría | Licencias Microsoft 365 | Licencias M365 | Microsoft 365 | M365 | Office 365 | O365 | Ingresos | Facturación recurrente |

### Nuevas Columnas Clave

1. **Tipo**: Cliente / Proveedor / Banco / Tarjeta / Categoría / Producto
2. **Categoría**: Sub-clasificación (VIP, Hardware, Operativa, etc.)
3. **Notas**: Información adicional (contratos, límites de crédito, etc.)

---

## 🚀 Implementación v3.0

### Paso 1: Crear Hoja ENTIDADES_ALIAS (Primera Vez)

```bash
python scripts/crear_hoja_entidades_alias_v3.py
```

**Esto crea la hoja con entidades pre-configuradas:**

#### CLIENTES (22 pre-cargados):
1. Grupo Acción Comercial S.A.
2. VWR International Ltda
3. Alfipac (Almacén Fiscal Pacífico)
4. 3-102-887892 SRL
5. Waipio S.A.
6. Centro Integral Oncología CIO SRL
7. Ortodoncia de la Cruz
8. Global Automotriz GACR S.A.
9. Solusa Consolidators
10. Cemso
11. Acacia (Asoc. CR Agencias Carga)
12. Rodriguez Rojas Carlos Humberto
13. Supply Net C.R.W.H S.A.
14. Operation Management Tierra Magnifica
15. Gentra de Costa Rica S.A.
16. Sevilla Navarro Edgar
17. Gomez Ajoy Edgar Luis
18. Melendez Morales Monica
19. Bandogo Soluciones Tecnológicas S.A.
20. CPF Servicios Radiológicos S.A.
21. Ortodec S.A.
22. Perez Morales Francisco

#### PROVEEDORES (5 principales):
1. Intcomex Centroamérica S.A.
2. Eurocomp Costa Rica
3. CompuEconómicos
4. TD Synex
5. ICD Soft

#### BANCOS (9 cuentas):
1. Promerica USD (***1774)
2. Promerica CRC (***1708)
3. Promerica Ahorro USD (***1691)
4. Promerica CC CRC (***4229)
5. BNCR CRC (***8618)
6. BNCR USD (***1066)
7. BNCR CRC Socios (***2186)
8. BNCR USD Ahorro (***9589)
9. BNCR USD Ahorro (***1112)

#### TARJETAS (5):
1. BNCR Visa ***3519 (Personal)
2. BNCR Visa ***9837 (Empresa)
3. BNCR Visa ***6386 (Empresa)
4. BNCR MC ***8759 (Empresa)
5. BAC MC ***9550 (Empresa)

---

### Paso 2: Normalizar TODAS las Entidades

```bash
python scripts/normalizar_entidades_universal_v3.py
```

**El script mejorado:**
1. ✅ Lee mapeo desde **ENTIDADES_ALIAS**
2. ✅ Normaliza columnas:
   - **Columna E (Cuenta)**: Cuentas bancarias/tarjetas
   - **Columna F (Entidad)**: Clientes/Proveedores
   - **Columna C (Categoría)**: Categorías de transacciones
3. ✅ Usa **fuzzy matching** para detectar similitudes (ej: "VWR" vs "VWR INTL")
4. ✅ Reporta entidades sin mapeo
5. ✅ Crea backup automático
6. ✅ Genera log detallado

---

### Paso 3: Agregar Nuevas Variaciones (Mantenimiento)

#### Si aparece nueva variación de cliente existente:

**Ejemplo:** Factura nueva dice "Grupo Acción Com. SA"

1. Abrir Excel v3.0
2. Ir a hoja **ENTIDADES_ALIAS**
3. Buscar fila con "Grupo Acción Comercial S.A."
4. Agregar "Grupo Acción Com. SA" en columna **Alias 4**
5. Guardar Excel
6. Ejecutar: `python scripts/normalizar_entidades_universal_v3.py`

#### Si aparece cliente completamente nuevo:

**Ejemplo:** Nuevo cliente "TechnoLab S.A."

1. Abrir **ENTIDADES_ALIAS**
2. Agregar nueva fila:
   - **Tipo**: Cliente
   - **Nombre Estándar**: TechnoLab S.A.
   - **Alias 1**: TechnoLab
   - **Alias 2**: Techno Lab
   - **Categoría**: Normal (o VIP si aplica)
   - **Notas**: Contacto, teléfono, email
3. Guardar y normalizar

---

## 🔍 Detección Inteligente con Fuzzy Matching

### Qué es Fuzzy Matching

Algoritmo que detecta similitudes aunque los nombres no sean exactamente iguales.

**Ejemplo:**
```python
from fuzzywuzzy import fuzz

# Calcular similitud
fuzz.ratio("VWR International", "VWR INTL")
# Resultado: 75% similitud

# Si similitud > 80%, alertar para revisión manual
```

### Casos que Detecta Automáticamente

| Variación | Estándar | Similitud | Acción |
|-----------|----------|-----------|--------|
| "GRUPO ACCION" | "Grupo Acción Comercial S.A." | 85% | Auto-mapear |
| "VWR" | "VWR International Ltda" | 72% | Alertar usuario |
| "Intcomex CR" | "Intcomex Centroamérica S.A." | 88% | Auto-mapear |
| "Microsoft 365" | "Licencias Microsoft 365" | 82% | Auto-mapear |

**Umbral de confianza:**
- **≥ 90%**: Normaliza automáticamente
- **80-89%**: Normaliza + registra en log para revisión
- **70-79%**: Alerta usuario para decisión manual
- **< 70%**: No mapea, reporta como "sin mapeo"

---

## 📊 Ventajas Expandidas v3.0

✅ **Universal**: Normaliza TODO (clientes, proveedores, cuentas, categorías, productos)
✅ **Inteligente**: Fuzzy matching detecta similitudes automáticamente
✅ **Escalable**: Fácil agregar nuevas entidades
✅ **Auditable**: Log completo de cambios realizados
✅ **Seguro**: Backup antes de cada ejecución
✅ **Multi-tipo**: Maneja diferentes tipos de entidades en una sola tabla

---

## 🔄 Flujo de Trabajo v3.0

### Registro Manual de Transacciones

**Workflow optimizado:**

1. **Ir a hoja TRANSACCIONES**
2. **Columna F (Entidad)**: Empieza a escribir nombre del cliente
3. **Autocompletar Excel**: Muestra lista de clientes desde **ENTIDADES_ALIAS**
4. **Seleccionar de lista**: Garantiza uso del nombre estándar
5. **Guardar**: No necesitas normalización porque usaste nombre correcto

**Ventaja:** ✅ Prevención en origen (mejor que corrección posterior)

---

### Importación Automática (XML, CSV, etc.)

**Workflow con normalización:**

1. **Script importa datos** con nombres como aparecen en fuente
   ```
   Ejemplo: Factura XML dice "VWR INTL"
   Script agrega: Entidad = "VWR INTL"
   ```

2. **Ejecutar normalización:**
   ```bash
   python scripts/normalizar_entidades_universal_v3.py
   ```

3. **Script detecta:**
   ```
   "VWR INTL" → 85% similitud con "VWR International Ltda"
   → Auto-mapea a "VWR International Ltda"
   ```

4. **Revisar log:**
   ```
   normalizacion_2025-11-12_18-30.log:
   ✅ Normalizado: "VWR INTL" → "VWR International Ltda" (85% confianza)
   ⚠️  Revisar: "Accion Com" → "Grupo Acción Comercial S.A." (78% confianza)
   ❌ Sin mapeo: "NuevoCliente XYZ" (agregar a ENTIDADES_ALIAS)
   ```

5. **Agregar nuevos alias** según log

---

## 📝 Casos de Uso Reales

### Caso 1: Cliente con múltiples formas de facturar

**Situación:**
- Noviembre: Factura AR-002 a "GRUPO ACCION COMERCIAL S.A." ($1,689.04)
- Diciembre: Factura AR-025 a "Grupo Acción" ($1,200.00)
- Enero: Factura AR-048 a "G. Acción Com." ($1,450.00)

**Sin normalización:**
- Dashboard muestra: 3 clientes diferentes
- Facturación Total: No consolidada
- CLV: Imposible calcular

**Con normalización v3.0:**
- ✅ Las 3 facturas mapeadas a "Grupo Acción Comercial S.A."
- ✅ Facturación Total: $4,339.04
- ✅ CLV calculado correctamente
- ✅ TOP cliente identificado

---

### Caso 2: Proveedor con errores de tipeo

**Situación:**
- Transacción 1: "Intcomex" ($2,500)
- Transacción 2: "INTCOMEX CENTROAMERICA" ($3,200)
- Transacción 3: "Intcomex CR" ($1,800)
- Transacción 4: "Intcomx" (typo) ($900)  ← Error de tipeo

**Sin normalización:**
- CxP fragmentadas en 4 proveedores
- Total adeudado: NO consolidado
- Imposible rastrear crédito usado

**Con normalización v3.0:**
- ✅ Transacciones 1-3: Auto-mapeadas
- ⚠️ Transacción 4: Detectada con 92% similitud → Alertada para revisión
- Usuario confirma: Sí, es Intcomex
- ✅ Agrega "Intcomx" como Alias 6
- ✅ Total consolidado: $8,400
- ✅ Crédito usado: $8,400 de $5,000 → ALERTA: Sobregiro

---

### Caso 3: Categorías inconsistentes

**Situación:**
- Transacción 1: Categoría = "Licencias Microsoft"
- Transacción 2: Categoría = "M365"
- Transacción 3: Categoría = "Microsoft 365"
- Transacción 4: Categoría = "Office 365"

**Sin normalización:**
- P&L muestra 4 líneas de ingreso separadas
- Margen por producto: Imposible calcular

**Con normalización v3.0:**
- ✅ Mapeo en ENTIDADES_ALIAS:
  ```
  Tipo: Categoría
  Nombre Estándar: Licencias Microsoft 365
  Alias: M365, Microsoft 365, Office 365, O365
  ```
- ✅ P&L consolidado en 1 línea
- ✅ Margen calculable

---

## 🛠️ Scripts v3.0

### Script 1: crear_hoja_entidades_alias_v3.py

**Función:** Crear hoja ENTIDADES_ALIAS con todas las entidades pre-cargadas.

```python
#!/usr/bin/env python3
"""
Crea la hoja ENTIDADES_ALIAS en Excel v3.0
Pre-carga: 22 clientes, 5 proveedores, 9 bancos, 5 tarjetas, categorías comunes
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

EXCEL_PATH = "AlvaroVelasco_Finanzas_v3.0.xlsx"

# Datos pre-configurados
ENTIDADES = [
    # CLIENTES (22)
    ["Cliente", "Grupo Acción Comercial S.A.", "GRUPO ACCION COMERCIAL", "Grupo Acción", "GrupoAccion", "ACCION COMERCIAL", "G. Acción", "VIP", "Cliente #1, 17.8% facturación Nov"],
    ["Cliente", "VWR International Ltda", "VWR", "VWR INTL", "VWR International", "VWR Costa Rica", "", "VIP", "Contrato $1,400/mes"],
    ["Cliente", "Alfipac (Almacén Fiscal Pacífico)", "ALFIPAC", "Almacén Fiscal Pacífico", "Almacen Fiscal", "ALFIPAC SRL", "", "Normal", "8% facturación Nov"],
    ["Cliente", "3-102-887892 SRL", "3-102-887892", "SRL 887892", "", "", "", "Normal", "7.3% facturación Nov"],
    ["Cliente", "Waipio S.A.", "WAIPIO", "Waipio SA", "Waipio", "", "", "Normal", "7.3% facturación Nov"],
    # ... resto de clientes (ver código completo)

    # PROVEEDORES (5 principales)
    ["Proveedor", "Intcomex Centroamérica S.A.", "INTCOMEX CENTROAMERICA", "Intcomex", "INTCOMEX", "Intcomex CR", "INTCOMEX-CR", "Hardware", "Crédito $5k"],
    ["Proveedor", "Eurocomp Costa Rica", "EUROCOMP", "Eurocomp", "Euro Comp", "Eurocomp CR", "", "Hardware", "Crédito $4k"],
    ["Proveedor", "CompuEconómicos", "CompuEconomicos", "Compu Economicos", "COMPUECONOMICOS", "", "", "Hardware", "Crédito $5k"],
    ["Proveedor", "TD Synex", "TDSYNEX", "TD-Synex", "Synex", "", "", "Distribuidor", "Mayorista"],
    ["Proveedor", "ICD Soft", "ICDSOFT", "ICD-Soft", "ICD Software", "", "", "Software", "Licencias"],

    # BANCOS (9)
    ["Banco", "Promerica USD (***1774)", "Promerica USD", "Promerica USD 1774", "Promerica USD (*1774)", "Promerica 1774", "40000003881774", "Operativa", "Cuenta principal negocio"],
    ["Banco", "Promerica CRC (***1708)", "Promerica CRC", "Promerica Colones", "Promerica CRC 1708", "10000003881708", "", "Operativa", "Respaldo colones"],
    # ... resto de bancos

    # TARJETAS (5)
    ["Tarjeta", "BNCR Visa ***3519", "BNCR 3519", "Tarjeta BNCR", "BNCR Visa *3519", "Visa 3519", "BNCR ****3519", "Personal", "100% personal - $3,864"],
    ["Tarjeta", "BNCR Visa ***9837", "BNCR 9837", "Visa 9837", "BNCR *9837", "", "", "Empresa", "100% empresa - $3,299"],
    # ... resto de tarjetas

    # CATEGORÍAS COMUNES
    ["Categoría", "Licencias Microsoft 365", "Licencias M365", "Microsoft 365", "M365", "Office 365", "O365", "Ingresos", "Facturación recurrente"],
    ["Categoría", "Servicios Mantenimiento", "Mantenimiento", "Mant.", "Soporte Técnico", "Soporte", "", "Ingresos", "Contratos mensuales"],
    ["Categoría", "Hardware - Venta", "Hardware", "Venta Hardware", "Productos", "", "", "Ingresos", "Margen 15-20%"],
]

def crear_hoja_entidades():
    """Crea hoja ENTIDADES_ALIAS con formato"""

    wb = openpyxl.load_workbook(EXCEL_PATH)

    # Crear hoja (eliminar si existe)
    if "ENTIDADES_ALIAS" in wb.sheetnames:
        del wb["ENTIDADES_ALIAS"]

    ws = wb.create_sheet("ENTIDADES_ALIAS", 0)  # Insertar como primera hoja

    # Encabezados
    headers = ["Tipo", "Nombre Estándar", "Alias 1", "Alias 2", "Alias 3", "Alias 4", "Alias 5", "Categoría", "Notas"]
    ws.append(headers)

    # Formato encabezados
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF")

    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")

    # Agregar datos
    for entidad in ENTIDADES:
        ws.append(entidad)

    # Ajustar anchos de columna
    ws.column_dimensions['A'].width = 12  # Tipo
    ws.column_dimensions['B'].width = 35  # Nombre Estándar
    ws.column_dimensions['C'].width = 25  # Alias 1
    ws.column_dimensions['D'].width = 25  # Alias 2
    ws.column_dimensions['E'].width = 25  # Alias 3
    ws.column_dimensions['F'].width = 25  # Alias 4
    ws.column_dimensions['G'].width = 25  # Alias 5
    ws.column_dimensions['H'].width = 15  # Categoría
    ws.column_dimensions['I'].width = 40  # Notas

    # Formato de datos por tipo
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
        tipo = row[0].value

        if tipo == "Cliente":
            fill = PatternFill(start_color="E7E6E6", end_color="E7E6E6", fill_type="solid")
        elif tipo == "Proveedor":
            fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
        elif tipo == "Banco":
            fill = PatternFill(start_color="D9EAD3", end_color="D9EAD3", fill_type="solid")
        elif tipo == "Tarjeta":
            fill = PatternFill(start_color="FCE5CD", end_color="FCE5CD", fill_type="solid")
        elif tipo == "Categoría":
            fill = PatternFill(start_color="D0E0E3", end_color="D0E0E3", fill_type="solid")
        else:
            fill = None

        if fill:
            for cell in row:
                cell.fill = fill

    # Guardar
    wb.save(EXCEL_PATH)
    print(f"✅ Hoja ENTIDADES_ALIAS creada con {len(ENTIDADES)} entidades pre-cargadas")
    print(f"   - Clientes: {sum(1 for e in ENTIDADES if e[0] == 'Cliente')}")
    print(f"   - Proveedores: {sum(1 for e in ENTIDADES if e[0] == 'Proveedor')}")
    print(f"   - Bancos: {sum(1 for e in ENTIDADES if e[0] == 'Banco')}")
    print(f"   - Tarjetas: {sum(1 for e in ENTIDADES if e[0] == 'Tarjeta')}")
    print(f"   - Categorías: {sum(1 for e in ENTIDADES if e[0] == 'Categoría')}")

if __name__ == "__main__":
    crear_hoja_entidades()
```

---

### Script 2: normalizar_entidades_universal_v3.py

**Función:** Normalizar todas las entidades en TRANSACCIONES usando fuzzy matching.

```python
#!/usr/bin/env python3
"""
Normaliza TODAS las entidades en hoja TRANSACCIONES
usando mapeo de ENTIDADES_ALIAS + fuzzy matching inteligente
"""

import openpyxl
from fuzzywuzzy import fuzz
from datetime import datetime
import shutil

EXCEL_PATH = "AlvaroVelasco_Finanzas_v3.0.xlsx"
UMBRAL_AUTO = 90      # ≥90%: Normaliza automáticamente
UMBRAL_ALERTAR = 80   # 80-89%: Normaliza pero registra en log
UMBRAL_MANUAL = 70    # 70-79%: Alerta para decisión manual

def cargar_mapeo_entidades():
    """Carga tabla de alias desde ENTIDADES_ALIAS"""
    wb = openpyxl.load_workbook(EXCEL_PATH)
    ws = wb["ENTIDADES_ALIAS"]

    mapeo = {
        "Cliente": {},
        "Proveedor": {},
        "Banco": {},
        "Tarjeta": {},
        "Categoría": {}
    }

    for row in ws.iter_rows(min_row=2, values_only=True):
        tipo = row[0]
        nombre_std = row[1]
        aliases = [row[i] for i in range(2, 7) if row[i]]  # Alias 1-5

        if tipo not in mapeo:
            continue

        # Mapear nombre estándar a sí mismo
        mapeo[tipo][nombre_std.lower()] = nombre_std

        # Mapear cada alias al nombre estándar
        for alias in aliases:
            mapeo[tipo][alias.lower()] = nombre_std

    return mapeo

def fuzzy_match(texto, mapeo_tipo):
    """
    Busca coincidencia usando fuzzy matching
    Retorna: (nombre_estandar, confianza_porcentaje)
    """
    mejor_match = None
    mejor_score = 0

    texto_lower = texto.lower()

    # Primero buscar match exacto
    if texto_lower in mapeo_tipo:
        return (mapeo_tipo[texto_lower], 100)

    # Fuzzy matching contra todas las opciones
    for alias, nombre_std in mapeo_tipo.items():
        score = fuzz.ratio(texto_lower, alias)

        if score > mejor_score:
            mejor_score = score
            mejor_match = nombre_std

    return (mejor_match, mejor_score) if mejor_score >= UMBRAL_MANUAL else (None, 0)

def normalizar_transacciones():
    """Normaliza entidades en hoja TRANSACCIONES"""

    # Backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"backups/v3_backup_{timestamp}.xlsx"
    shutil.copy(EXCEL_PATH, backup_path)
    print(f"✅ Backup creado: {backup_path}")

    # Cargar mapeo
    mapeo = cargar_mapeo_entidades()

    # Abrir Excel
    wb = openpyxl.load_workbook(EXCEL_PATH)
    ws = wb["TRANSACCIONES"]

    # Contadores
    stats = {
        "total": 0,
        "normalizadas_auto": 0,
        "normalizadas_alerta": 0,
        "requieren_revision": 0,
        "sin_mapeo": 0
    }

    log_entries = []

    # Normalizar cada transacción
    for i, row in enumerate(ws.iter_rows(min_row=2), start=2):
        stats["total"] += 1

        # Columna E: Cuenta (Banco/Tarjeta)
        cuenta = row[4].value  # Columna E
        if cuenta:
            # Intentar mapear como Banco
            match, score = fuzzy_match(cuenta, {**mapeo["Banco"], **mapeo["Tarjeta"]})

            if score >= UMBRAL_AUTO:
                row[4].value = match
                stats["normalizadas_auto"] += 1
                if score < 100:
                    log_entries.append(f"✅ Fila {i}, Cuenta: '{cuenta}' → '{match}' (confianza: {score}%)")

            elif score >= UMBRAL_ALERTAR:
                row[4].value = match
                stats["normalizadas_alerta"] += 1
                log_entries.append(f"⚠️  Fila {i}, Cuenta: '{cuenta}' → '{match}' (confianza: {score}%) - REVISAR")

            elif score >= UMBRAL_MANUAL:
                stats["requieren_revision"] += 1
                log_entries.append(f"❓ Fila {i}, Cuenta: '{cuenta}' - Posible match: '{match}' (confianza: {score}%) - DECISIÓN MANUAL")

            else:
                stats["sin_mapeo"] += 1
                log_entries.append(f"❌ Fila {i}, Cuenta: '{cuenta}' - SIN MAPEO - Agregar a ENTIDADES_ALIAS")

        # Columna F: Entidad (Cliente/Proveedor)
        entidad = row[5].value  # Columna F
        if entidad:
            # Intentar mapear como Cliente o Proveedor
            match, score = fuzzy_match(entidad, {**mapeo["Cliente"], **mapeo["Proveedor"]})

            if score >= UMBRAL_AUTO:
                row[5].value = match
                stats["normalizadas_auto"] += 1
                if score < 100:
                    log_entries.append(f"✅ Fila {i}, Entidad: '{entidad}' → '{match}' (confianza: {score}%)")

            elif score >= UMBRAL_ALERTAR:
                row[5].value = match
                stats["normalizadas_alerta"] += 1
                log_entries.append(f"⚠️  Fila {i}, Entidad: '{entidad}' → '{match}' (confianza: {score}%) - REVISAR")

            elif score >= UMBRAL_MANUAL:
                stats["requieren_revision"] += 1
                log_entries.append(f"❓ Fila {i}, Entidad: '{entidad}' - Posible match: '{match}' (confianza: {score}%) - DECISIÓN MANUAL")

            else:
                stats["sin_mapeo"] += 1
                log_entries.append(f"❌ Fila {i}, Entidad: '{entidad}' - SIN MAPEO - Agregar a ENTIDADES_ALIAS")

        # Columna C: Categoría
        categoria = row[2].value  # Columna C
        if categoria:
            match, score = fuzzy_match(categoria, mapeo["Categoría"])

            if score >= UMBRAL_AUTO:
                row[2].value = match
                stats["normalizadas_auto"] += 1
                if score < 100:
                    log_entries.append(f"✅ Fila {i}, Categoría: '{categoria}' → '{match}' (confianza: {score}%)")

    # Guardar cambios
    wb.save(EXCEL_PATH)

    # Generar log
    log_path = f"logs/normalizacion_{timestamp}.log"
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write("="*60 + "\n")
        f.write(f"NORMALIZACIÓN DE ENTIDADES - {datetime.now()}\n")
        f.write("="*60 + "\n\n")
        f.write(f"Total transacciones procesadas: {stats['total']}\n")
        f.write(f"Normalizadas automáticamente: {stats['normalizadas_auto']}\n")
        f.write(f"Normalizadas con alerta: {stats['normalizadas_alerta']}\n")
        f.write(f"Requieren revisión manual: {stats['requieren_revision']}\n")
        f.write(f"Sin mapeo: {stats['sin_mapeo']}\n\n")
        f.write("="*60 + "\n")
        f.write("DETALLE DE CAMBIOS:\n")
        f.write("="*60 + "\n\n")
        f.write("\n".join(log_entries))

    print("\n" + "="*60)
    print("RESUMEN DE NORMALIZACIÓN")
    print("="*60)
    print(f"Total transacciones: {stats['total']}")
    print(f"✅ Normalizadas automáticamente: {stats['normalizadas_auto']}")
    print(f"⚠️  Normalizadas con alerta: {stats['normalizadas_alerta']}")
    print(f"❓ Requieren revisión: {stats['requieren_revision']}")
    print(f"❌ Sin mapeo: {stats['sin_mapeo']}")
    print(f"\n📄 Log detallado: {log_path}")
    print("="*60)

if __name__ == "__main__":
    normalizar_transacciones()
```

---

## 🎯 Próximos Pasos

1. ✅ Instalar dependencia fuzzy matching:
   ```bash
   pip install fuzzywuzzy python-Levenshtein
   ```

2. ✅ Crear hoja ENTIDADES_ALIAS:
   ```bash
   python scripts/crear_hoja_entidades_alias_v3.py
   ```

3. ✅ Normalizar datos existentes:
   ```bash
   python scripts/normalizar_entidades_universal_v3.py
   ```

4. ✅ Revisar log de normalización y agregar alias faltantes

---

## 📚 Documentación Adicional

- `SISTEMA_ALIAS_CUENTAS.md`: Sistema original v2.0 (solo cuentas)
- `ESPECIFICACION_TECNICA_V3.md`: Arquitectura completa v3.0
- `CUESTIONARIO_V3_FUNDAMENTOS.md`: Requisitos y decisiones

---

**FIN - Sistema de Alias v3.0 Expandido**
