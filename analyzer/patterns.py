# analyzer/patterns.py

COMMON_PATTERNS = [
    "123456", "password", "qwerty", "abc123"
]

KEYBOARD_PATTERNS = [
    "qwerty", "asdf", "zxcv"
]

LEET_MAP = {
    "@": "a",
    "0": "o",
    "1": "l",
    "3": "e",
    "4": "a",
    "5": "s",
    "7": "t"
}

def normalize_leet(password: str) -> str:
    password = password.lower()
    return "".join(LEET_MAP.get(c, c) for c in password)

def has_leet_dictionary_match(password: str, word_list: set) -> bool:
    normalized = normalize_leet(password)
    return any(word in normalized for word in word_list if len(word) >= 4)

def check_common_password(password: str, common_list: set) -> bool:
    return password.lower() in common_list


def contains_dictionary_word(password: str, common_list: set) -> bool:
    password = password.lower()
    return any(word in password for word in common_list if len(word) > 3)


def has_sequence(password: str) -> bool:
    sequences = ["0123456789", "abcdefghijklmnopqrstuvwxyz"]
    password = password.lower()

    for seq in sequences:
        for i in range(len(seq) - 2):
            if seq[i:i+3] in password:
                return True
    return False


def has_repeats(password: str) -> bool:
    return any(password.count(c) > len(password) // 2 for c in set(password))


def has_keyboard_pattern(password: str) -> bool:
    password = password.lower()
    return any(p in password for p in KEYBOARD_PATTERNS)

def has_weak_numeric_pattern(password: str) -> bool:
    weak_patterns = ["123", "1234", "111", "000", "2024", "2025"]
    return any(p in password for p in weak_patterns)

def has_common_suffix(password: str, suffixes: set) -> bool:
    password = password.lower()
    return any(password.endswith(suffix) for suffix in suffixes)

def extract_dictionary_words(password: str, word_list: set):
    password = password.lower()
    found_words = []

    for word in word_list:
        if len(word) >= 4 and word in password:
            found_words.append(word)
    return found_words
