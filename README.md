# Análisis y Visualización de Datos: Funciones para DataFrames en Python

Este repositorio incluye un conjunto de funciones diseñadas para analizar y visualizar datos almacenados en DataFrames de Pandas. A continuación, se describe brevemente la funcionalidad de cada función.

---

## Funciones

### 1. `describe_df(df_origen)`
**Descripción**:  
Analiza un DataFrame y devuelve un resumen con información de las columnas, incluyendo tipo de dato, porcentaje de valores nulos, número de valores únicos y cardinalidad.  

**Argumentos**:
- `df_origen` (DataFrame): El DataFrame a analizar.

**Retorna**:
- DataFrame traspuesto con las siguientes columnas:
  - `COL_N`: Nombre de la columna.
  - `DATA_TYPE`: Tipo de dato.
  - `MISSINGS (%)`: Porcentaje de valores nulos.
  - `UNIQUE_VALUES`: Número de valores únicos.
  - `CARDIN (%)`: Porcentaje de cardinalidad.

---

### 2. `clasifica_variables(df, umbral_categoria, umbral_continua)`
**Descripción**:  
Clasifica las columnas de un DataFrame en categorías como: Binaria, Categórica, Numérica Continua o Numérica Discreta.  

**Argumentos**:
- `df` (DataFrame): El DataFrame a analizar.
- `umbral_categoria` (int): Límite de cardinalidad para diferenciar entre categórica y numérica.
- `umbral_continua` (float): Límite del porcentaje de cardinalidad para diferenciar entre numérica continua y discreta.

**Retorna**:
- DataFrame con las columnas:
  - `nombre_variable`: Nombre de la columna.
  - `tipo_sugerido`: Clasificación sugerida.

---

### 3. `get_features_num_regression(dataframe, target_col, umbral_corr, pvalue=None, umbral_cat=20)`
**Descripción**:  
Selecciona las columnas numéricas cuya correlación con la columna objetivo (`target_col`) supera un umbral especificado. Opcionalmente, aplica un test de hipótesis para asegurar significancia estadística.  

**Argumentos**:
- `dataframe` (DataFrame): Conjunto de datos de entrada.
- `target_col` (str): Columna objetivo (numérica continua).
- `umbral_corr` (float): Mínimo valor de correlación aceptado.
- `pvalue` (float, opcional): Nivel de significancia estadística.
- `umbral_cat` (int, opcional): Umbral para distinguir variables categóricas.

**Retorna**:
- Lista de columnas numéricas que cumplen los criterios de correlación y significancia.

---

### 4. `plot_features_num_regression(dataframe, target_col="", columns=[], umbral_corr=0, pvalue=None)`
**Descripción**:  
Genera gráficos de dispersión (`pairplot`) para analizar las relaciones entre variables numéricas y la columna objetivo.  

**Argumentos**:
- `dataframe` (DataFrame): Conjunto de datos de entrada.
- `target_col` (str): Columna objetivo.
- `columns` (list, opcional): Columnas a analizar.
- `umbral_corr` (float, opcional): Mínimo valor de correlación.
- `pvalue` (float, opcional): Nivel de significancia estadística.

**Retorna**:
- Lista de columnas que cumplen los criterios, además de gráficos generados.

---

### 5. `get_features_cat_regression(dataframe, target_col, pvalue=0.05)`
**Descripción**:  
Identifica columnas categóricas que tienen una relación estadísticamente significativa con una columna objetivo numérica.  

**Argumentos**:
- `dataframe` (DataFrame): Conjunto de datos de entrada.
- `target_col` (str): Columna objetivo (numérica).
- `pvalue` (float, opcional): Nivel de significancia estadística.

**Retorna**:
- Lista de columnas categóricas significativas.

---

### 6. `plot_features_cat_regression(dataframe, target_col="", columns=[], pvalue=0.05, with_individual_plot=False)`
**Descripción**:  
Genera histogramas para visualizar la relación entre variables categóricas y una columna objetivo numérica.  

**Argumentos**:
- `dataframe` (DataFrame): Conjunto de datos de entrada.
- `target_col` (str): Columna objetivo.
- `columns` (list, opcional): Columnas categóricas a analizar.
- `pvalue` (float, opcional): Nivel de significancia estadística.
- `with_individual_plot` (bool, opcional): Si se desea generar un histograma por cada variable categórica.

**Retorna**:
- Lista de columnas categóricas significativas, además de los gráficos generados.

---

## Notas
- Estas funciones son útiles para la preparación de datos y el análisis exploratorio en proyectos de ciencia de datos.
- Requieren bibliotecas como `pandas`, `numpy`, `seaborn`, `matplotlib`, y `scipy`.
