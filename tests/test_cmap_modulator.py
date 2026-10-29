import torch
from src.gnn_pharmacology.cmap_modulator import modulate_adjacency

def test_modulate_adjacency():
    edge_index = torch.tensor([[0, 1], [1, 0]])
    edge_attr = torch.tensor([[1.0], [1.0]])
    z_scores = torch.tensor([1.0, -2.0])
    mod_attr = modulate_adjacency(edge_index, edge_attr, z_scores)
    assert mod_attr.shape == edge_attr.shape
    assert mod_attr[0].item() < 1.0
