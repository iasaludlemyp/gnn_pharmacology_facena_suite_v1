import torch
from src.gnn_pharmacology.gae_model import SimpleGCN

def test_gae_model():
    model = SimpleGCN(in_dim=640, hidden_dim=128, latent_dim=64)
    x = torch.randn(5, 640)
    z, adj_hat = model(x)
    assert z.shape == (5, 64)
    assert adj_hat.shape == (5, 5)
