#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SISTEMA DE ALIAS - CUENTAS BANCARIAS Y CONCEPTOS
Define todas las variaciones posibles de nombres de cuenta y conceptos
y mapea automáticamente al nombre canónico
"""

# ============================================================================
# DEFINICIÓN DE ALIAS - CONCEPTOS/TIPOS DE MOVIMIENTO
# ============================================================================

ALIAS_CONCEPTOS = {
    # Balance inicial / Apertura inicial
    "Balance inicial": [
        "Balance inicial",
        "Apertura Inicial",
        "Apertura inicial",
        "BALANCE INICIAL",
        "APERTURA INICIAL",
        "balance inicial",
        "apertura inicial",
        "Saldo inicial",
        "saldo inicial",
        "SALDO INICIAL",
    ],
}

# ============================================================================
# DEFINICIÓN DE ALIAS - CUENTAS BANCARIAS
# ============================================================================

ALIAS_CUENTAS = {
    # PROMERICA USD 1774
    "Promerica USD 1774": [
        "Promerica USD 1774",
        "Promerica USD",
        "Promerica USD (40000003881774)",
        "PROMERICA USD 1774",
        "promerica usd 1774",
        "Promerica 1774",
        "1774",
        "40000003881774",
    ],

    # PROMERICA CRC 1708
    "Promerica CRC 1708": [
        "Promerica CRC 1708",
        "Promerica CRC",
        "Promerica CRC (10000003881708)",
        "PROMERICA CRC",
        "10000003881708",
    ],

    # BNCR USD 601066 (Empresarial)
    "BNCR USD 601066": [
        "BNCR USD 601066",
        "BNCR USD (601066-4)",
        "BNCR USD 601066-4",
        "601066",
        "601066-4",
        "BNCR Empresarial USD",
    ],

    # BNCR USD 11121 (Personal)
    "BNCR USD 11121": [
        "BNCR USD 11121",
        "BNCR USD (11121)",
        "BNCR USD 1112-1",
        "11121",
        "1112-1",
        "200020870111121",
        "200-02-087-011121",
    ],

    # BNCR CRC 188618
    "BNCR CRC 188618": [
        "BNCR CRC 188618",
        "BNCR CRC (188618-3)",
        "BNCR CRC 188618-3",
        "BNCR CRC",
        "188618",
        "188618-3",
        "100-01-000-188618-3",
    ],

    # TARJETA BNCR VISA 3519
    "TC BNCR Visa 3519": [
        "TC BNCR Visa 3519",
        "Tarjeta BNCR Visa 3519",
        "TC BNCR TC BNCR 3519",
        "BNCR Visa 3519",
        "Visa 3519",
        "3519",
        "************3519",
    ],

    # TARJETA BNCR MC 8759
    "TC BNCR MC 8759": [
        "TC BNCR MC 8759",
        "Tarjeta BNCR MC 8759",
        "TC BNCR TC BNCR 8759",
        "BNCR MC 8759",
        "MC 8759",
        "8759",
        "************8759",
    ],

    # TARJETA BNCR VISA 9837
    "TC BNCR Visa 9837": [
        "TC BNCR Visa 9837",
        "Tarjeta BNCR Visa 9837",
        "TC BNCR TC BNCR 9837",
        "BNCR Visa 9837",
        "Visa 9837",
        "9837",
        "************9837",
    ],

    # TARJETA BNCR 6386
    "TC BNCR 6386": [
        "TC BNCR 6386",
        "TC BNCR TC BNCR 6386",
        "Tarjeta BNCR 6386",
        "6386",
        "************6386",
    ],

    # TARJETA BAC
    "TC BAC": [
        "TC BAC",
        "TC BAC TC BAC",
        "Tarjeta BAC",
        "BAC",
    ],

    # AHORROS BNCR
    "BNCR Ahorro Matrimonio": [
        "BNCR Ahorro Matrimonio",
        "BNCR Ahorro 1002335826",
        "Ahorro Matrimonio",
        "1002335826",
    ],

    "BNCR Ahorro Impuestos": [
        "BNCR Ahorro Impuestos",
        "BNCR Ahorro 1002273441",
        "BNCR Ahorro Impuestos Municipales",
        "Ahorro Impuestos Municipales",
        "1002273441",
    ],

    "BNCR Ahorro Black Friday": [
        "BNCR Ahorro Black Friday",
        "BNCR Ahorro 1002388223",
        "Ahorro Black Friday",
        "1002388223",
    ],

    "BNCR Ahorro Vehiculo": [
        "BNCR Ahorro Vehiculo",
        "BNCR Ahorro 17000002201",
        "BNCR Ahorro Vehículo Nuevo",
        "Ahorro Vehículo Nuevo",
        "17000002201",
    ],

    # CUENTAS ESPECIALES
    "Por Cobrar": [
        "Por Cobrar",
        "Cuentas por Cobrar",
        "A_R",
        "Accounts Receivable",
    ],

    "Por Pagar": [
        "Por Pagar",
        "Cuentas por Pagar",
        "A_P",
        "Accounts Payable",
    ],

    "Pasivos": [
        "Pasivos",
        "Liabilities",
        "Deudas",
    ],
}

# ============================================================================
# ÍNDICE INVERTIDO (para búsqueda rápida)
# ============================================================================

# Crear índice: alias -> nombre_canonico (CUENTAS)
INDICE_ALIAS = {}

for nombre_canonico, aliases in ALIAS_CUENTAS.items():
    for alias in aliases:
        # Normalizar: mayúsculas, sin espacios extras
        alias_norm = alias.strip().upper()
        INDICE_ALIAS[alias_norm] = nombre_canonico

# Crear índice: alias -> nombre_canonico (CONCEPTOS)
INDICE_ALIAS_CONCEPTOS = {}

for nombre_canonico, aliases in ALIAS_CONCEPTOS.items():
    for alias in aliases:
        # Normalizar: mayúsculas, sin espacios extras
        alias_norm = alias.strip().upper()
        INDICE_ALIAS_CONCEPTOS[alias_norm] = nombre_canonico

# ============================================================================
# FUNCIONES PÚBLICAS
# ============================================================================

def obtener_nombre_canonico(nombre_cuenta):
    """
    Recibe cualquier variación de nombre de cuenta
    y devuelve el nombre canónico oficial.

    Args:
        nombre_cuenta (str): Cualquier variación del nombre

    Returns:
        str: Nombre canónico, o None si no se encuentra

    Ejemplo:
        >>> obtener_nombre_canonico("Promerica USD")
        "Promerica USD 1774"
        >>> obtener_nombre_canonico("TC BNCR TC BNCR 8759")
        "TC BNCR MC 8759"
        >>> obtener_nombre_canonico("************3519")
        "TC BNCR Visa 3519"
    """
    if not nombre_cuenta:
        return None

    # Normalizar
    nombre_norm = str(nombre_cuenta).strip().upper()

    # Buscar en índice
    return INDICE_ALIAS.get(nombre_norm, None)


def obtener_todos_alias(nombre_cuenta):
    """
    Devuelve todos los alias conocidos para una cuenta.

    Args:
        nombre_cuenta (str): Nombre canónico o cualquier alias

    Returns:
        list: Lista de todos los alias, o lista vacía si no existe
    """
    nombre_canonico = obtener_nombre_canonico(nombre_cuenta)

    if nombre_canonico:
        return ALIAS_CUENTAS.get(nombre_canonico, [])
    else:
        return []


def es_misma_cuenta(nombre1, nombre2):
    """
    Verifica si dos nombres se refieren a la misma cuenta.

    Args:
        nombre1 (str): Primer nombre
        nombre2 (str): Segundo nombre

    Returns:
        bool: True si son la misma cuenta, False en caso contrario

    Ejemplo:
        >>> es_misma_cuenta("Promerica USD", "Promerica USD 1774")
        True
        >>> es_misma_cuenta("TC BNCR Visa 3519", "Tarjeta BNCR Visa 3519")
        True
    """
    canon1 = obtener_nombre_canonico(nombre1)
    canon2 = obtener_nombre_canonico(nombre2)

    if canon1 and canon2:
        return canon1 == canon2
    else:
        return False


def listar_cuentas():
    """
    Lista todas las cuentas canónicas disponibles.

    Returns:
        list: Lista de nombres canónicos
    """
    return list(ALIAS_CUENTAS.keys())


def agregar_alias(nombre_canonico, nuevo_alias):
    """
    Agrega un nuevo alias dinámicamente.

    Args:
        nombre_canonico (str): Nombre canónico de la cuenta
        nuevo_alias (str): Nuevo alias a agregar

    Returns:
        bool: True si se agregó, False si la cuenta no existe
    """
    if nombre_canonico in ALIAS_CUENTAS:
        if nuevo_alias not in ALIAS_CUENTAS[nombre_canonico]:
            ALIAS_CUENTAS[nombre_canonico].append(nuevo_alias)

            # Actualizar índice
            alias_norm = nuevo_alias.strip().upper()
            INDICE_ALIAS[alias_norm] = nombre_canonico

            return True

    return False


# ============================================================================
# FUNCIONES PÚBLICAS - CONCEPTOS
# ============================================================================

def obtener_concepto_canonico(concepto):
    """
    Recibe cualquier variación de concepto/tipo de movimiento
    y devuelve el nombre canónico oficial.

    Args:
        concepto (str): Cualquier variación del concepto

    Returns:
        str: Nombre canónico, o None si no se encuentra

    Ejemplo:
        >>> obtener_concepto_canonico("Apertura Inicial")
        "Balance inicial"
        >>> obtener_concepto_canonico("SALDO INICIAL")
        "Balance inicial"
    """
    if not concepto:
        return None

    # Normalizar
    concepto_norm = str(concepto).strip().upper()

    # Buscar en índice
    return INDICE_ALIAS_CONCEPTOS.get(concepto_norm, None)


def es_balance_inicial(concepto):
    """
    Verifica si un concepto se refiere a "Balance inicial" o cualquier alias.

    Args:
        concepto (str): Concepto a verificar

    Returns:
        bool: True si es un balance inicial, False en caso contrario

    Ejemplo:
        >>> es_balance_inicial("Apertura Inicial")
        True
        >>> es_balance_inicial("Balance inicial")
        True
        >>> es_balance_inicial("Compra")
        False
    """
    if not concepto:
        return False

    concepto_canonico = obtener_concepto_canonico(concepto)
    return concepto_canonico == "Balance inicial"


def listar_conceptos():
    """
    Lista todos los conceptos canónicos disponibles.

    Returns:
        list: Lista de nombres canónicos de conceptos
    """
    return list(ALIAS_CONCEPTOS.keys())


# ============================================================================
# TESTING / DEMOSTRACIÓN
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("SISTEMA DE ALIAS - CUENTAS BANCARIAS")
    print("="*80)

    print(f"\nTotal cuentas canónicas: {len(ALIAS_CUENTAS)}")
    print(f"Total alias en índice: {len(INDICE_ALIAS)}")

    print("\n" + "="*80)
    print("PRUEBAS DE RECONOCIMIENTO")
    print("="*80)

    # Casos de prueba
    casos_prueba = [
        "Promerica USD",
        "Promerica USD 1774",
        "40000003881774",
        "TC BNCR Visa 3519",
        "Tarjeta BNCR Visa 3519",
        "************8759",
        "BNCR USD 601066",
        "BNCR USD (601066-4)",
        "200-02-087-011121",
        "TC BAC TC BAC",
        "Por Cobrar",
        "Cuenta Inexistente",
    ]

    for caso in casos_prueba:
        canonico = obtener_nombre_canonico(caso)
        if canonico:
            print(f"\n✓ '{caso}'")
            print(f"  → Reconocido como: {canonico}")
        else:
            print(f"\n✗ '{caso}'")
            print(f"  → NO RECONOCIDO")

    print("\n" + "="*80)
    print("TODAS LAS CUENTAS Y SUS ALIAS")
    print("="*80)

    for nombre_canonico in sorted(ALIAS_CUENTAS.keys()):
        aliases = ALIAS_CUENTAS[nombre_canonico]
        print(f"\n📊 {nombre_canonico}")
        print(f"   Alias: {len(aliases)}")
        for alias in aliases:
            if alias != nombre_canonico:
                print(f"      - {alias}")

    print("\n" + "="*80)
    print("PRUEBA DE COMPARACIÓN")
    print("="*80)

    comparaciones = [
        ("Promerica USD", "Promerica USD 1774"),
        ("TC BNCR Visa 3519", "Tarjeta BNCR Visa 3519"),
        ("BNCR USD 601066", "BNCR USD 11121"),
        ("************8759", "TC BNCR MC 8759"),
    ]

    for nombre1, nombre2 in comparaciones:
        resultado = es_misma_cuenta(nombre1, nombre2)
        simbolo = "✓" if resultado else "✗"
        print(f"\n{simbolo} '{nombre1}' == '{nombre2}': {resultado}")

    print("\n" + "="*80)
