import re
import pandas as pd
import os
import sys


def operation(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                print('divide by zero error')
                return None
            return num1 / num2
        case _:
            print('Operator not recognized')
            return None


def checks(num1, num2, operator):
    # split in commas/dots to check if numeric
    num1_parts = re.split(r'[.,]+', num1)
    num2_parts = re.split(r'[.,]+', num2)
    num_parts = num1_parts + num2_parts

    for num_part in num_parts:
        if not num_part.isnumeric():
            print('contains other symbols other than numbers or "." or ","')
            return False

    # check if more than 2 parts
    if len(num1_parts)>2 or len(num2_parts)>2:
        print('too many parts in number (invalid)')
        return False

    if operator not in ['+', '-', '*', '/']:
        print('Operator not recognized')
        return False

    print("VALID")
    return True


def process(num1, num2):
    # remove whitespace
    num1 = num1.replace(' ', '')
    num2 = num2.replace(' ', '')
    num1 = num1.replace(',', '.')
    num2 = num2.replace(',', '.')

    num1 = float(num1)
    num2 = float(num2)

    return num1, num2


def main():
    # input
    num1 = input('Enter first number (float with . or ,): ')
    num2 = input('Enter second number (float with . or ,): ')
    operator = input('Enter operation (+, -, *, /): ')

    if not checks(num1, num2, operator):
        print('Invalid input', file=sys.stderr)
        sys.exit(1)

    num1, num2 = process(num1, num2)

    result = operation(num1, num2, operator)
    print(result)

    default_dir = os.getcwd()
    try:
        if not os.path.exists(f"{default_dir}/calc_logs.csv"):
            df = pd.DataFrame()
        else:
            df = pd.read_csv(f"{default_dir}/calc_logs.csv")
    except Exception as e:
        print(f"something wrong with that file my friend: {e}\nI will nuke it for you with this calc operation!!")
        df = pd.DataFrame()

    df_new = pd.concat([df, pd.DataFrame([{'num1': num1, 'num2': num2, 'operator': operator, 'result': result}])], ignore_index=True)

    df_new.to_csv('calc_logs.csv', index=False)


if __name__ == '__main__':
    main()
