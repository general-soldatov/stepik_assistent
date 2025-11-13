from models.tester import Step
from typing import Tuple

class Test:
    def __init__(self, path: str = 'test/sample_test.step') -> None:
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
        template = f'<code class="language-{language}">{code}</code>'
        return template

    def set_text(self, text: str, num: str, path_code: str) -> None:
        super().set_text(text, num)
        self.data.block.text += self.set_code(path_code)
