# utils/helpers.py

def format_time(seconds):
    if seconds < 1:
        return "instant"
    elif seconds < 60:
        return f"{int(seconds)} seconds"
    elif seconds < 3600:
        return f"{int(seconds/60)} minutes"
    elif seconds < 86400:
        return f"{int(seconds/3600)} hours"
    elif seconds < 31536000:
        return f"{int(seconds/86400)} days"
    else:
        return f"{int(seconds/31536000)} years"

    
def load_list(filepath):
    try:
        with open(filepath, "r") as f:
            return set(line.strip().lower() for line in f)
    except FileNotFoundError:
        return set()
