import pandas as pd
from calc import checks, process, operation

if __name__ == '__main__':
    with open("test_calc_dataset.csv", "r") as f:
        df = pd.read_csv(f)
        print(df.head())

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

    df.to_csv("test_calc_dataset_results.csv", index=False)