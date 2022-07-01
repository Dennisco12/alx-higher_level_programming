#!/isr/bin/python3
def islower(c):
    """A function that checks for lowercase letters"""
    if (ord(c) > 96 and ord(c) < 123):
        return True
    else:
        return False
