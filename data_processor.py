
import pandas as pd
import json
from pathlib import Path

INPUT_CSV = Path("inputDataSet/testDataSet1.csv")
INPUT_JSON = Path("inputDataSet/testDataSet2.json")
TEMP_PATH = Path("temp/merged_data.csv")
OUTPUT_TEST = Path("outputDataSet/test.csv")
OUTPUT_ODI = Path("outputDataSet/odi.csv")
RESULT_CSV = Path("test_result.csv")

def determine_player_type(runs, wickets):
    if pd.isnull(runs) or pd.isnull(wickets):
        return None
    if runs > 500 and wickets > 50:
        return "All-Rounder"
    elif runs > 500:
        return "Batsman"
    elif runs < 500:
        return "Bowler"
    return None

def process_data():
    df_csv = pd.read_csv(INPUT_CSV)
    with open(INPUT_JSON) as f:
        json_lines = f.readlines()
    df_json = pd.DataFrame([json.loads(line) for line in json_lines])
    
    df = pd.concat([df_csv, df_json], ignore_index=True)
    df.to_csv(TEMP_PATH, index=False)

    df["Player Type"] = df.apply(lambda row: determine_player_type(row["runs"], row["wickets"]), axis=1)
    df = df[(df["age"] <= 50) & (df["age"] >= 15)]
    df.dropna(subset=["runs", "wickets", "Player Type"], inplace=True)

    df_test = df[df["eventType"] == "TEST"]
    df_odi = df[df["eventType"] == "ODI"]

    df_test.to_csv(OUTPUT_TEST, index=False)
    df_odi.to_csv(OUTPUT_ODI, index=False)

    return df

if __name__ == "__main__":
    process_data()
