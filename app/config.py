from app.models.main_model import YamlProject
from typing import Dict
import os

PATH = "app/config.yaml"

class Config(YamlProject):
    app: str
    path_ai: str
    path_default: str
    data_prog: Dict[str, str]
    prompt: str
    file_cpp: str

config = Config.model_validate_yaml(PATH)

def create_division(message: str = None, division: str = '#') -> str:
    columns = os.get_terminal_size().columns
    if message:
        padding_length = columns - len(message) - 2
        left_padding = division * (padding_length // 2)
        right_padding = division * ((padding_length + 1) // 2)
        return f"{left_padding} {message.upper()} {right_padding}"
    return division * columns