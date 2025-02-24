from pandas import DataFrame
from dataloader import carica_dati, csv_file
from prevision import grafico_prestazioni_e_previsioni
from statistics import genera_statistiche
from visualization import genera_grafico_giocatore # ✅ Import corretto


def main():
    df: DataFrame = carica_dati(csv_file)
    giocatori: list[str] = df["Giocatore"].unique().tolist()

    for giocatore in giocatori:
        dati_giocatore: DataFrame = df[df["Giocatore"] == giocatore]
        genera_grafico_giocatore(dati_giocatore, giocatore)
        for statistica in ["Goal", "Assist", "Media_Voto"]:
            grafico_prestazioni_e_previsioni(dati_giocatore, giocatore, statistica)

    df_statistiche: DataFrame = genera_statistiche(df)
    print("\n📊 Statistiche Giocatori 📊")
    print(df_statistiche)


if __name__ == "__main__":
    main()