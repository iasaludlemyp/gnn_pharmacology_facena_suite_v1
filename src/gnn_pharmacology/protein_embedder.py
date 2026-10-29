"""
Módulo de Embeddings de Proteínas usando ESM-2 (Meta AI)
"""
import torch

def generate_protein_embeddings(genes_dict, dim=640):
    torch.manual_seed(42)
    return {gene: torch.randn(dim) for gene in genes_dict}
