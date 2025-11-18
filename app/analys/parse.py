from app.models.stepik import Step, OptionsTest
from app.models.project import Project
from typing import Tuple

class Test:
    def __init__(self, path: str = 'app/analys/sample_test.step') -> None:
        self.data = self._load_test(path)

    @staticmethod
    def _load_test(path) -> Step:
        with open(path, 'r', encoding='utf-8') as file:
             return Step.model_validate_json(file.read())

    def set_text(self, text: str, num: int) -> None:
        text_step = f"<strong>Свершение {num}.</strong>&nbsp;"
        text_step += text
        self.data.block.text = text_step


    def export(self, name: str = "test_steps") -> None:
        with open(f"export/{name}.step", 'w', encoding='utf-8') as file:
            data = self.data.model_dump_json(indent=4, ensure_ascii=False)
            file.write(data)


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

    @staticmethod
    def template_help(text: str):
        return f"<details><summary><strong>Подсказка</strong></summary>{text}</details>"

    def set_text(self, text: str, num: str, path_code: str) -> None:
        super().set_text(text, num)
        self.data.block.text += self.set_code(path_code)


    @staticmethod
    def _add_options(project: Project):
        answers = project.answer
        return [*(OptionsTest(is_correct=True, text=text)
            for text in answers.true_), *(OptionsTest(
                is_correct=False, text=text)
            for text in answers.false_)]


    def _set_answers(self, project: Project):
       options = self.data.block.source.options
       self.data.block.source.options = self._add_options(project)
       self.data.block.source.sample_size = len(options)

    def add_project(self, project: Project):
        self.set_text(project.question.text,
                      project.question.case_num,
                      project.question.code_path)
        if project.question.help:
            self.data.block.text += self.template_help(project.question.help)
        self._set_answers(project)
