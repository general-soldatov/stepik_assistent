from pydantic import BaseModel, field_validator, computed_field
from typing import List, Union

class Question(BaseModel):
    types: str
    text_data: str
    code_path: str | None = None
    help: str | None = None

    @field_validator('types')
    def check_name(cls, value):
        if value in ['text', 'choice', 'matching', 'sorting']:
            return value
        raise ValueError('Неопознанный объект!')

class Feedback(BaseModel):
    correct: str = ""
    wrong: str = ""

class Answer(BaseModel):
    sample_size: int | None = None
    feedback: Feedback = Feedback()

class AnswerTest(Answer):
    correct: List[str]
    wrong: List[str]

class AnswerMatching(Answer):
    first: List[str]
    second: List[str]

class AnswerSorting(Answer):
    steps: List[str]

class Text(BaseModel):
    path: str | None = None
    data: str | None = None