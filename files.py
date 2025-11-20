import pandas as pd
from calc import checks, process, operation
import os


def log_results(df, filepath):
    for i, row in df.iterrows():
        print(row, i)
        num1, num2, operator = str(row.iloc[0]), str(row.iloc[1]), str(row.iloc[2])

        if not checks(num1, num2, operator):
            print("Invalid input")
            df.loc[i, "result"] = "NaN"
            continue

        num1, num2 = process(num1, num2)
        result = operation(num1, num2, operator)
        print(result)
        df.loc[i, "result"] = result

    df.to_csv(f"{filepath}", index=False)


def main():
    dir_path = os.getcwd() + "/data"
    with open(f"{dir_path}/test_calc_dataset.csv", "r") as f:
        df = pd.read_csv(f)
        print(df.head())

    log_results(df, dir_path + "/test_calc_dataset_results.csv")

    print(f"printed logs to {dir_path}!!!")

if __name__ == '__main__':
    main()