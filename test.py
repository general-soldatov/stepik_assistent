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

def json_indent(path='text.step'):
    with open(path, 'r', encoding='utf-8') as fl:
        text = json.load(fl)
    with open(path , 'w', encoding='utf-8') as file:
        json.dump(text, file, ensure_ascii=False, indent=4)

def read_yaml(path="projects/project_2.yaml"):
    with open(path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file.read())
        print(data)

json_indent()
# read_yaml()
txt = "projects/text.md"
# with open(txt, 'r', encoding='utf-8') as file:
#     data = markdown_to_html(file.read())
# with open('text.html', 'w', encoding='utf-8') as file:
#     file.write(data)
# print(data)
obj = ReadMD.file_import(txt)
obj.to_html_file('text.html')