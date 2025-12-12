from app.creator.test_task import TestChoice, MatchingTest, SortingTest
from app.creator.template import Test
from app.models.main_model import TestAI, TaskTemplate
from app.creator.create import BuildProject, ImportProject

import json
import click



TEXT = '''Представь, что ты автор курса по микроконтроллерам. Напиши вопросы к теме "Логические операции в языке Си, больше, меньше, равно, не равно и т.д.". Должно быть 10 заданий тестовых на выбор одного правильного ответа, а также 5 на сортировку или сопоставление. Ответ представь в формате json по образцу:{
    "test_tasks": [
    {
        "text": "Text question",
        "correct": ["correct"],
        "wrong": ["uncorrect_1", "uncorrect_2", "uncorrect_3"]
    }],
    "sequence_task": [
        {
            "text": "Text",
            "steps": ["one", "two", "three"]
        }
    ],
    "matching_task": [
    {
        "text": "Question",
        "therms": ["one", "two", "three"],
        "definitions": ["first", "second", "third"]
    }
    ]
}'''
PATH_AI = "ai_request.json"
PATH = "projects/003_bit's_logical.yaml"

def build_test_project():
    project = TaskTemplate.model_validate_yaml(PATH)
    data: Test = TestChoice(project)
    data.export()

def parseAI():
    with open(PATH_AI, 'r', encoding='utf-8') as file:
        data = json.load(file)
    project = BuildProject()
    # project.add_text()
    project.import_ai(data)
    # project.add_choice()
    # project.add_matching()
    # project.add_sorting()
    # print(*project.project, sep='\n')
    project.export_to_yaml(PATH)

def import_data():
    data = ImportProject(PATH)
    # print(*[dt for dt in data.data], sep='\n')
    data.create()

# build_test_project()
# parseAI()
# comment
import_data()