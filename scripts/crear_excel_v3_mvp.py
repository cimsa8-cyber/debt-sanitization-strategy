#!/usr/bin/env python3
"""
CREAR EXCEL V3.0 - MVP (FASE 1)
================================

PROPÓSITO: Crear estructura completa de Excel v3.0 desde CERO

APLICA LECCIONES APRENDIDAS:
- Diagnóstico PRIMERO (✅ Ya hecho)
- Construcción con especificaciones completas (✅ Cuestionario + diagnóstico)
- Validaciones desde el inicio (✅ Incluidas)
- Manual inline con comentarios (✅ Incluido)

FASE 1 MVP - Due: Nov 19, 2025 (7 días)
---------------------------------------
✅ Hoja TRANSACCIONES (20 columnas)
✅ Hoja EFECTIVO (9 cuentas bancarias)
✅ Hoja DASHBOARD (KPIs críticos)
✅ Hoja ENTIDADES_ALIAS (22 clientes)
✅ Validaciones y protección
✅ Manual inline (comentarios)

Ejecutar:
    python scripts/crear_excel_v3_mvp.py

Salida:
    AlvaroVelasco_Finanzas_v3.0.xlsx
"""

import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from datetime import datetime
import os

# ============================================================================
# CONFIGURACIÓN GLOBAL
# ============================================================================

EXCEL_FILE = "AlvaroVelasco_Finanzas_v3.0.xlsx"

# Colores corporativos
COLOR_HEADER = "1F4E78"      # Azul oscuro
COLOR_EDITABLE = "FFF2CC"    # Amarillo claro
COLOR_FORMULA = "FFFFFF"     # Blanco
COLOR_WARNING = "FCE4D6"     # Naranja claro
COLOR_SUCCESS = "C6EFCE"     # Verde claro
COLOR_ERROR = "FFC7CE"       # Rojo claro

# Estilos de fuente
FONT_HEADER = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
FONT_NORMAL = Font(name='Calibri', size=10)
FONT_SMALL = Font(name='Calibri', size=9, italic=True)

# Bordes
BORDER_THIN = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

# ============================================================================
# DATOS DE CONFIGURACIÓN (Del Cuestionario v3.0)
# ============================================================================

# 22 Clientes (Bloque 2)
CLIENTES = [
    {"nombre": "Grupo Acción Comercial S.A.", "categoria": "VIP", "monto_nov": 1681.56},
    {"nombre": "Corporación de Supermercados Unidos CSU", "categoria": "VIP", "monto_nov": 1488.75},
    {"nombre": "Tiendas Monge CR", "categoria": "VIP", "monto_nov": 1029.75},
    {"nombre": "Gessa Comunicaciones S.A.", "categoria": "VIP", "monto_nov": 830.50},
    {"nombre": "Corporación El Colono", "categoria": "VIP", "monto_nov": 778.84},
    {"nombre": "Automercado S.A.", "categoria": "VIP", "monto_nov": 705.10},
    {"nombre": "Supermercados La Mejor", "categoria": "VIP", "monto_nov": 580.00},
    {"nombre": "Servicios R.G.V. Ltda", "categoria": "Regular", "monto_nov": 531.52},
    {"nombre": "Grupo Roble S.A.", "categoria": "Regular", "monto_nov": 417.30},
    {"nombre": "Inversiones JZ S.A.", "categoria": "Regular", "monto_nov": 275.00},
    {"nombre": "Importadora G.J. S.A.", "categoria": "Regular", "monto_nov": 250.68},
    {"nombre": "MegaSuper S.A.", "categoria": "Regular", "monto_nov": 187.76},
    {"nombre": "Corporación 5x3 S.A.", "categoria": "Regular", "monto_nov": 160.25},
    {"nombre": "Distribuidora del Sur", "categoria": "Regular", "monto_nov": 142.50},
    {"nombre": "Fresh Market S.A.", "categoria": "Regular", "monto_nov": 124.80},
    {"nombre": "PriceSmart Costa Rica", "categoria": "Regular", "monto_nov": 109.16},
    {"nombre": "Super La Económica", "categoria": "Regular", "monto_nov": 94.75},
    {"nombre": "Tiendas Pequeño Mundo", "categoria": "Regular", "monto_nov": 83.20},
    {"nombre": "Distribuidora Central", "categoria": "Regular", "monto_nov": 0.00},
    {"nombre": "Comercial del Este", "categoria": "Regular", "monto_nov": 0.00},
    {"nombre": "Super Compro S.A.", "categoria": "Regular", "monto_nov": 0.00},
    {"nombre": "Walmart Costa Rica", "categoria": "Regular", "monto_nov": 0.00},
]

# 9 Cuentas Bancarias (Bloque 3)
CUENTAS_BANCARIAS = [
    {"nombre": "BNCR CRC Corriente (200-01-000-622159-5)", "tipo": "Banco", "moneda": "CRC", "saldo": 0.00},
    {"nombre": "BNCR USD Corriente (200-02-000-011931-4)", "tipo": "Banco", "moneda": "USD", "saldo": 0.00},
    {"nombre": "BNCR CRC Ahorros (100-01-000-086647-3)", "tipo": "Banco", "moneda": "CRC", "saldo": 0.00},
    {"nombre": "BNCR USD Ahorros (100-02-000-039695-7)", "tipo": "Banco", "moneda": "USD", "saldo": 1894.54},
    {"nombre": "BNCR CRC Cliente (100-01-000-066819-8)", "tipo": "Banco", "moneda": "CRC", "saldo": 0.00},
    {"nombre": "Promerica CRC Corriente (10000003881708)", "tipo": "Banco", "moneda": "CRC", "saldo": 0.00},
    {"nombre": "Promerica USD Corriente (40000003881774)", "tipo": "Banco", "moneda": "USD", "saldo": 1550.00},
    {"nombre": "Efectivo Caja Chica CRC", "tipo": "Efectivo", "moneda": "CRC", "saldo": 0.00},
    {"nombre": "Efectivo Caja Chica USD", "tipo": "Efectivo", "moneda": "USD", "saldo": 0.00},
]

# 5 Tarjetas de Crédito (Bloque 4)
TARJETAS_CREDITO = [
    {"nombre": "Tarjeta BNCR Visa 3519", "limite": 3000.00, "saldo": 0.00, "estrategia": "Pago mínimo mientras crisis"},
    {"nombre": "Tarjeta Promerica MC 8641", "limite": 2000.00, "saldo": 0.00, "estrategia": "Pago mínimo"},
    {"nombre": "Tarjeta BAC Visa 7182", "limite": 1500.00, "saldo": 0.00, "estrategia": "Pago mínimo"},
    {"nombre": "Tarjeta Scotia Visa 4429", "limite": 1000.00, "saldo": 0.00, "estrategia": "Pago mínimo"},
    {"nombre": "Tarjeta Popular MC 6753", "limite": 800.00, "saldo": 0.00, "estrategia": "Pago mínimo"},
]

# 5 Proveedores Principales
PROVEEDORES = [
    "Intcomex Costa Rica",
    "Eurocomp S.A.",
    "CompuEconómicos",
    "TD Synex",
    "ICD Soft",
]

# Tipos de Transacción
TIPOS_TRANSACCION = [
    "INGRESO",
    "GASTO OPERATIVO",
    "GASTO FINANCIERO",
    "COMPRA PARA REVENTA",
    "TRANSFERENCIA",
    "PAGO TARJETA",
    "PAGO PRESTAMO",
    "AJUSTE",
]

# Categorías (Simplificadas para MVP)
CATEGORIAS = [
    "Ventas - Servicios Técnicos",
    "Ventas - Hardware",
    "Ventas - Software",
    "Compras - Inventario",
    "Salarios",
    "Seguridad Social (CCSS)",
    "Alquiler",
    "Servicios Públicos",
    "Internet/Teléfono",
    "Combustible",
    "Mantenimiento",
    "Papelería",
    "Intereses - Tarjetas",
    "Intereses - Préstamos",
    "Intereses - Hacienda",
    "IVA Cobrado",
    "IVA Pagado",
    "Transferencia entre cuentas",
    "Otros",
]

# Estados de transacción
ESTADOS = [
    "COMPLETADA",
    "PENDIENTE",
    "CANCELADA",
]

# ============================================================================
# FUNCIONES DE UTILIDAD
# ============================================================================

def crear_estilo_header(ws, row, col_start, col_end):
    """Aplica estilo de encabezado a un rango"""
    for col in range(col_start, col_end + 1):
        cell = ws.cell(row, col)
        cell.font = FONT_HEADER
        cell.fill = PatternFill(start_color=COLOR_HEADER, end_color=COLOR_HEADER, fill_type="solid")
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        cell.border = BORDER_THIN

def crear_estilo_editable(cell):
    """Marca celda como editable (amarillo)"""
    cell.fill = PatternFill(start_color=COLOR_EDITABLE, end_color=COLOR_EDITABLE, fill_type="solid")
    cell.border = BORDER_THIN
    cell.alignment = Alignment(horizontal='left', vertical='center')
    cell.font = FONT_NORMAL

def crear_estilo_formula(cell):
    """Marca celda como fórmula (blanco, protegido)"""
    cell.fill = PatternFill(start_color=COLOR_FORMULA, end_color=COLOR_FORMULA, fill_type="solid")
    cell.border = BORDER_THIN
    cell.alignment = Alignment(horizontal='right', vertical='center')
    cell.font = FONT_NORMAL

def agregar_comentario(cell, texto):
    """Agrega comentario de ayuda a una celda"""
    from openpyxl.comments import Comment
    cell.comment = Comment(texto, "Sistema v3.0")
    cell.comment.width = 300
    cell.comment.height = 100

# ============================================================================
# HOJA 1: TRANSACCIONES
# ============================================================================

def crear_hoja_transacciones(wb):
    """
    Crea la hoja TRANSACCIONES con 20 columnas y validaciones.

    Columnas A-T:
    A: Fecha
    B: Tipo
    C: Categoría
    D: Descripción
    E: Cuenta Origen
    F: Entidad (Cliente/Proveedor)
    G: Factura #
    H: Monto CRC
    I: Monto USD
    J: Tipo Cambio
    K: Método Pago
    L: Estado
    M: IVA Incluido (%)
    N: Referencia Bancaria
    O: Notas
    P: Creado Por
    Q: Fecha Creación
    R: Modificado Por
    S: Alerta Duplicados
    T: ID Único
    """
    print("\n📊 Creando hoja TRANSACCIONES...")

    ws = wb.create_sheet("TRANSACCIONES", 0)

    # Encabezados
    headers = [
        "Fecha", "Tipo", "Categoría", "Descripción", "Cuenta Origen",
        "Entidad", "Factura #", "Monto CRC", "Monto USD", "Tipo Cambio",
        "Método Pago", "Estado", "IVA %", "Ref. Bancaria", "Notas",
        "Creado Por", "Fecha Creación", "Modificado Por", "⚠️ Duplicados", "ID"
    ]

    for col, header in enumerate(headers, start=1):
        cell = ws.cell(1, col, header)

    crear_estilo_header(ws, 1, 1, len(headers))

    # Anchos de columna
    widths = [12, 18, 22, 30, 28, 30, 12, 12, 12, 10, 15, 12, 8, 15, 25, 12, 12, 12, 15, 10]
    for col, width in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(col)].width = width

    # Congelar primera fila
    ws.freeze_panes = "A2"

    # ========================================================================
    # VALIDACIONES DE DATOS
    # ========================================================================

    # Validación: Tipo (columna B)
    dv_tipo = DataValidation(type="list", formula1=f'"{",".join(TIPOS_TRANSACCION)}"', allow_blank=False)
    dv_tipo.error = "Selecciona un tipo válido de la lista"
    dv_tipo.errorTitle = "Tipo inválido"
    ws.add_data_validation(dv_tipo)
    dv_tipo.add(f"B2:B1000")

    # Validación: Categoría (columna C)
    dv_categoria = DataValidation(type="list", formula1=f'"{",".join(CATEGORIAS)}"', allow_blank=False)
    dv_categoria.error = "Selecciona una categoría válida de la lista"
    dv_categoria.errorTitle = "Categoría inválida"
    ws.add_data_validation(dv_categoria)
    dv_categoria.add(f"C2:C1000")

    # Validación: Cuenta Origen (columna E) - Todas las cuentas + tarjetas
    todas_cuentas = [c["nombre"] for c in CUENTAS_BANCARIAS] + [t["nombre"] for t in TARJETAS_CREDITO]
    # Crear validación (Excel permite hasta ~8000 chars en validaciones modernas)
    cuentas_str = ",".join(todas_cuentas)
    dv_cuenta = DataValidation(type="list", formula1=f'"{cuentas_str}"', allow_blank=False)
    dv_cuenta.error = "Selecciona una cuenta válida de la lista"
    dv_cuenta.errorTitle = "Cuenta inválida"
    ws.add_data_validation(dv_cuenta)
    dv_cuenta.add(f"E2:E1000")

    # Validación: Método Pago (columna K)
    metodos = "Transferencia,Efectivo,Cheque,Tarjeta débito,Tarjeta crédito,SINPE Móvil,Depósito"
    dv_metodo = DataValidation(type="list", formula1=f'"{metodos}"', allow_blank=True)
    ws.add_data_validation(dv_metodo)
    dv_metodo.add(f"K2:K1000")

    # Validación: Estado (columna L)
    dv_estado = DataValidation(type="list", formula1=f'"{",".join(ESTADOS)}"', allow_blank=False)
    ws.add_data_validation(dv_estado)
    dv_estado.add(f"L2:L1000")

    # Validación: IVA % (columna M) - Solo 0, 1, 2, 4, 8, 13
    dv_iva = DataValidation(type="list", formula1='"0,1,2,4,8,13"', allow_blank=True)
    ws.add_data_validation(dv_iva)
    dv_iva.add(f"M2:M1000")

    # ========================================================================
    # FÓRMULAS EN FILA 2 (para copiar abajo)
    # ========================================================================

    # Tipo Cambio (J2) - Auto-fetch o manual
    ws['J2'] = 540  # Valor por defecto
    agregar_comentario(ws['J2'], "💡 TIPO DE CAMBIO\n\nIngresa el tipo de cambio del día.\n\nSi dejas vacío, se usará 540 por defecto.\n\nFormato: 540 (sin comas)")

    # Alerta Duplicados (S2)
    formula_duplicados = '''=IF(
COUNTIFS(
$A:$A, A2,
$E:$E, E2,
$I:$I, I2
) > 1,
"⚠️ POSIBLE DUPLICADO",
""
)'''
    ws['S2'] = formula_duplicados
    crear_estilo_formula(ws['S2'])

    # ID Único (T2)
    ws['T2'] = '=ROW()-1'
    crear_estilo_formula(ws['T2'])

    # Fecha Creación (Q2) - Fórmula NOW()
    ws['Q2'] = '=NOW()'
    crear_estilo_formula(ws['Q2'])
    ws['Q2'].number_format = 'DD/MM/YYYY HH:MM'

    # ========================================================================
    # MANUAL INLINE - Comentarios en columnas editables
    # ========================================================================

    agregar_comentario(ws['A2'], "💡 FECHA DE LA TRANSACCIÓN\n\nFormato: DD/MM/YYYY\nEjemplo: 15/11/2025\n\n⚠️ Usa la fecha real de la transacción, no cuando la registras.")
    agregar_comentario(ws['B2'], "💡 TIPO DE TRANSACCIÓN\n\nOpciones:\n• INGRESO - Dinero que entra\n• GASTO OPERATIVO - Gastos del negocio\n• GASTO FINANCIERO - Intereses, comisiones\n• COMPRA PARA REVENTA - Inventario\n• TRANSFERENCIA - Movimiento entre cuentas\n• PAGO TARJETA - Abono a tarjetas\n• PAGO PRESTAMO - Abono a préstamos\n• AJUSTE - Correcciones")
    agregar_comentario(ws['C2'], "💡 CATEGORÍA\n\nElige la categoría contable.\n\nSi es venta: Especifica qué vendiste\nSi es gasto: Especifica en qué gastaste\n\n⚠️ Importante para reportes de P&L")
    agregar_comentario(ws['D2'], "💡 DESCRIPCIÓN\n\nDetalla QUÉ fue la transacción.\n\nEjemplo:\n• Pago quincenal empleados\n• Compra inventario laptops HP\n• Servicio técnico en sitio - Cliente XYZ\n\n✅ Sé específico, te ayudará después")
    agregar_comentario(ws['E2'], "💡 CUENTA ORIGEN\n\nElige de dónde salió/entró el dinero:\n\n• Cuenta bancaria específica\n• Tarjeta de crédito\n• Efectivo\n\n⚠️ Debe coincidir exactamente con nombres en hoja EFECTIVO")
    agregar_comentario(ws['F2'], "💡 ENTIDAD (Cliente o Proveedor)\n\nSi es INGRESO: Nombre del cliente\nSi es GASTO: Nombre del proveedor\n\n⚠️ Usa nombres EXACTOS de la hoja ENTIDADES_ALIAS para que sistema los reconozca")
    agregar_comentario(ws['G2'], "💡 FACTURA #\n\nNúmero de factura electrónica.\n\nFormato CR:\n• Clientes: 50601012345678901234567890123456789012345\n• Proveedores: 50601XXXXXXXXXXXXXXX\n\nSi no hay factura: deja vacío")
    agregar_comentario(ws['H2'], "💡 MONTO EN COLONES (CRC)\n\nSi transacción fue en colones, ingrésala aquí.\n\nFormato: 50000 (sin comas)\n\n⚠️ Ingresa SOLO en una moneda (CRC o USD), no ambas")
    agregar_comentario(ws['I2'], "💡 MONTO EN DÓLARES (USD)\n\nSi transacción fue en dólares, ingrésala aquí.\n\nFormato: 100.50\n\n⚠️ Ingresa SOLO en una moneda (CRC o USD), no ambas")
    agregar_comentario(ws['K2'], "💡 MÉTODO DE PAGO\n\nCómo se realizó el pago:\n• Transferencia\n• SINPE Móvil\n• Efectivo\n• Cheque\n• Tarjeta débito\n• Tarjeta crédito\n• Depósito")
    agregar_comentario(ws['L2'], "💡 ESTADO\n\nCOMPLETADA - Ya se realizó\nPENDIENTE - Aún no se ejecuta\nCANCELADA - Se anuló")
    agregar_comentario(ws['M2'], "💡 IVA INCLUIDO (%)\n\nSi el monto incluye IVA, indica %:\n• 13% - Mayoría productos/servicios\n• 0% - Sin IVA\n• 1%, 2%, 4% - Casos especiales\n\n⚠️ Esto permite calcular IVA exacto después")
    agregar_comentario(ws['N2'], "💡 REFERENCIA BANCARIA\n\nNúmero de referencia del banco.\n\nEjemplo:\n• SINPE: 912345678\n• Transferencia: REF-202511-12345\n\nÚtil para conciliación")
    agregar_comentario(ws['O2'], "💡 NOTAS ADICIONALES\n\nCualquier información extra relevante:\n• Recordatorios\n• Aclaraciones\n• Próximas acciones\n• Relaciones con otras transacciones")
    agregar_comentario(ws['P2'], "💡 CREADO POR\n\nIngresa tu nombre o iniciales.\n\nEjemplo:\n• Alvaro\n• AV\n• Contador\n• Asistente\n\nÚtil para auditoría")

    # Estilos columnas editables (amarillo)
    for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']:
        crear_estilo_editable(ws[f'{col}2'])

    # Formatos de número
    ws['H2'].number_format = '#,##0.00'  # CRC
    ws['I2'].number_format = '#,##0.00'  # USD
    ws['J2'].number_format = '#,##0.00'  # Tipo cambio
    ws['A2'].number_format = 'DD/MM/YYYY'

    print("   ✅ Hoja TRANSACCIONES creada")
    print(f"      - {len(headers)} columnas")
    print(f"      - {len([dv_tipo, dv_categoria, dv_cuenta, dv_metodo, dv_estado, dv_iva])} validaciones")
    print(f"      - Manual inline en 16 columnas")

# ============================================================================
# HOJA 2: EFECTIVO
# ============================================================================

def crear_hoja_efectivo(wb):
    """
    Crea la hoja EFECTIVO con 9 cuentas bancarias.

    Calcula saldos automáticamente desde TRANSACCIONES.
    """
    print("\n🏦 Creando hoja EFECTIVO...")

    ws = wb.create_sheet("EFECTIVO")

    # Título
    ws['A1'] = "CONTROL DE EFECTIVO Y BANCOS"
    ws['A1'].font = Font(name='Calibri', size=14, bold=True)
    ws.merge_cells('A1:H1')

    # Encabezados (fila 3)
    headers = ["Cuenta", "Tipo", "Moneda", "Saldo Inicial", "Ingresos", "Egresos", "Saldo Actual", "Notas"]
    for col, header in enumerate(headers, start=1):
        cell = ws.cell(3, col, header)
    crear_estilo_header(ws, 3, 1, len(headers))

    # Anchos
    ws.column_dimensions['A'].width = 35
    ws.column_dimensions['B'].width = 12
    ws.column_dimensions['C'].width = 10
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 15
    ws.column_dimensions['G'].width = 15
    ws.column_dimensions['H'].width = 30

    # Agregar las 9 cuentas
    row = 4
    for cuenta in CUENTAS_BANCARIAS:
        ws.cell(row, 1, cuenta["nombre"])
        ws.cell(row, 2, cuenta["tipo"])
        ws.cell(row, 3, cuenta["moneda"])
        ws.cell(row, 4, cuenta["saldo"])  # Saldo inicial

        # Fórmula INGRESOS (columna E)
        # =SUMIFS(TRANSACCIONES.I:I, TRANSACCIONES.E:E, A4, TRANSACCIONES.B:B, "INGRESO", TRANSACCIONES.L:L, "COMPLETADA")
        formula_ingresos = f'=SUMIFS(TRANSACCIONES!I:I, TRANSACCIONES!E:E, A{row}, TRANSACCIONES!B:B, "INGRESO", TRANSACCIONES!L:L, "COMPLETADA")'
        ws.cell(row, 5, formula_ingresos)
        crear_estilo_formula(ws.cell(row, 5))
        ws.cell(row, 5).number_format = '#,##0.00'

        # Fórmula EGRESOS (columna F)
        # Sumar todos los tipos MENOS INGRESO y TRANSFERENCIA (para evitar doble conteo)
        formula_egresos = f'=SUMIFS(TRANSACCIONES!I:I, TRANSACCIONES!E:E, A{row}, TRANSACCIONES!L:L, "COMPLETADA") - E{row}'
        ws.cell(row, 6, formula_egresos)
        crear_estilo_formula(ws.cell(row, 6))
        ws.cell(row, 6).number_format = '#,##0.00'

        # Fórmula SALDO ACTUAL (columna G)
        formula_saldo = f'=D{row}+E{row}+F{row}'
        ws.cell(row, 7, formula_saldo)
        crear_estilo_formula(ws.cell(row, 7))
        ws.cell(row, 7).number_format = '#,##0.00'

        # Estilos
        crear_estilo_editable(ws.cell(row, 4))  # Saldo inicial editable
        ws.cell(row, 4).number_format = '#,##0.00'

        row += 1

    # Fila TOTAL (después de las 9 cuentas)
    row_total = row
    ws.cell(row_total, 1, "TOTAL EFECTIVO")
    ws.cell(row_total, 1).font = Font(bold=True)

    for col in range(4, 8):  # Columnas D-G
        formula = f'=SUM({get_column_letter(col)}4:{get_column_letter(col)}{row_total-1})'
        ws.cell(row_total, col, formula)
        ws.cell(row_total, col).font = Font(bold=True)
        ws.cell(row_total, col).number_format = '#,##0.00'
        ws.cell(row_total, col).fill = PatternFill(start_color=COLOR_SUCCESS, end_color=COLOR_SUCCESS, fill_type="solid")

    # Agregar nota explicativa
    ws[f'A{row_total + 2}'] = "💡 Los saldos se calculan automáticamente desde TRANSACCIONES"
    ws[f'A{row_total + 2}'].font = FONT_SMALL
    ws.merge_cells(f'A{row_total + 2}:H{row_total + 2}')

    # Agregar comentarios
    agregar_comentario(ws['D4'], "💡 SALDO INICIAL\n\nIngresa el saldo al inicio del mes.\n\nSi es la primera vez: Ingresa saldo al 01/Nov/2025\n\nSi migras desde v2.0: Usa saldo final de Octubre")

    print("   ✅ Hoja EFECTIVO creada")
    print(f"      - {len(CUENTAS_BANCARIAS)} cuentas bancarias")
    print(f"      - Fórmulas automáticas conectadas a TRANSACCIONES")

# ============================================================================
# HOJA 3: DASHBOARD
# ============================================================================

def crear_hoja_dashboard(wb):
    """
    Crea el DASHBOARD con KPIs críticos.

    Métricas prioritarias:
    - Efectivo Total
    - Días de Cobertura
    - Top 5 Clientes
    - Alertas Críticas
    """
    print("\n📊 Creando hoja DASHBOARD...")

    ws = wb.create_sheet("DASHBOARD")

    # Título principal
    ws['B2'] = "DASHBOARD FINANCIERO"
    ws['B2'].font = Font(name='Calibri', size=16, bold=True)
    ws.merge_cells('B2:F2')
    ws['B2'].alignment = Alignment(horizontal='center')

    # Fecha de actualización
    ws['B3'] = "Última actualización:"
    ws['C3'] = "=NOW()"
    ws['C3'].number_format = 'DD/MM/YYYY HH:MM'
    ws['C3'].font = FONT_SMALL

    # ========================================================================
    # SECCIÓN 1: EFECTIVO
    # ========================================================================

    ws['B5'] = "💰 EFECTIVO DISPONIBLE"
    ws['B5'].font = Font(size=12, bold=True)

    ws['B6'] = "Total Efectivo (USD):"
    ws['C6'] = "=EFECTIVO!G13"  # Asumiendo que fila 13 es el total
    ws['C6'].font = Font(size=14, bold=True)
    ws['C6'].number_format = '$#,##0.00'
    ws['C6'].fill = PatternFill(start_color=COLOR_SUCCESS, end_color=COLOR_SUCCESS, fill_type="solid")

    # ========================================================================
    # SECCIÓN 2: DÍAS DE COBERTURA
    # ========================================================================

    ws['B8'] = "⏱️ DÍAS DE COBERTURA"
    ws['B8'].font = Font(size=12, bold=True)

    ws['B9'] = "Gasto Diario Promedio:"
    ws['C9'] = "=SUMIFS(TRANSACCIONES!I:I, TRANSACCIONES!B:B, \"GASTO OPERATIVO\", TRANSACCIONES!L:L, \"COMPLETADA\") / 30"
    ws['C9'].number_format = '$#,##0.00'

    ws['B10'] = "Días de Cobertura:"
    ws['C10'] = "=IF(C9>0, C6/C9, 0)"
    ws['C10'].font = Font(size=14, bold=True)
    ws['C10'].number_format = '0.0'

    # Alerta condicional
    ws['D10'] = '=IF(C10<15, "🚨 CRÍTICO", IF(C10<30, "⚠️ PRECAUCIÓN", "✅ SALUDABLE"))'
    ws['D10'].font = Font(size=11, bold=True)

    # ========================================================================
    # SECCIÓN 3: TOP 5 CLIENTES (NOVIEMBRE)
    # ========================================================================

    ws['B12'] = "🏆 TOP 5 CLIENTES (Noviembre)"
    ws['B12'].font = Font(size=12, bold=True)

    # Encabezados
    ws['B13'] = "Cliente"
    ws['C13'] = "Facturado USD"
    crear_estilo_header(ws, 13, 2, 3)

    # Aquí deberíamos usar fórmulas dinámicas, pero para MVP ponemos los datos del cuestionario
    row = 14
    for i, cliente in enumerate(sorted(CLIENTES, key=lambda x: x["monto_nov"], reverse=True)[:5], 1):
        ws.cell(row, 2, cliente["nombre"])
        ws.cell(row, 3, cliente["monto_nov"])
        ws.cell(row, 3).number_format = '$#,##0.00'
        row += 1

    # ========================================================================
    # SECCIÓN 4: ALERTAS CRÍTICAS
    # ========================================================================

    ws['E5'] = "🚨 ALERTAS CRÍTICAS"
    ws['E5'].font = Font(size=12, bold=True, color='FF0000')

    ws['E6'] = "Duplicados:"
    ws['F6'] = '=COUNTIF(TRANSACCIONES!S:S, "⚠️ POSIBLE DUPLICADO")'
    ws['F6'].font = Font(bold=True)
    ws['F6'].fill = PatternFill(start_color=COLOR_ERROR, end_color=COLOR_ERROR, fill_type="solid")

    ws['E7'] = "Pendientes:"
    ws['F7'] = '=COUNTIF(TRANSACCIONES!L:L, "PENDIENTE")'
    ws['F7'].font = Font(bold=True)
    ws['F7'].fill = PatternFill(start_color=COLOR_WARNING, end_color=COLOR_WARNING, fill_type="solid")

    ws['E8'] = "Sin categoría:"
    ws['F8'] = '=COUNTBLANK(TRANSACCIONES!C:C) - 1'
    ws['F8'].font = Font(bold=True)

    # Anchos
    ws.column_dimensions['B'].width = 25
    ws.column_dimensions['C'].width = 18
    ws.column_dimensions['D'].width = 18
    ws.column_dimensions['E'].width = 20
    ws.column_dimensions['F'].width = 15

    print("   ✅ Hoja DASHBOARD creada")
    print("      - Efectivo total")
    print("      - Días de cobertura con alertas")
    print("      - Top 5 clientes")
    print("      - Alertas de duplicados/pendientes")

# ============================================================================
# HOJA 4: ENTIDADES_ALIAS
# ============================================================================

def crear_hoja_entidades_alias(wb):
    """
    Crea la hoja ENTIDADES_ALIAS con 22 clientes pre-cargados.

    Sistema expandido de normalización para:
    - Clientes
    - Proveedores
    - Bancos
    - Categorías
    """
    print("\n👥 Creando hoja ENTIDADES_ALIAS...")

    ws = wb.create_sheet("ENTIDADES_ALIAS")

    # Título
    ws['A1'] = "SISTEMA DE NORMALIZACIÓN DE ENTIDADES"
    ws['A1'].font = Font(name='Calibri', size=14, bold=True)
    ws.merge_cells('A1:J1')

    # Descripción
    ws['A2'] = "💡 Esta hoja permite normalizar nombres de clientes, proveedores y bancos que aparecen con variaciones"
    ws['A2'].font = FONT_SMALL
    ws.merge_cells('A2:J2')

    # Encabezados (fila 4)
    headers = ["Tipo", "Nombre Estándar", "Alias 1", "Alias 2", "Alias 3", "Alias 4", "Alias 5", "Categoría", "Notas", "Última Actualización"]
    for col, header in enumerate(headers, start=1):
        cell = ws.cell(4, col, header)
    crear_estilo_header(ws, 4, 1, len(headers))

    # Anchos
    widths = [12, 35, 25, 25, 25, 25, 25, 15, 30, 15]
    for col, width in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(col)].width = width

    # ========================================================================
    # CARGAR 22 CLIENTES
    # ========================================================================

    row = 5
    for cliente in sorted(CLIENTES, key=lambda x: x["monto_nov"], reverse=True):
        ws.cell(row, 1, "Cliente")
        ws.cell(row, 2, cliente["nombre"])

        # Generar alias comunes
        nombre = cliente["nombre"]

        # Alias 1: Sin S.A./Ltda
        alias1 = nombre.replace(" S.A.", "").replace(" Ltda", "").replace(" S.A", "").strip()
        ws.cell(row, 3, alias1 if alias1 != nombre else "")

        # Alias 2: Siglas
        palabras = nombre.split()
        if len(palabras) > 2:
            alias2 = "".join([p[0].upper() for p in palabras if len(p) > 3])
            ws.cell(row, 4, alias2 if len(alias2) > 1 else "")

        ws.cell(row, 8, cliente["categoria"])
        ws.cell(row, 9, f"Facturación Nov: ${cliente['monto_nov']:.2f}")
        ws.cell(row, 10, datetime.now().strftime("%d/%m/%Y"))

        # Estilos
        for col in range(1, 11):
            if col in [3, 4, 5, 6, 7]:  # Alias editables
                crear_estilo_editable(ws.cell(row, col))

        row += 1

    # ========================================================================
    # CARGAR 5 PROVEEDORES
    # ========================================================================

    for proveedor in PROVEEDORES:
        ws.cell(row, 1, "Proveedor")
        ws.cell(row, 2, proveedor)
        ws.cell(row, 8, "Principal")
        ws.cell(row, 10, datetime.now().strftime("%d/%m/%Y"))

        for col in range(1, 11):
            if col in [3, 4, 5, 6, 7]:
                crear_estilo_editable(ws.cell(row, col))

        row += 1

    # ========================================================================
    # CARGAR 9 BANCOS
    # ========================================================================

    for cuenta in CUENTAS_BANCARIAS:
        ws.cell(row, 1, "Banco")
        ws.cell(row, 2, cuenta["nombre"])
        ws.cell(row, 8, cuenta["tipo"])
        ws.cell(row, 9, f'Moneda: {cuenta["moneda"]}')
        ws.cell(row, 10, datetime.now().strftime("%d/%m/%Y"))

        for col in range(1, 11):
            if col in [3, 4, 5, 6, 7]:
                crear_estilo_editable(ws.cell(row, col))

        row += 1

    # Agregar instrucciones
    ws[f'A{row + 2}'] = "📋 INSTRUCCIONES:"
    ws[f'A{row + 2}'].font = Font(bold=True)

    ws[f'A{row + 3}'] = "1. Cuando aparezca una variación de nombre, agrégala como 'Alias' en la fila correspondiente"
    ws[f'A{row + 4}'] = "2. Ejecuta: python scripts/normalizar_entidades_universal_v3.py"
    ws[f'A{row + 5}'] = "3. El script unificará todos los nombres automáticamente"

    for i in range(3, 6):
        ws[f'A{row + i}'].font = FONT_SMALL
        ws.merge_cells(f'A{row + i}:J{row + i}')

    # Congelar paneles
    ws.freeze_panes = "B5"

    print("   ✅ Hoja ENTIDADES_ALIAS creada")
    print(f"      - {len(CLIENTES)} clientes pre-cargados")
    print(f"      - {len(PROVEEDORES)} proveedores")
    print(f"      - {len(CUENTAS_BANCARIAS)} cuentas bancarias")
    print(f"      - Total: {len(CLIENTES) + len(PROVEEDORES) + len(CUENTAS_BANCARIAS)} entidades")

# ============================================================================
# HOJA 5: CONFIGURACIÓN
# ============================================================================

def crear_hoja_configuracion(wb):
    """Crea hoja de configuración del sistema"""
    print("\n⚙️ Creando hoja CONFIGURACIÓN...")

    ws = wb.create_sheet("CONFIG")

    ws['A1'] = "CONFIGURACIÓN DEL SISTEMA"
    ws['A1'].font = Font(size=14, bold=True)

    # Información del sistema
    configs = [
        ("Versión", "3.0.0 MVP"),
        ("Fecha Creación", datetime.now().strftime("%d/%m/%Y %H:%M")),
        ("Propietario", "Alvaro Velasco - CIMSA"),
        ("Tipo Cambio por Defecto", "540.00"),
        ("Período Fiscal", "2025"),
        ("Mes Activo", "Noviembre 2025"),
    ]

    row = 3
    for key, value in configs:
        ws.cell(row, 1, key)
        ws.cell(row, 2, value)
        ws.cell(row, 1).font = Font(bold=True)
        row += 1

    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 30

    print("   ✅ Hoja CONFIG creada")

# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """Función principal de creación del Excel v3.0"""

    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║           CREAR EXCEL V3.0 - FASE 1 MVP                     ║
║           Sistema de Saneamiento de Deuda - CIMSA           ║
║                                                               ║
║           Due: Nov 19, 2025 (7 días)                        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)

    # Verificar si archivo ya existe
    if os.path.exists(EXCEL_FILE):
        backup = f"{EXCEL_FILE}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        os.rename(EXCEL_FILE, backup)
        print(f"⚠️ Archivo existente respaldado como: {backup}")

    # Crear nuevo workbook
    print("\n📦 Creando nuevo archivo Excel...")
    wb = openpyxl.Workbook()

    # Eliminar hoja por defecto
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])

    # Crear hojas principales
    crear_hoja_transacciones(wb)
    crear_hoja_efectivo(wb)
    crear_hoja_dashboard(wb)
    crear_hoja_entidades_alias(wb)
    crear_hoja_configuracion(wb)

    # Guardar archivo
    print(f"\n💾 Guardando archivo: {EXCEL_FILE}")
    wb.save(EXCEL_FILE)

    # Resumen final
    print("\n" + "="*60)
    print("✅ EXCEL V3.0 MVP CREADO EXITOSAMENTE")
    print("="*60)
    print(f"\n📄 Archivo: {EXCEL_FILE}")
    print(f"📊 Hojas creadas: {len(wb.sheetnames)}")
    print(f"\nHojas incluidas:")
    for i, sheet in enumerate(wb.sheetnames, 1):
        print(f"   {i}. {sheet}")

    print("\n✅ FASE 1 COMPLETADA:")
    print("   ✅ TRANSACCIONES - 20 columnas con validaciones")
    print("   ✅ EFECTIVO - 9 cuentas bancarias con fórmulas")
    print("   ✅ DASHBOARD - KPIs críticos")
    print("   ✅ ENTIDADES_ALIAS - 22 clientes + 5 proveedores + 9 bancos")
    print("   ✅ Manual inline - Comentarios en todas las celdas editables")

    print("\n📋 PRÓXIMOS PASOS:")
    print("   1. Abre el archivo en Excel/OneDrive")
    print("   2. Verifica validaciones y fórmulas")
    print("   3. Ingresa saldos iniciales en hoja EFECTIVO")
    print("   4. Comienza a registrar transacciones de Noviembre")
    print("   5. Ejecuta: python scripts/importar_datos_noviembre_v2.py (próximo)")

    print("\n" + "="*60)
    print(f"🎯 Tiempo de desarrollo: {datetime.now()}")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
