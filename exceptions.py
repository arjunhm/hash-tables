class KeyError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Key not found"
