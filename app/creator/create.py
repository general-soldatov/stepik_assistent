import yaml
from app.models.project import Question, AnswerTest, AnswerSorting, AnswerMatching, Text
from app.models.main_model import TaskTemplate, TestAI
from typing import List, Dict, Union
from pydantic import BaseModel

class Data(BaseModel):
    project: List[Dict[str, Union[TaskTemplate, Text]]]

class Project:
    def __init__(self) -> None:
        # self.project: List[TaskTemplate] = []
        self.data = Data(project=[])

    @staticmethod
    def _create_question(types: str) -> Question:
        text = "Sample text for {}".format(types)
        return Question(types=types, text_data=text)
    
    def _add(self, question, answer, type) -> None:
        self.data.project.append({type: TaskTemplate(question=question, answer=answer)})

    def _extend(self, tasks: list, type) -> None:
        self.data.project.extend([{type: TaskTemplate.model_validate_ai(item)} for item in tasks])

    def add_text(self) -> None:
        self.data.project.append({'text': Text()})

    def add_choice(self) -> None:
        types = 'choice'
        question = self._create_question(types)
        answer = AnswerTest(correct=['correct_answer'], wrong=['wrong_answer'])
        self._add(question, answer, types)

    def add_sorting(self) -> None:
        types = 'sorting'
        question = self._create_question(types)
        answer = AnswerSorting(steps=['step 1', 'step 2'])
        self._add(question, answer, types)

    def add_matching(self) -> None:
        types = 'matching'
        question = self._create_question(types)
        answer = AnswerMatching(first=['first', 'second'], second=['one', 'two'])
        self._add(question, answer, types)

    def import_ai(self, data: Dict[str, List[dict]]) -> None:
        pr = TestAI.model_validate(data)
        self._extend(pr.test_tasks, 'choice')
        self._extend(pr.matching_task, 'matching')
        self._extend(pr.sequence_task, 'sorting')

    def export_to_yaml(self, path: str) -> None:
        data = self.data.model_dump()
        with open(path, 'w', encoding='utf-8') as file:
            yaml.dump(data['project'], file)
