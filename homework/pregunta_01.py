"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    # Cargar datos
    file = 'files/input/solicitudes_de_credito.csv'
    data = pd.read_csv(file, sep=';')

    # Eliminar registros con valores faltantes
    data = data.dropna()

    # Eliminar primera columna
    data = data.drop(columns=["Unnamed: 0"])

    # Limpieza de la columna 'monto_del_credito'
    data['monto_del_credito'] = data['monto_del_credito'].str.replace("[$, ]", "", regex=True).str.strip() 
    data['monto_del_credito'] = pd.to_numeric(data['monto_del_credito'], errors='coerce') 
    data['monto_del_credito'] = data['monto_del_credito'].astype(str).str.replace('.00', '')  
    data['monto_del_credito'] = data['monto_del_credito'].fillna(0).astype(float).astype(int) 
    
    # Limpieza de columnas de texto
    tex_columns = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito'] 
    data[tex_columns] = data[tex_columns].apply(lambda x: x.str.lower().replace(['-', '_'], ' ', regex=True).str.strip())
    data['barrio'] = data['barrio'].str.lower().replace(['-', '_'], ' ', regex=True)

    #modificar fecha
    def org_Fecha(fecha):
        try:
            return pd.to_datetime(fecha, format='%Y/%m/%d')
        except ValueError:
            return pd.to_datetime(fecha, format='%d/%m/%Y')

    data['fecha_de_beneficio'] = data['fecha_de_beneficio'].apply(org_Fecha)

    #dar el formato correcto a las columnas
    data['monto_del_credito'] = data['monto_del_credito'].astype(float)
    data['comuna_ciudadano'] = data['comuna_ciudadano'].astype(int)
    data['estrato'] = data['estrato'].astype(int)
    data['barrio'] = data['barrio'].astype(str)

    #eliminar duplicados
    data.drop_duplicates(inplace=True)

    # Crear directorio de salida si no existe
    output_dir = 'files/output' # Define la carpeta de salida
    os.makedirs(output_dir, exist_ok=True) # Crea la carpeta si no existe.

    # Guardar el archivo limpio
    data.to_csv('files/output/solicitudes_de_credito.csv', index=False, sep=';')

if __name__ == '__main__':
    print(pregunta_01())


