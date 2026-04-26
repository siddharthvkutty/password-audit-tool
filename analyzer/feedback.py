# analyzer/feedback.py

def generate_feedback(result: dict):
    suggestions = []
    score = result["score"]
    issues = result["issues"]

    if score <= 3:
        suggestions.append("Very weak password — easily guessable")
        suggestions.append("Use at least 12–16 characters")

    elif score <= 6:
        suggestions.append("Password is moderate but could be improved")
        suggestions.append("Increase length and avoid predictable patterns")

    elif score <= 8:
        suggestions.append("Strong password, but minor improvements possible")

    else:
        suggestions.append("Very strong password")

    # Issue-based suggestions
    if "Contains common word" in issues:
        suggestions.append("Avoid using single common words")

    if "Multiple common words" in issues:
        suggestions.append("Combine words less predictably or increase length")

    if "Passphrase detected" in issues and score >= 8:
        suggestions.append("Good use of passphrase — consider adding separators or randomness")

    if "Contains sequence" in issues:
        suggestions.append("Avoid predictable sequences like 1234")

    if "Keyboard pattern detected" in issues:
        suggestions.append("Avoid keyboard patterns like qwerty")

    if "Too many repeated characters" in issues:
        suggestions.append("Reduce repeated characters")

    return suggestions
