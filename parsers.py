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
    word = word.lower()
    return word


def xml_parser(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    data = []
    for text in root:
        for paragraph in text[1]:
            for sentence in paragraph:
                data += list(filter(None, [symbol_cleaner(word) for word in sentence[0].text.split()]))
    return data
