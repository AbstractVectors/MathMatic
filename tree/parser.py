import re
import sys

def extract_numbered_points(input_string, n = None) -> list[str]:
    pattern = r'\d+[.)]\s+(.*?)\n'
    matches = re.findall(pattern, input_string, re.MULTILINE)
    if matches is None:
        return input_string
    if n is None or n > len(matches):
        return matches
    else:
        return matches[:n]
    
def extract_python_source_code(input_string) -> list[str]:
    pattern = re.compile(r"```(?:python)?(.*?)```", re.DOTALL)

    match = pattern.search(input_string)

    return match.group(1).strip() if match else input_string

if __name__ == "__main__":
    content = ""
    with open(sys.argv[1], "r") as file:
        content = file.read()
    print(extract_python_source_code(content))