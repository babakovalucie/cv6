def analyze_password(password, min_length=8, require_digit=True, require_upper=True,
                     require_symbol=False, banned_words = None):
    passed_rules = 0
    total_rules = 0
    missed_rules = []

    # minimalni delka hesla
    total_rules += 1
    if len(password) >= min_length:
        passed_rules += 1
    else:
        missed_rules.append("minimální délka hesla")

    # pritomost cislice
    if require_digit:
        total_rules += 1
        has_digit = False
        for char in password:
            if char.isdigit():
                has_digit = True
        if has_digit:
            passed_rules += 1
        else:
            missed_rules.append("pritomnost cislice")

    # pritomnost velkeho pismene
    if require_upper:
        total_rules += 1
        has_upper = False
        for char in password:
            if char.isupper():
                has_upper = True
        if has_upper:
            passed_rules += 1
        else:
            missed_rules.append("pritomnost velkeho pismene")

    # pritomnost symbolu
    if require_symbol:
        total_rules += 1
        has_symbol = False
        symbols = "!@#$%^&*()-_=+[]{};:,.?"
        for char in password:
            if char in symbols:
                has_symbol = True
        if has_symbol:
            passed_rules += 1
        else:
            missed_rules.append("pritomnost symbolu")

    # zakazane slovo
    total_rules += 1
    has_banned_word = False
    if banned_words is None:
        banned_words = ['heslo', 'password', '1234']
    for word in banned_words:
        if word in password:
            has_banned_word = True
    if has_banned_word:
        missed_rules.append("zakazane slovo")
    else:
        passed_rules += 1

    is_strong = (passed_rules == total_rules)
    score_percent = (passed_rules/total_rules) * 100

    return is_strong, score_percent, missed_rules

print(analyze_password("bubUb4b*", require_symbol=True))