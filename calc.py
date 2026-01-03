import re
import pandas as pd
import os
import sys


def split_compute_string(compute_string):
    if len(re.findall(r'[+*/-]', compute_string)) != 1:
        return None, None, None, False
    operator = re.findall(r'[+*/-]', compute_string)[0]
    num1, num2= re.split(r'[+*/-]', compute_string)
    if not num1 or not num2:
        return None, None, None, False
    return num1, num2, operator, True


def operation(num1, num2, operator):
    """
    def for the operation of the calculator
    :param num1:
    :param num2:
    :param operator:
    :return: return num or none if error
    """
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
    """
    check if the input is valid
    :param num1:
    :param num2:
    :param operator:
    :return: bool
    """
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
    """
    float conversion and remove whitespace
    :param num1:
    :param num2:
    :return: num1 and num2 as floats
    """
    # remove whitespace
    num1 = num1.replace(' ', '')
    num2 = num2.replace(' ', '')
    num1 = num1.replace(',', '.')
    num2 = num2.replace(',', '.')

    num1 = float(num1)
    num2 = float(num2)

    return num1, num2


def log_results(num1, num2, operator, result,):
    """
    log the results to a csv file
    :param num1:
    :param num2:
    :param operator:
    :param result:
    :return:
    """
    default_dir = os.getcwd()
    try:
        if not os.path.exists(f"{default_dir}/data/calc_logs.csv"):
            df = pd.DataFrame()
        else:
            df = pd.read_csv(f"{default_dir}/data/calc_logs.csv")
    except Exception as e:
        print(f"something wrong with that file my friend: {e}\nI will nuke it for you with this calc operation!!")
        df = pd.DataFrame()

    df_new = pd.concat([df, pd.DataFrame([{'num1': num1, 'num2': num2, 'operator': operator, 'result': result}])],
                       ignore_index=True)

    df_new.to_csv('data/calc_logs.csv', index=False)


def main():
    '''
    main function of the calculator
    :return:
    '''
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

    log_results(num1, num2, operator, result)

if __name__ == '__main__':
    main()
