import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '/root/stepik_assistent')))

from app.automatize.folders import SearchFiles
from app.creator.create import BuildProject, Text

PATH = "/root/stepik/theorethical_mechanics"
PROJECT = 'tests/test.yaml'

def collecting_files(path: str):
    project = BuildProject()
    files = SearchFiles(PATH)
    files.search()
    print(f"Всего найдено {files.count} файлов с расширением .md")
    for key, value in files.data.items():
        print(key.decode(), '->', end=' ')
        for elem in value:
            project.add_text(text=Text(path=elem))
        print('Succesfull')
    project.export_to_yaml(path)

collecting_files(PROJECT)