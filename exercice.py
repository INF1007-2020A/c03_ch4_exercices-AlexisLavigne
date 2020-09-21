#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    #return len(string) % 2 == 0 (plus clair)
    return not bool(len(string) % 2)


def remove_third_char(string: str) -> str:
    return string[:2] + string[3:]


def replace_char(string: str, old_char: str, new_char: str) -> str:
    old_char_index = string.find(old_char)
    return string[:old_char_index] + new_char + string[old_char_index + 1:]
    # return string[:string.find(old_char) + new_char + string[string.find(old_char)+1:] (moins bonne, car il y a find deux fois)
    # return string.replace(old_char, new_char) (si on a le droit de replace)


def get_nb_char(string: str, char: str) -> int:
    #return string.count(char)
    if char not in string:
        return 0
    else:
        counter = 0
        for c in string:
            if c == char:
                counter += 1
    return counter


def get_nb_words(sentence: str) -> int:
    return len(sentence.split())



def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
