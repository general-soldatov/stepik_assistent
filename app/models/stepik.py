from pydantic import BaseModel

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


class Step(BaseModel):
    block: Block
    id: str
    has_review: bool
    time: str
