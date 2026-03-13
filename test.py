# from app.creator.test_task import TestOfCode
from app.models.project import ObjectsTypes
PATH = "projects/test_1.yaml"
# project = Project.model_validate_yaml(PATH)
# # print(project)
# test = TestOfCode()
# test.add_project(project)
# test.export()

import json
import yaml
from py_markdown import ReadMD
from app.config import config

def json_indent(path='text.step'):
    with open(path, 'r', encoding='utf-8') as fl:
        text = json.load(fl)
    with open(path , 'w', encoding='utf-8') as file:
        json.dump(text, file, ensure_ascii=False, indent=4)

def read_yaml(path="projects/project_2.yaml"):
    with open(path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file.read())
        print(data)

# json_indent('2270650_2_string.step')
# read_yaml()
# txt = "projects/text.md"
# with open(txt, 'r', encoding='utf-8') as file:
#     data = markdown_to_html(file.read())
# with open('text.html', 'w', encoding='utf-8') as file:
#     file.write(data)
# print(data)
# obj = ReadMD.file_import(txt)
# obj.to_html_file('text.html')

import re
import subprocess

def create_file():
    with open("projects/template_led.c", 'r', encoding='utf-8') as file:
        with open("projects/test.c", "r", encoding="utf-8") as test:
            text = re.sub(r'::code[^::]*::footer', test.read(), file.read())
        text = re.sub(r"::", '//', text)
        with open("test.c", 'w', encoding='utf-8') as test:
            test.write(text)

# process = subprocess.Popen(
#     ['python3', '-c', 'print("console: ", input())'], # Replace with your command
#     stdin=subprocess.PIPE,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE
# )

# stdout, stderr = process.communicate(input="data to send to stdin".encode())

# print(f"Stdout: {stdout.decode()}")
# print(f"Stderr: {stderr.decode()}")

# from app.creator.program import ProgramStep

# ProgramStep.create_file_to_test()
# # res = ProgramStep.subprocess_python("test.c", "Datave")
# res = ProgramStep.subprocess_cpp(test='df')
# print(res)

# print(data)

from app.connections.bucket import ImageMover

# Пример строки
html_string = '<img width="960" height="1280" alt="image" src="https://github.com/user-attachments/assets/6002f3c0-e366-4c73-aff0-7f910da566d6" />\n<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/6eb51127-7225-498d-9945-6565c01d271d" />'
img = ImageMover(html_string)
img.replace_url()
print(img.html)


# response = requests.get(url)
# with open('data.jpg', 'wb') as file:
#     file.write(response.content)