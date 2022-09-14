
def is_pali(x):
        if x < 0:
            return False

        x = str(x)
        if x == x[::-1]:
            return True
        return False


assert is_pali(121) is True
assert is_pali(-121) is False
assert is_pali(10) is False
