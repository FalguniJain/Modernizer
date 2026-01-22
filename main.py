from analyzer.code_analyzer import analyze_code
from detector.legacy_detector import detect_legacy_patterns
from converter.llm_converter import convert_code

file_path = "sample_inputs/sales_invoice.py"

with open(file_path, "r") as f:
    code = f.read()

analysis_result = analyze_code(file_path)
legacy_issues = detect_legacy_patterns(code)
converted_code = convert_code(code)

print("\nANALYSIS RESULT:")
print(analysis_result)

print("\nLEGACY ISSUES FOUND:")
for issue in legacy_issues:
    print("-", issue)

with open("sample_outputs/sales_invoice_modern.py", "w") as f:
    f.write(converted_code)

print("\nModernized code saved in sample_outputs/")
