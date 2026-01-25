import re 
import subprocess
from .template import TestOfCode
from app.models.stepik import SourceProgram, OptionsProgram

class ProgramStep(TestOfCode):
    @staticmethod
    def open_code(path):
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
        
    @staticmethod
    def create_file_to_test(path_template="projects/template_led.c", path_example="projects/test.c", path_test="test.c"):
        with open(path_template, 'r', encoding='utf-8') as file:
            with open(path_example, "r", encoding="utf-8") as test:
                text = re.sub(r'::code[^::]*::footer', test.read(), file.read())    
            text = re.sub(r"::", '//', text)
            with open(path_test, 'w', encoding='utf-8') as test:
                test.write(text)

    def _set_source(self):
        tests = self.build_prog_test()
        self.block.source = SourceProgram(
            code=self.open_code(self.project.answer.code_path.code_run),
            samples_count=self.project.answer.sample_size,
            templates_data=self.open_code(self.project.answer.code_path.templates_data),
            test_cases=tests,
            feedback_correct=self.project.answer.feedback.correct,
            feedback_wrong=self.project.answer.feedback.wrong
        )
        self.block.options = OptionsProgram(
            limits={self.language: {"time": 5, "memory": 256}},
            code_templates={self.language: self.open_code(self.project.answer.code_path.code_template)},
            code_templates_header_lines_count={self.language: 11},
            code_templates_footer_lines_count={self.language: 5},
            samples=tests
        )

    def build_prog_test(self):
        path = self.project.answer.code_path.example
        self.language = "c"
        self.create_file_to_test(self.project.answer.code_path.templates_data,
                                 self.project.answer.code_path.example,
                                 self.project.answer.code_path.test)
        if path.endswith('.c') or path.endswith('.cpp'):
            func = self.subprocess_cpp
        if path.endswith('.py'):
            func = self.subprocess_python
            self.language = "python"
        return [[item, func(self.project.answer.code_path.test, item.encode())] 
                for item in self.project.answer.tests['input']]


    @staticmethod
    def subprocess_cpp(file_path="test.c", test=None):  
        subprocess.run(["gcc", file_path])
        if test:
            test = test.encode()
        result = subprocess.run(['./a.out'],
                capture_output=True, input=test)
        return result.stdout.decode()
    
    @staticmethod
    def subprocess_python(file_path='test.py', test=None):
        if test:
            test = test.encode()
        result = subprocess.run(['python3', file_path], 
                                capture_output=True, input=test)
        return result.stdout.decode()
        
# result = 
# print(f"Command finished with return code: \n{result.stdout.decode()}")

# process = subprocess.Popen(
#     ['python3', '-c', 'print("console: ", input())'], # Replace with your command
#     stdin=subprocess.PIPE,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE
# )

# stdout, stderr = process.communicate(input="data to send to stdin".encode())

# print(f"Stdout: {stdout.decode()}")
# print(f"Stderr: {stderr.decode()}")