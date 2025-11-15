import yaml
from pydantic import BaseModel, field_validator
from typing import List

class Question(BaseModel):
    types: str
    case_num: int
    text: str
    code_path: str

    @field_validator('types')
    def check_name(cls, value):
        if value in ['text', 'choice']:
            return value
        raise ValueError('Неопознанный объект!')

class Answer(BaseModel):
    true_: List[str]
    false_: List[str]

class YamlProject(BaseModel):
    @classmethod
    def model_validate_yaml(cls, path, encoding='utf-8'):
        with open(path, 'r', encoding=encoding) as file:
            data = yaml.safe_load(file.read())
            return cls.model_validate(data)

class Project(YamlProject):
    question: Question
    answer: Answer
