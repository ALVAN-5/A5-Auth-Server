def validateSessionKey(session_key: str):
    if len(session_key) != 64 or not session_key.isalnum():
        return False

    return True
