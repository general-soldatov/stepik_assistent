from app.models.main_model import YamlProject
from typing import Dict
import os
from boto_orm.models.config import AWSConfig, AWSSession

PATH = "/Users/general_soldatov/own_app/stepik_assistent/app/config.yaml"
SERVICE = "/Users/general_soldatov/Yandex.Disk.localized/Stepik/session.yaml"

class Config(YamlProject):
    app: str
    path_ai: str
    path_default: str
    data_prog: Dict[str, str]
    prompt: str
    file_cpp: str
    course: Dict[str, int | str]
    template: str

class Service(YamlProject):
    aws_session: Dict[str, str]
    s3_config: Dict[str, str]
    stepik: Dict[str, str]

config = Config.model_validate_yaml(PATH)
service = Service.model_validate_yaml(SERVICE)

s3_config = AWSConfig(**service.s3_config)
session = AWSSession(**service.aws_session)

def create_division(message: str = None, division: str = '#') -> str:
    columns = os.get_terminal_size().columns
    if message:
        padding_length = columns - len(message) - 2
        left_padding = division * (padding_length // 2)
        right_padding = division * ((padding_length + 1) // 2)
        return f"{left_padding} {message.upper()} {right_padding}"
    return division * columns