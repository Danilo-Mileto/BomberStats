import os
from matplotlib import pyplot as plt
from pandas import DataFrame

# 📂 Cartella dove salvare i grafici
grafici_dir: str = "grafici"

# Crea la cartella se non esiste
os.makedirs(grafici_dir, exist_ok=True)

def genera_grafico_giocatore(dati_giocatore: DataFrame, giocatore: str) -> None:
    plt.figure(figsize=(10, 6))

    # Plot dei Goal
    plt.plot(dati_giocatore["Anno"], dati_giocatore["Goal"], marker='o', label='Goal')

    # Plot degli Assist
    plt.plot(dati_giocatore["Anno"], dati_giocatore["Assist"], marker='o', label='Assist')

    # Plot della Media Voto
    plt.plot(dati_giocatore["Anno"], dati_giocatore["Media_Voto"], marker='o', label='Media Voto')

    plt.title(f'Statistiche di {giocatore} (2021-2025)')
    plt.xlabel("Anno")
    plt.ylabel("Statistiche")
    plt.legend()
    plt.grid(True)
    plt.xticks(dati_giocatore["Anno"])  # Mostra tutti gli anni sull'asse x
    plt.tight_layout()

    # 📂 Percorso del file PNG
    file_path: str = os.path.join(grafici_dir, f"{giocatore}_statistiche.png")

    plt.savefig(file_path) # Salva il grafico nella cartella
    plt.show() # mostra grafico