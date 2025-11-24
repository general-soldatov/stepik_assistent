# from app.analys.parse import TestOfCode
# from app.models.project import Project

PATH = "projects/test_1.yaml"
# project = Project.model_validate_yaml(PATH)
# # print(project)
# test = TestOfCode()
# test.add_project(project)
# test.export()

import json

def json_indent(path='matching.step'):
    with open(path, 'r', encoding='utf-8') as fl:
        text = json.load(fl)
    with open(path , 'w', encoding='utf-8') as file:
        json.dump(text, file, ensure_ascii=False, indent=4)

json_indent()