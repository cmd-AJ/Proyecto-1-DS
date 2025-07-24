import pandas as pd


departments = [
    "ALTA VERAPAZ",
    "BAJA VERAPAZ",
    "CHIMALTENANGO",
    "EL PROGRESO",
    "ESCUINTLA",
    "GUATEMALA",
    "HUEHUETENANGO",
    "IZABAL",
    "JALAPA",
    "JUTIAPA",
    "PETEN",
    "QUETZALTENANGO",
    "QUICHE",
    "RETALHULEU",
    "SACATEPEQUEZ",
    "SAN MARCOS",
    "SANTA ROSA",
    "SOLOLA",
    "TOTONICAPAN",
    "ZACAPA",
    "CIUDAD CAPITAL"
]



dfs = []

for dept in departments: #(Union de todos los colegios de cada departamento que esta clasificado por cada archivo excel)
    filename = f"Proyecto-1-DS/datos/{dept}.xlsx"
    print(f"Reading {filename}")
    
    dftemp = pd.read_excel(filename, skiprows=27)
    
    # Eliminamos una columna donde no tenia datos relevantes ya que todos los valores vistos son NAs
    if "Unnamed: 1" in dftemp.columns:
        dftemp = dftemp.drop(columns=["Unnamed: 1"])
    
    # No se toma en cuenta las filas o columnas en cuales son solo descripciones ya escritas y columnas que tienen valores NA
    dftemp = dftemp.iloc[:-5, :-2]

    dftemp['DEPARTMENT'] = dept
    dfs.append(dftemp)

# Concatenatena los DataFrames
df = pd.concat(dfs, ignore_index=True)

# Exportamos a CSV
df.to_csv("Proyecto-1-DS/datos/establecimiento_all.csv", index=False)



print(df)




