# analyzer/entropy.py
import math

def calculate_charset(password: str) -> int:
    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(not c.isalnum() for c in password):
        charset += 32  # rough symbol estimate

    return charset


def calculate_entropy(password: str) -> float:
    length = len(password)
    charset = calculate_charset(password)

    if charset == 0:
        return 0

    return length * math.log2(charset)
