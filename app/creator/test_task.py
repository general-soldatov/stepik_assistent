from app.models.stepik import Pairs, SourceMatching, SourceSorting, Options
from .template import TestOfCode, Data
from app.models.project import ObjectsTypes, Text
from app.models.main_model import TaskTemplate
from py_markdown import ReadMD

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
            preserve_firsts_order = True,
            pairs=options)

    def _set_options(self, multiply_choice=False):
        self.block.options = dict()
        self._set_source()

class SortingTest(TestOfCode):
    @staticmethod
    def _add_options(project):
        return [Options(text=txt) for txt in project.answer.steps]

    def _set_source(self):
        _, options = self._set_answers()
        self.block.source = SourceSorting(options=options)

class TextData(Data):
    def _build(self):
        if self.project.path:
            self.block.text = ReadMD.file_import(self.project.path).to_html_text()
        if self.project.data:
            self.block.text = ReadMD(self.project.data).to_html_text()
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
