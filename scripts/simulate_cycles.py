import pandas as pd

def load_debt_data(path):
    df = pd.read_csv(path)
    return df

def simulate_interest(df):
    df['interest'] = df['amount_due'] * df['interest_rate']
    df['total_due'] = df['amount_due'] + df['interest']
    return df

if __name__ == "__main__":
    data = load_debt_data("data/sample_debt_cycles.csv")
    result = simulate_interest(data)
    print(result)
  Add simulate_cycles.py script
