
import pandas as pd

def test_output_schema():
    df = pd.read_csv("outputDataSet/odi.csv")
    expected_columns = ["eventType", "playerName", "age", "runs", "wickets", "Player Type"]
    for col in expected_columns:
        assert col in df.columns
