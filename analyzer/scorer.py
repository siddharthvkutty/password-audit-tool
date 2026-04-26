# analyzer/scorer.py
from analyzer.entropy import calculate_entropy
from analyzer.patterns import (
    check_common_password,
    contains_dictionary_word,
    extract_dictionary_words,
    has_sequence,
    has_repeats,
    has_weak_numeric_pattern,
    has_keyboard_pattern,
    has_common_suffix,
    has_leet_dictionary_match
)

# Defining attack vector time estimates
ATTACK_SCENARIOS = {
    "online_attack": 1e3,
    "basic_cpu": 1e6,
    "gpu_attack": 1e9,
    "advanced_cluster": 1e12
}

def estimate_crack_time(guesses):
    results = {}

    for scenario, rate in ATTACK_SCENARIOS.items():
        seconds = guesses / rate
        results[scenario] = seconds

    return results

def calculate_score(password: str, common_passwords: set, common_suffixes: set):
    base_entropy = calculate_entropy(password)

    penalty = 1.0
    guess_factor = 1.0
    issues = []

    if check_common_password(password, common_passwords):
        penalty *= 0.1
        guess_factor *= 1e-6
        issues.append("Common password")

    # commented to update scorer logic with better dictionary handling
    #if contains_dictionary_word(password, common_passwords):
    #    penalty *= 0.6
    #    issues.append("Contains dictionary word")

    # section for better dictionary handling
    words_found = extract_dictionary_words(password, common_passwords)
    num_words = len(words_found)
    if num_words == 1:
        penalty *= 0.6
        guess_factor *= 1e-3
        issues.append("Contains common word")
    elif num_words >= 3 and "-" in password:
        penalty *= 0.9 # very light penalty
        guess_factor *= 0.5
        issues.append("Passphrase detected")
    elif num_words == 2:
        penalty *= 0.75
        guess_factor *= 1e-2
        issues.append("Multiple common words")

    if any(char.isdigit() for char in password):
        guess_factor *= 1e-1
        issues.append("Contains numeric pattern")

    if has_sequence(password):
        penalty *= 0.6
        guess_factor *= 1e-2
        issues.append("Contains sequence")
    
    if has_common_suffix(password, common_suffixes):
        guess_factor *= 1e-3
        issues.append("Common suffix pattern")

    if has_repeats(password):
        penalty *= 0.7
        issues.append("Too many repeated characters")

    if has_leet_dictionary_match(password, common_passwords):
        guess_factor *= 1e-2
        issues.append("Leet-based dictionary pattern")

    if has_weak_numeric_pattern(password):
        guess_factor *= 1e-2
        issues.append("Weak numeric pattern")

    if has_keyboard_pattern(password):
        penalty *= 0.5
        issues.append("Keyboard pattern detected")

    adjusted_entropy = base_entropy * penalty

    # Converted entropy -> guesses
    base_guesses = 2 ** adjusted_entropy
    guesses = base_guesses * guess_factor

    crack_times = estimate_crack_time(guesses)

    from utils.helpers import format_time

    formatted_times = {
        k: format_time(v) for k, v in crack_times.items()
    }

    # Convert to score
    if adjusted_entropy < 28:
        score = 2
    elif adjusted_entropy < 36:
        score = 4
    elif adjusted_entropy < 60:
        score = 6
    elif adjusted_entropy < 80:
        score = 8
    else:
        score = 10

    return {
        "password": password,
        "entropy": round(base_entropy, 2),
        "adjusted_entropy": round(adjusted_entropy, 2),
        "score": score,
        "issues": issues,
        "crack_times": formatted_times
    }
