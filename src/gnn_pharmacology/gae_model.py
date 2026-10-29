"""
Modelo Graph Autoencoder (GAE) para Aprendizaje del Espacio Latente
"""
import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleGCN(nn.Module):
    def __init__(self, in_dim=640, hidden_dim=128, latent_dim=64):
        super().__init__()
        self.fc1 = nn.Linear(in_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, latent_dim)
        
    def encode(self, x, edge_index=None, edge_weight=None):
        h = F.relu(self.fc1(x))
        return self.fc2(h)

    def decode(self, z):
        return torch.sigmoid(torch.matmul(z, z.t()))

    def forward(self, x, edge_index=None, edge_weight=None):
        z = self.encode(x, edge_index, edge_weight)
        return z, self.decode(z)
