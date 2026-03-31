import math
import os
import json
from typing import Dict, List, Tuple
import random
from random import randint, choice, uniform
from scipy.optimize import root
from scipy.integrate import quad

from app.creator.create import BuildProject
from app.models.project import Question, AnswerNumber, OptionNumber

class TaskData:
    def __init__(self, data):
        self.data: Dict[str, Dict[str, List, Dict[str, str]]] = data

    @classmethod
    def load_json(cls, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)[0]
            return cls(data)

    @staticmethod
    def task_code(txt_task, derivative) -> Tuple[str, float]:
        lcls = dict(rad = math.radians,
                    grad = lambda x: 180 * x / math.pi, a_x=0, ax=0, **locals())
        glbl = {
            'pi': math.pi,
            'cos': math.cos,
            'sin': math.sin,
            'tan': math.tan,
            'arctan': math.atan,
            'randint': randint,
            'choice': choice,
            'random': random,
            'uniform': uniform,
            'root': root,
            'y_k': round(uniform(0.1, 0.6), 1),
            'derivative': derivative,
            'quad': quad,
            'boost': randint(5, 15),
            'corner': randint(10, 20),
            'v': lambda t : 4 * t **2,
            'speed': randint(1, 10),
            'a1': round(uniform(0.1, 0.9), 1),
            'log': math.log,
            # 'T': None, #random.uniform(0.1, 0.9),
            # 'c': choice([200, 250, 300, 350, 400, 450, 500]),
            'xx': lambda t : math.sin(math.pi * t),
            'y': (lambda t : 0.5 * t**2),
            'g': 9.8061,
            # 's': lambda k : s1 * k
        }
        exec(txt_task, glbl, lcls)
        return lcls['text'], lcls['result']

    @staticmethod
    def derivative(f,a,method='central',h=0.01):
        if method == 'central':
            return (f(a + h) - f(a - h))/(2*h)
        elif method == 'forward':
            return (f(a + h) - f(a))/h
        elif method == 'backward':
            return (f(a) - f(a - h))/h
        else:
            print("Method must be 'central', 'forward' or 'backward'.")

    def get_list_tasks(self, group: str, level: str) -> List[Dict[str, str]]:
        return self.data[group][level]

    def get_task(self, number: int = 0, level: str = '3'):
        tasks = self.get_list_tasks("STATICS", level)
        return self.run_task(tasks[number])

    def get_tasks_category(self, group: str, level: str = "3") -> List[dict]:
        tasks = []
        for task in self.get_list_tasks(group, level):
            text, number = self.run_task(task)
            tasks.append({"text": text, "image": task['image'], "answer": number, "max_error": 0.05})
        return tasks

    def create_all_tasks(self, path, level: str = '3'):
        types = 'number'
        for group, _ in self.data.items():
            project = BuildProject()
            for task in self.get_list_tasks(group, level):
                text, number = self.run_task(task)
                answer = AnswerNumber(data=[
                    OptionNumber(answer=str(round(number, 5)), max_error='0.05')])
                url = f"https://storage.yandexcloud.net/phys-bot/{task['image']}" if task['image'] else None
                project._add(Question(types=types, text_data=text,
                                      image=url),
                             answer, types)
            path_project = os.path.join(path, f'{group}.yaml')
            project.export_to_yaml(
                path=path_project)
            print("Project created", path_project)

    def run_task(self, task: Dict[str, str]):
        text, number = self.task_code(task["code"], self.derivative)
        return text.replace('\n', '').strip(), number
