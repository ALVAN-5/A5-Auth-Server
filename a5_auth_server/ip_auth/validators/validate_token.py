def validateToken(token: str):
    SPECIAL_CHARS = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    stripped_token = token
    _ = [(stripped_token := stripped_token.replace(c, '')) for c in SPECIAL_CHARS]
    if len(token) < 6 or len(token) > 32 or len(stripped_token) < 0 or len(token) == len(stripped_token):
        return False
    if not stripped_token.isalnum():
        return False

    return True
