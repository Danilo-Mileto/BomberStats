from typing import Any
from pandas import DataFrame

# Calcola statistiche avanzate per ogni giocatore e restituisce un DataFrame con i risultati.
def genera_statistiche(df: DataFrame) -> DataFrame:
    statistiche: list[dict[str, Any]] = []
    giocatori: list[str] = df["Giocatore"].unique().tolist()

    for giocatore in giocatori:
        dati_giocatore: DataFrame = df[df["Giocatore"] == giocatore]
        media_goal: float = dati_giocatore["Goal"].mean()
        media_assist: float = dati_giocatore["Assist"].mean()
        miglior_anno: int = int(dati_giocatore.loc[dati_giocatore["Goal"].idxmax(), "Anno"])
        miglior_voto: float = dati_giocatore["Media_Voto"].max()

        statistiche.append({
            "Giocatore": giocatore,
            "Media Goal": round(media_goal, 2),
            "Media Assist": round(media_assist, 2),
            "Miglior Anno": miglior_anno,
            "Voto Massimo": miglior_voto
        })

    df_statistiche: DataFrame = DataFrame(statistiche)
    df_statistiche.index = df_statistiche.index + 1  # Fa partire l'indice da 1
    return df_statistiche