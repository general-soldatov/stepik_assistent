from pydantic import BaseModel, field_validator

class Block(BaseModel):
    name: str
    text: str
    video: str | None
    options: dict
    subtitle_files: list
    is_deprecated: bool
    source: dict
    subtitles: dict
    tests_archive: str | None
    feedback_correct: str
    feedback_wrong: str

    @field_validator('name')
    def check_name(cls, value):
        if value in ['text', 'choice']:
            return value
        raise ValueError('Неопознанный объект!')


class Step(BaseModel):
    block: Block
    id: str
    has_review: bool
    time: str