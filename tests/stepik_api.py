import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '/root/stepik_assistent')))

from app.automatize.stepik import StepikAPI
from app.config import service
from app.models.stepik import Section

from app.models.pipeline import Pipeline

PL = "tests/pipeline.yaml"

def testedAPI():
    stepik = StepikAPI(service.stepik)
    section = Section(course_id=278225, title="Механика", position=3)
    response = stepik.create_section(section)
    print(response)

def testedPipeLine():
    pl = Pipeline.model_validate_yaml(PL)
    pl.create_sections()

# testedAPI()
testedPipeLine()
