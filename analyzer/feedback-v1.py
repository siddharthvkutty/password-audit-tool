# analyzer/feedback.py

def generate_feedback(result: dict):
    suggestions = []

    if result["score"] <= 4:
        suggestions.append("Increase password length (12+ recommended)")
        suggestions.append("Avoid common words or patterns")

    if "Contains dictionary word" in result["issues"]:
        suggestions.append("Avoid using real words")

    if "Contains sequence" in result["issues"]:
        suggestions.append("Avoid predictable sequences like 1234")

    if "Keyboard pattern detected" in result["issues"]:
        suggestions.append("Avoid keyboard patterns like qwerty")

    if "Too many repeated characters" in result["issues"]:
        suggestions.append("Reduce repeated characters")

    return suggestions
