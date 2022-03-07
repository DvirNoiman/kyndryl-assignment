def validate_string(data):
    if data.isalpha() and data.istitle():
        return True
    else:
        return False
