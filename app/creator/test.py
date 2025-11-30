from app.models.stepik import Step, OptionsTest, Block
from app.models.project import Project, Question, Answer
from app.models.ai_prompt import PromptAI, TestTask
from typing import Tuple

from .template import TestOfCode

class TestChoice(TestOfCode):
    def __init__(self, project, case_num=None, path = 'app/analys/sample_test.step'):
        super().__init__(project, case_num, path)
        if isinstance(project, TestTask):
            question = Question(
                types='choice',
                case_num=case_num,
                text_data=project.question
            )
            answer = Answer(
                correct=project.correct,
                wrong=project.wrong
            )
            self.project = Project(
                question = question,
                answer=answer
            )

    def set_text(self) -> None:
        super().set_text()
        if self.project.question.code_path:
            self.block.text += self.set_code(
                self.project.question.code_path)
        self._set_help()