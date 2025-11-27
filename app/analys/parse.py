from abc import ABC, abstractmethod
from app.models.stepik import Step, OptionsTest, Block
from app.models.project import Project, Question, Answer
from app.models.ai_prompt import PromptAI, TestTask
from typing import Tuple

class Data(ABC):
    def __init__(self, project: Project | PromptAI, case_num = None, path: str = 'app/analys/sample_test.step'):
        step = self._load_temp(path)
        self.block: Block = step.block
        if isinstance(project, Project):
            self.project = project


    @staticmethod
    def _load_temp(path) -> Step:
        with open(path, 'r', encoding='utf-8') as file:
             return Step.model_validate_json(file.read())


    def create_step(self) -> Step:
        return Step(self.block, id="8736153",
                    has_review = False,
                    time = "2025-11-12T07:09:19.592Z")

    @abstractmethod
    def _build(self):
        pass

    def preview(self):
        self._build()
        return self.block.model_dump_json(indent=4, ensure_ascii=False)

    def export(self, name: str) -> None:
        data = self.preview()
        with open(f"export/{name}.step", 'w', encoding='utf-8') as file:
            file.write(data)

class Test(Data):
    def _build(self):
        self.block.name = self.project.question.types
        self.block.feedback_correct = self.project.answer.feedback.correct
        self.block.feedback_wrong = self.project.answer.feedback.wrong
        self.set_text()
        self._set_answers()

    @staticmethod
    def template_text(text: str, num: int) -> str:
        text_step = f"<strong>Свершение {num}.</strong>&nbsp;"
        text_step += text
        return text_step

    def set_text(self) -> None:
        self.block.text = self.template_text(
            text=self.project.question.text_data,
            num=self.project.question.case_num
        )

    def _set_help(self):
        if self.project.question.help:
            self.block.text += self.template_help(self.project.question.help)

    def _set_options(self, multiply_choice: bool):
        self.block.options = dict(is_multiple_choice=multiply_choice)
        self.block.source.is_multiple_choice = multiply_choice
        self.block.source.preserve_order = False
        self.block.source.is_html_enabled = True

    @staticmethod
    def _add_options(project: Project):
        answers = project.answer
        return [*(OptionsTest(is_correct=True, text=text)
            for text in answers.correct), *(OptionsTest(
                is_correct=False, text=text)
            for text in answers.wrong)]

    def _set_answers(self):
        self.block.source.options = self._add_options(self.project)
        if self.project.answer.sample_size:
            self.block.source.sample_size = self.project.answer.sample_size
        else:
            self.block.source.sample_size = len(self.block.source.options)

    @staticmethod
    def template_help(text: str):
        return f"<details><summary><strong>Подсказка</strong></summary>{text}</details>"

    def export(self):
        return super().export(name=f"test_step_{self.project.question.case_num}")


class TestChoice(Test):
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

    def set_text(self):
        super().set_text()
        self._set_help()


class TestOfCode(Test):
    @staticmethod
    def import_file_code(path) -> Tuple[str, str]:
        if '.py' in path:
            language = 'python'
        with open(path, 'r', encoding='utf-8') as code:
            return language, code.read()

    def set_code(self, path_code) -> str:
        language, code = self.import_file_code(path_code)
        template = f'<pre><code class="language-{language}">{code}</code></pre>'
        return template

    def set_text(self) -> None:
        super().set_text()
        self.block.text += self.set_code(
            self.project.question.code_path)
        self._set_help()
