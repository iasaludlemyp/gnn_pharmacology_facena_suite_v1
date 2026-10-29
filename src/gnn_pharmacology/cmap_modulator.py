"""
Módulo de Modulación Dinámica del Interactoma por Firmas CMap L1000
"""
import torch

def modulate_adjacency(edge_index, edge_attr, z_scores, alpha=0.3):
    src, tgt = edge_index[0], edge_index[1]
    delta_z = torch.abs(z_scores[src] - z_scores[tgt])
    factor = torch.exp(-alpha * delta_z).unsqueeze(1)
    return edge_attr * factor
