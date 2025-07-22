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

for dept in departments:
    filename = f"Proyecto-1-DS/datos/{dept}.xlsx"
    print(f"Reading {filename}")
    
    dftemp = pd.read_excel(filename, skiprows=27)
    
    # Drop the column if it exists
    if "Unnamed: 1" in dftemp.columns:
        dftemp = dftemp.drop(columns=["Unnamed: 1"])
    
    # Drop last 5 rows and last 2 columns (if needed)
    dftemp = dftemp.iloc[:-5, :-2]

    dftemp['DEPARTMENT'] = dept
    dfs.append(dftemp)

# Concatenate all DataFrames
df = pd.concat(dfs, ignore_index=True)

# Export to CSV
df.to_csv("Proyecto-1-DS/datos/establecimiento_all.csv", index=False)



print(df)




