def check_pwd(pwd):
    for c in pwd:
        if c.islower():
            continue
            return True
    return False