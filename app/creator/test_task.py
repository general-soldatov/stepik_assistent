from app.models.stepik import Pairs, SourceMatching, SourceSorting, Options
from .template import TestOfCode, Data
from app.models.project import ObjectsTypes, Text
from app.models.main_model import TaskTemplate
from app.markdown import markdown_to_html

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

class SortingTest(TestOfCode):
    @staticmethod
    def _add_options(project):
        return [Options(text=txt) for txt in project.answer.steps]

    def _set_source(self):
        _, options = self._set_answers()
        self.block.source = SourceSorting(options=options)

class TextData(Data):
    @staticmethod
    def _from_md_to_html(path: str):
        with open(path, 'r', encoding='utf-8') as file:
            return markdown_to_html(file.read())

    def _build(self):
        if self.project.path:
            self.block.text = self._from_md_to_html(self.project.path)
        if self.project.data:
            self.block.text = markdown_to_html(self.project.data)
        self.block.name = "text"
        self.block.options = {}


class TaskObject(ObjectsTypes):
    def __init__(self):
        super().__init__()
        self.number = 0

    def choice(self, project: TaskTemplate):
        self.number += 1
        return TestChoice(project, self.number)

    def text(self, project: Text):
        return TextData(project)

    def matching(self, project: TaskTemplate):
        self.number += 1
        return MatchingTest(project, self.number)

    def sorting(self, project: TaskTemplate):
        self.number += 1
        return SortingTest(project, self.number)
