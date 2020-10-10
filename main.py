from ML_collections.parsers import xml_parser, json_parser, csv_parser
from ML_collections.word_fuctions import most_frequent_rare_unique_words, \
    most_frequent_bigram, longest_word, count_of_words


def first_task():
    text = "1 - OpenCorpora\n2 - Romeo and Juliet\n3 - Avito\ne - exit\n"
    data = None
    while True:
        answer = input(text).strip()
        if answer == "1":
            data = xml_parser("annot.opcorpora.no_ambig.xml")
            break
        elif answer == "2":
            data = json_parser("RomeoAndJuliet.json")
            break
        elif answer == "3":
            data = csv_parser("stage3_test.csv")
            break
        elif answer == "e":
            return
    task_a, task_b, task_e = most_frequent_rare_unique_words(data)
    print(*task_a)
    print(*task_b)
    print(longest_word(data))
    print(*most_frequent_bigram(data), sep=' | ')
    print(task_e)
    print(count_of_words(data))


if __name__ == "__main__":
    first_task()
