import json
import os
from typing import List, Dict, Union
from pydantic import Field, ConfigDict
from app.models.main_model import YamlProject
from app.models.project import SectionProject, Course
from app.models.stepik import Unit
from app.automatize.stepik import StepikAPI, Section
from app.creator.create import ImportProject
from app.config import service

class BaseData:
    def __init__(self, path: str = 'course.json'):
        self._data: Dict[str, Union[int, Dict[str, List[int]]]] = self.read(path)
        self.path = path

    @staticmethod
    def read(path):
        if not os.path.exists(path):
            return {}
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write(self):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(self._data, file, ensure_ascii=False, indent=4)

    def add_section(self, title: str, _id: int):
        self._data[title] = {'id': _id, 'lessons': {}}
        print('Added section:', title)
        self.write()

    def add_lesson(self, section_name: str, lesson_id: int):
        self._data[section_name]['lessons'].setdefault(lesson_id, {'steps': [], 'units': None})
        print('-> Added lesson:', lesson_id)
        self.write()

    def add_steps(self, section_name: str, lesson_id: int, step_id: int):
        self._data[section_name]['lessons'][lesson_id]['steps'].append(step_id)
        print('-> -> Added step:', step_id)
        self.write()

    def add_units(self, section_name: str, lesson_id: int, unit_id: int):
        self._data[section_name]['lessons'][lesson_id]['units'] = unit_id
        print('🔗 Added unit:', unit_id)
        self.write()



class Pipeline(YamlProject):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    course: Course
    sections: List[SectionProject]
    data: BaseData = Field(default=BaseData())
    stepik: StepikAPI = Field(default=StepikAPI(service.stepik))

    def create_section(self, section: SectionProject, position: int) -> Section:
        return Section(course_id=self.course.course_id, title=section.title, position=position)

    def create_sections(self):
        for position, section in enumerate(self.sections, 1):
            data = self.create_section(section, position)
            section_info = self.stepik.create_section(data)
            self.data.add_section(section.title, section_info['id'])
            for position_lesson, lesson in enumerate(section.lessons, 1):
                lesson_info = self.stepik.create_lesson(lesson)
                self.data.add_lesson(section.title, lesson_info['id'])
                project = ImportProject(lesson.steps)
                for step in project.get_dict(lesson_info['id'], self.course):
                    with open('test.step', 'w', encoding='utf-8') as file:
                        file.write(step.model_dump_json())
                    step_info = self.stepik.create_step(step)
                    self.data.add_steps(section.title, lesson_info['id'], step_info['id'])
                unit = Unit(section=section_info['id'], lesson=lesson_info['id'], position=position_lesson)
                response = self.stepik.create_unit(unit)
                self.data.add_units(section.title, lesson_info['id'], response['id'])