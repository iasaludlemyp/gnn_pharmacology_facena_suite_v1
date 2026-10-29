from src.gnn_pharmacology.protein_embedder import generate_protein_embeddings

def test_generate_protein_embeddings():
    embs = generate_protein_embeddings(["BRAF", "TP53"])
    assert "BRAF" in embs
    assert embs["BRAF"].shape[0] == 640
