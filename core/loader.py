import pandas as pd

def load_history(path):
    df = pd.read_csv(path, encoding="utf-8")
    required_cols = ["年份", "期号", "号1", "号2", "号3", "号4", "号5", "号6"]

    for col in required_cols:
        if col not in df.columns:
            raise Exception(f"缺少字段：{col}")

    return df
# loader.py 读取 CSV
