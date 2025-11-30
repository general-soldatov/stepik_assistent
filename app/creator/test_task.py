from app.models.project import TaskTemplate, Question, AnswerTest, AnswerMatching
from app.models.ai_prompt import PromptAI, TestTask, MatchingTask
from app.models.stepik import Pairs, SourceMatching

from .template import TestOfCode

class TestChoice(TestOfCode):
    def __init__(self, project, case_num=None, path = 'app/creator/sample_test.step'):
        super().__init__(project, case_num, path)
        if isinstance(project, TestTask):
            question = Question(
                types='choice',
                case_num=case_num,
                text_data=project.question
            )
            answer = AnswerTest(
                correct=project.correct,
                wrong=project.wrong
            )
            self.project = TaskTemplate(
                question = question,
                answer=answer
            )

    def set_text(self) -> None:
        super().set_text()
        if self.project.question.code_path:
            self.block.text += self.set_code(
                self.project.question.code_path)
        self._set_help()

class MatchingTest(TestOfCode):
    def __init__(self, project, case_num=None, path = 'app/creator/sample_test.step'):
        super().__init__(project, case_num, path)
        if isinstance(project, MatchingTask):
            question = Question(
                types='matching',
                case_num=case_num,
                text_data=project.task
            )
            answer = AnswerMatching(
                first=project.therms,
                second=project.definitions
            )
            self.project = TaskTemplate(
                question = question,
                answer=answer
            )

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