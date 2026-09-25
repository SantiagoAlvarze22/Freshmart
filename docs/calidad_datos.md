# Calidad de los datos de entrada

Análisis de los CSV entregados por María para la campaña de verano.

## Resumen

| Archivo | Filas | Estado | Problemas principales |
|---|---|---|---|
| `campana_verano_clientes.csv` | 15.247 | ⚠️ Con problemas | IDs repetidos, nulos |
| `campana_verano_ventas.csv` | 42.891 | ❌ Crítico | Fechas, precios, duplicados |
| `productos_promo_verano.csv` | 312 | ✅ Fiable | Ninguno |

## Detalle por archivo

### `campana_verano_clientes.csv` (15.247 filas)

- **301 `cliente_id` repetidos** → 2,0% del total
- **28.750 nulos** → la mayoría son esperables (campos opcionales)

### `campana_verano_ventas.csv` (42.891 filas)

- **3 formatos de fecha distintos** en la misma columna
- **`precio` como texto** con formato `"4,66€"` → 100% de las filas
- **847 `cliente_id` vacíos** → 2,0%
- **155 filas duplicadas exactas** → 0,4%
- **3 filas con `cantidad = 0`**

### `productos_promo_verano.csv` (312 filas)

- ✅ Sin problemas detectados — usar como referencia fiable

## Impacto en el pipeline

- Las fechas deben **normalizarse** antes de cualquier cálculo temporal.
- El precio debe **parsearse** (quitar `€`, cambiar `,` por `.`, convertir a float).
- Es necesario **deduplicar** ventas y decidir qué hacer con los `cliente_id` vacíos.
- Los `cliente_id` repetidos en clientes requieren definir una **regla de desambiguación**.

## Pendiente con María

- [ ] Confirmar formato de fecha oficial
- [ ] Enviar CSV de ventas sin duplicados
- [ ] Aclarar los 3 registros con `cantidad = 0`