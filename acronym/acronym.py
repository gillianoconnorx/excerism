import re
import string

def abbreviate(plain):
    plain = re.sub('([a-z0-9])([A-Z])', r'\1 \2', plain.replace('-', ' '))
    words = plain.split()
    return ''.join([i[0] for i in words]).upper()