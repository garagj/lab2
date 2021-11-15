# python validator.py input.txt output.txt

import json
import re
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('input', help='Get path file input')
parser.add_argument('output', help='Get path file output')
args = parser.parse_args()


class validator:
    def __init__(self):
        pass

    def check_email(self: str) -> bool:
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, self):
            return True
        return False

    def check_weight(self: int) -> bool:
        if type(self) != int:
            return False
        if self < 30 or self > 150:
            return False
        return True

    def check_inn(self: str) -> bool:
        if type(self) != str:
            return False
        if len(self) == 12:
            return True
        return False

    def check_passport(self: str) -> bool:
        pattern = "\d\d\s\d\d"
        if re.match(pattern, self):
            return True
        return False

    def check_university(self: str) -> bool:
        if type(self) != str:
            return False
        return True

    def check_experience(self: int) -> bool:
        if type(self) != int:
            return False
        if 3 <= self <= 30:
            return True
        return False

    def check_views(self: str) -> bool:
        if type(self) != str:
            return False
        return True

    def check_worldview(self: str) -> bool:
        if type(self) != str:
            return False
        return True

    def check_address(self: str) -> bool:
        if type(self) == str:
            pattern = '[а-яА-Я.\s\d-]+\s+[0-9]+$'
            if re.match(pattern, self):
                return True
        return False


data = json.load(open(args.input, encoding='windows-1251'))

valid_data = list()
email = 0
weight = 0
inn = 0
passport_series = 0
university = 0
work_experience = 0
political_views = 0
worldview = 0
address = 0

with tqdm(total=len(data)) as progressbar:
    for person in data:
        temp = True
        if not validator.check_email(person["email"]):
            email += 1
            temp = False
        if not validator.check_weight(person["weight"]):
            weight += 1
            temp = False
        if not validator.check_inn(person["inn"]):
            inn += 1
            temp = False
        if not validator.check_passport(person["passport_series"]):
            passport_series += 1
            temp = False
        if not validator.check_university(person["university"]):
            university += 1
            temp = False
        if not validator.check_experience(person["work_experience"]):
            work_experience += 1
            temp = False
        if not validator.check_views(person["political_views"]):
            political_views += 1
            temp = False
        if not validator.check_worldview(person["worldview"]):
            worldview += 1
            temp = False
        if not validator.check_address(person["address"]):
            address += 1
            temp = False
        if temp:
            valid_data.append(person)
        progressbar.update(1)

out_put = open(args.output, 'w', encoding='utf-8')
data_for_output = json.dumps(valid_data, ensure_ascii=False, indent=4)
out_put.write(data_for_output)
out_put.close()

print(f'{len(valid_data)} валидных записей')
print(f'{len(data) - len(valid_data)} невалидных записей')
print(f'{email} невалидных записей электронной почты')
print(f'{weight}  невалидных вес')
print(f'{inn} невалидных ИНН')
print(f'{passport_series} невалидных серий паспорта')
print(f'{university} невалидных университетов ')
print(f'{work_experience} невалидных записей об опыте работы')
print(f'{political_views} невалидных политических взглядов')
print(f'{worldview} невалидных мировоззрений')
print(f'{address} невалидных адресов')
