from pydantic import BaseModel
from typing import List

class TestTask(BaseModel):
    question: str
    true_: List[str]
    false_: List[str]

class SequenceTask(BaseModel):
    task: str
    steps: List[str]

class MatchingTask(BaseModel):
    task: str
    therms: List[str]
    definitions: List[str]

class TestAI(BaseModel):
    test_tasks: List[TestTask] | None = None
    sequence_task: List[SequenceTask] | None = None
    matching_task: List[MatchingTask] | None = None