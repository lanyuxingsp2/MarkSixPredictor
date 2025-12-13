import pandas as pd

def load_history(path):
    df = pd.read_csv(path, encoding="utf-8")
    cols = ["年份","期号","号1","号2","号3","号4","号5","号6"]
    df = df[cols]
    return df.astype(int)
