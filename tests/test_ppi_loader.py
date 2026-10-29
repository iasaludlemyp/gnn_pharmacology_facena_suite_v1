from src.gnn_pharmacology.ppi_loader import fetch_string_ppi

def test_fetch_string_ppi():
    df = fetch_string_ppi(["BRAF", "MAP2K1"])
    assert not df.empty
    assert "preferredName_A" in df.columns
