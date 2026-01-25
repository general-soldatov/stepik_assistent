from pydantic import BaseModel, field_validator
from typing import List, Dict

class Feedback(BaseModel):
    correct: str = ""
    wrong: str = ""

class LimitsProg(BaseModel):
    time: int = 5
    memory: int = 256

class CodePath(BaseModel):
    templates_data: str = ''
    example: str = ''
    test: str = ''
    code_run: str = ''
    code_template: str = ''

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

class AnswerProgram(Answer):
    tests: Dict[str, List[str]]
    limits: LimitsProg
    code_path: CodePath

class Text(BaseModel):
    path: str | None = None
    data: str | None = None

class ObjectsTypes:
    def __init__(self):
        self.objects = tuple(filter(lambda x: not x.startswith('__'),
                                        self.__class__.__dict__.keys()))

    def text(self):
        return Text

    def choice(self):
        return AnswerTest

    def matching(self):
        return AnswerMatching

    def sorting(self):
        return AnswerSorting
    
    def code(self):
        return AnswerProgram

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
