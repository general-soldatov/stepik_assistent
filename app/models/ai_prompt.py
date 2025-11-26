from pydantic import BaseModel
from typing import List

class PromptAI(BaseModel):
    pass

class TestTask(PromptAI):
    question: str
    correct: List[str]
    wrong: List[str]

class SequenceTask(PromptAI):
    task: str
    steps: List[str]

class MatchingTask(PromptAI):
    task: str
    therms: List[str]
    definitions: List[str]

class TestAI(PromptAI):
    test_tasks: List[TestTask] | None = None
    sequence_task: List[SequenceTask] | None = None
    matching_task: List[MatchingTask] | None = None
