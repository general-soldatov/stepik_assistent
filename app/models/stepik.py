from pydantic import BaseModel
from typing import List, Union

class Options(BaseModel):
    text: str

class OptionsTest(Options):
    is_correct: bool
    feedback: str = ""

class Source(BaseModel):
    is_html_enabled: bool = True

class TestSamples(BaseModel):
    test_in: List[str]
    test_out: List[str]

    def output_list(self):
        return [
            [sample_in, sample_out] 
            for sample_in, sample_out in zip(self.test_in, self.test_out)
        ]
    
class OptionsProgram(BaseModel):
    execution_time_limit: int = 5
    execution_memory_limit: int = 256
    limits: dict
    code_templates: dict
    code_templates_header_lines_count: dict
    code_templates_footer_lines_count: dict
    code_templates_options: dict = {}
    samples: List[List[str]]
    is_run_user_code_allowed: bool = True
    
class SourceProgram(BaseModel):
    code: str
    execution_time_limit: int = 5
    execution_memory_limit: int = 256
    samples_count: int = 1
    templates_data: str
    is_time_limit_scaled: bool = True
    is_memory_limit_scaled: bool = True
    is_run_user_code_allowed: bool = True
    manual_time_limits: list = []
    manual_memory_limits: list = []
    test_archive: list = []
    test_cases: List[List[str]]
    feedback_correct: str = ""
    feedback_wrong: str = ""

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
    preserve_firsts_order: bool = False
    pairs: List[Pairs]

class Block(BaseModel):
    name: str
    text: str
    video: str | None = None
    options: dict
    subtitle_files: list
    is_deprecated: bool = False
    source: Union[SourceTest, SourceMatching, SourceSorting, None] = None
    subtitles: dict
    tests_archive: str | None = None
    feedback_correct: str
    feedback_wrong: str

class Step(BaseModel):
    block: Block
    id: str
    has_review: bool
    time: str
