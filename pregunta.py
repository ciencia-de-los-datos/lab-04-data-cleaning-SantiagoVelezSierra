"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    #
    # Inserte su código aquí
    #

    df1 = df.copy()

    df1["sexo"] = df1["sexo"].str.lower()

    df1["tipo_de_emprendimiento"] = df1["tipo_de_emprendimiento"].str.lower()

    df1["idea_negocio"] = df1["idea_negocio"].str.lower()
    df1["idea_negocio"] = df1["idea_negocio"].str.replace("_", " ")
    df1["idea_negocio"] = df1["idea_negocio"].str.replace("-", " ")
    df1["idea_negocio"] = df1["idea_negocio"].str.strip()

    df1["barrio"] = df1["barrio"].str.lower()
    df1["barrio"] = df1["barrio"].str.replace("_", " ")
    df1["barrio"] = df1["barrio"].str.replace("-", " ")

    df1["fecha_de_beneficio_1"] = pd.to_datetime(
        df1["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"
    )
    df1["fecha_de_beneficio_2"] = pd.to_datetime(
        df1["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
    )

    df1["fecha_de_beneficio"] = df1.apply(
        lambda x: f"{x['fecha_de_beneficio_1']} {x['fecha_de_beneficio_2']}", axis=1
    )

    df1["fecha_de_beneficio"] = df1["fecha_de_beneficio"].str.replace("NaT ", "")
    df1["fecha_de_beneficio"] = df1["fecha_de_beneficio"].str.replace(" NaT", "")

    df1["comuna_ciudadano"] = df1["comuna_ciudadano"].replace(".", ",")

    df1["monto_del_credito"] = df1["monto_del_credito"].str.replace(".00", "")
    df1["monto_del_credito"] = df1["monto_del_credito"].str.replace(",", "")
    df1["monto_del_credito"] = df1["monto_del_credito"].str.replace("$ ", "")
    df1["monto_del_credito"] = df1["monto_del_credito"].str.replace(".00", "")
    df1["monto_del_credito"] = df1["monto_del_credito"].str.replace(",", "")
    df1["monto_del_credito"] = df1["monto_del_credito"].str.strip()

    df1["línea_credito"] = df1["línea_credito"].str.lower()
    df1["línea_credito"] = df1["línea_credito"].str.replace("_", " ")
    df1["línea_credito"] = df1["línea_credito"].str.replace("-", " ")
    df1["línea_credito"] = df1["línea_credito"].str.strip()

    df2 = df1.drop(["fecha_de_beneficio_1", "fecha_de_beneficio_2"], axis=1)

    df2 = df2.dropna(subset=["tipo_de_emprendimiento", "barrio"], how="any")

    df2 = df2.drop_duplicates()

    df2 = df2.sort_values(
        by=[
            "sexo",
            "tipo_de_emprendimiento",
            "idea_negocio",
            "barrio",
            "estrato",
            "comuna_ciudadano",
            "fecha_de_beneficio",
            "monto_del_credito",
            "línea_credito",
        ],
        ascending=[False, False, False, False, False, False, False, False, False],
    )

    return df2
