from app.models.stepik import Pairs, SourceMatching, SourceSorting, Options, SourceNumber, OptionNumber, SourceString
from .template import TestOfCode, Data
from app.models.project import ObjectsTypes, Text
from app.models.main_model import TaskTemplate
from app.creator.program import ProgramStep
from py_markdown import ReadMD
from app.connections.bucket import ImageMover

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

    def _set_answers(self):
        return (self.project.answer.sample_size,
                self._add_options(self.project))

class SortingTest(TestOfCode):
    @staticmethod
    def _add_options(project):
        return [Options(text=txt) for txt in project.answer.steps]

    def _set_source(self):
        options = [Options(text=elem) for elem in self.project.answer.steps]
        self.block.source = SourceSorting(options=options)

class NumberTest(TestOfCode):
    def _build(self):
        self.block.name = self.project.question.types
        self.set_text()
        self._set_source()

    def _set_source(self):
        number = [OptionNumber(answer=elem.answer, max_error=elem.max_error) for elem in self.project.answer.data]
        self.block.source = SourceNumber(
            options=number)


class StringTest(TestOfCode):
    def _build(self):
        self.block.name = self.project.question.types
        self.set_text()
        self._set_source()

    def _set_source(self):
        self.block.source = self.project.answer

class TextData(Data):
    def _build(self):
        if self.project.path:
            text = ReadMD.file_import(self.project.path).to_html_text()
        if self.project.data:
            text = ReadMD(self.project.data).to_html_text()
        img = ImageMover(text)
        img.replace_url()
        self.block.text = img.html
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

    def code(self, project: TaskTemplate):
        self.number += 1
        return ProgramStep(project, self.number)

    def number(self, project: TaskTemplate):
        self.number += 1
        return NumberTest(project, self.number)

    def string(self, project: TaskTemplate):
        self.number += 1
        return StringTest(project, self.number)
