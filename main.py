# main.py
import argparse

from analyzer.scorer import calculate_score
from analyzer.feedback import generate_feedback
from utils.helpers import load_list

def main():
    parser = argparse.ArgumentParser(description="Password Audit Tool")
    parser.add_argument("password", help="Password to evaluate")

    args = parser.parse_args()

    common_passwords = load_list("data/common_passwords.txt")
    common_suffixes = load_list("data/common_suffixes.txt")

    result = calculate_score(args.password, common_passwords, common_suffixes)
    suggestions = generate_feedback(result)

    print("\n=== Password Audit ===")
    print(f"Password: {result['password']}")
    print(f"Score: {result['score']}/10")
    print(f"Entropy: {result['entropy']}")
    print(f"Adjusted Entropy: {result['adjusted_entropy']}")

    if result["issues"]:
        print("\nIssues:")
        for issue in result["issues"]:
            print(f"- {issue}")

    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print(f"- {s}")

    print("\nEstimated Crack Time:")

    for scenario, time in result["crack_times"].items():
        print(f"- {scenario}: {time}")


if __name__ == "__main__":
    main()
