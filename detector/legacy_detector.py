def detect_legacy_patterns(code):
    issues = []

    if "print " in code:
        issues.append("Old Python 2 print statement detected")

    if "except:" in code:
        issues.append("Bare except detected (bad practice)")

    if len(code.splitlines()) > 400:
        issues.append("Very large file – needs refactoring")

    if "global " in code:
        issues.append("Global variables used")

    return issues
