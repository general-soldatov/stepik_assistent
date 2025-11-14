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

class Project(BaseModel):
    question: Question
    answer: Answer
