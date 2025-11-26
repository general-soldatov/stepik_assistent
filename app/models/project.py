import yaml
from pydantic import BaseModel, field_validator, computed_field
from typing import List
from .ai_prompt import TestAI

class Question(BaseModel):
    types: str
    case_num: int
    text_data: str
    code_path: str | None = None
    help: str | None = None

    @field_validator('types')
    def check_name(cls, value):
        if value in ['text', 'choice', 'matching']:
            return value
        raise ValueError('Неопознанный объект!')

    @computed_field
    def text(self) -> str:
        pass

class Feedback(BaseModel):
    correct: str
    wrong: str

class Answer(BaseModel):
    true_: List[str]
    false_: List[str]
    sample_size: int | None = None
    feedback: Feedback

class YamlProject(BaseModel):
    @classmethod
    def model_validate_yaml(cls, path, encoding='utf-8'):
        with open(path, 'r', encoding=encoding) as file:
            data = yaml.safe_load(file.read())
            return cls.model_validate(data)

class Project(YamlProject):
    question: Question
    answer: Answer
