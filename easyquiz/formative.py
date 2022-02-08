import string
import random
import hashlib
from itertools import cycle


def get_random_string(length):
    """ Generates a random string with lower and upper case letters.

    Args:
        length (int): String length.

    Returns:
        str: Random string.
    """

    letters = string.ascii_lowercase + string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def mix_str(id, key):
    """ Concatenates tow strings letter by letter.

    Args:
        id (str): First string. Sets the length of the resulting string.
        key (str): Second string.

    Returns:
        str: Concetenated strings.
    """

    code = ""
    for i, char in enumerate(id):
        code += char + key[i]
    return code


def get_key(id, quiz):
    """ Returns activity key based on the student ID and a easyQuiz instance.

    Args:
        id (str): Student ID.
        quiz (easyquiz.Quiz): easyQuiz instance.

    Returns:
        str: Activity ID.
    """

    str2hash = mix_str(id, quiz.quiz_key)
    result = hashlib.md5(str2hash.encode())
    return result.hexdigest()


def check_key(id, quiz, key_comp):
    """ Checks if the provided key matches the true activity ID.

    Args:
        id (str): Student ID.
        key (str): Quiz key.
        key_comp (str): Key to check.

    Returns:
        bool: Returns True is keys match.
    """

    key_check = hashlib.md5(mix_str(id, quiz.quiz_key).encode()).hexdigest()
    return key_comp == key_check


def valida_rut(rut):
    """ Checks is the provided string is a valid Chilean RUT based on
        verification digit.

    Args:
        rut (str): Chilean RUT candidate.

    Returns:
        (bool, str): True if the string is a valid Chilean RUT.
                     Chilean RUT without verification digit.
    """

    rut = str(rut)
    rut = "".join(u for u in rut if u not in ('-', '.'))
    rut = rut.upper()

    rut_d = rut[:-1]
    verificador = rut[-1:]

    reverso = map(int, rut_d[::-1])
    factores = cycle(range(2, 8))

    suma = sum(digito * factor for digito, factor in zip(reverso, factores))
    resto = suma % 11
    verificador_correcto = 11 - resto

    if verificador_correcto == 10:
        verificador_correcto = 'K'
    else:
        verificador_correcto = str(verificador_correcto)

    return verificador == verificador_correcto, rut_d


def format_msg(base_msg, correct):
    """ Adds color to a string to be displayed in console.

    Args:
        base_msg (str): Text.
        correct (bool): True -> Message in green.
                        False -> Message in red.

    Returns:
        str: Formated string.
    """

    bcolors = {'start': '\033[95m',
               'green': '\033[32m',
               'red': '\033[31m',
               'magenta': '\033[35m',
               'end': '\033[0m'}

    msg = bcolors['start']

    if correct:
        msg += '{}{}'.format(bcolors['green'], base_msg)
    else:
        msg += '{}{}'.format(bcolors['red'], base_msg)

    msg += bcolors['end']

    return msg
