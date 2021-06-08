from vervoeger import Vervoeger

option_dict = {
    "0": "all",
    "1": "Indicativo presente",
    "2": "Indefinido",
    "3": "Imperfecto",
    "4": "Pretérito perfecto compuesto",
    "5": "Pluscuamperfecto",
    "6": "Futuro I",
    "7": "Futuro perfecto"
}


def print_dict(dictionary):
    for key in dictionary:
        print(key, dictionary[key])


if __name__ == '__main__':
    vervoeger = Vervoeger()

    print_dict(option_dict)
    while True:
        werkwoord = input('werkwoord: ')
        optie = input('nummer: ')
        if optie == '0':
            vervoeger.get_conjugations(werkwoord)
        else:
            vervoeger.get_conjugation(werkwoord, option_dict[optie])
