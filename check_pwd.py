def check_pwd(pwd):
    for c in pwd:
        if c.islower():
            continue
            return True
        if c.isupper():
            continue
            return True
        if c.isdigit():
            return True
    return False