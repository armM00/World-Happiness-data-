import pandas as pd

df = pd.read_csv('happy.csv')


def columns():
    with open('happy.csv') as file:
        content = file.readline()

    my_list = content.split(',')
    my_list[-1] = my_list[-1].replace('\n', '')
    return my_list


def compare(name):
    my_list = columns()
    new_name = name.lower().replace(" ", "_")
    if new_name == my_list[-1]:
        my_name = (new_name + '\n')
    else:
        my_name = new_name

    my_list = []
    for index, row in df.iterrows():
        my_list.append(row[my_name])
    return my_list
