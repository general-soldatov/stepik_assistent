from app.creator.test_task import TestOfCode, TestChoice, MatchingTest
from app.creator.template import Test
from app.models.project import TaskTemplate
from app.models.ai_prompt import TestAI

import json

PATH = "projects/project_1.yaml"

TEXT = '''{
    "test_tasks": [
    {
        "question": "str data is super string!",
        "correct": ["Privet"],
        "wrong": ["Hi", "Hello"]
    }],
    "sequence_task": [
        {
            "task": "str",
            "steps": ["dfdf", "sdd", "sdrefd"]
        }
    ],
    "matching_task": [
    {
        "task": "str",
        "therms": ["str", "sdd", "ds"],
        "definitions": ["str", "sdd", "gh"]
    }
    ]
}'''

def build_test_project():
    project = TaskTemplate.model_validate_yaml(PATH)
    data: Test = TestChoice(project)
    data.export()

def parseAI(start=1):
    data = json.loads(TEXT)
    pr = TestAI.model_validate(data)
    for i, item in enumerate(pr.test_tasks, start):
        proj = TestChoice(item, i)
        print(proj.preview())
        start += 1
    for i, item in enumerate(pr.matching_task, start):
        proj = MatchingTest(item, i)
        print(proj.preview())

# build_test_project()
parseAI()