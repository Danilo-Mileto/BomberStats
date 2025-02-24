import os
from pandas import DataFrame, read_csv

csv_file: str = "../../OneDrive/Desktop/statistiche_giocatori.csv"


# Carica i dati dal file CSV e verifica la sua esistenza
def carica_dati(file: str) -> DataFrame:
    if not os.path.exists(file):
        raise FileNotFoundError(f"Errore: Il file '{file}' non è stato trovato.")
    return read_csv(file)