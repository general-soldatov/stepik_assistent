from pydantic import BaseModel, Field, model_serializer
from typing import List, Union, Optional, Annotated

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

class SourceTest(Source):
    is_multiple_choice: bool
    is_always_correct: bool
    sample_size: Optional[int]
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

class OptionNumber(BaseModel):
    answer: str
    max_error: str = 0

class SourceNumber(BaseModel):
    options: List[OptionNumber]

class SourceString(BaseModel):
    pattern: str
    use_re: bool
    match_substring: bool
    case_sensitive: bool
    code: str
    is_text_disabled: bool
    is_file_disabled: bool

class Block(BaseModel):
    name: str
    text: str
    video: str | None = None
    options: dict
    subtitle_files: list
    is_deprecated: bool = False
    source: Union[SourceTest, SourceMatching, SourceSorting, SourceNumber, SourceString, None] = None
    subtitles: dict
    tests_archive: str | None = None
    feedback_correct: str
    feedback_wrong: str

class Step(BaseModel):
    block: Block
    id: str
    has_review: bool
    time: str

class OmitIfNone:
    pass

class NoSerializeNoneModel(BaseModel):
    @model_serializer
    def _serialize(self):
        omit_if_none_fields = {
            k
            for k, v in self.model_fields.items()
            if any(isinstance(m, OmitIfNone) for m in v.metadata)
        }
        return {k: v for k, v in self if k not in omit_if_none_fields or v is not None}

class StepSource(NoSerializeNoneModel):
    block: Block
    lesson: int
    position: int
    cost: Annotated[Optional[int], OmitIfNone()] = None

class Section(BaseModel):
    course: Optional[int] = Field(alias='course_id')
    title: str
    position: int = 1

class Lesson(BaseModel):
    title: str
    is_public: bool = False

class Unit(BaseModel):
    section: int
    lesson: int
    position: int