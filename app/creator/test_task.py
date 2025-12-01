from app.models.project import TaskTemplate, Question, AnswerTest, AnswerMatching
from app.models.ai_prompt import PromptAI, TestTask, MatchingTask
from app.models.stepik import Pairs, SourceMatching

from .template import TestOfCode

class TestChoice(TestOfCode):
    def set_text(self) -> None:
        super().set_text()
        if self.project.question.code_path:
            self.block.text += self.set_code(
                self.project.question.code_path)
        self._set_help()


class MatchingTest(TestOfCode):
    @staticmethod
    def _add_options(project):
        answer = project.answer
        return [Pairs(first=first, second=second)
                for first, second in zip(answer.first, answer.second)]

    def _set_source(self):
        _, options = self._set_answers()
        self.block.source = SourceMatching(
            is_html_enabled = True,
            preserve_first_order = False,
            pairs=options)