from pydantic import BaseModel
from typing import List, Union

class Options(BaseModel):
    text: str

class OptionsTest(Options):
    is_correct: bool
    feedback: str = ""

class Source(BaseModel):
    is_html_enabled: bool = True

class SourceTest(Source):
    is_multiple_choice: bool
    is_always_correct: bool
    sample_size: int
    preserve_order: bool
    is_options_feedback: bool
    options: List[OptionsTest]

class SourceSorting(Source):
    options: List[Options]

class Pairs(BaseModel):
    first: str
    second: str

class SourceMatching(Source):
    preserve_first_order: bool = False
    pairs: List[Pairs]

class Block(BaseModel):
    name: str
    text: str
    video: str | None = None
    options: dict
    subtitle_files: list
    is_deprecated: bool = False
    source: Union[SourceTest, SourceMatching, None] = None
    subtitles: dict
    tests_archive: str | None = None
    feedback_correct: str
    feedback_wrong: str

class Step(BaseModel):
    block: Block
    id: str
    has_review: bool
    time: str
