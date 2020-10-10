import csv
import json
import xml.etree.ElementTree as ET


def symbol_cleaner(word: str):
    word = word.replace('!', '')
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace(':', '')
    word = word.replace(';', '')
    word = word.replace('"', '')
    word = word.replace("'", '')
    word = word.replace('?', '')
    word = word.replace('(', '')
    word = word.replace(')', '')
    word = word.replace('-', '')
    word = word.replace('—', '')
    word = word.replace('<', '')
    word = word.replace('>', '')
    word = word.replace('…', '')
    word = word.replace('–', '')
    word = word.replace('•', '')
    word = word.replace('*', '')
    word = word.replace('{', '')
    word = word.replace('}', '')
    for i in range(10):
        if str(i) in word:
            word = ''
            break
    if '/' in word or "\\" in word or '|' in word:
        word = ''
    word = word.lower()
    return word


def str_to_list(sentence):
    return [list(filter(None, [symbol_cleaner(word) for word in sentence.split()]))]


def xml_parser(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    data = []
    for text in root:
        for paragraph in text[1]:
            for sentence in paragraph:
                new_data = str_to_list(sentence[0].text)
                if new_data != [[]]:
                    data += new_data
    return data


def json_parser(file_name):
    data = []
    with open(file_name, "r") as read_json:
        file = json.load(read_json)
        for act in file['acts']:
            for scene in act['scenes']:
                for action in scene['action']:
                    for sentence in action['says']:
                        new_data = str_to_list(sentence)
                        if new_data != [[]]:
                            data += new_data
    return data


def csv_parser(file_name):
    data = []
    with open(file_name, "r", encoding="utf-8") as read_csv:
        file = csv.reader(read_csv, dialect='unix')
        for row in file:
            new_data = str_to_list(row[2])
            if new_data != [[]]:
                data += new_data
    return data
