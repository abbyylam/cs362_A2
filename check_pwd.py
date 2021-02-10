def check_pwd(pwd):
    SYMBOLS = "~`!@#$%^&*()_+-="
    for c in pwd:
        if c.islower():
            continue
            return True
        if c.isupper():
            continue
            return True
        if c.isdigit():
            continue
            return True
        if c in SYMBOLS:
            continue
            return True
        if len(pwd) >= 8:
            continue
            return True
        if len(pwd) <=20:
            continue
            return True
    return False