"""Module for encryptions"""

# def caesar_crypt(inp: str, pos: int) -> str:
#     pass

def multi_coding_cryptor(mode:int, data:str, crypt_sequence:str) -> typing.Tuple[str, typing.Union[str, None]]:
    """Crypts data
    Args:
        mode (int): Mode: 0 is "decrypt", 1 is "encrypt"
        data (str): Data to be crypted
        crypt_sequence (str): Crypt sequence to be used
    Raises:
        ValueError: if mode is not 0 or 1
    Returns:
        typing.Tuple[str, typing.Union[str, None]]: A tuple with encrypted/decrypted data and newly generated crypt sequence (only when decrypting).
    """
    codings = {
        "u": 'utf-8',
        #"c": 'cp1251',
        "a": "1256"
    }
    en_to_ru = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                            'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'),
                            "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                            'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))
    ru_to_en = dict(zip(map(ord, "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                            'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'),
                            "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                            'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'))
    data = data.translate(en_to_ru) if mode == 0 else data
    data:typing.Union[str, bytes] = data
    if mode == 0:
        crypt_sequence = 'u'+crypt_sequence if not crypt_sequence.startswith('u') else crypt_sequence
    elif mode == 1:
        crypt_sequence = crypt_sequence[::-1]+'u' if not crypt_sequence.endswith('u') else crypt_sequence
    else: raise ValueError("Mode is not equal to 0 (decrypt) or 1 (encrypt)")
    for coding in crypt_sequence:
        data = data.encode(codings[coding]) if isinstance(data, str) else data.decode(codings[coding])
    data = data.translate(ru_to_en) if mode == 1 else data
    return data, "".join([random.choice(list(codings.keys())) for _ in range(len(crypt_sequence))]) if mode == 1 else None