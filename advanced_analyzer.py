import math
import re
COMMON_PASSWORDS = ["123456", "password", "admin", "12345678"]
def entropy(password):
    charset = 0
if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^A-Za-z0-9]", password):
        charset += 32
 if charset == 0:
        return 0
 return len(password) * math.log2(charset)

def crack_time(entropy_score):
    guesses_per_second = 1e10
    seconds = (2 ** entropy_score) / guesses_per_second

    return seconds
def check_password(password):
    if password in COMMON_PASSWORDS:
        return "Very Weak (Common Password)"

    e = entropy(password)
    time = crack_time(e)
 return {
        "entropy": round(e, 2),
        "crack_time_seconds": time}
