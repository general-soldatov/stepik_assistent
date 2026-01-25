import re 
import subprocess
from .template import TestOfCode
from app.models.stepik import SourceProgram

class ProgramStep(TestOfCode):
    @staticmethod
    def create_file_to_test(path_template="projects/template_led.c", path_example="projects/test.c", path_test="test.c"):
        with open(path_template, 'r', encoding='utf-8') as file:
            with open(path_example, "r", encoding="utf-8") as test:
                text = re.sub(r'::code[^::]*::footer', test.read(), file.read())    
            text = re.sub(r"::", '//', text)
            with open(path_test, 'w', encoding='utf-8') as test:
                test.write(text)

    

# result = subprocess.run(["gcc", "test.c"])
# result = subprocess.run(['./a.out'],
#         capture_output=True,
#         text=True
#         )
result = subprocess.run(['python3', 'test.c'], capture_output=True, input='Data'.encode())
print(f"Command finished with return code: \n{result.stdout.decode()}")

# process = subprocess.Popen(
#     ['python3', '-c', 'print("console: ", input())'], # Replace with your command
#     stdin=subprocess.PIPE,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE
# )

# stdout, stderr = process.communicate(input="data to send to stdin".encode())

# print(f"Stdout: {stdout.decode()}")
# print(f"Stderr: {stderr.decode()}")