
import pandas as pd
from src.data_processor import process_data

def test_player_type_and_output():
    df = process_data()
    assert not df.empty
    assert "Player Type" in df.columns
    assert all(df["Player Type"].notnull())
