# Lecciones Aprendidas - QuickBooks Desktop 2013 Multi-Currency

**Fecha:** 06/11/2025
**Sesión:** Ajustes de apertura y configuración multi-currency

---

## 🎯 Regla de Oro: NUNCA asumir, SIEMPRE verificar

Antes de dar instrucciones al usuario:
1. ✅ Pedir reportes actualizados
2. ✅ Verificar registros de cuentas específicas
3. ✅ Confirmar tipos de cuenta (Bank, Credit Card, Equity, etc.)
4. ✅ Investigar en documentación oficial si hay duda
5. ❌ NO dar instrucciones basadas en suposiciones

---

## 📚 Conocimientos Críticos QB Desktop 2013

### 1. Cuentas Credit Card - Contabilidad INVERTIDA

**En cuentas tipo Credit Card (tarjetas de crédito):**

- **CREDIT** = CHARGE (AUMENTA el saldo de la tarjeta) ✅
- **DEBIT** = PAYMENT (REDUCE el saldo de la tarjeta) ✅

**Esto es OPUESTO a cuentas Bank o Asset.**

**Ejemplo práctico:**
- Tarjeta tiene $100 de deuda
- Necesito AUMENTAR a $150
- Journal Entry: **CREDIT** la cuenta Credit Card por $50 (no DEBIT)

**Registro muestra:**
- CHARGE = Aumenta deuda
- PAYMENT = Reduce deuda

---

### 2. Exchange Rate en Journal Entries

**Reglas según contexto:**

**A) Currency del Journal Entry = USD:**
- Al seleccionar cuenta CRC, QB muestra: "1 CRC = X USD"
- **Debes ingresar:** 0.00197239 (1 CRC = $0.00197239 USD)

**B) Currency del Journal Entry = CRC:**
- Al seleccionar cuenta USD, QB muestra: "1 CRC = X USD"
- **Debes ingresar:** 0.00197239 también

**C) QB puede mostrar "1 CRC = 1 USD" por defecto:**
- SIEMPRE corregir a 0.00197239
- NO asumir que está correcto

**Fórmulas de conversión:**
- 1 USD = 507 CRC
- 1 CRC = 0.00197239 USD
- Para convertir: CRC ÷ 507 = USD
- Para convertir: USD × 507 = CRC

---

### 3. Home Currency Adjustment (Función Especial)

**Descubrimiento clave:**

QB Desktop tiene checkbox **"Home Currency Adjustment"** en Journal Entries que permite:
- Ajustar el valor en USD de cuentas en moneda extranjera
- SIN afectar el balance en la moneda extranjera
- El offset va automáticamente a "Exchange Gain or Loss" (77000)

**Cuándo usar:**
- Ajustes de fin de año
- Corrección de diferencias de tipo de cambio
- Cuando el saldo en moneda extranjera es correcto pero la conversión USD está mal

**Referencias:**
- Intuit Support: "Foreign currency bank account year-end adjustment"
- InsightfulAccountant: "QuickBooks Desktop Home Currency Adjustment Super Trick"

---

### 4. Tipos de Cuenta y Moneda Extranjera

**Restricciones QB Desktop 2013:**

| Tipo de Cuenta | ¿Permite moneda extranjera? | Notas |
|----------------|----------------------------|-------|
| Bank | ✅ Sí | Checkbox "Foreign Currency" disponible |
| Credit Card | ⚠️ **SÍ pero SIN checkbox** | **HALLAZGO 07/11:** NO aparece checkbox "Foreign Currency" al crear, pero acepta transacciones en moneda extranjera |
| Accounts Receivable | ✅ Sí (auto-creado) | |
| Accounts Payable | ✅ Sí (auto-creado) | |
| Other Current Asset | ❌ NO | |
| Other Current Liability | ❌ NO | |
| Equity | ✅ Sí (pero usar USD como home currency) | |

**IMPORTANTE - Descubrimiento 07/11/2025:**

Al crear cuenta tipo **Credit Card**, QuickBooks Desktop 2013:
- ❌ **NO muestra** el checkbox "Foreign Currency" durante creación
- ✅ **SÍ permite** registrar transacciones en CRC después de creada
- ✅ La cuenta **SÍ funciona** correctamente con moneda extranjera
- ⚠️ Comportamiento diferente a cuentas tipo Bank

**Workarounds necesarios:**
- IVA Crédito Fiscal (asset CRC): Crear como **Bank** + nota en descripción ✅ checkbox disponible
- IVA Débito Fiscal (liability CRC): Crear como **Credit Card** + nota en descripción ⚠️ checkbox NO aparece pero funciona

---

### 5. Balance Sheet - Conversión Automática

**Importante:**

El Balance Sheet SIEMPRE muestra todos los montos en **Home Currency (USD)**.

**Ejemplo:**
- Cuenta 2140 (CRC) tiene saldo: ₡1,481,391.92
- Balance Sheet muestra: $2,921.75 USD (₡1,481,391.92 ÷ 507)

**Para ver saldo en moneda original:**
- Abrir Chart of Accounts
- Doble-click en la cuenta específica
- El registro muestra el saldo en su moneda nativa (CRC)

---

### 6. Verificación de Tipo de Cambio

**Comando de verificación:**
1. Edit menu → Preferences → Multiple Currencies → Currency List
2. Verificar que CRC muestre: 1 USD = 507.00000 CRC
3. Si muestra 1 CRC = 1 USD → ERROR CRÍTICO, corregir inmediatamente

---

### 7. Journal Entry - Mejores Prácticas

**Antes de crear Journal Entry:**
1. ✅ Confirmar tipo de cuenta (Bank vs Credit Card vs Equity)
2. ✅ Verificar moneda de AMBAS cuentas involucradas
3. ✅ Confirmar dirección del ajuste (aumentar vs disminuir)
4. ✅ Verificar tipo de cambio actual en QB
5. ✅ Calcular monto esperado en ambas monedas

**Durante Journal Entry:**
1. ✅ Seleccionar Currency apropiada (USD para simplicidad)
2. ✅ Corregir Exchange Rate si es necesario
3. ✅ Para Credit Card: CREDIT = aumenta, DEBIT = reduce
4. ✅ Para Bank/Asset: DEBIT = aumenta, CREDIT = reduce
5. ✅ Verificar que Difference = 0.00

**Después de guardar:**
1. ✅ Abrir registro de cuenta afectada
2. ✅ Verificar que el saldo cambió en la DIRECCIÓN correcta
3. ✅ Verificar el MONTO en la moneda nativa
4. ✅ Si está mal: Borrar inmediatamente y recrear

---

## 🚨 Errores Comunes y Soluciones

### Error 1: Ajuste va en dirección opuesta

**Síntoma:**
- Esperaba aumentar $100, pero disminuyó $100

**Causa:**
- Confusión entre DEBIT/CREDIT en Credit Card accounts

**Solución:**
1. Borrar Journal Entry incorrecto
2. Confirmar tipo de cuenta (Bank vs Credit Card)
3. Si es Credit Card: usar CREDIT para aumentar
4. Si es Bank/Asset: usar DEBIT para aumentar

---

### Error 2: Exchange Rate incorrecto

**Síntoma:**
- Montos convertidos no coinciden con cálculos manuales

**Causa:**
- QB mostrando "1 CRC = 1 USD" por defecto
- Usuario no corrigiendo a 0.00197239

**Solución:**
1. SIEMPRE verificar Exchange Rate al seleccionar cuenta CRC
2. Corregir a 0.00197239 si es necesario
3. Presionar Tab para aplicar

---

### Error 3: Account 77000 · Exchange Gain or Loss aparece automáticamente

**Síntoma:**
- Journal Entry crea línea extra no solicitada en cuenta 77000

**Causa:**
- QB detecta desbalance en conversión multi-currency

**Solución:**
1. Verificar que Exchange Rate sea correcto
2. Considerar usar "Home Currency Adjustment" checkbox
3. Si persiste, aceptar la línea 77000 (es normal en ajustes multi-currency)

---

## 📖 Recursos de Referencia

### Documentación Oficial Intuit:
- Set up and use Multicurrency: https://quickbooks.intuit.com/learn-support/en-ca/help-article/multicurrency/
- Foreign currency bank account adjustment: https://quickbooks.intuit.com/learn-support/en-us/reports-and-accounting/foreign-currency-bank-account-year-end-adjustment/00/820935
- Enter home currency adjustments: https://quickbooks.intuit.com/learn-support/en-us/help-article/multicurrency/enter-home-currency-adjustments-foreign-balances/

### Artículos Especializados:
- InsightfulAccountant: "QuickBooks Desktop Home Currency Adjustment Super Trick"
- FirmOfTheFuture: "Home currency adjustment in QuickBooks Online"

---

## ✅ Checklist Pre-Ajuste

Antes de dar instrucciones al usuario sobre un ajuste:

- [ ] Obtener Balance Sheet completo actualizado
- [ ] Obtener registro de cuenta específica a ajustar
- [ ] Confirmar tipo de cuenta (Bank/Credit Card/Equity/etc.)
- [ ] Confirmar moneda de la cuenta
- [ ] Verificar tipo de cambio actual en QB
- [ ] Calcular monto esperado en ambas monedas (USD y CRC)
- [ ] Confirmar dirección del ajuste (aumentar/disminuir)
- [ ] Identificar cuenta contrapartida (Equity, Gain/Loss, etc.)
- [ ] SI HAY DUDA: Investigar en documentación oficial ANTES de proceder

---

## 🎓 Compromiso de Mejora Continua

1. **Antes de cada sesión de ajustes:** Revisar este documento
2. **Cuando algo falle:** Investigar documentación oficial inmediatamente
3. **Después de cada sesión:** Actualizar este documento con nuevos aprendizajes
4. **NUNCA asumir:** Siempre pedir datos concretos al usuario

---

**Última actualización:** 06/11/2025 8:45 PM
**Lecciones aprendidas de:** Sesión de ajustes 02-06 Nov 2025
