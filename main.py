from app.analys.parse import Test, TestOfCode, TestChoice
from app.models.project import Project
from app.models.ai_prompt import TestAI

import json

# PATH = "projects/test_1.yaml"
# project = Project.model_validate_yaml(PATH)
# data: Test = TestOfCode(project)
# data.export()

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

data = json.loads(TEXT)
pr = TestAI.model_validate(data)
for i, item in enumerate(pr.test_tasks, 1):
    print(item.question)
    proj = TestChoice(item, i)
    print(proj.preview())
