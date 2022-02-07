import string
import random
import hashlib
from itertools import cycle


def get_random_string(length):
    letters = string.ascii_lowercase + string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def mix_str(id, key):
    code = ""
    for i, char in enumerate(id):
        code += char + key[i]
    return code


def get_key(id, activity_key):
    str2hash = mix_str(id, activity_key)
    result = hashlib.md5(str2hash.encode())
    return result.hexdigest()


def check_key(RUT, key, key_comp):
    key_check = hashlib.md5(mix_str(RUT, key).encode()).hexdigest()
    return key_comp == key_check


def valida_rut(rut):
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
