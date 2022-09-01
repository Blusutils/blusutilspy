"""Module with text utilities
"""
def int_to_roman(n: int) -> str:
    """Converts an integer to Roman form

    Args:
        n (int): Integer to convert

    Returns:
        str: Integer in Roman form
    """
    return 'M' + int_to_roman(n - 1000) if n >= 1000 \
        else ('CM' + int_to_roman(n - 900) if n >= 900 \
            else 'D' + int_to_roman(n - 500)) if n >= 500  \
                else ('CD' + int_to_roman(n - 400) if n >= 400  \
                    else 'C' + int_to_roman(n - 100)) if n >= 100  \
                        else ('XC' + intToRoman(n - 90) if n >= 90  \
                            else 'L' + int_to_roman(n - 50)) if n >= 50  \
                                else ('XL' + int_to_roman(n - 40) if n >= 40  \
                                    else 'X' + int_to_roman(n - 10)) if n >= 10  \
                                        else ('IX' if n == 9  \
                                            else 'V' + int_to_roman(n - 5)) if n >= 5  \
                                                else ('IV' if n == 4  \
                                                    else 'I' + int_to_roman(n - 1)) if n > 0  \
                                                        else ''
                                                        # опять лесенка из тернарок, юххуу
                                                        # кста, свич из либы нафиг :D

def caps_percent(txt: str) -> float:
    """Calculates the percentage of letters written with CapsLock (in uppercase)

    Args:
        txt (str): Inputted text to calculate

    Returns:
        float: Percent of uppercase letters
    """
    return 100/len(txt)*sum([1 for i in txt if i.isupper()])

def ru_en_transliterate(inp: str) -> str:
    """Transliterate a string from Russian to English.

    Args:
        inp (str): String to transliterate on Russian

    Returns:
        str: Transliterated string
    """
    return inp.replace('а', 'a')\
                        .replace('б', 'b')\
                        .replace('в', 'v')\
                        .replace('г', 'g')\
                        .replace('д', 'd')\
                        .replace('е', 'e')\
                        .replace('ё', 'e')\
                        .replace('ж', 'zh')\
                        .replace('з', 'z')\
                        .replace('и', 'i')\
                        .replace('й', 'j')\
                        .replace('к', 'k')\
                        .replace('л', 'l')\
                        .replace('м', 'm')\
                        .replace('н', 'n')\
                        .replace('о', 'o')\
                        .replace('п', 'p')\
                        .replace('р', 'r')\
                        .replace('с', 's')\
                        .replace('т', 't')\
                        .replace('у', 'u')\
                        .replace('ф', 'f')\
                        .replace('х', 'h')\
                        .replace('ц', 'ts')\
                        .replace('ч', 'ch')\
                        .replace('ш', 'sh')\
                        .replace('щ', 'sh\'')\
                        .replace('ъ', '^')\
                        .replace('ы', 'i')\
                        .replace('ь', '\'')\
                        .replace('э', 'e')\
                        .replace('ю', 'yu')\
                        .replace('я', 'ya')\
                        .replace('А', 'A')\
                        .replace('Б', 'B')\
                        .replace('В', 'V')\
                        .replace('Г', 'G')\
                        .replace('Д', 'D')\
                        .replace('Е', 'E')\
                        .replace('Ё', 'E')\
                        .replace('Ж', 'Zh')\
                        .replace('З', 'Z')\
                        .replace('И', 'I')\
                        .replace('Й', 'J')\
                        .replace('К', 'K')\
                        .replace('Л', 'L')\
                        .replace('М', 'M')\
                        .replace('Н', 'N')\
                        .replace('О', 'O')\
                        .replace('П', 'P')\
                        .replace('Р', 'R')\
                        .replace('С', 'S')\
                        .replace('Т', 'T')\
                        .replace('У', 'U')\
                        .replace('Ф', 'F')\
                        .replace('Х', 'H')\
                        .replace('Ц', 'Ts')\
                        .replace('Ч', 'Ch')\
                        .replace('Ш', 'Sh')\
                        .replace('Щ', 'Sh\'')\
                        .replace('Ъ', '^')\
                        .replace('Ы', 'I')\
                        .replace('Ь', '\'')\
                        .replace('Э', 'E')\
                        .replace('Ю', 'Yu')\
                        .replace('Я', 'Ya')

# def galaxyCrypt(inp: str):
#     """международный галактический алфавит, ака стол зачарования из майнкрафта"""