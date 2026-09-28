import boto3
from botocore.exceptions import ClientError
import os

# Creo sesion con el perfil de freshmart
session = boto3.Session(profile_name='freshmart')

# Archivos de María
archivos = [
    "freshmart_datasets\campana_verano_clientes.csv",
    "freshmart_datasets\campana_verano_ventas.csv",
    "freshmart_datasets\productos_promo_verano.csv",
]

mi_bucket = 'freshmart-project-2026'
s3_client = session.client('s3')


# Crear bucket y verificar si se encuentra en la lista
def crear_bucket_s3(bucket_name, region='us-east-1'):
    try:
        s3_client = session.client('s3', region_name=region)
        response = s3_client.list_buckets()

        # diccionario con lista de buckets
        bucket_list = [name['Name'] for name in response['Buckets']]

        # verificar si existe el bucket sino se crea y sino pues lo reemplaza pero no lo dubplica
        if bucket_name not in bucket_list:
            if region == 'us-east-1':
                s3_client.create_bucket(Bucket=bucket_name)
            else:
                s3_client.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': region},
                )
        return True

    except ClientError as e:
        print(f"Error al crear el bucket: {e}")
        return False


crear_bucket_s3(mi_bucket)

# Subir archivos al bucket

for archivo in archivos:
    try:
        # se toma el nombre base de los archivos
        nombre_archivo = os.path.basename(archivo)

        # se genera la ruta donde iran los archivos dentro del bucket
        ruta_s3 = f"datos-crudos/{nombre_archivo}"

        # se suben los archivos al bucket
        s3_client.upload_file(archivo, mi_bucket, ruta_s3)
        print(f'se sube archivo {nombre_archivo}')

    except ClientError as e:
        print(f"Error al crear el bucket: {e}")
