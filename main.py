from app.analys.parse import Test, TestOfCode
from app.models.project import Project

PATH = "projects/test_1.yaml"
project = Project.model_validate_yaml(PATH)
data: Test = TestOfCode(project)
data.export()
