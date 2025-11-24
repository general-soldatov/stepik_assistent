from app.models.stepik import Step, OptionsTest, Block
from app.models.project import Project
from typing import Tuple

class Data:
    def __init__(self, project: Project):
        self.project = project
        self.block = Block()

    def create_step(self) -> Step:
        return Step(self.block, id="8736153",
                    has_review = False,
                    time = "2025-11-12T07:09:19.592Z")

    def export(self, name: str) -> None:
        with open(f"export/{name}.step", 'w', encoding='utf-8') as file:
            data = self.block.model_dump_json(indent=4, ensure_ascii=False)
            file.write(data)

class Test(Data):
    # def __init__(self, path: str = 'app/analys/sample_test.step') -> None:
    #     self.data = self._load_test(path)

    # @staticmethod
    # def _load_test(path) -> Step:
    #     with open(path, 'r', encoding='utf-8') as file:
    #          return Step.model_validate_json(file.read())

    def _name(self):
        if len(self.project.answer.true_) > 1:
            self.block.name = ''

    def set_text(self, text: str, num: int) -> None:
        text_step = f"<strong>Свершение {num}.</strong>&nbsp;"
        text_step += text
        self.block.text = text_step

    @staticmethod
    def template_help(text: str):
        return f"<details><summary><strong>Подсказка</strong></summary>{text}</details>"

    def export(self):
        return super().export(name=f"test_step_{self.project.question.case_num}")


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

    def set_text(self, text: str, num: str, path_code: str) -> None:
        super().set_text(text, num)
        self.block.text += self.set_code(path_code)

    @staticmethod
    def _add_options(project: Project):
        answers = project.answer
        return [*(OptionsTest(is_correct=True, text=text)
            for text in answers.true_), *(OptionsTest(
                is_correct=False, text=text)
            for text in answers.false_)]


    def _set_answers(self, project: Project):
       options = self.block.source.options
       self.block.source.options = self._add_options(project)
       self.block.source.sample_size = len(options)

    def add_project(self, project: Project):
        self.set_text(project.question.text,
                      project.question.case_num,
                      project.question.code_path)
        if project.question.help:
            self.block.text += self.template_help(project.question.help)
        self._set_answers(project)
