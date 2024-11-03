import pandas as pd 
import numpy as np 
import yaml
import os

params=yaml.safe_load(open("params.yaml"))['preprocess']

def preprocess(input_path, output_path):
    data=pd.read_csv(input_path)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_csv(output_path, index=False)
    print(f"Preprocess data saved to {output_path}")


if __name__=="__main__":
    preprocess(params["input"], params['output'])
