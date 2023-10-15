import subprocess
import sys
import os
from enum import Enum

class ExitCode(Enum):
    OK = 0
    MANIM_ERROR = 1
    NON_MANIM_ERROR = 2

def execute(file_path) -> str:
    print(os.path.abspath(file_path))
    command = ['manim', file_path]
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        print('Manim Output:')
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print('Manim Error:')
        return (ExitCode.MANIM_ERROR, e.stderr)
    except Exception as e:
        print('Other Exception')
        return (ExitCode.NON_MANIM_ERROR, e.stderr)
    else:
        print('No Errors')
        return (ExitCode.OK, "")

if __name__ == "__main__":
    print("Execute Output:\n", execute(sys.argv[1]))