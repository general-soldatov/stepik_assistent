import json
import yaml
from app.models.project import Project

def step_visual():
    with open('2055467_1_text.step', 'r', encoding='utf-8') as file:
        text = json.load(file)

    with open('text.step', 'w', encoding='utf-8') as file:
        data = json.dumps(text, ensure_ascii=False, indent=4)
        file.write(data)

def read_yaml():
    with open('projects/test_1.yaml', 'r', encoding='utf-8') as file:
        text = yaml.safe_load(file.read())
        data = Project.model_validate(text)
        print(data)

# step_visual()
read_yaml()
