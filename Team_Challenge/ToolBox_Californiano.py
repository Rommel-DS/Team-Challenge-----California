#Imports conjunto
import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import seaborn as sns
import matplotlib.pyplot as plt

def describe_df(df_origen):
    '''La función recibe un dataframe origen y devuelve un dataframe resultado 
    con información sobre el tipo de dato, valores faltantes, valores únicos y cardinalidad
    
    Argumento: 
    1. Parámetro único: DataFrame a analizar

    Retorna:
    1. Nombre de la variable
    2. Tipo de dato de la variable
    3. Porcentaje de valores nulos de la variable
    4. Número de valores únicos de la variable
    5. Porcentaje de cardinalidad de la variable


    '''
    # Creamos el diccionario para almacenar los resultados de los indicadores:
    resultado = {
        "COL_N": [],
        "DATA_TYPE": [],
        "MISSINGS (%)": [],
        "UNIQUE_VALUES":[],
        "CARDIN (%)": []
    }
    # Rellenamos los valores iterando en las columnas del DataFrame de origen:
    for col in df_origen.columns:
        resultado["COL_N"].append(col)
        resultado["DATA_TYPE"].append(df_origen[col].dtype)
        missings = round(df_origen[col].isna().sum()/len(df_origen)*100, 1)
        resultado["MISSINGS (%)"].append(missings)
        valores_unicos=df_origen[col].nunique()
        resultado["UNIQUE_VALUES"].append(valores_unicos)
        cardinalidad = round((valores_unicos/len(df_origen))*(1-missings/100),2)
        resultado["CARDIN (%)"].append(cardinalidad)
    
    df_resultado = pd.DataFrame(resultado) # convertimos en un DataFrame

    df_resultado.set_index("COL_N", inplace=True) # Establecemos como indices los nombres de las variables


    return df_resultado.T #Trasponemos el DataFrame

def clasifica_variables(df, umbral_categoria, umbral_continua):
    """
    Clasifica las columnas de un DataFrame en Binaria, Categórica, Numérica Continua o Numérica Discreta.

    Argumentos:
    df (pd.DataFrame): El DataFrame a analizar.
    umbral_categoria (int): Umbral de cardinalidad para diferenciar entre categórica y numérica.
    umbral_continua (float): Umbral del porcentaje de cardinalidad para diferenciar entre numérica continua y discreta.

    Retorna:
    pd.DataFrame: DataFrame con las columnas 'nombre_variable' y 'tipo_sugerido'.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("El argumento proporcionado no es un DataFrame.")

    total_filas = len(df)
    resultados = []

    for col in df.columns:
        cardinalidad = df[col].nunique(dropna=True)  # Ignorar valores nulos para el conteo único
        porcentaje_cardinalidad = cardinalidad / total_filas if total_filas > 0 else 0
        es_numerica = pd.api.types.is_numeric_dtype(df[col])

        if cardinalidad == 2:
            tipo = "Binaria"
        elif cardinalidad < umbral_categoria:
            tipo = "Categórica"
        elif cardinalidad >= umbral_categoria:
            if es_numerica:
                tipo = "Numérica Continua" if porcentaje_cardinalidad >= umbral_continua else "Numérica Discreta"
            else:
                tipo = "Categórica"
        else:
            tipo = "Indefinida"

        resultados.append({"nombre_variable": col, "tipo_sugerido": tipo})

    return pd.DataFrame(resultados)
