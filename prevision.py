import os
from typing import Any
import numpy as np
from matplotlib import pyplot as plt
from pandas import DataFrame

# 📂 Cartella per i grafici delle previsioni
grafici_dir: str = "grafici"

# Crea la cartella se non esiste
os.makedirs(grafici_dir, exist_ok=True)

# Previsione delle performance future con regressione lineare
def prevedi_prestazioni(dati_giocatore: DataFrame, statistica: str, anni_futuri: int = 3) -> list[dict[str, Any]]:
    anni: np.ndarray = dati_giocatore["Anno"].values
    valori: np.ndarray = dati_giocatore[statistica].values

    coeff = np.polyfit(anni, valori, 1)  # Calcola i coefficienti della retta
    modello = np.poly1d(coeff)  # Crea la funzione di predizione

    anni_futuri_lista: list[int] = list(range(anni[-1] + 1, anni[-1] + 1 + anni_futuri))
    previsioni = [modello(anno) for anno in anni_futuri_lista]

    return [{"Anno": anno, statistica: round(valore, 2)} for anno, valore in zip(anni_futuri_lista, previsioni)]


# Genera un grafico con le previsioni future
def grafico_prestazioni_e_previsioni(dati_giocatore: DataFrame, giocatore: str, statistica: str) -> None:
    previsioni:  list[dict[str, Any]] = prevedi_prestazioni(dati_giocatore, statistica)

    anni_storici = dati_giocatore["Anno"].values
    valori_storici = dati_giocatore[statistica].values
    anni_futuri = [p["Anno"] for p in previsioni]
    valori_previsti = [p[statistica] for p in previsioni]

    plt.figure(figsize=(10, 5))
    plt.plot(anni_storici, valori_storici, marker="o", linestyle="-", label=f"{statistica} Storici", color="blue")
    plt.plot(anni_futuri, valori_previsti, marker="o", linestyle="dashed", label=f"{statistica} Previsti", color="red")

    plt.title(f"Previsione {statistica} di {giocatore} (fino al {anni_futuri[-1]})")
    plt.xlabel("Anno")
    plt.ylabel(statistica)
    plt.legend()
    plt.grid(True)
    plt.xticks(list(anni_storici) + anni_futuri)
    plt.tight_layout()

    # 📂 Percorso del file PNG
    file_path: str = os.path.join(grafici_dir, f"{giocatore}_{statistica}_previsione.png")

    plt.savefig(file_path)  # Salva il grafico nella cartella
    plt.show()