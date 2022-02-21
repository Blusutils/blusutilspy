"""Module with text utilities
"""
def intToRoman(n: int) -> str:
    """Converts an integer to Roman form

    Args:
        n (int): Integer to convert

    Returns:
        str: Integer in Roman form
    """
    return 'M' + intToRoman(n - 1000) if n >= 1000 \
        else ('CM' + intToRoman(n - 900) if n >= 900 \
            else 'D' + intToRoman(n - 500)) if n >= 500  \
                else ('CD' + intToRoman(n - 400) if n >= 400  \
                    else 'C' + intToRoman(n - 100)) if n >= 100  \
                        else ('XC' + intToRoman(n - 90) if n >= 90  \
                            else 'L' + intToRoman(n - 50)) if n >= 50  \
                                else ('XL' + intToRoman(n - 40) if n >= 40  \
                                    else 'X' + intToRoman(n - 10)) if n >= 10  \
                                        else ('IX' if n == 9  \
                                            else 'V' + intToRoman(n - 5)) if n >= 5  \
                                                else ('IV' if n == 4  \
                                                    else 'I' + intToRoman(n - 1)) if n > 0  \
                                                        else ''
                                                        # опять лесенка, юххуу
                                                        # кста, свич из либы нафиг :D
def int_to_roman(n: int) -> str:
    """An alias to intToRoman

    Args:
        n (int): Integer to convert

    Returns:
        str: Integer in Roman form
    """
    return intToRoman(n)

def capsPercent(txt: str) -> float:
    """Calculates the percentage of letters written with CapsLock (in uppercase)

    Args:
        txt (str): Inputted text to calculate

    Returns:
        float: Percent of uppercase letters
    """
    return 100/len(txt)*sum([1 for i in txt if i.isupper()])


def caps_percent(txt: str) -> float:
    """An alias for capsPercent

    Args:
        txt (str): Inputted text to calculate

    Returns:
        float: Percent of uppercase letters
    """
    return capsPercent(txt)