def validateHomeGroup(home_group: str):
    if len(home_group) < 6 or len(home_group) > 32:
        return False
    return True
