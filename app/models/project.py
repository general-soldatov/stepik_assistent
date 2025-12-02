from pydantic import BaseModel, field_validator
from typing import List

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

class ObjectsTypes:
    def __init__(self):
        self.objects = tuple(filter(lambda x: not x.startswith('__'),
                                        self.__class__.__dict__.keys()))

    @staticmethod
    def text():
        return Text

    @staticmethod
    def choice():
        return AnswerTest

    @staticmethod
    def matching():
        return AnswerMatching

    @staticmethod
    def sorting():
        return AnswerSorting

class Question(BaseModel):
    types: str
    text_data: str
    code_path: str | None = None
    help: str | None = None

    @field_validator('types')
    def check_name(cls, value):
        if value in ObjectsTypes().objects:
            return value
        raise ValueError('Неопознанный объект!')
