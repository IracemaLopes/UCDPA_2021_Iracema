import pandas as pd
def import_dataset(path):
    df = pd.read_csv("city_temperature.csv", low_memory=False, na_values=[-99])
    print("starting dataset")
    print(df)
    return df