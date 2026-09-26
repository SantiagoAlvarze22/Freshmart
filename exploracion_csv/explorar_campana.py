import pandas as pd

# se cargan los 3 archivos que se requieren
clientes = pd.read_csv(r'..\freshmart_datasets\campana_verano_clientes.csv')
ventas = pd.read_csv(r'..\freshmart_datasets\campana_verano_ventas.csv')
productos = pd.read_csv(r'..\freshmart_datasets\productos_promo_verano.csv')

print('=' * 60)
print('CLIENTES DE LA CAMPAÑA')
print('=' * 60)
print(f'Filas: {len(clientes):,}')
print(f'Columnas: {clientes.shape[1]}')
print()

print('Estructura DataFrame:')
print()
print(clientes.info())
print()

print('Primeras 5 filas:')
print()
print(clientes.head())
print()

print('Cantidad Nulos por columna')
print()
# print(clientes.isna().sum())
print(clientes.isnull().sum())
print()

print('Cantidad IDs únicos')
print(f"{clientes['cliente_id'].nunique():,}")
print()

print('IDs Totales: ')
print(f"{len(clientes):,}")
print('')

print('Posibles duplicados')
print(f'{len(clientes) - clientes["cliente_id"].nunique():,}')
print()

print('Confirmación valores duplicados')
ddpli = len(clientes.drop_duplicates(subset=['cliente_id']))
print(f'Valores duplicados: {len(clientes) - ddpli}')
print()

print('Otro confirmación con duplicated')
dupli_va = clientes.duplicated().sum()
print(f'Valores duplicados TODA UNA FILA COMPLETA calculados con duplicated().sum(): {dupli_va}')
print()

print('Otro confirmación con duplicated')
dupli_va = clientes['cliente_id'].duplicated().sum()
print(
    f'Valores duplicados en una columna especifica, calculados con duplicated().sum(): {dupli_va}'
)
