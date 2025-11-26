from app.analys.parse import Test, TestOfCode
from app.models.project import Project

PATH = "projects/test_1.yaml"
project = Project.model_validate_yaml(PATH)
data: Test = TestOfCode(project)
# text = "Что выдаст код, если пользователь введёт <code>data</code>"
# data.template_text(text, num=2, path_code='code.py')
data.export()
