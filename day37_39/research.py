import os
import csv
import collections
from typing import List

Record = collections.namedtuple(
    'Record', 'country,beer_servings,spirit_servings,wine_servings,total_litres_of_pure_alcohol'
)

data = []


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'drinks.csv')

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        data.clear()
        for row in reader:
            row = parse_row(row)
            data.append(row)


def parse_row(row):
    row['beer_servings'] = int(row['beer_servings'])
    row['spirit_servings'] = int(row['spirit_servings'])
    row['wine_servings'] = int(row['wine_servings'])
    row['total_litres_of_pure_alcohol'] = float(row['total_litres_of_pure_alcohol'])

    record = Record(**row)

    return record


def drink_most() -> List[Record]:
    return sorted(data, key=lambda r: r.total_litres_of_pure_alcohol, reverse=True)


def drink_least() -> List[Record]:
    return sorted(data, key=lambda r: r.total_litres_of_pure_alcohol)


def drink_nonzero_least() -> List[Record]:
    new_data = [dat for dat in data if dat.total_litres_of_pure_alcohol > 0]
    return sorted(new_data, key=lambda r: r.total_litres_of_pure_alcohol)


def most_spirits() -> List[Record]:
    return sorted(data, key=lambda r: r.spirit_servings, reverse=True)


def least_spirits() -> List[Record]:
    return sorted(data, key=lambda r: r.spirit_servings)


def least_nonzero_spirits() -> List[Record]:
    new_data = [dat for dat in data if dat.spirit_servings > 0]
    return sorted(new_data, key=lambda r: r.spirit_servings)