def convert_analysis_to_text(analysis_result, file_path):
    text = f"Analysis of file {file_path}:\n"

    text += f"- Number of classes: {analysis_result['classes']}\n"
    text += f"- Number of functions: {analysis_result['functions']}\n"

    if analysis_result["syntax_error"]:
        text += f"- Syntax Error: {analysis_result['syntax_error']}\n"
    else:
        text += "- No syntax errors found.\n"

    return text
