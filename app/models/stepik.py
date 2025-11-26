from pydantic import BaseModel, computed_field, Field
from typing import List

from .project import Project

class OptionsTest(BaseModel):
    is_correct: bool
    text: str
    feedback: str = ""

class Source(BaseModel):
    is_multiple_choice: bool
    is_always_correct: bool
    sample_size: int
    preserve_order: bool = False
    is_html_enabled: bool = True
    is_options_feedback: bool
    options: List[OptionsTest]

class Block(BaseModel):
    name: str = "text"
    text: str = ""
    video: str | None = None
    options: dict = {}
    subtitle_files: list = []
    is_deprecated: bool = False
    source: Source
    subtitles: dict = {}
    tests_archive: str | None = None
    feedback_correct: str = ""
    feedback_wrong: str = ""



class Step(BaseModel):
    block: Block
    id: str
    has_review: bool
    time: str
