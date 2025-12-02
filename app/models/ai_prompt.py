from pydantic import BaseModel, computed_field, Field
from typing import List
from .project import Question, AnswerTest, AnswerMatching, AnswerSorting
from abc import ABC, abstractmethod

class PromptAI(BaseModel, ABC):
    text: str
    types: str = Field(default="test_tasks", exclude=True)
    case_num: int = 0

    @computed_field(return_type=Question)
    def question(self):
        return Question(text_data=self.text,
                        case_num=self.case_num, types=self.types)

    @abstractmethod
    @computed_field(return_type=Question)
    def answer(self):
        pass


class TestTask(PromptAI):
    text: str
    correct: List[str]
    wrong: List[str]
    types: str = Field(default="choice", exclude=True)

    @computed_field(return_type=Question)
    def answer(self):
        return AnswerTest(correct=self.correct, wrong=self.wrong)

class SortingTask(PromptAI):
    text: str
    steps: List[str]
    types: str = Field(default="sorting", exclude=True)

    @computed_field(return_type=AnswerSorting)
    def answer(self):
        return AnswerSorting(steps=self.steps)

class MatchingTask(PromptAI):
    therms: List[str]
    definitions: List[str]
    types: str = Field(default="matching", exclude=True)

    @computed_field(return_type=Question)
    def answer(self):
        return AnswerMatching(first=self.therms, second=self.definitions)

class TestAI(BaseModel):
    test_tasks: List[TestTask] | None = None
    sequence_task: List[SortingTask] | None = None
    matching_task: List[MatchingTask] | None = None
