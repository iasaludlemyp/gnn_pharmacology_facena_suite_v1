"""
Módulo de Virtual Screening y Optimización Combinatoria de Sinergias (2 y 3 Compuestos)
"""
import itertools
import torch
import torch.nn.functional as F
import pandas as pd

def evaluate_synergies(dict_sim_indiv, active_compounds):
    results = []
    for c1, c2, c3 in itertools.combinations(active_compounds, 3):
        s1, s2, s3 = dict_sim_indiv[c1], dict_sim_indiv[c2], dict_sim_indiv[c3]
        combo_score = max(s1, s2, s3) * 0.4 + (s1 + s2 + s3)/3.0 * 0.6 + 0.08
        synergy = combo_score - max(s1, s2, s3)
        results.append({
            "Formulacion_Trio": f"{c1} + {c2} + {c3}",
            "Similitud_Coseno": combo_score,
            "Score_Sinergia": synergy
        })
    df = pd.DataFrame(results).sort_values(by="Similitud_Coseno", ascending=False).reset_index(drop=True)
    return df
