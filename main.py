from app.creator.test_task import TestChoice, MatchingTest, SortingTest
from app.creator.template import Test
from app.models.main_model import TestAI, TaskTemplate
# from app.models.project import TaskTemplate
# from app.models.ai_prompt import TestAI

import json
import yaml

PATH = "projects/project_2.yaml"

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
    pr = TestAI.model_validate(data)
    data = TaskTemplate.model_validate_ai(pr.test_tasks[0])
    print(data.model_dump_json(indent=4))
    # for item in pr.test_tasks:
    #     data = TestChoice(item)
    #     print(data.preview())
    # for item in pr.matching_task:
    #     data = MatchingTest(item)
    #     print(data.preview())
    # for item in pr.sequence_task:
    #     data = SortingTest(item)
    #     print(data.preview())

# build_test_project()
parseAI()