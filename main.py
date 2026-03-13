import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname('/root/stepik_assistent')))

import click
import subprocess
import logging
from app.creator.create import BuildProject, ImportProject
from app.config import config, create_division, PATH
from app.models.ai_prompt import analys_md

logging.basicConfig(
    level=logging.INFO,
    format='[{asctime}] #{levelname:8} {filename}:'
           '{lineno} - {name} - {message}',
    style='{'
)
logger = logging.getLogger(__name__)

@click.group()
def cli():
    pass

def division(func):
    def inner(*args, **kwargs):
        # try:
            click.echo(create_division(config.data_prog['start']))
            func(*args, **kwargs)
            click.echo(create_division(config.data_prog["end"]))
        # except Exception as e:
        #     logger.error(e)
    return inner

@cli.command("config", help="Update of config data")
@division
def configurate():
    click.echo('Load of program`s config')
    subprocess.run([config.app, PATH])
    click.echo('Update file succesfull')

@cli.command("prompt", help="Print of the prompt to AI-model")
@click.option("--path", prompt="Path", help="Check path to theory-file", default=None)
@division
def prompt(path):
    prompt = config.prompt
    if path:
        data = config.course
        data.update(analys_md(config.course['name'], path))
        prompt = prompt.format(**data)
    click.echo(prompt + config.template)
    if not os.path.exists(config.path_ai):
        with open(config.path_ai, 'w', encoding='utf-8') as file:
            file.write('Insert your responsible from AI-model at json')

@cli.command("create", help="Create project's makefile")
@click.option("--path", prompt="Path", help="Check path to makefile", default=config.path_default)
@click.option("--ai_path", prompt="Path to AI", help="Path to AI-responsible from json", default=config.path_ai)
@division
def create(path, ai_path):
    project = BuildProject()
    if click.confirm(f"Do you want to add text to the project"):
        project.add_text()
    if click.confirm(f"Do you want to add AI-responsible to the project"):
        with open(ai_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            project.import_ai(data)
    if click.confirm(f"Do you want to add choice's test to the project"):
        project.add_choice()
    if click.confirm(f"Do you want to add sorting task to the project"):
        project.add_sorting()
    if click.confirm(f"Do you want to add matching task to the project"):
        project.add_matching()
    if click.confirm(f"Do you want to add number task to the project"):
        project.add_number()
    if click.confirm(f"Do you want to add string task to the project"):
        project.add_string()
    if click.confirm(f"Do you want to add program to the project"):
        project.add_program()
    project.export_to_yaml(path)

@cli.command("build", help="Build project from makefile")
@click.option("--path", prompt="Path", help="Check path to makefile", default=config.path_default)
@division
def build(path):
    data = ImportProject(path)
    data.create()

@cli.command("check", help="Check of test project from makefile")
@click.option("--path", prompt="Path", help="Check path to makefile", default=config.path_default)
@division
def check(path):
    data = ImportProject(path)
    data.check()

if __name__ == '__main__':
    cli()