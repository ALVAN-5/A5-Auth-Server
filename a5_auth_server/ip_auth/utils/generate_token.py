import random
import string
from ..validators.validate_token import validateToken


def generateToken():
    token_length = random.randint(24, 32)
    while not validateToken(new_token := ''.join(chooseChar() for _ in range(token_length))):
        continue
    return new_token


def chooseChar():
    SPECIAL_CHARS = "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    return random.choice(string.ascii_letters*3 + string.digits*2 + SPECIAL_CHARS)
