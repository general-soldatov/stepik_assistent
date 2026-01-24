import yaml
from pydantic import BaseModel
from typing import List, Union
from .ai_prompt import TestTask, SortingTask, MatchingTask, PromptAI
from .project import Question, AnswerTest, AnswerSorting, AnswerMatching

class YamlProject(BaseModel):
    @classmethod
    def model_validate_yaml(cls, path, encoding='utf-8'):
        with open(path, 'r', encoding=encoding) as file:
            data = yaml.safe_load(file.read())
            return cls.model_validate(data)

class TestAI(BaseModel):
    choice: List[TestTask] | None = None
    sequence: List[SortingTask] | None = None
    matching: List[MatchingTask] | None = None

class TaskTemplate(YamlProject):
    question: Question
    answer: Union[AnswerTest, AnswerMatching, AnswerSorting]

    @classmethod
    def model_validate_ai(cls, obj: PromptAI):
        return TaskTemplate(question=obj.question, answer=obj.answer)
