from src.gnn_pharmacology.synergy_optimizer import evaluate_synergies

def test_evaluate_synergies():
    dict_sim = {"C1": 0.8, "C2": 0.7, "C3": 0.9}
    df = evaluate_synergies(dict_sim, ["C1", "C2", "C3"])
    assert not df.empty
    assert "Formulacion_Trio" in df.columns
