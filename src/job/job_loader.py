import pandas as pd

def load_jobs(file):
    df = pd.read_csv(file)
    jobs = df.to_dict("records")

    return jobs

