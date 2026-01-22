import ast

def analyze_code(file_path):
    result = {
        "syntax_error": None,
        "functions": 0,
        "classes": 0
    }

    with open(file_path, "r") as f:
        code = f.read()

    try:
        tree = ast.parse(code)

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                result["functions"] += 1
            elif isinstance(node, ast.ClassDef):
                result["classes"] += 1

    except SyntaxError as e:
        result["syntax_error"] = str(e)

    return result
