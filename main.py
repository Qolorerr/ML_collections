from parsers import xml_parser


def main():
    text = "1 - OpenCorpora\n2 - Romeo and Juliet\n3 - Avito\ne - exit\n"
    data = None
    while True:
        answer = input(text).strip()
        if answer == "1":
            data = xml_parser("annot.opcorpora.no_ambig.xml")
            break
        elif answer == "2":
            # Parse RJ
            break
        elif answer == "3":
            # Parse Av
            break
        elif answer == "e":
            return


if __name__ == "__main__":
    main()
