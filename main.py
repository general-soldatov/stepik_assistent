from app.creator.test_task import TestChoice, MatchingTest, SortingTest
from app.creator.template import Test
from app.models.main_model import TestAI, TaskTemplate
from app.creator.create import BuildProject, ImportProject

import json
import yaml

PATH = "projects/project_3.yaml"

TEXT = '''{
    "test_tasks": [
    {
        "text": "str data is super string!",
        "correct": ["Privet"],
        "wrong": ["Hi", "Hello"]
    }],
    "sequence_task": [
        {
            "text": "str",
            "steps": ["dfdf", "sdd", "sdrefd"]
        }
    ],
    "matching_task": [
    {
        "text": "str",
        "therms": ["str", "sdd", "ds"],
        "definitions": ["str", "sdd", "gh"]
    }
    ]
}'''

def build_test_project():
    project = TaskTemplate.model_validate_yaml(PATH)
    data: Test = TestChoice(project)
    data.export()

def parseAI():
    data = json.loads(TEXT)
    project = BuildProject()
    # project.add_text()
    project.import_ai(data)
    project.add_choice()
    project.add_matching()
    # project.add_sorting()
    # print(*project.project, sep='\n')
    project.export_to_yaml(PATH)

def import_data():
    data = ImportProject(PATH)
    # print(*[dt for dt in data.data], sep='\n')
    data.create()

# build_test_project()
# parseAI()
import_data()